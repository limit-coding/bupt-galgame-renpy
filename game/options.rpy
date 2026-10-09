define config.name = "北邮物语：开学第一天"
define config.version = "0.2.0"
define build.name = "BUPTStories"
define config.save_directory = "BUPTStories-FirstDay-2026"
define config.window_icon = "gui/window_icon.png"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.default_text_cps = 32
define config.default_afm_time = 12
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = fade
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define gui.about = "原创校园视觉小说原型。\n故事与人物均为虚构，与学校官方无隶属关系。\n西门与摩斯码路背景参考官网照片经 AI 绘制，非实景照片。其余为占位背景。剧情立绘仍为占位；美术预览直接展示 ZipZipPipe 社区 AI 娘原样参考图，按收录库注明的非商业条件保存来源。\n引擎：Ren’Py 8.5.3；字体：Noto Sans SC（OFL）。"
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.pyc', None)
    build.classify('game/saves/**', None)
    build.classify('game/testcases.rpy', None)
    build.classify('game/testcases.rpyc', None)
    build.classify('.git/**', None)
    build.classify('.gitignore', None)
    build.classify('**/.DS_Store', None)
    build.classify('**/.gitkeep', None)
    build.classify('artifacts/**', None)
    build.classify('tests/**', None)
    build.classify('assets/**', None)
    build.classify('source_assets/**', None)
    build.classify('tools/**', None)
    build.classify('Start.command', None)
    build.classify('errors.txt', None)
    build.classify('traceback.txt', None)
    build.classify('log.txt', None)
    build.documentation('README.md')
    build.documentation('docs/**')
