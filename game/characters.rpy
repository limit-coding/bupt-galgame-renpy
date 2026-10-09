default protagonist_name = "许言"
default classmate_name = "林晴"
default senior_name = "沈知遥"
define p = Character("protagonist_name", dynamic=True, color="#c3e4ef")
define b = Character("classmate_name", dynamic=True, color="#f0c899")
define c = Character("senior_name", dynamic=True, color="#a6ddd2")
default affection_b = 0
default affection_c = 0
default route = ""
default clue = ""
default chapter = "开学第一天"
init python:
    for person in ('protagonist', 'classmate', 'senior'):
        for expression in ('normal', 'happy', 'surprised', 'sad', 'angry'):
            renpy.image((person, expression), 'images/characters/%s_%s.png' % (person, expression))
    for scene_id in ('entrance','road','plaza','library','lab','cafeteria','evening'):
        path = 'images/backgrounds/illustrated/%s-v1.png' % scene_id if scene_id in ('entrance', 'road') else 'images/backgrounds/%s.png' % scene_id
        renpy.image(('bg', scene_id), Transform(path, xysize=(1280, 720)))
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
