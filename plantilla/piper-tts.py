# Voz en off con Piper (local, gratis). La llama make-exercise.mjs desde videos/<slug>/:
#   python plantilla/piper-tts.py audio_request.json audio_engine_meta.json
# Lee { voice, speed, enVoice?, lines: [{id, text, speed?, en?}] } (speed de la línea pisa la general) y escribe
# assets/voice/<id>.wav + el meta que usa build-index (mismo formato que el motor de Kokoro: voices[{id, path, duration_s, words}]).
# Línea con "en": primero dice ese texto la voz inglesa (enVoice, ej. "kokoro:af_heart"), pausa corta con fundido y
# después "text" con la voz principal (Daniela). El volumen del inglés se iguala al de Daniela para que el cambio no salte.
# Modelos en plantilla/voces-piper/<voice>.onnx (+ .onnx.json). Daniela (es_AR): CC BY-SA 4.0, ver README.
# Kokoro (Apache 2.0): kokoro-v1.0.onnx + voices-v1.0.bin en plantilla/voces-kokoro/ o en ~/.cache/hyperframes/tts/.
import io, json, os, sys, wave
import numpy as np
from piper import PiperVoice, SynthesisConfig

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 22050                 # Daniela (high) es 22050 Hz; las otras voces se re-muestrean a esto
GAP, FADE = 0.35, 0.03     # pausa entre el nombre en inglés y la explicación; fundido en los bordes del inglés

_piper, _kokoro = {}, None


def resample(x, sr_in):
    if sr_in == SR:
        return x
    n = int(len(x) * SR / sr_in)
    return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)


def kokoro():
    global _kokoro
    if _kokoro is None:
        from kokoro_onnx import Kokoro
        for d in (os.path.join(HERE, "voces-kokoro"), os.path.join(os.path.expanduser("~"), ".cache", "hyperframes", "tts")):
            m = [os.path.join(d, "kokoro-v1.0.onnx"), os.path.join(d, "voices-v1.0.bin")]
            if not os.path.exists(m[0]):
                m = [os.path.join(d, "models", "kokoro-v1.0.onnx"), os.path.join(d, "voices", "voices-v1.0.bin")]
            if all(os.path.exists(p) for p in m):
                _kokoro = Kokoro(*m)
                break
        else:
            sys.exit("falta el modelo de Kokoro (ver plantilla/README.md, sección Voz)")
    return _kokoro


def say(voice, text, speed=1.0):
    if voice.startswith("kokoro:"):
        v = voice[7:]
        s, sr = kokoro().create(text, voice=v, speed=speed, lang="en-gb" if v.startswith("b") else "en-us")
        return resample(np.asarray(s, np.float32), sr)
    if voice not in _piper:
        model = os.path.join(HERE, "voces-piper", voice + ".onnx")
        if not os.path.exists(model):
            sys.exit(f"falta el modelo {model} (ver plantilla/README.md, sección Voz)")
        _piper[voice] = PiperVoice.load(model)
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        _piper[voice].synthesize_wav(text, w, syn_config=SynthesisConfig(length_scale=1.0 / speed))
    buf.seek(0)
    with wave.open(buf, "rb") as w:
        sr, data = w.getframerate(), w.readframes(w.getnframes())
    return resample(np.frombuffer(data, np.int16).astype(np.float32) / 32768, sr)


def trim(x, thr=0.01):
    idx = np.where(np.abs(x) > thr)[0]
    return x[max(idx[0] - 200, 0): idx[-1] + 600] if len(idx) else x


def rms(x):
    v = x[np.abs(x) > 0.01]
    return float(np.sqrt(np.mean(v ** 2))) if len(v) else 1.0


def mezcla(en_voice, en_text, es_voice, es_text, speed):
    es = say(es_voice, es_text, speed)
    en = trim(say(en_voice, en_text))
    en = en * (rms(es) / rms(en))
    n = min(int(SR * FADE), len(en) // 2)
    en[:n] *= np.linspace(0, 1, n)
    en[-n:] *= np.linspace(1, 0, n)
    z = lambda s: np.zeros(int(SR * s), np.float32)
    return np.concatenate([z(0.05), en, z(GAP), trim(es)])


req_path, out_path = sys.argv[1], sys.argv[2]
req = json.load(open(req_path, encoding="utf-8"))
os.makedirs("assets/voice", exist_ok=True)
voices, total = [], 0.0
for line in req["lines"]:
    path = f"assets/voice/{line['id']}.wav"
    sp = line.get("speed") or req.get("speed") or 1.0
    if line.get("en"):
        x = mezcla(req.get("enVoice") or "kokoro:af_heart", line["en"], req["voice"], line["text"], sp)
    else:
        x = say(req["voice"], line["text"], sp)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())
    dur = round(len(x) / SR, 3)
    voices.append({"id": line["id"], "path": path, "duration_s": dur, "words": []})
    total += dur
    print(f"  {line['id']}: {dur:.2f} s")
json.dump({"tts_provider": "piper", "voice_id": req["voice"], "enVoice": req.get("enVoice"), "bgm": None, "voices": voices,
           "sfx": [], "total_duration_s": round(total, 3)}, open(out_path, "w", encoding="utf-8"), indent=2)
