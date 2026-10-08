# Development-only engine-driven UI tests; excluded from distributions.
init python:
    _test.timeout = 30

testsuite demo:
    setup:
        $ preferences.text_cps = 0
        pause until screen "main_menu"
    teardown:
        exit

    testcase menu_and_settings:
        assert screen "main_menu"
        pause 0.7
        screenshot "main-menu.png"
        click "设置"
        assert screen "preferences"
        pause 0.7
        screenshot "settings.png"
        click "返回"
        assert screen "main_menu"
        click "读取游戏"
        assert screen "load"
        click "返回"

    testcase library:
        run Start()
        advance until screen "choice" timeout 120
        pause 0.7
        screenshot "choice.png"
        click "去图书馆，找一处安静的地方。"
        advance until "她接过卡片，却没有立刻收起来，而是把背面的空白朝向我们。" timeout 60
        pause 0.7
        screenshot "library-dialogue.png"
        advance until screen "demo_end" timeout 120
        assert eval (route == "图书馆" and affection_b == 1 and affection_c == 1)
        assert eval (clue == "书页间的一小段安静")
        pause 0.7
        screenshot "library-ending.png"
        click "返回主菜单"
        assert screen "main_menu"

    testcase laboratory:
        run Start()
        advance until screen "choice" timeout 120
        click "去实验室，看看声音如何被记录。"
        advance until screen "demo_end" timeout 120
        assert eval (route == "实验室" and affection_b == 0 and affection_c == 2)
        assert eval (clue == "两次敲击与一个新问题")
        pause 0.7
        screenshot "lab-ending.png"
        click "返回主菜单"

    testcase cafeteria:
        run Start()
        advance until screen "choice" timeout 120
        click "去食堂，从一顿饭开始认识校园。"
        advance until screen "demo_end" timeout 120
        assert eval (route == "食堂" and affection_b == 2 and affection_c == 1)
        assert eval (clue == "三只杯子的轻响")
        pause 0.7
        screenshot "cafeteria-ending.png"
        click "返回主菜单"

    testcase save_load_history:
        run Start()
        advance until screen "choice" timeout 120
        click "保存"
        assert screen "save"
        run FileSave(1, confirm=False)
        pause 1.0
        pause 0.7
        screenshot "save.png"
        click "返回"
        click "去实验室，看看声音如何被记录。"
        advance
        assert eval (route == "实验室")
        run ShowMenu("load")
        run FileLoad(1, confirm=False)
        pause 1.0
        assert screen "choice"
        assert eval (route == "" and affection_c == 0)
        click "去食堂，从一顿饭开始认识校园。"
        advance
        click "历史"
        assert screen "history"
        assert eval (len(_history_list) > 10)
        pause 0.7
        screenshot "history.png"
        click "返回"
        advance until screen "demo_end" timeout 120
        assert eval (route == "食堂" and affection_b == 2)
        click "返回主菜单"

    testcase expressions_and_controls:
        run Start()
        advance until "你是不是在找报到点？" timeout 120
        assert eval ('happy' in renpy.get_attributes('classmate'))
        pause 0.7
        screenshot "character-happy.png"
        advance until "你已经对着同一棵树看了三次地图。它再热心，也没办法给你指路。"
        assert eval ('normal' in renpy.get_attributes('classmate'))
        click id "quick_auto"
        assert eval (preferences.afm_enable)
        click id "quick_auto"
        assert eval (not preferences.afm_enable)
        run ShowMenu("preferences")
        click "标题菜单"
        assert screen "confirm"
        click "确定"
        assert screen "main_menu"
