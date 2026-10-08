# 北邮物语：开学第一天

基于 Ren’Py 8.5.3 的中文 2D 视觉小说原型，版本 0.1.0。人物和剧情均为原创虚构；非学校官方作品。

**当前是功能原型。所有场景和人物图都是明确标注的占位素材，不是北邮照片，也不是最终日式立绘。当前无配乐，音频接口在缺文件时自动静音。**

## 立即试玩

- 本机 macOS：双击工程内 `Start.command`；已安装的 SDK 位于 `/Users/limit/Tools/renpy-8.5.3-sdk`。
- Windows：解压随交付提供的 `BUPTStories-0.1.0-win.zip`，运行 `BUPTStories.exe`，无需安装 Python 或 Ren’Py。
- macOS 独立包：解压 `BUPTStories-0.1.0-mac.zip`，打开 `BUPTStories.app`。包未做开发者签名/公证；如系统阻止，可在确认来源后使用系统“仍要打开”流程。
- 源码开发：从 https://www.renpy.org/latest.html 下载稳定版 SDK，在 Ren’Py 启动器的设置中把项目父目录选为本工程的上一级，再选择 `BUPT-Galgame` → 启动项目。
- 命令行：`"$RENPY_SDK/renpy.sh" /绝对路径/BUPT-Galgame`。Windows 可直接使用启动器。

存档默认位于 Ren’Py 的用户存档目录，不要求写入程序安装位置。本机为 `~/Library/RenPy/BUPTStories-FirstDay-2026/`，Windows 为 `%APPDATA%/RenPy/BUPTStories-FirstDay-2026/`。自动化测试另用独立存档目录。

## 已实现

- 1280×720、16:9、自适应窗口/全屏；Noto Sans SC 中文字体。
- 自定义主菜单、半透明对话框、选项、章节标识、路线结束页。
- 五个场景；图书馆、实验室、食堂三条分支；两位配角好感标记与不同的回忆线索。
- 三位可改名原创角色；主角第一人称、两位配角同屏；每人五种表情资源接口。
- 7 张占位背景、背景淡入淡出/缓慢缩放、立绘左右位置/切换/隐藏。
- Ren’Py 原生保存/读取、快存/快读、回退、历史、快进、自动、设置、帮助和退出。
- 背景来源登记及照片导入工具；保留原图，导入照片后无需 AI 风格化即可使用。
- 主菜单/日常/傍晚音乐、环境音及按钮声音接口，缺少音频不影响运行。

共 181 段对话、约 4,151 个引擎统计字符（包含所有路线）。单次只经过一条路线，预计约 8–12 分钟，未进行真人计时；10–20 分钟目标将在实测后扩写。

## 操作

鼠标左键 / 空格 / Enter 继续；鼠标滚轮向上回退；Esc 或右键打开菜单；H 隐藏界面；Ctrl 临时快进已读文本。底部也可直接选择历史、保存、自动、快进、设置、隐藏。隐藏后点击或按 H 恢复。

## 目录

- `game/`：运行用脚本、中文字体、图片、可选音频。
- `assets/backgrounds/raw/`：原始照片的只增不改副本。当前无用户照片。
- `assets/backgrounds/processed/`：导入工具生成的裁剪版本。
- `assets/backgrounds/registry.json`：背景唯一 ID、真实地点、时段、来源、版本、剧情用途及路径。
- `source_assets/characters/`、`audio/`、`ui/`：未来的美术制作源文件。
- `tools/`：导入、资源检查、占位图生成、测试与构建工具。
- `tests/`、`game/testcases.rpy`：照片导入测试、Ren’Py 引擎交互测试。
- `artifacts/`：本次实际运行的测试报告。
- `docs/`：设计、素材说明、阶段进度、测试结果及许可证。

背景统一采用任务书首先指定的 `assets/backgrounds/` 路径，不再复制一套 `source_assets/backgrounds/`，避免原图归属混乱。

## 验证与构建

安装导入工具依赖：`python3 -m pip install -r tools/requirements.txt`。游戏运行本身不需要安装这些依赖。

在工程目录执行 `./tools/verify.sh`。可通过 `RENPY_SDK` 指定 SDK 路径。执行原生图形测试时需要可用的桌面环境；测试使用专用存档，不覆盖玩家存档。

执行 `./tools/build.sh`，Windows 和 macOS 包输出到父目录 `renpy-releases/`。引擎测试脚本、原始照片、开发测试数据不会进入玩家包。

试玩截图位于 `docs/screenshots/`。详见 `docs/test_results.md`。macOS 上已实际运行引擎；Windows 包仍需 Windows 真机复测。

## 下一步素材

优先提供横向原图：校门、校园道路、广场、图书馆、实验室或教学楼、食堂、傍晚道路各 1–3 张。建议宽度不低于 1920 像素，保留原图、不在照片上叠字。每组注明真实地点、拍摄时间和摄影者/使用许可。

先用一组照片完成入口 → 道路 → 广场 → 傍晚的连续观感，再完善日式正式立绘与统一配乐。详细规范见 `docs/asset_guide.md`。
