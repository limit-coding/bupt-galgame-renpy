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

当前图为白底常态参考图，所以放在主菜单的“美术预览”中原样展示。它们尚不是透明五表情组，不能声称已经完成剧情立绘替换。后续优先寻找同设定的透明源图；若需技术抠图或补表情，也必须保留原有造型，不得再次自行改设计。

## 已接入的校园背景

入口：北邮西土城校区西门，参考 https://vi.bupt.edu.cn/info/1102/1055.htm 。

道路：西土城校区摩斯码路，参考 https://vi.bupt.edu.cn/info/1102/1060.htm 。

两张背景由内置 imagegen 工具依据官网图片绘制，已接入主菜单和前两场剧情。人物图未使用 imagegen 改写。参考照片保存在开发素材目录，不进入游戏发行包。图像不是实拍，不承诺与 2026 年现状逐项一致；树木、光照和铺装细节包含艺术化处理。

生成图原件位于 `source_assets/backgrounds/generated/`，运行版本位于 `game/images/backgrounds/illustrated/`。生成提示词（包括已弃用的校园人物稿）完整保存在 `docs/art-prompts-v1.json`。所有图像文件均由内置 imagegen 生成或原样复制，没有使用 CLI 生图。
