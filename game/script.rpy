# 《北邮物语：开学第一天》原创虚构剧情。
# 校园背景含官网参考绘图与占位场景；AI 娘以社区同人角色身份出演虚构校园故事。
label start:
    $ quick_menu = True
    $ affection_b = 0
    $ affection_c = 0
    $ route = ""
    $ clue = ""
    $ chapter = "01 / 初入北邮"
    $ play_optional('daily')
    $ play_optional('campus', 'ambience')
    scene bg entrance at establishing
    with fade
    show screen chapter_stamp
    "九月的风绕过行李箱，把我手里的报到单翻到了背面。"
    "地址早就背熟了。可当导航提示“您已到达目的地”的时候，我还是站在原地，重新看了一遍。"
    p "北京邮电大学……真的到了。"
    "出发前，我在脑子里排练过很多次这一幕。最好是很从容地走进校门，像一个已经知道未来会去哪里的人。"
    "实际情况是：背包带缠住了耳机线，手机只剩百分之十七的电，我甚至没想好先把左脚还是右脚迈进去。"
    "家里的群聊弹出一条消息：到了记得说一声。"
    p "到了，一切顺利。"
    "发送成功。我把那点小小的慌张留在了输入框外面。"
    "身边的人拖着箱子走过去，轮子碾过地砖的声音此起彼伏。有人和父母挥手，有人举着手机找同伴。"
    "我忽然意识到，对我来说崭新的一天，对这座校园而言，不过是又一个普通的早晨。"
    "这样的想法反而让我放松了一点。至少，我不必在第一天就成为某个了不起的人。"
    p "先找到报到的地方吧。"
    "我展开折过四次的纸质地图。地图很平，现实却有树、有岔路，还有一群挡住路牌的人。"
    show guide normal at stage_center
    with dissolve
    g "新同学？我是 GPT 娘，今天的迎新志愿者。报到点顺着这条路走。"
    p "太好了。我刚才差点把地图研究成抽象画。"
    show guide happy
    with Dissolve(.15)
    g "地图不用一次记住。先找到下一个路口就好。"
    p "你手边那朵小云，也能帮忙导航吗？"
    show guide surprised
    with Dissolve(.15)
    g "它？它刚才还把我带到同一棵树下两次。"
    show guide sad
    with Dissolve(.15)
    g "第一次当志愿者的时候，我也担心自己帮倒忙。"
    p "可你还是站在这里了。"
    show guide shy
    with Dissolve(.15)
    g "因为有人对我说过：可以先陪别人走一小段。"
    show guide angry
    with Dissolve(.15)
    g "不过有一条要认真说——别一边过路口一边低头看地图。"
    p "收到。先看路，再看地图。"
    show guide happy
    with Dissolve(.15)
    g "那就祝你开学顺利。迷路了再来找我。"
    hide guide
    with dissolve
    "就在我收好地图的时候，旁边传来一声忍不住的笑。"
    $ chapter = "02 / 校园偶遇"
    scene bg road
    with dissolve
    show classmate happy at stage_right
    with dissolve
    b "你是不是在找报到点？"
    p "有这么明显吗？"
    show classmate normal
    with Dissolve(.15)
    b "你已经对着同一棵树看了三次地图。它再热心，也没办法给你指路。"
    p "也可能我正在研究校园植被分布。"
    show classmate happy
    with Dissolve(.15)
    b "那研究员同学，你的报到单拿反了。"
    "我低头看了一眼，把那张纸默默转了回来。"
    p "好吧。我叫[protagonist_name]，新生。"
    b "[classmate_name]。也是新生，不过比你早到一会儿。"
    "她晃了晃手机，屏幕上是班级群里刚发的集合提醒。"
    p "等等，这个头像……你是群里那个一直回复‘收到’的人？"
    show classmate surprised
    with Dissolve(.15)
    b "你是那个问‘报到当天需要带网线吗’的人？"
    p "我的网络焦虑比本人提前入学了。"
    show classmate happy
    with Dissolve(.15)
    b "那就对上了。同班同学，欢迎线下连接成功。"
    "她把手机收进口袋，顺手指了指前面的路。"
    b "一起走吧。先办手续，下午再慢慢认路。"
    p "你看起来一点都不紧张。"
    show classmate normal
    with Dissolve(.15)
    b "因为我紧张的时候话比较多。你要是一直不打断我，我可以介绍到明天。"
    "我看着她。她也看着我。"
    show classmate shy
    with Dissolve(.15)
    b "好啦，被你发现了。我刚才走错过一次，不想再一个人走错第二次。"
    p "那我们算是互相提供冗余备份？"
    b "听起来很可靠。虽然我不知道你在说什么。"
    "沿着树荫往前走的时候，陌生的道路开始有了参照物。不是楼号，而是刚刚在哪个转角笑过。"
    "报到、核对信息、安置行李。一上午在反复确认和签字之间，很快过去了。"
    "等我们重新回到路边，阳光已经把树影从路的这一侧推到了另一侧。"
    $ chapter = "03 / 第一次选择"
    scene bg plaza
    show classmate normal at stage_left
    with fade
    b "下午还有一点自由时间。你想先去哪儿？"
    p "我原本的计划是，按地图从左到右逛完。"
    show classmate surprised
    with Dissolve(.15)
    b "那要是地图拿反了呢？"
    p "从右到左。很有弹性的计划。"
    show classmate happy
    with Dissolve(.15)
    b "不如选一个真正想去的地方。图书馆、实验室，或者食堂？"
    "她说着，从包里抽出一张浅蓝色的小卡片。卡片一角有一串手写的数字。"
    p "这是？"
    show classmate normal
    with Dissolve(.15)
    b "路上捡到的。背面写着‘把今天的声音留给明天’，旁边还有一个活动联系人的名字。"
    p "[senior_name]……"
    b "我问过了，是位学姐。今天在做一个面向新生的小体验，说我们方便的话可以把卡片带回去。"
    p "声音？和实验室有关系吗？"
    b "也可能是校园寻宝。她的回复只有一句：‘先找到一个你愿意停下来的地方。’"
    "我把卡片翻了个面。那些数字不像密码，更像一个被认真记下来的时间。"
    "第一天下午，没有标准答案。倒也不错。"
    menu:
        "去图书馆，找一处安静的地方。":
            $ route = "图书馆"
            $ affection_b += 1
            jump library_event
        "去实验室，看看声音如何被记录。":
            $ route = "实验室"
            $ affection_c += 1
            jump lab_event
        "去食堂，从一顿饭开始认识校园。":
            $ route = "食堂"
            $ affection_b += 2
            jump cafeteria_event

