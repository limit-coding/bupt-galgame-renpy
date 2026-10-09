# Original community images are copied byte-for-byte. No AI redraw or costume redesign.
screen art_preview():
    tag menu
    default preview_person = "DeepSeek"
    add "bg road"
    add Solid("#132b4440")
    frame:
        xpos 38 ypos 42 xsize 660 ysize 636
        padding (28, 22)
        background Solid("#183747ed")
        vbox:
            spacing 7
            text "AI 娘 · 原图预览" size 34 color "#fff1d2"
            text "DeepSeek / GPT / Claude" size 22 color "#a7d8d0"
            null height 4
            if preview_person == "DeepSeek":
                text "DeepSeek 娘" size 27
                text "蓝白女仆装、鲸鳍耳与鲸尾。" size 22
            elif preview_person == "ChatGPT":
                text "GPT 娘" size 27
                text "白发龙角、龙翼龙尾与白色长裙。" size 22
            else:
                text "Claude 娘" size 27
                text "橙色长发、花形饰品、手持书本。" size 22
            text "直接显示收录库中的原样参考图。\n未重绘、未换装、未修改人物比例。" size 20 color "#bdced3"
            text "原作：ZipZipPipe《大 AI 与小 AI 们》\nDeepSeek 原角色：上善无形\n收录：ApprenTice / AI-Fanworks" size 18 color "#bdced3"
            text "非官方社区角色 · 保留署名及非商业使用说明" size 16 color "#ecc89d"
            null height 2
            textbutton "DeepSeek 娘" action SetScreenVariable("preview_person", "DeepSeek") style "title_button"
            textbutton "GPT 娘" action SetScreenVariable("preview_person", "ChatGPT") style "title_button"
            textbutton "Claude 娘" action SetScreenVariable("preview_person", "Claude") style "title_button"
            textbutton "返回" action ShowMenu("sprite_gallery") style "title_button"
    add Transform("images/characters/community-originals/%s-Girl.png" % preview_person, xysize=(384, 683)) xpos 805 ypos 18

screen sprite_gallery():
    tag menu
    default sprite_person = "classmate"
    default sprite_emotion = "normal"
    add "bg road"
    add Solid("#132b4440")
    add ai_sprite(sprite_person, sprite_emotion) xpos 775 ypos 20
    frame:
        xpos 38 ypos 42 xsize 660 ysize 636
        padding (28, 25)
        background Solid("#183747ed")
        vbox:
            spacing 12
            text "AI 娘 · 剧情立绘" size 34 color "#fff1d2"
            text "保留原有造型 · 六种表情" size 22 color "#a7d8d0"
            hbox:
                spacing 8
                for person, name in (("classmate", "DeepSeek 娘"), ("guide", "GPT 娘"), ("senior", "Claude 娘")):
                    textbutton name action SetScreenVariable("sprite_person", person) selected (sprite_person == person) style "expression_button"
            null height 8
            grid 3 2:
                spacing 8
                for emotion, name in (("normal", "常态"), ("happy", "开心"), ("surprised", "惊讶"), ("sad", "难过"), ("angry", "生气"), ("shy", "害羞")):
                    textbutton name action SetScreenVariable("sprite_emotion", emotion) selected (sprite_emotion == emotion) style "expression_button"
            text "同班同学：DeepSeek 娘\n实验室学姐：Claude 娘\n迎新志愿者：GPT 娘" size 22 color "#bdced3"
            text "原设：ZipZipPipe / 上善无形（DeepSeek）\n以原图制作透明表情版本；原图另存，可对照查看。\n社区同人角色 · 非官方 · 来源与许可见关于页面" size 17 color "#bdced3"
            textbutton "原图对照" action ShowMenu("art_preview") style "title_button"
            textbutton "返回主菜单" action ShowMenu("main_menu") style "title_button"

style expression_button is title_button:
    xsize 194
    selected_background Solid("#557d83")
style expression_button_text is title_button_text:
    size 22
    selected_color "#ffe1aa"
