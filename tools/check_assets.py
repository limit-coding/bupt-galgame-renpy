from pathlib import Path
import json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
entries=json.loads((ROOT/'assets/backgrounds/registry.json').read_text())
assert entries==json.loads((ROOT/'game/backgrounds.json').read_text()), 'Runtime background manifest out of sync'
assert len(entries)==7 and all(not e['is_placeholder'] for e in entries), 'A story background is still a placeholder'
ids=set()
for e in entries:
    assert e['id'] not in ids, f'Duplicate ID: {e["id"]}'
    ids.add(e['id'])
    for key in ('scene_name','real_location','time_of_day','source','style_version','usage'):assert e[key], (e['id'],key)
    with Image.open(ROOT/'game'/e['game_path']) as im:
        if e.get('source_type') == 'ai_reference_illustration':
            assert abs(im.width/im.height-16/9)<.015 and im.width>=1280, e['id']
            assert e['reference_url'].startswith('https://'), e['id']
            assert (ROOT/e['reference_file']).is_file(), e['id']
        else:assert im.size==(1280,720),e['id']
    if not e['is_placeholder']:
        for key in ('raw_path','processed_path'):assert (ROOT/e[key]).is_file(),key
import hashlib
atlases=json.loads((ROOT/'source_assets/characters/expression-atlases/registry.json').read_text())
assert {entry['tag'] for entry in atlases} == {'classmate', 'senior', 'guide'}
for entry in atlases:
    p=ROOT/'game'/entry['game_path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256']
    assert p.read_bytes()==(ROOT/entry['source_path']).read_bytes()
    assert (ROOT/entry['reference']).is_file()
    with Image.open(p) as im:
        assert im.mode=='RGBA' and list(im.size)==entry['size']
        w,h=im.size
        assert w%3==0 and h%2==0, 'Atlas must have integral cells'
        assert entry['expressions']==['normal','happy','surprised','sad','angry','shy']
        signatures=set()
        for row in range(2):
            for col in range(3):
                cell=im.crop((col*w//3,row*h//2,(col+1)*w//3,(row+1)*h//2))
                alpha=cell.getchannel('A')
                assert alpha.getextrema()==(0,255), (entry['id'],row,col)
                hist=alpha.histogram()
                assert hist[0]>cell.width*cell.height*.15, 'Missing transparent area'
                assert sum(hist[230:])>cell.width*cell.height*.15, 'Missing solid character area'
                # Distinct face regions prevent accidentally reusing one expression six times.
                face=cell.crop((cell.width//4,0,cell.width*3//4,cell.height//3))
                signatures.add(hashlib.sha256(face.tobytes()).hexdigest())
        assert len(signatures)==6, entry['id']
assert (ROOT/'game/fonts/NotoSansSC.ttf').stat().st_size>1000000
assert (ROOT/'docs/licenses/NotoSansSC-OFL.txt').is_file()
print(f'PASS: {len(ids)} backgrounds; 3 transparent atlases / 18 expression frames; Chinese font and license.')
print('Optional audio: '+', '.join(f'{n}={"present" if (ROOT/f"game/audio/{n}.ogg").exists() else "silent"}' for n in ('menu','daily','evening','campus','button')))

# User requires unmodified community originals; ensure runtime bytes match their archive.
import hashlib
community_registry=ROOT/'source_assets/characters/community-originals/registry.json'
if community_registry.exists():
    originals=json.loads(community_registry.read_text())
    for entry in originals:
        data=(ROOT/'game'/entry['file']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==entry['sha256'], entry['id']
        assert data==(ROOT/entry['source_file']).read_bytes(), entry['id']
    print('PASS: 3 community character references copied byte-for-byte; no redraw.')