label library_event:
    $ chapter = "04 / 书页之间"
    scene bg library at establishing
    show classmate normal at stage_left
    with dissolve
    "走近图书馆时，我们不约而同地放轻了脚步。连拖鞋擦过地面的声音，都像有了标点。"
    p "我以前想象中的大学，大部分时候就是这样的。"
    b "一排排书，还有一个特别努力的自己？"
    p "差不多。最好手边还有一杯永远不会凉的咖啡。"
    show classmate happy
    with Dissolve(.15)
    b "听起来，你对咖啡的要求比对自己的还高。"
    "她在一排书前停下来。原本热闹的话音，降成了只有我们能听见的轻声。"
    b "其实我有一点怕图书馆。"
    p "为什么？"
    show classmate sad
    with Dissolve(.15)
    b "每次看见那么多书，就觉得别人已经懂了很多，而我连从哪一本开始都不知道。"
    "我望向那些并不熟悉的书脊。刚才觉得让人安心的整齐，此刻突然也显得有些遥远。"
    p "也许这里这么大，就是因为谁都不可能全部懂。"
    show classmate normal
    with Dissolve(.15)
    b "你这句可以印在新生安慰手册上。"
    p "署名记得写对。"
    "一道声音从旁边传来，语气平稳，像替这句话补上了一个句号。"
    show senior normal at stage_right
    with dissolve
    c "先选一个问题，比先选一整排书更容易。"
    b "学姐？你是[senior_name]学姐吗？我们带着那张卡片。"
    c "是我。谢谢。我来查一点资料，没想到先遇到了失物招领。"
    "她接过卡片，却没有立刻收起来，而是把背面的空白朝向我们。"
    c "这是一份声音日记的记录卡。数字是录音的时刻，不是答案。"
    p "我还以为会是一道入学测试。"
    show senior happy
    with Dissolve(.15)
    c "你已经有很多正式测试了。这个不计分。"
    b "那‘把今天的声音留给明天’是什么意思？"
    c "我们在做一个很小的声音记录练习。不同的人，在同一个地方，往往会注意到完全不同的事。"
    p "这里很安静，也可以记录吗？"
    c "可以。空调、翻页、椅子移动。安静不是没有声音，而是声音之间有空隙。"
    "我们安静了一会儿。远处有一页纸被翻过去，轻得像有人悄悄修改了今天的结尾。"
    show classmate happy
    with Dissolve(.15)
    b "我想记这个。第一天不用什么都懂，可以先翻开第一页。"
    c "那就写下来。比我原先的活动介绍好。"
    "[classmate_name]认真写了半行，又把笔递给我。"
    p "我写：今天找到一个可以慢慢想的地方。"
    $ clue = "书页间的一小段安静"
    $ affection_c += 1
    show senior normal
    with Dissolve(.15)
    c "下次想来看记录怎么处理，可以来找我。先问问题，不急着给自己定方向。"
    b "那我下次带着问题来，问题很多也可以？"
    show senior happy
    with Dissolve(.15)
    c "可以。不过建议先带最想问的一个。"
    "离开前，我没有制定读完一百本书的计划。只记下了一个以后愿意再来的位置。"
    hide senior
    hide classmate
    with dissolve
    jump evening_scene

