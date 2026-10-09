# 美术方向 · 2026-10-09

## 用户最终选择

人物直接采用网络上现成的 AI 娘原有形象，包括 DeepSeek 娘、GPT 娘、Claude 娘。不要把她们改造成林晴/沈知遥的校园服装，不改发型、身体特征、饰品或原有比例。此前生成的两张原创校园角色设计已撤出美术预览，保留在 `source_assets/characters/concepts/` 作为废弃方向记录。

## 已导入的原样图片

来自 https://github.com/Apprentice-Geo/AI-Fanworks/tree/main/ApprenTice/references 。收录库说明此目录原样保存 ZipZipPipe《大 AI 与小 AI 们》的素材；我们直接复制 PNG，没有使用 AI 重画，没有裁剪、换装或调色。游戏预览只将 2160×3840 等比例显示为 384×683。

- DeepSeek：蓝白女仆装、鲸鳍耳、鲸尾。上善无形原角色，ZipZipPipe 二次设计。
- GPT：白发、龙角、龙翼、龙尾和白色长裙。
- Claude：橙发、花形饰品、书本和米白/黑/橙配色。

每张原始文件、来源链接、哈希和改动记录见 `source_assets/characters/community-originals/registry.json`。用于预览的图与保存的源图字节一致。

作者与许可来源：原作 https://www.bilibili.com/video/BV1tE9XBbErS/ ；作者 https://space.bilibili.com/4168597 ；收录者 ApprenTice https://space.bilibili.com/634972797 。已保存收录者 README 的原文，其中对原作声明 CC BY-NC-SA 4.0（非商业、署名、相同方式共享）。本次无法实时读取 B 站原视频及 Pixiv 原帖，不把收录库说明写成已直接核验原作者声明。保留全部来源，不把素材标为本工程原创或模型厂商官方角色；商业用途不在该说明的授权范围内。

v0.2 阶段仅提供白底原图预览。v0.3 已完成下文所述透明表情编辑与剧情替换；白底原图移至“美术预览 → 原图对照”保留展示。

## 已接入的校园背景

入口：北邮西土城校区西门，参考 https://vi.bupt.edu.cn/info/1102/1055.htm 。

道路：西土城校区摩斯码路，参考 https://vi.bupt.edu.cn/info/1102/1060.htm 。

两张背景由内置 imagegen 工具依据官网图片绘制，已接入主菜单和前两场剧情。人物图未使用 imagegen 改写。参考照片保存在开发素材目录，不进入游戏发行包。图像不是实拍，不承诺与 2026 年现状逐项一致；树木、光照和铺装细节包含艺术化处理。

生成图原件位于 `source_assets/backgrounds/generated/`，运行版本位于 `game/images/backgrounds/illustrated/`。生成提示词（包括已弃用的校园人物稿）完整保存在 `docs/art-prompts-v1.json`。所有图像文件均由内置 imagegen 生成或原样复制，没有使用 CLI 生图。

## v0.3：剧情透明立绘与表情

用户进一步要求替换剧情占位人物并搭配表情。已使用内置 imagegen 以三张原图为编辑参考制作透明图集：每位常态、开心、惊讶、难过、生气、害羞，共 18 帧。保留原设的发型、服装、配饰及身体特征；编辑版本不是原图逐像素复制，不能再标成“未修改原图”。原始图片仍原样保存在此前目录及原图对照页面。

剧情：DeepSeek 娘担任同班同学，Claude 娘担任实验室学姐，GPT 娘担任新增迎新志愿者。玩家继续第一人称。旧占位立绘全部移入 `source_assets/characters/legacy-placeholders/`，游戏不再引用。

运行素材：`game/images/characters/ai-girls/{DeepSeek,Claude,ChatGPT}-v1.png`。源版本及来源登记：`source_assets/characters/expression-atlases/`。实际提示词：`docs/ai-expression-prompts.json`。引擎直接裁取图集各格，不另行修改 PNG。

主菜单“美术预览”可以查看全部表情，“原图对照”查看未修改素材。三条剧情分支、表情切换、透明合成和双人站位均纳入原生引擎测试。

## v0.4：校园背景补齐

全部七个剧情背景与菜单衬底均已使用北邮西土城实景参考绘图。新增五张与既有西门/道路画风统一，详见 `campus-backgrounds.md`。此前关于其余背景仍占位的记录属于历史阶段。
