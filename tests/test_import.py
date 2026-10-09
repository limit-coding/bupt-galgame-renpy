import unittest, tempfile, sys, json, hashlib
from pathlib import Path
from PIL import Image
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from import_background import import_photo
class PhotoImport(unittest.TestCase):
    def test_preserves_raw_and_maps_runtime(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); path=root/'assets/backgrounds';path.mkdir(parents=True)
            (path/'registry.json').write_text(json.dumps([dict(id='road',game_path='images/backgrounds/road.png')]))
            source=root/'user.png';Image.new('RGB',(1000,1500),'red').save(source)
            before=source.read_bytes()
            item=import_photo(root,source,'road','test photographer',(.5,.1))
            self.assertEqual(source.read_bytes(),before)
            self.assertEqual((root/item['raw_path']).read_bytes(),before)
            with Image.open(root/'game'/item['game_path']) as image:
                self.assertEqual(image.size,(1280,720))
            self.assertFalse(item['is_placeholder'])
            self.assertEqual(json.loads((root/'game/backgrounds.json').read_text()), json.loads((path/'registry.json').read_text()))
            self.assertEqual(item['source_sha256'],hashlib.sha256(before).hexdigest())
            import_photo(root,source,'road','test photographer',(.1,.9))
            self.assertEqual(len(list((path/'raw').iterdir())),1)
            self.assertEqual(len(list((path/'processed').iterdir())),2)
            with self.assertRaises(ValueError):import_photo(root,source,'../unsafe','credit')
            with self.assertRaises(ValueError):import_photo(root,source,'road','credit',(2,0))
if __name__=='__main__':unittest.main()