label lab_event:
    $ chapter = "04 / 噪声里的信号"
    scene bg lab
    hide classmate
    show senior normal at stage_right
    with fade
    "我们按约定来到学姐所在的活动房间。门开着，桌上放着耳机、一台电脑和几张画着波形的纸。"
    c "你们就是捡到卡片的新生？谢谢，进来坐。"
    show classmate happy at stage_left
    with dissolve
    b "卡片完好无损。我们还附赠了两位好奇的体验者。"
    show senior happy
    with Dissolve(.15)
    c "那今天的招募效率比预期高。"
    p "我们什么都还没学，会不会打扰？"
    show senior normal
    with Dissolve(.15)
    c "这是体验活动。要是必须先学会才能来，活动的顺序就反了。"
    "她没有直接打开复杂的软件，而是把两张纸摆到我们面前。"
    c "假设左边是你想听的声音，右边是旁边经过的车。录在一起以后，电脑怎么知道你想留下哪一个？"
    p "把比较吵的那个去掉？"
    show classmate surprised
    with Dissolve(.15)
    b "那我可能会被去掉。"
    show senior happy
    with Dissolve(.15)
    c "所以‘吵’不是一个足够清楚的标准。我们得先告诉它，想要的信号是什么。"
    "我看了看纸上的线条。它们不再像一道等着我做错的题，而像两种还没听懂的语言。"
    p "也就是说，先弄清楚问题，再决定用什么方法？"
    show senior normal
    with Dissolve(.15)
    c "对。有时候最费时间的不是写程序，是确认自己到底在问什么。"
    b "那如果我的问题是‘怎样在大学里不迷路’呢？"
    c "你指的是实际道路，还是别的？"
    show classmate normal
    with Dissolve(.15)
    b "……都有一点。"
    "学姐停了一下，没有用一句轻巧的话把这个问题带过去。"
    c "实际道路可以多走几次。其他事情，我也还在试。"
    p "我以为学姐们已经都有明确答案了。"
    show senior sad
    with Dissolve(.15)
    c "我昨天还花了很久，才发现结果不对是因为读错了一份文件。"
    show senior shy
    with Dissolve(.15)
    b "原来高手也会这样！"
    show senior angry
    with Dissolve(.15)
    c "会。而且文件名还是我自己起的。"
    "她指着纸角写下的一行字：先检查输入。我们三个一起笑了。"
    show senior normal
    with Dissolve(.15)
    c "不过，今天我们只观察，不采集别人的谈话。以后真的录音，要先说明用途，取得同意。"
    p "那我们可以从不用打扰任何人的声音开始？"
    c "比如你自己翻一页纸，或者轻轻敲一下桌面。"
    "我敲了两下桌面。短促的声音消失得很快，屏幕上的线条却替它留下了形状。"
    show classmate surprised
    with Dissolve(.15)
    b "像两座很小的山。"
    p "也像某个人发出了两次不太确定的问候。"
    show senior happy
    with Dissolve(.15)
    c "可以。科学负责描述，怎么记住它，可以由你决定。"
    "她把一张空白记录卡递给我。我写下今天的日期，又在‘内容’一栏停了几秒。"
    p "第一条信号：有人说，可以从不会开始。"
    $ clue = "两次敲击与一个新问题"
    $ affection_c += 1
    c "这个不是实验结论。不过，作为日记，很好。"
    b "下次我们再来，可以把‘不知道’带来吗？"
    c "当然。记得把问题写具体一点就行。"
    "走出房间的时候，我仍然说不出自己未来想研究什么。但我开始觉得，不知道也可以是一个入口。"
    hide senior
    hide classmate
    with dissolve
    jump evening_scene

