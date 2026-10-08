"""Import an owned/authorized photo without modifying the original. Pillow required."""
from pathlib import Path
from PIL import Image, ImageOps
import argparse, hashlib, json, shutil, sys
ROOT = Path(__file__).resolve().parents[1]
def import_photo(root, source, scene_id, credit, focal=(.5,.5)):
    root, source = Path(root), Path(source).resolve()
    registry_path = root/'assets/backgrounds/registry.json'
    entries = json.loads(registry_path.read_text())
    entry = next((e for e in entries if e['id'] == scene_id), None)
    if entry is None: raise ValueError('Unknown scene ID; add it to the registry and script first.')
    if not credit.strip(): raise ValueError('A photo source/credit is required.')
    if not all(0 <= x <= 1 for x in focal): raise ValueError('Focal coordinates must be between 0 and 1.')
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert('RGB')
        size = image.size
        if min(size) < 300: raise ValueError('Image is too small for a readable background.')
        result = ImageOps.fit(image, (1280,720), method=Image.Resampling.LANCZOS, centering=focal)
    # Content-addressed copies preserve every original and every processed revision.
    raw = root/f'assets/backgrounds/raw/{scene_id}-{digest[:16]}{source.suffix.lower()}'
    raw.parent.mkdir(parents=True, exist_ok=True)
    if not raw.exists(): shutil.copy2(source, raw)
    elif hashlib.sha256(raw.read_bytes()).hexdigest() != digest:
        raise ValueError('Existing raw copy does not match its hash; refusing to overwrite.')
    processed = root/f'assets/backgrounds/processed/{scene_id}-{digest[:16]}-{focal[0]:.3f}-{focal[1]:.3f}.png'
    processed.parent.mkdir(parents=True, exist_ok=True)
    result.save(processed)
    runtime = root/'game'/entry['game_path']
    runtime.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(processed, runtime)
    entry.update(source=credit, raw_path=str(raw.relative_to(root)), processed_path=str(processed.relative_to(root)), source_sha256=digest, original_size=list(size), crop_focal=list(focal), style_version='photo-v1', is_placeholder=False, privacy_review='人工检查：可识别人脸、证件、车牌；本工具不自动识别人脸')
    registry_path.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
    return entry
if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('photo',type=Path);p.add_argument('--id',required=True)
    p.add_argument('--source',required=True,help='Photographer/source and permission note')
    p.add_argument('--focal',nargs=2,type=float,default=(.5,.5),metavar=('X','Y'))
    a=p.parse_args()
    try: print(json.dumps(import_photo(ROOT,a.photo,a.id,a.source,a.focal),ensure_ascii=False,indent=2))
    except (ValueError,OSError) as e: p.exit(1,f'Import failed: {e}\n')
