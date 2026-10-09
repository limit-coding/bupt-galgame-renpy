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
            textbutton "返回" action ShowMenu("main_menu") style "title_button"
    add Transform("images/characters/community-originals/%s-Girl.png" % preview_person, xysize=(384, 683)) xpos 805 ypos 18