label cafeteria_event:
    $ chapter = "04 / 今日推荐"
    scene bg cafeteria
    show classmate happy at stage_right
    with dissolve
    b "欢迎来到我的优先级最高的校园探索项目。"
    p "你刚才不是说图书馆也很想去吗？"
    b "求知欲和食欲可以同时存在。只是现在后者的提醒比较响。"
    "她看着不同窗口前的队伍，露出了比刚才看地图还认真的表情。"
    p "你有推荐吗？"
    show classmate normal
    with Dissolve(.15)
    b "严格地说，我也是第一次来。我可以推荐一种方法：选闻起来最香的。"
    "我们各自选好午饭，找到一张空桌。盘子碰到桌面的瞬间，我才发现自己已经饿了很久。"
    p "刚才太忙了，连饿都忘记了。"
    b "所以人生需要同伴，按时提醒你吃饭。"
    "她举起水杯，像要宣布一件很正式的事。"
    show classmate happy
    with Dissolve(.15)
    b "为今天顺利完成报到，也为没有继续研究那棵树。"
    p "那棵树在我的学术生涯里已经留下了深刻影响。"
    "杯子轻轻碰在一起。窗外有人骑车经过，车铃隔着玻璃只剩下一点模糊的响动。"
    "吃到一半，[classmate_name]拿出那张卡片，给学姐发去消息。没多久，一个抱着笔记本的人在桌边停下。"
    show classmate normal at stage_left
    show senior normal at stage_right
    with dissolve
    c "你们好，我是[senior_name]。谢谢帮我保管卡片。这里还可以坐吗？"
    b "当然！学姐也还没吃饭？"
    show senior sad
    with Dissolve(.15)
    c "刚才忙着整理活动记录，忘了看时间。"
    show classmate angry
    with Dissolve(.15)
    b "不可以。学姐也需要按时吃饭。"
    show senior surprised
    with Dissolve(.15)
    "她说得太认真，我和学姐都愣了一下。"
    show classmate shy
    with Dissolve(.15)
    b "啊，对不起，我不是在训人……"
    show senior happy
    with Dissolve(.15)
    c "没关系。这个提醒比手机上的有效。"
    p "她刚刚给自己定义的角色，就是按时提醒同伴吃饭。"
    show classmate happy
    with Dissolve(.15)
    b "业务范围扩展了。"
    "学姐坐下来，向我们解释卡片上的声音记录活动。周围的声音很多：餐盘、脚步，还有偶尔盖过一切的笑声。"
    p "如果在这里录，会不会全是噪声？"
    c "取决于你想记录什么。不过人多的地方涉及别人的谈话，今天只用文字记观察就好。"
    b "我想记‘第一天有人一起吃饭’。这算一种声音吗？"
    "学姐想了想，轻轻用自己的水杯碰了一下我们的杯子。"
    show senior happy
    with Dissolve(.15)
    c "现在有了。"
    "很轻的一声，在热闹里几乎听不见。可那一刻，它比其他声音都清楚。"
    p "那我的记录就叫，三只杯子。"
    $ clue = "三只杯子的轻响"
    $ affection_c += 1
    show classmate normal
    with Dissolve(.15)
    b "其实我出门前也担心过，要是整个学期都找不到一起吃饭的人怎么办。"
    p "整个学期有点远。先约下一次？"
    show classmate happy
    with Dissolve(.15)
    b "好。下次换你来挑，我负责评价。"
    c "如果时间合适，也可以叫上我。"
    "那张记录卡在桌上转了一圈。最后我们各自写了一句话，没有谁的字特别整齐。"
    "但它看起来比刚才更像一份完整的记录了。"
    hide senior
    hide classmate
    with dissolve
    jump evening_scene

