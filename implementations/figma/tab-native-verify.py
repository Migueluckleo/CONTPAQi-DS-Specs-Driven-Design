"""Pixel checks on captured native Figma playback and final rendered theme paints.

Run with the bundled Python runtime (Pillow); no browser or Figma mutation.
"""
import json
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

ROOT=Path(__file__).resolve().parents[2]
E=ROOT/'evidence/tab-pilot';N=E/'native';D=E/'destination'
read=lambda p:json.loads(p.read_text())
policy=read(E/'audit-policy.json');showcase=read(D/'showcase.json')
failures=[];cases=[]
def check(value,name,**data):
    if not value:failures.append(dict(control=name,**data))
base=Image.open(N/'baseline.jpg').convert('RGB')
# Native screen observed at 100% with frame y=62; coordinates came from screenshots.
frame=showcase['playbackBounds'];offset_y=62
def crop_rect(bounds):
    x=bounds['x']-frame['x'];y=bounds['y']-frame['y']+offset_y
    return (round(x-1),round(y-1),round(x+bounds['width']+1),round(y+bounds['height']+1))
def metrics(a,b):
    diff=ImageChops.difference(a,b)
    pixels=list(diff.get_flattened_data() if hasattr(diff,'get_flattened_data') else diff.getdata())
    return {'changed_pixels':sum(max(p)>4 for p in pixels),'mean_absolute_channel_difference':sum(ImageStat.Stat(diff).mean)/3}
for example in showcase['hoverExamples']:
    name=example['type']+'-'+('selected'if example['selected']=='true'else'normal');rect=crop_rect(example['bounds'])
    default=base.crop(rect);hover=Image.open(N/(name+'-hover.jpg')).convert('RGB').crop(rect);returned=Image.open(N/(name+'-return.jpg')).convert('RGB').crop(rect)
    changed=metrics(default,hover);restored=metrics(default,returned)
    check(changed['changed_pixels']>=20,'native-hover-visible-change',case=name,metrics=changed)
    check(restored['mean_absolute_channel_difference']<=1,'native-default-restored',case=name,metrics=restored)
    cases.append(dict(case=name,hover=changed,returned=restored))
for example in showcase['disabledExamples']:
    name=example['type']+'-'+example['selected'];rect=crop_rect(example['bounds'])
    diff=metrics(base.crop(rect),Image.open(N/('disabled-'+name+'.jpg')).convert('RGB').crop(rect))
    check(diff['mean_absolute_channel_difference']<=1,'native-disabled-unchanged',case=name,metrics=diff)
    cases.append(dict(case='disabled/'+name,metrics=diff))
selection=metrics(Image.open(N/'selection-resumen.jpg').convert('RGB'),Image.open(N/'selection-disabled.jpg').convert('RGB'))
check(selection['mean_absolute_channel_difference']<=1,'native-disabled-keeps-selected-panel',metrics=selection)
# Selection/panel changes were additionally reviewed visually in three native screenshots.
screen=Image.open(D/'review.png').convert('RGB');rendered=[];origin=showcase['reviewBounds']
for name in ['final-consumers-0.json','final-consumers-1.json']:
    for item in read(D/name)['records']:
        if item['type']!='pill':continue
        bounds=item['bounds'];point=(round(bounds['x']-origin['x']+4),round(bounds['y']-origin['y']+bounds['height']/2))
        expected=tuple(round(item['fills'][0]['color'][c]*255)for c in 'rgb');actual=screen.getpixel(point)
        check(max(abs(a-b)for a,b in zip(actual,expected))<=policy['rendered_srgb_channel_tolerance'],'native-rendered-theme-background',mode=item['mode'],point=point,expected=expected,actual=actual)
        rendered.append(dict(mode=item['mode'],point=point,expected=expected,actual=actual))
result={'status':'FAIL'if failures else'PASS','scope':'Native Figma hover/return, disabled clicks, separately demonstrated selection/panels and rendered theme backgrounds; no keyboard/ARIA web claim','hover_cases':4,'disabled_cases':6,'selection_panel_transitions_visually_verified':['Resumen -> Movimientos','Movimientos -> Documentos','Documentos -> Resumen'],'cases':cases,'selection_disabled':selection,'rendered_theme_backgrounds':rendered,'failures':failures}
(N/'comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(failures))
