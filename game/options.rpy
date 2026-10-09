define config.name = "北邮物语：开学第一天"
define config.version = "0.4.0"
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
define gui.about = "原创校园视觉小说原型。\n故事与人物均为虚构，与学校官方无隶属关系。\n全部七个场景均参考北邮西土城校区官方照片绘制：西门、摩斯码路、未来学习大楼喷泉、图书馆、教三楼、综合餐厅一层、傍晚摩斯码路。季节与光照为艺术处理，非实景照片。实验室体验安排在教三楼外，为虚构活动。剧情已使用 DeepSeek / GPT / Claude 娘透明六表情立绘，由原图经 AI 编辑；原图对照仍保留原始文件。原设：ZipZipPipe；DeepSeek 原角色：上善无形；素材收录：ApprenTice / AI-Fanworks。\n收录库声明原作 CC BY-NC-SA 4.0；原作者页面本次未直接核验。原作 bilibili.com/video/BV1tE9XBbErS/；收录 github.com/Apprentice-Geo/AI-Fanworks。按该说明保留署名、非商业与相同方式共享条件。\n引擎：Ren’Py 8.5.3；字体：Noto Sans SC（OFL）。"
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
