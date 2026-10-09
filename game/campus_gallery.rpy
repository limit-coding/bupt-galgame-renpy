screen campus_gallery():
    tag menu
    default campus_scene = "entrance"
    $ place = BACKGROUND_BY_ID[campus_scene]
    add "bg " + campus_scene
    frame:
        xpos 24 ypos 24
        background Solid("#183747dc")
        padding (20, 14)
        vbox:
            spacing 6
            text place["real_location"] size 26 color "#fff1d2"
            text (place["time_of_day"] + " · 北邮西土城校区 · 实景参考绘制") size 17 color "#bbd7dd"
    textbutton "返回立绘" action ShowMenu("sprite_gallery") style "title_button" xpos 1060 ypos 24 xsize 190
    frame:
        xpos 0 ypos 578 xsize 1280 ysize 142
        padding (25, 18)
        background Solid("#183747ed")
        vbox:
            spacing 14
            hbox:
                spacing 10
                for scene_id, caption in (("entrance", "西门"), ("road", "摩斯码路"), ("plaza", "喷泉广场"), ("library", "图书馆"), ("lab", "教三楼"), ("cafeteria", "风味餐厅"), ("evening", "傍晚道路")):
                    textbutton caption action SetScreenVariable("campus_scene", scene_id) selected (campus_scene == scene_id) style "expression_button" xsize 166
            text "依据北邮官方照片绘制；建筑保留实景特征，季节与光照经过艺术处理。" size 17 color "#bdced3"
