init offset = 2
style default:
    font "fonts/NotoSansSC.ttf"
style window:
    background Solid("#142e3fe8")
    ysize 202
style namebox:
    background None
    xpos 90
    ypos 11
style say_label:
    size 25
style say_dialogue:
    xpos 90
    ypos 55
    xsize 1100
    size 26
    line_spacing 7
style quick_button_text:
    size 17
    idle_color "#b8ced4"
    hover_color "#fff0cc"
style quick_button:
    padding (12, 8)
style title_button is button:
    xsize 370
    padding (14, 6)
    background Solid("#244a59")
    hover_background Solid("#3e6874")
style title_button_text is button_text:
    size 23
    color "#edf3eb"
    hover_color "#ffe1aa"
style choice_button:
    background Solid("#173c50ed")
    hover_background Solid("#426d78fa")
    xsize 750
    padding (24, 17)
style choice_button_text:
    color "#f0eee1"
    hover_color "#ffe0a8"
    size 26
style choice_vbox:
    spacing 18
style button:
    activate_sound (AUDIO['button'] if renpy.loadable(AUDIO['button']) else None)

screen chapter_stamp():
    zorder 5
    $ campus_info = current_campus_info()
    if campus_info:
        $ campus_caption = campus_info.get("display_name", campus_info["real_location"])
        text campus_caption xpos 24 ypos 24 size 16 color "#ffffff" outlines [(1, "#183343", 0, 0)]
    frame:
        xpos 1258 xanchor 1.0 ypos 16
        padding (12, 8)
        background Solid("#193b4de0")
        text "[chapter]" size 16 color "#e1eee5"

screen demo_end():
    modal True
    add Solid("#102838ed")
    vbox:
        xalign .5 yalign .47 spacing 18
        text "第一天，已存入记忆。" size 48 color "#fff1d4" xalign .5
        text "DEMO COMPLETE / [route]" size 22 color "#9dd3c7" xalign .5
        text "今日留下的线索：[clue]" size 24 xalign .5
        text "[classmate_name]的信任：[affection_b]    [senior_name]的信任：[affection_c]" size 20 xalign .5
        text "后续章节开发中" size 24 xalign .5
        text "七个北邮实景参考场景 · 三位 AI 娘 · 后续章节制作中" size 18 xalign .5
        null height 20
        textbutton "返回主菜单" action Return() xalign .5 style "title_button"
