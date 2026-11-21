import json,sys,re,glob,os
slug=sys.argv[1]
pf='salida/subidos/plan-tiktok-2026-11-14.json'
p=json.load(open(pf,encoding='utf8'))
for v in p:
    if v.get('slug')==slug: v['borrador']=True
json.dump(p,open(pf,'w',encoding='utf8'),ensure_ascii=False,indent=2)
f='SUBIR-A-TIKTOK.md'
L=open(f,encoding='utf8').read().split('\n')
for i,l in enumerate(L):
    if l.startswith('|') and f'| {slug} |' in l and 'BORRADOR' not in l:
        L[i]=re.sub(r'\|[^|]*\|\s*$','| BORRADOR en TikTok (subido, sin publicar ni programar) |',l)
open(f,'w',encoding='utf8').write('\n'.join(L))
for t in glob.glob('salida/_tiktok-tmp/*'): os.remove(t)
print('ok',slug)
