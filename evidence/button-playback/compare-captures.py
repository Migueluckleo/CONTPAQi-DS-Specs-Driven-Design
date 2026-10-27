"""Read-only replay of recorded UI evidence; Pillow is only a QA dependency."""
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parent.parent
trace = json.loads((DIRECTORY / 'runtime-trace.json').read_text())
baseline = Image.open(DIRECTORY / 'fit-baseline.jpg').convert('RGB')


def image(path):
    return Image.open(ROOT / path).convert('RGB')


def difference(left, right):
    return sum(ImageStat.Stat(ImageChops.difference(left, right)).mean) / 3


interactive = []
for case in trace['runtimeCases']:
    x, y = case['coordinate']
    box = (x - 12, y - 7, x + 13, y + 8)
    reference = baseline.crop(box)
    active = difference(reference, image(case['active']).crop(box))
    returned = difference(reference, image(case['returned']).crop(box))
    held = case.get('capturedWhileHeld', True)
    interactive.append({**case, 'active_difference': active,
                        'return_difference': returned,
                        'status': 'PASS' if active > 0 and returned == 0 and held else 'FAIL'})

static = []
for case in trace['staticCases']:
    x, y = case['coordinate']
    box = (x - 12, y - 7, x + 13, y + 8)
    changed = difference(baseline.crop(box), image(case['image']).crop(box))
    static.append({**case, 'difference': changed,
                   'status': 'PASS' if changed == 0 else 'FAIL'})

motion = []
for size, rows in {'large': [127, 144, 161, 178, 195],
                   'medium': [232, 249, 266, 283, 300],
                   'small': [337, 354, 371, 388, 405]}.items():
    for family, y in zip(['primary', 'secondary', 'text', 'link', 'danger'], rows):
        box = (484, y - 6, 493, y + 7)
        crops = [image(sample['path']).crop(box) for sample in trace['animationSamples']]
        changed = [difference(crops[0], crop) for crop in crops[1:]]
        static_box = (349, y - 7, 374, y + 8)
        controls = [image(sample['path']).crop(static_box) for sample in trace['animationSamples']]
        stable = all(difference(controls[0], crop) == 0 for crop in controls[1:])
        motion.append({'size': size, 'family': family, 'sample_differences': changed,
                       'stable_neighbour': stable,
                       'status': 'PASS' if any(changed) and stable else 'FAIL'})

report = {'status': 'PASS' if all(c['status'] == 'PASS' for c in interactive + static + motion) else 'FAIL',
          'method': 'Same control/viewport pixels: active differs, return and static controls match exactly; motion has a stable neighbour.',
          'scope': 'Recorded native Figma player observations, not a new browser run or a frame-rate/accessibility certification.',
          'interactive': interactive, 'static': static, 'motion': motion}
print(json.dumps(report, ensure_ascii=False, indent=2))
