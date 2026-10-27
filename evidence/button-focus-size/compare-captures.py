"""Measure the two native-player captures, excluding unrelated loader animation."""
import json
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

ROOT = Path(__file__).parent
cases = []
for size, y in [('medium', 266), ('small', 321)]:
    images = {phase: Image.open(ROOT / (size + '-' + phase + '.jpg')).convert('RGB')
              for phase in ['focus-before', 'hover-active', 'focus-returned']}

    def outline(cx):
        region = images['hover-active'].crop((cx - 44, y - 24, cx + 44, y + 24))
        mask = Image.new('1', region.size)
        mask.putdata([r < 215 and g < 215 and b > 145 and b - r > 15
                      for r, g, b in region.get_flattened_data()])
        bounds = mask.getbbox()
        return {'width_px': bounds[2] - bounds[0], 'height_px': bounds[3] - bounds[1]}

    active, control = outline(541), outline(304)
    roi = (496, y - 26, 586, y + 26)
    difference = ImageChops.difference(images['focus-before'].crop(roi), images['focus-returned'].crop(roi))
    mae = sum(ImageStat.Stat(difference).mean) / 3
    result = {'size': size, 'logical_height_px': 40 if size == 'medium' else 32,
              'native_scale': 865 / 1112, 'active_outline': active,
              'same_size_hover_control': control, 'raster_tolerance_px': 1,
              'focus_return_crop_mean_absolute_error': round(mae, 4),
              'size_matches_control': all(abs(active[k] - control[k]) <= 1 for k in active),
              'focus_restored': mae < 1}
    assert result['size_matches_control'] and result['focus_restored'], result
    cases.append(result)

report = {'status': 'PASS', 'method': 'Native screenshots: blue border silhouette versus static same-size hover; 1px subpixel raster tolerance. Before/returned crop comparison. Exact logical dimensions and destinations verified separately through Figma API.', 'cases': cases}
(ROOT / 'visual-observations.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
