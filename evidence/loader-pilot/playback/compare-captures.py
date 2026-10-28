from pathlib import Path
from PIL import Image,ImageChops
import json
R=Path(__file__).resolve().parent
images=[Image.open(R/('fit-'+str(i)+'.jpg')).convert('RGB')for i in range(5)]
centers=[354.5,418.5,482.5,547.5];rows=[]
for name,cx in zip(['brand','neutral','strong','on-color'],centers):
 box=(int(cx)-14,339,int(cx)+14,368);crops=[im.crop(box)for im in images];diffs=[sum(any(v>8 for v in px)for px in ImageChops.difference(crops[0],im).getdata())for im in crops[1:]];rows.append(dict(color=name,box=box,changedPixels=diffs,animationObserved=any(n>5 for n in diffs)))
box=(281,75,500,113);static=[sum(any(v>8 for v in px)for px in ImageChops.difference(images[0].crop(box),im.crop(box)).getdata())for im in images[1:]]
report=dict(status='PASS_PLAYBACK_SAMPLES'if all(r['animationObserved']for r in rows)and max(static)<5 else'REVIEW',frames=['fit-'+str(i)+'.jpg'for i in range(5)],cases=rows,staticReference=dict(box=box,changedPixels=static),visualReview='Native presenter shows moving arcs in all six sizes and four colors, stable white inverse/0.3 track, four brand themes and linked Button loading. Readable captures 0/1/2 show color persistence and no navigation on secondary loading click.',limits=['No frame-rate or exact-cycle wall-clock measurement','No web/ARIA/reduced-motion implementation','No independent reviewer'])
(R/'observations.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report))
