import sys,os,shutil,json,re
root='C:/DATOS/DESARROLLO/Hyperframes/VidesoEjercicios/'
slug=sys.argv[1]
pj=root+'salida/subidos/plan-tiktok-2026-11-14.json'
plan=json.load(open(pj,encoding='utf8'))
p=next(x for x in plan if x['slug']==slug)
d=root+p['dir']
exts=['.mp4','.tiktok.txt','.miniatura.png','.miniatura.tiktok.png','.youtube.txt']
for e in exts:
    for f in os.listdir(d):
        if f==slug+e or (f.endswith('_'+slug+e) and f.startswith('OC_')):
            shutil.move(d+f,root+'salida/subidos/EnTikTok/'+f)
p['done']=True
json.dump(plan,open(pj,'w',encoding='utf8'),indent=1,ensure_ascii=False)
t=open(root+'SUBIR-A-TIKTOK.md',encoding='utf8').read()
t=re.sub(r'(\| %s %s \| %s \|[^\n]*?\| )(?:✅ )?Plan 4/día \(sin subir\)'%(p['fecha'],p['hora'],slug),r'\1Programado (plan 4/día)',t)
open(root+'SUBIR-A-TIKTOK.md','w',encoding='utf8').write(t)
print('ok',slug,p['fecha'],p['hora'])
