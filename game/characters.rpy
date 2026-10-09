default protagonist_name = "许言"
define classmate_name = "DeepSeek 娘"
define senior_name = "Claude 娘"
define guide_name = "GPT 娘"
define p = Character("protagonist_name", dynamic=True, color="#c3e4ef")
define b = Character("classmate_name", dynamic=True, color="#a8cefa")
define c = Character("senior_name", dynamic=True, color="#f0c899")
define g = Character("guide_name", dynamic=True, color="#ded5f5")
default affection_b = 0
default affection_c = 0
default route = ""
default clue = ""
default chapter = "开学第一天"
init python:
    # Atlas crops are performed by the renderer; original and edited PNGs stay intact.
    AI_EXPRESSIONS = ('normal', 'happy', 'surprised', 'sad', 'angry', 'shy')
    AI_CAST = {'classmate': 'DeepSeek', 'senior': 'Claude', 'guide': 'ChatGPT'}
    def ai_sprite(person, expression):
        path = 'images/characters/ai-girls/%s-v1.png' % AI_CAST[person]
        width, height = renpy.image_size(path)
        index = AI_EXPRESSIONS.index(expression)
        col, row = index % 3, index // 3
        x0, x1 = round(col * width / 3), round((col + 1) * width / 3)
        y0, y1 = round(row * height / 2), round((row + 1) * height / 2)
        return Transform(Crop((x0, y0, x1-x0, y1-y0), path), xysize=(460, 690))
    for person in AI_CAST:
        for expression in AI_EXPRESSIONS:
            renpy.image((person, expression), ai_sprite(person, expression))
    import json
    with renpy.file('backgrounds.json') as background_file:
        BACKGROUNDS = json.load(background_file)
    BACKGROUND_BY_ID = {item['id']: item for item in BACKGROUNDS}
    for item in BACKGROUNDS:
        renpy.image(('bg', item['id']), Transform(item['game_path'], xysize=(1280, 720)))
    def current_campus_info():
        attributes = renpy.get_attributes('bg') or ()
        return BACKGROUND_BY_ID.get(attributes[0], {}) if attributes else {}
transform stage_left:
    xalign .19
    yalign 1.0
transform stage_right:
    xalign .81
    yalign 1.0
transform stage_center:
    xalign .5
    yalign 1.0
transform establishing:
    subpixel True
    zoom 1.035
    xalign .5
    yalign .5
    ease 9.0 zoom 1.0

# Old prototype saves stored the previous default character names.
label after_load:
    $ classmate_name = "DeepSeek 娘"
    $ senior_name = "Claude 娘"
    $ guide_name = "GPT 娘"
    return
