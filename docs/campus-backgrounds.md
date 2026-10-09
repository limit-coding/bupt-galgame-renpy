# 北邮实景参考背景 · v0.4

七个剧情场景均已替换为统一动漫背景。全部地点位于北邮西土城校区，参照学校官方照片绘制，保留主要建筑形态；季节、光照、取景扩展与细节经过艺术处理。以下链接是参考依据，不表示北邮认可本同人作品。

| 场景 | 对应真实地点 | 官方参考 |
|---|---|---|
| entrance | 西土城校区西门 | [来源](https://vi.bupt.edu.cn/info/1102/1055.htm) |
| road | 西土城校区摩斯码路 | [来源](https://vi.bupt.edu.cn/info/1102/1060.htm) |
| plaza | 未来学习大楼前喷泉广场 | [来源](https://vi.bupt.edu.cn/info/1102/1058.htm) |
| library | 西土城校区图书馆外景 | [来源](https://vi.bupt.edu.cn/info/1102/1061.htm) |
| lab | 西土城校区教三楼外景 | [来源](https://vi.bupt.edu.cn/info/1102/1064.htm) |
| cafeteria | 西土城校区综合餐厅楼一层风味餐厅 | [来源](https://hq.bupt.edu.cn/info/1010/1380.htm) |
| evening | 西土城校区摩斯码路（傍晚光照版本） | [来源](https://vi.bupt.edu.cn/info/1102/1060.htm) |

## 绘制与剧情

使用内置 imagegen，以官方照片为地点参考、已有摩斯码路绘图为风格参考。傍晚道路直接由白天版本调整光照，保持构图连续。完整提示词见 `campus-background-prompts-v04.json`；前两张见 `art-prompts-v1.json`。

图书馆事件改为借阅后在馆外交流；实验室路线改为教三楼前的声音体验，画面没有冒充真实实验室内部。食堂采用后勤部 2025-09-08 公告中的综合餐厅楼一层环境照片，原图为两幅室内照片拼版，绘制版合成单一视角，部分细节为补全。喷泉参考图的临时 70 周年数字装置未保留。

## 资源与运行

- 运行背景：`game/images/backgrounds/illustrated/`，共 7 张。
- 生成原件：`source_assets/backgrounds/generated/`。
- 官方参考照片：`assets/backgrounds/references/`，原文件保留，未修改。
- 完整登记：`assets/backgrounds/registry.json`；运行清单：`game/backgrounds.json`。
- 简易背景与原菜单图归档于 `source_assets/backgrounds/legacy-placeholders/`，不进入玩家包。

主菜单 → 美术预览 → 校园背景，可以逐张查看。各剧情场景左上角显示地点。菜单的衬底也使用北邮背景。导入新照片时，工具同时更新登记与运行清单，照片路径不再由脚本硬编码。

## 来源与使用记录

照片来自北邮视觉形象识别系统及后勤部，原页保留学校版权声明；公开可见不等于开放再分发许可。参考原照片仅留在开发素材，不进入玩家包。绘制版本的来源与修改方式均保留在登记表；没有据此宣称商业授权已核验。参考照片拍摄日期未完全明确，不作为 2026 年校园现状记录。
