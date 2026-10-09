# Development-only engine-driven UI tests; excluded from distributions.
# On an unfocused macOS desktop RenPy maps mouse events to (-1,-1), including
# virtual test events. Restore virtual mouse focus before each simulated click.
# This does not activate the OS window and is not a manual desktop input test.
init python:
    _test.timeout = 30
    # Keep rendering at the normal display cadence for reproducible screenshots.
    _test.maximum_framerate = False

testsuite demo:
    setup:
        $ preferences.text_cps = 0
        pause until screen "main_menu"
    teardown:
        exit

    testcase menu_and_settings:
        pause until screen "main_menu" timeout 10
        assert screen "main_menu"
        pause 0.7
        screenshot "main-menu.png"
        $ renpy.display.interface.mouse_focused = True
        click id "main_settings" pos (0.5, 0.5)
        pause until screen "preferences" timeout 10
        assert screen "preferences"
        pause 0.7
        screenshot "settings.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回" pos (0.5, 0.5)
        pause until screen "main_menu" timeout 10
        assert screen "main_menu"
        $ renpy.display.interface.mouse_focused = True
        click "读取游戏" pos (0.5, 0.5)
        pause until screen "load" timeout 10
        assert screen "load"
        $ renpy.display.interface.mouse_focused = True
        click "返回" pos (0.5, 0.5)

    testcase library:
        run Start()
        advance until screen "choice" timeout 120
        pause 0.7
        screenshot "choice.png"
        $ renpy.display.interface.mouse_focused = True
        click "去图书馆，找一处安静的地方。" pos (0.5, 0.5)
        advance until "她接过卡片，却没有立刻收起来，而是把背面的空白朝向我们。" timeout 60
        pause 0.7
        screenshot "library-dialogue.png"
        advance until "明天还一起走吗？我现在可以保证，只会偶尔走错。" timeout 60
        assert eval ('evening' in renpy.get_attributes('bg'))
        pause 0.5
        screenshot "evening-dialogue-v04.png"
        advance until screen "demo_end" timeout 120
        assert eval (route == "图书馆" and affection_b == 1 and affection_c == 1)
        assert eval (clue == "书页间的一小段安静")
        pause 0.7
        screenshot "library-ending.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回主菜单" pos (0.5, 0.5)
        pause until screen "main_menu" timeout 10
        assert screen "main_menu"

    testcase laboratory:
        run Start()
        advance until screen "choice" timeout 120
        $ renpy.display.interface.mouse_focused = True
        click "去实验室，看看声音如何被记录。" pos (0.5, 0.5)
        advance until "这是体验活动。要是必须先学会才能来，活动的顺序就反了。" timeout 60
        assert eval ('lab' in renpy.get_attributes('bg'))
        pause 0.5
        screenshot "lab-dialogue-v04.png"
        advance until screen "demo_end" timeout 120
        assert eval (route == "实验室" and affection_b == 0 and affection_c == 2)
        assert eval (clue == "两次敲击与一个新问题")
        pause 0.7
        screenshot "lab-ending.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回主菜单" pos (0.5, 0.5)

    testcase cafeteria:
        run Start()
        advance until screen "choice" timeout 120
        $ renpy.display.interface.mouse_focused = True
        click "去食堂，从一顿饭开始认识校园。" pos (0.5, 0.5)
        advance until "严格地说，我也是第一次来。我可以推荐一种方法：选闻起来最香的。" timeout 60
        assert eval ('cafeteria' in renpy.get_attributes('bg'))
        pause 0.5
        screenshot "cafeteria-dialogue-v04.png"
        advance until screen "demo_end" timeout 120
        assert eval (route == "食堂" and affection_b == 2 and affection_c == 1)
        assert eval (clue == "三只杯子的轻响")
        pause 0.7
        screenshot "cafeteria-ending.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回主菜单" pos (0.5, 0.5)

    testcase save_load_history:
        run Start()
        advance until screen "choice" timeout 120
        $ renpy.display.interface.mouse_focused = True
        click "保存" pos (0.5, 0.5)
        pause until screen "save" timeout 10
        assert screen "save"
        run FileSave(1, confirm=False)
        pause 1.0
        pause 0.7
        screenshot "save.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回" pos (0.5, 0.5)
        $ renpy.display.interface.mouse_focused = True
        click "去实验室，看看声音如何被记录。" pos (0.5, 0.5)
        advance
        assert eval (route == "实验室")
        run ShowMenu("load")
        run FileLoad(1, confirm=False)
        pause 1.0
        pause until screen "choice" timeout 10
        assert screen "choice"
        assert eval (route == "" and affection_c == 0)
        $ renpy.display.interface.mouse_focused = True
        click "去食堂，从一顿饭开始认识校园。" pos (0.5, 0.5)
        advance
        $ renpy.display.interface.mouse_focused = True
        click "历史" pos (0.5, 0.5)
        pause until screen "history" timeout 10
        assert screen "history"
        assert eval (len(_history_list) > 10)
        pause 0.7
        screenshot "history.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回" pos (0.5, 0.5)
        advance until screen "demo_end" timeout 120
        assert eval (route == "食堂" and affection_b == 2)
        $ renpy.display.interface.mouse_focused = True
        click "返回主菜单" pos (0.5, 0.5)

    testcase expressions_and_controls:
        run Start()
        advance until "你是不是在找报到点？" timeout 120
        assert eval ('happy' in renpy.get_attributes('classmate'))
        pause 0.7
        screenshot "character-happy.png"
        advance until "你已经对着同一棵树看了三次地图。它再热心，也没办法给你指路。"
        assert eval ('normal' in renpy.get_attributes('classmate'))
        $ renpy.display.interface.mouse_focused = True
        click id "quick_auto"
        assert eval (preferences.afm_enable)
        $ renpy.display.interface.mouse_focused = True
        click id "quick_auto"
        assert eval (not preferences.afm_enable)
        run ShowMenu("preferences")
        $ renpy.display.interface.mouse_focused = True
        click "标题菜单" pos (0.5, 0.5)
        pause until screen "confirm" timeout 10
        assert screen "confirm"
        $ renpy.display.interface.mouse_focused = True
        click "确定" pos (0.5, 0.5)
        pause until screen "main_menu" timeout 10
        assert screen "main_menu"

    testcase art_preview:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        $ renpy.display.interface.mouse_focused = True
        click "美术预览" pos (0.5, 0.5)
        pause until screen "sprite_gallery" timeout 10
        assert screen "sprite_gallery"
        $ renpy.display.interface.mouse_focused = True
        click "原图对照" pos (0.5, 0.5)
        pause until screen "art_preview" timeout 10
        assert screen "art_preview"
        pause 0.7
        screenshot "original-deepseek.png"
        $ renpy.display.interface.mouse_focused = True
        click "GPT 娘" pos (0.5, 0.5)
        pause 0.7
        screenshot "original-gpt.png"
        $ renpy.display.interface.mouse_focused = True
        click "Claude 娘" pos (0.5, 0.5)
        pause 0.7
        screenshot "original-claude.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回" pos (0.5, 0.5)
        pause until screen "sprite_gallery" timeout 10
        assert screen "sprite_gallery"
        $ renpy.display.interface.mouse_focused = True
        click "返回主菜单" pos (0.5, 0.5)
        pause until screen "main_menu" timeout 10
        assert screen "main_menu"

    testcase ai_expressions:
        $ renpy.display.interface.mouse_focused = True
        click "美术预览" pos (0.5, 0.5)
        pause until screen "sprite_gallery" timeout 10
        assert screen "sprite_gallery"
        assert eval (all(renpy.has_image((person, emotion)) for person in AI_CAST for emotion in AI_EXPRESSIONS))
        $ renpy.display.interface.mouse_focused = True
        click "DeepSeek 娘" pos (0.5, 0.5)
        $ renpy.display.interface.mouse_focused = True
        click "常态" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "normal")
        pause 0.25
        screenshot "deepseek-normal.png"
        $ renpy.display.interface.mouse_focused = True
        click "开心" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "happy")
        pause 0.25
        screenshot "deepseek-happy.png"
        $ renpy.display.interface.mouse_focused = True
        click "惊讶" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "surprised")
        pause 0.25
        screenshot "deepseek-surprised.png"
        $ renpy.display.interface.mouse_focused = True
        click "难过" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "sad")
        pause 0.25
        screenshot "deepseek-sad.png"
        $ renpy.display.interface.mouse_focused = True
        click "生气" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "angry")
        pause 0.25
        screenshot "deepseek-angry.png"
        $ renpy.display.interface.mouse_focused = True
        click "害羞" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "shy")
        pause 0.25
        screenshot "deepseek-shy.png"
        $ renpy.display.interface.mouse_focused = True
        click "Claude 娘" pos (0.5, 0.5)
        $ renpy.display.interface.mouse_focused = True
        click "常态" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "normal")
        pause 0.25
        screenshot "claude-normal.png"
        $ renpy.display.interface.mouse_focused = True
        click "开心" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "happy")
        pause 0.25
        screenshot "claude-happy.png"
        $ renpy.display.interface.mouse_focused = True
        click "惊讶" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "surprised")
        pause 0.25
        screenshot "claude-surprised.png"
        $ renpy.display.interface.mouse_focused = True
        click "难过" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "sad")
        pause 0.25
        screenshot "claude-sad.png"
        $ renpy.display.interface.mouse_focused = True
        click "生气" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "angry")
        pause 0.25
        screenshot "claude-angry.png"
        $ renpy.display.interface.mouse_focused = True
        click "害羞" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "shy")
        pause 0.25
        screenshot "claude-shy.png"
        $ renpy.display.interface.mouse_focused = True
        click "GPT 娘" pos (0.5, 0.5)
        $ renpy.display.interface.mouse_focused = True
        click "常态" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "normal")
        pause 0.25
        screenshot "gpt-normal.png"
        $ renpy.display.interface.mouse_focused = True
        click "开心" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "happy")
        pause 0.25
        screenshot "gpt-happy.png"
        $ renpy.display.interface.mouse_focused = True
        click "惊讶" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "surprised")
        pause 0.25
        screenshot "gpt-surprised.png"
        $ renpy.display.interface.mouse_focused = True
        click "难过" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "sad")
        pause 0.25
        screenshot "gpt-sad.png"
        $ renpy.display.interface.mouse_focused = True
        click "生气" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "angry")
        pause 0.25
        screenshot "gpt-angry.png"
        $ renpy.display.interface.mouse_focused = True
        click "害羞" pos (0.5, 0.5)
        assert eval (renpy.get_screen("sprite_gallery").scope["sprite_emotion"] == "shy")
        pause 0.25
        screenshot "gpt-shy.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回主菜单" pos (0.5, 0.5)
        run Start()
        advance until "地图不用一次记住。先找到下一个路口就好。" timeout 120
        assert eval ('happy' in renpy.get_attributes('guide'))
        pause 0.4
        screenshot "gpt-welcome.png"
        run MainMenu(confirm=False)

    testcase campus_backgrounds:
        $ renpy.display.interface.mouse_focused = True
        click "美术预览" pos (0.5, 0.5)
        $ renpy.display.interface.mouse_focused = True
        click "校园背景" pos (0.5, 0.5)
        pause until screen "campus_gallery" timeout 10
        assert screen "campus_gallery"
        assert eval (len(BACKGROUNDS) == 7 and all(not place['is_placeholder'] for place in BACKGROUNDS))
        $ renpy.display.interface.mouse_focused = True
        click "西门" pos (0.5, 0.5)
        assert eval (renpy.get_screen("campus_gallery").scope["campus_scene"] == "entrance")
        pause 0.4
        screenshot "campus-entrance-v04.png"
        $ renpy.display.interface.mouse_focused = True
        click "摩斯码路" pos (0.5, 0.5)
        assert eval (renpy.get_screen("campus_gallery").scope["campus_scene"] == "road")
        pause 0.4
        screenshot "campus-road-v04.png"
        $ renpy.display.interface.mouse_focused = True
        click "喷泉广场" pos (0.5, 0.5)
        assert eval (renpy.get_screen("campus_gallery").scope["campus_scene"] == "plaza")
        pause 0.4
        screenshot "campus-plaza-v04.png"
        $ renpy.display.interface.mouse_focused = True
        click "图书馆" pos (0.5, 0.5)
        assert eval (renpy.get_screen("campus_gallery").scope["campus_scene"] == "library")
        pause 0.4
        screenshot "campus-library-v04.png"
        $ renpy.display.interface.mouse_focused = True
        click "教三楼" pos (0.5, 0.5)
        assert eval (renpy.get_screen("campus_gallery").scope["campus_scene"] == "lab")
        pause 0.4
        screenshot "campus-lab-v04.png"
        $ renpy.display.interface.mouse_focused = True
        click "风味餐厅" pos (0.5, 0.5)
        assert eval (renpy.get_screen("campus_gallery").scope["campus_scene"] == "cafeteria")
        pause 0.4
        screenshot "campus-cafeteria-v04.png"
        $ renpy.display.interface.mouse_focused = True
        click "傍晚道路" pos (0.5, 0.5)
        assert eval (renpy.get_screen("campus_gallery").scope["campus_scene"] == "evening")
        pause 0.4
        screenshot "campus-evening-v04.png"
        $ renpy.display.interface.mouse_focused = True
        click "返回立绘" pos (0.5, 0.5)
        $ renpy.display.interface.mouse_focused = True
        click "返回主菜单" pos (0.5, 0.5)
        pause until screen "main_menu" timeout 10
        assert screen "main_menu"
