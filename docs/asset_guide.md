> 2026-10-09 更新：全部七个背景已接入官网实景参考绘制版；人物改为现有 AI 娘原形象方向。以下原型规格保留，最新状态及署名见 `art-direction.md`。

# 素材与照片导入

## 当前资产

7 个背景场景均为北邮西土城官方照片参考绘制，包含同机位的摩斯码路日间/傍晚两版。简易占位图已全部移出运行目录。人物使用社区 AI 娘原设的透明六表情编辑版本，共 3 张图集 / 18 帧。原图和编辑版分别保留，来源及修改记录见 `art-direction.md`。没有使用其他商业游戏资产。

## 照片清单

| ID | 照片建议 | 剧情位置 |
|---|---|---|
| entrance | 西土城校区入口，白天，完整入口与前景 | Scene 1 / 主菜单 |
| road | 有纵深的校内道路、树荫，白天 | Scene 2 |
| plaza | 校园广场或教学楼前开放空间 | Scene 3 |
| library | 图书馆外景或可使用的阅览空间 | 图书馆路线 |
| lab | 经允许拍摄的实验室/教学空间，避开屏幕资料 | 实验室路线 |
| cafeteria | 食堂外景或不拥挤的内部空间 | 食堂路线 |
| evening | 傍晚校园道路，尽量与白天道路为同一机位 | Scene 5 |

每个地点 1–3 张横向照片，优先 1920×1080 或更大。人物站在左右两侧、底部有对话框，因此主体建筑尽量位于中上部；避免极端广角和过曝天空。照片还需真实地点、时段、摄影者及使用许可。收到照片后再核对注册表中的真实地点，目前带“待确认”的名称不当作已核实信息。

## 导入

在工程目录运行：

```sh
python3 tools/import_background.py /绝对路径/原图.jpg --id entrance --source "摄影者姓名；本人拍摄并授权用于此 Demo" --focal 0.5 0.5
```

导入会按 EXIF 修正方向、保持比例裁剪为 1280×720，输出 RGB PNG；原始文件不改动，原图副本以内容哈希命名并保存。焦点坐标从 0 到 1，可调整裁剪重心。运行图片同步至登记表的 `game_path`，并同步更新 `game/backgrounds.json`，下次启动即可显示照片；不需要 AI 风格化。

处理图不保留 EXIF；原图副本仍含原始信息，始终不进入玩家发行包。工具不自动识别人脸；导入前后需检查并妥善处理可识别人脸、学生证、电话号码、车牌和实验资料。需要遮挡时制作一份处理副本，保留原始照片不变。

所有背景元数据在 `assets/backgrounds/registry.json`，运行清单在 `game/backgrounds.json`。修改登记后应同步运行清单；验证脚本会检查两者一致。新地点先新增 ID、脚本图像声明及剧情引用；现有 ID 的照片直接替换，无需修改剧情。多次导入保留原图与不同裁剪版本，当前注册表指向最新版本；版本历史由 Git 保存。

## 立绘

运行图位于 `game/images/characters/ai-girls/`，每张为 1254×1254 RGBA、3 列 × 2 行图集。按行排列 normal/happy/surprised/sad/angry/shy。Ren’Py 在运行时裁取 418×627 单格并显示为 460×690；不改写图集。DeepSeek 对应 classmate，Claude 对应 senior，GPT 对应 guide。源图集、哈希、参考图与提示词登记在 `source_assets/characters/expression-atlases/registry.json`。原来的程序立绘已移至开发素材的 `legacy-placeholders/`，不会被运行或打包。

## 音频

将有使用许可的 OGG 文件放入 `game/audio/`：menu.ogg、daily.ogg、evening.ogg、campus.ogg、button.ogg。背景音乐/环境声循环播放；按钮文件应简短。当前文件均为空缺。代码在文件不存在时静音，不需要虚构授权或用空白音频伪装完成。

## 第三方许可

Noto Sans SC：SIL Open Font License 1.1，来自 Google Fonts 官方仓库，完整许可见 `licenses/NotoSansSC-OFL.txt`。Ren’Py 及其模板/依赖许可见 `licenses/RenPy-LICENSE.txt` 和发行包引擎许可证。新增素材必须记录来源、作者、许可和修改内容后再打包。