label evening_scene:
    $ chapter = "05 / 未完待续"
    $ play_optional('evening')
    scene bg evening at establishing
    with fade
    "傍晚的风比早晨柔和。走回熟悉的岔路口，我这次没有再展开地图。"
    "手机充上了电，家里的群聊又弹出一条消息：今天怎么样？"
    if route == "图书馆":
        "我想起书页翻过去的声音，想起那句‘先选一个问题’，还有[classmate_name]认真写字的样子。"
    elif route == "实验室":
        "我想起屏幕上两座小小的山，想起学姐承认自己也会出错时，忽然轻松起来的房间。"
    else:
        "我想起三只杯子碰在一起的轻响，还有那句不需要说得太郑重的‘下次一起’。"
    p "挺好的。认识了同学，也遇到了一位学姐。"
    "这一次，‘挺好的’后面没有藏着没说出口的慌张。至少，比早晨少了一点。"
    show classmate normal at stage_left
    with dissolve
    b "明天还一起走吗？我现在可以保证，只会偶尔走错。"
    p "可以。我们不是有冗余备份吗？"
    show classmate happy
    with Dissolve(.15)
    b "这次我听懂了。"
    show senior normal at stage_right
    with dissolve
    c "记录卡的电子版，我稍后发给你们。不用急着写完，想到的时候再补。"
    p "如果以后再听见今天的声音，会不会想起现在？"
    show senior happy
    with Dissolve(.15)
    c "可能。也可能到时候，你会听见今天没注意到的东西。"
    "天色一点点暗下来。教学楼的窗子亮起，像地图上刚刚被点亮的坐标。"
    "我仍然不熟悉这所校园，也不熟悉那个被称作‘大学生’的自己。"
    "但今天已经有了几个可以确认的事实。"
    "有一条路，我走过了。有一个问题，我问出口了。还有几个人，明天见面时可以直接叫出名字。"
    p "那就明天见。"
    b "明天见！"
    c "明天见。"
    hide classmate
    hide senior
    with dissolve
    "第一天结束了。我们的故事，刚刚接通信号。"
    hide screen chapter_stamp
    window hide
    $ quick_menu = False
    call screen demo_end
    return
