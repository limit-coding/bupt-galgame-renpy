from pathlib import Path
import json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
entries=json.loads((ROOT/'assets/backgrounds/registry.json').read_text())
ids=set()
for e in entries:
    assert e['id'] not in ids, f'Duplicate ID: {e["id"]}'
    ids.add(e['id'])
    for key in ('scene_name','real_location','time_of_day','source','style_version','usage'):assert e[key], (e['id'],key)
    with Image.open(ROOT/'game'/e['game_path']) as im:assert im.size==(1280,720),e['id']
    if not e['is_placeholder']:
        for key in ('raw_path','processed_path'):assert (ROOT/e[key]).is_file(),key
for person in ('protagonist','classmate','senior'):
    for expr in ('normal','happy','surprised','sad','angry'):
        with Image.open(ROOT/f'game/images/characters/{person}_{expr}.png') as im:
            assert im.mode=='RGBA' and im.size==(470,680)
assert (ROOT/'game/fonts/NotoSansSC.ttf').stat().st_size>1000000
assert (ROOT/'docs/licenses/NotoSansSC-OFL.txt').is_file()
print(f'PASS: {len(ids)} backgrounds; 15 transparent expression sprites; Chinese font and license.')
print('Optional audio: '+', '.join(f'{n}={"present" if (ROOT/f"game/audio/{n}.ogg").exists() else "silent"}' for n in ('menu','daily','evening','campus','button')))
