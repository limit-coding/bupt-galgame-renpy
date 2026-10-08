"""Original diagram-style placeholder assets. Requires Pillow; never touches raw photos."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, math
ROOT = Path(__file__).resolve().parents[1]
registry_file = ROOT/'assets/backgrounds/registry.json'
if registry_file.exists() and any(not e['is_placeholder'] for e in json.loads(registry_file.read_text())):
    raise SystemExit('Real photos already imported; refusing to overwrite them with placeholders.')
FONT = str(ROOT / 'game/fonts/NotoSansSC.ttf')
def font(n): return ImageFont.truetype(FONT, n)
scenes = [('entrance','校园入口','西土城校区入口','上午'),('road','校园道路','校内道路，待照片确认','上午'),('plaza','校园广场','校内广场，待照片确认','中午'),('library','图书馆','图书馆，待照片确认','下午'),('lab','实验室','虚构实验室','下午'),('cafeteria','食堂','食堂，待照片确认','下午'),('evening','傍晚校园','校内道路，待照片确认','傍晚')]
registry=[]
for idx,(key,name,location,time) in enumerate(scenes):
    im=Image.new('RGB',(1280,720)); d=ImageDraw.Draw(im)
    top=(235,180,161) if key=='evening' else (155,200,215)
    for y in range(720):
        t=y/720; d.line((0,y,1280,y),fill=tuple(int(v*(1-t)+245*t) for v in top))
    d.ellipse((970,70,1070,170),fill='#fff4d5')
    d.polygon([(0,390),(1280,370),(1280,720),(0,720)],fill='#a6bca1')
    d.polygon([(585,410),(675,410),(1090,720),(180,720)],fill='#e0d7c8')
    if key in ('lab','library','cafeteria'):
        d.rectangle((70,135,1210,480),fill='#e5e6dd'); d.rectangle((90,155,1190,195),fill='#557e88')
        for x in range(110,1170,135):
            d.rectangle((x,220,x+100,370),fill='#9bbcc5')
            if key=='library':
                for z in range(x+7,x+95,13):d.rectangle((z,232,z+8,350),fill=['#668586','#ad8c72','#d8bf8d'][z%3])
        d.rectangle((260,405,1020,442),fill='#c1a78e')
        d.text((640,163),name,anchor='mt',font=font(22),fill='white')
    else:
        for x,w,h in [(70,250,210),(360,180,140),(780,340,230)]:
            d.rectangle((x,430-h,x+w,430),fill='#e7e0d2');d.rectangle((x-8,425-h,x+w+8,442-h),fill='#63808b')
            for xx in range(x+20,x+w-20,40):
                for yy in range(450-h,404,45):d.rectangle((xx,yy,xx+23,yy+28),fill='#8eafbc')
        if key=='entrance':
            d.rectangle((435,283,845,328),fill='#3d6776');d.rectangle((435,320,459,465),fill='#c0c8c2');d.rectangle((821,320,845,465),fill='#c0c8c2')
            d.text((640,285),'校园入口 · 示意',anchor='mt',font=font(24),fill='#f2eddf')
    for x,y,s in [(55,410,65),(1185,395,80),(230,460,45),(1040,470,48)]:
        d.rectangle((x-5,y-20,x+5,y+85),fill='#837365');d.ellipse((x-s,y-s*1.7,x+s,y+s*.3),fill='#789b87');d.ellipse((x-s*.6,y-s*1.8,x+s*.8,y),fill='#8eae93')
    d.rounded_rectangle((30,27,455,90),radius=10,fill='#203f4d')
    d.text((48,37),f'{idx+1:02d} / {name} · {time}',font=font(24),fill='#f4eddf')
    d.text((30,110),'占位背景 / 非北邮实景还原',font=font(18),fill='#345466')
    out=ROOT/f'game/images/backgrounds/{key}.png';im.save(out)
    registry.append(dict(id=key,scene_name=name,real_location=location,time_of_day=time,source='原创程序绘制占位图；无用户照片',raw_path=None,processed_path=None,style_version='placeholder-v1',game_path=f'images/backgrounds/{key}.png',usage=[{'entrance':'start / Scene 1; main_menu','road':'start / Scene 2','plaza':'start / Scene 3','library':'library_event / Scene 4','lab':'lab_event / Scene 4','cafeteria':'cafeteria_event / Scene 4','evening':'evening_scene / Scene 5'}[key]],is_placeholder=True))
(ROOT/'assets/backgrounds/registry.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2))
for person,name,hair,coat in [('classmate','林晴','#634e48','#deba8c'),('senior','沈知遥','#343f52','#8aabb6'),('protagonist','许言','#475368','#a1b6a7')]:
    for expression in ['normal','happy','surprised','sad','angry']:
        im=Image.new('RGBA',(470,680));d=ImageDraw.Draw(im)
        d.ellipse((115,30,355,330),fill=hair)
        d.polygon([(143,285),(327,285),(415,405),(455,680),(15,680),(55,405)],fill=coat)
        d.polygon([(185,289),(235,357),(285,289),(267,560),(200,560)],fill='#f2eee3')
        d.rounded_rectangle((205,233,267,310),radius=18,fill='#efd1b4')
        d.ellipse((145,79,325,274),fill='#f4d8bf')
        d.pieslice((117,28,354,217),180,355,fill=hair)
        d.polygon([(150,100),(166,224),(139,236),(129,154)],fill=hair)
        d.polygon([(300,104),(308,225),(337,245),(339,144)],fill=hair)
        for x in [196,278]:
            if expression=='happy':d.arc((x-12,171,x+12,190),190,345,fill=hair,width=4)
            else:d.ellipse((x-6,173,x+6,188 if expression!='surprised' else 196),fill=hair)
        if expression=='surprised':d.ellipse((225,216,245,239),fill='#9e6c67')
        elif expression=='sad':d.arc((222,226,250,242),185,350,fill='#9e6c67',width=3)
        else:d.arc((221,206,253,230),0,180,fill='#9e6c67',width=3)
        if expression=='angry':
            d.line((182,157,208,167),fill=hair,width=4);d.line((267,167,292,157),fill=hair,width=4)
        if expression=='sad':
            d.line((182,165,206,156),fill=hair,width=3);d.line((267,156,292,165),fill=hair,width=3)
        if person=='senior':
            for x in [176,258]:d.rounded_rectangle((x,165,x+42,199),radius=5,outline=hair,width=3)
            d.line((218,180,258,180),fill=hair,width=3)
        d.rounded_rectangle((130,420,340,497),radius=12,fill='#284958')
        d.text((235,424),name,anchor='mt',font=font(23),fill='#f8f3e6')
        d.text((235,458),f'占位立绘 · {expression}',anchor='mt',font=font(16),fill='#a5d8cd')
        im.save(ROOT/f'game/images/characters/{person}_{expression}.png')
print('Generated 7 scene placeholders and 15 expression sprites.')
