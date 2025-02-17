screen next_chapter2_button():
    vbox:
        xalign 0.5
        yalign 0.9
        ## 闪烁文本内容
        textbutton "深呼吸，你准备好回归现实。":
            text_size 60
            text_color "#FFFFFF"
            action Return()
            at breathing_animation

init:
    transform breathing_animation:
        alpha 0.2
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.2
        repeat

    transform fade_centered:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        linear 1.5 alpha 1.0

define c2role1 = Character('我', color="#c8c8ff", image="c2role1")
define c2role2 = Character('“她”', color="#c8c8ff", image="c2role2")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label chapter2:
## 章节初始化处理
hide screen next_chapter1_button
scene black
nvl clear
window hide


## 音效控制
stop sound
$ renpy.pause(0.1, hard=True)

## 时间指示器相关处理
show text "2015年，夏" at fade_centered with fade
pause 3.0
hide text with fade
pause 2.0

## 显示窗口
play sound "audio/element_summer.ogg" loop
scene bg12 with fade
pause 2.0

$ current_date = "2015年 6月 28日"
show screen time_display
window show

c2role1 "“我们可不可以和好？”"
narrator_nvl "我大概能想象出收到这条信息后她哑然失笑的样子。"
narrator_nvl "她也许早料到，我会有一天像这样央求她和我复合。"
nvl clear
c2role2 "“你可不可以冷静一下？我觉得……”"
narrator_nvl "电话的那头，她的声音冷静而沉稳。"
nvl clear
c2role1 "“我很冷静！真的！”"
narrator_nvl "还没等她说完，我的声音动摇着，充满了自己的慌乱。"
nvl clear
c2role2 "“你不，你好好想想可以吗？"
c2role2 "上次你跟我说我们分手的时候你也说你很冷静，抱歉呀，我会当真的。”"
nvl clear
narrator_nvl "依然是那个冷静而沉稳的声音。"
c2role1 "“可是，我真的……”"
nvl clear
narrator_nvl "我很想再坚持己见一下，"
narrator_nvl "但无奈，她说的句句属实，我无法反驳。"
nvl clear
c2role2 "“当初我有跟你说过，异地真的很难，你要考虑清楚，你答应了。"
c2role2 "后来最先反悔的也是你，我有没有说错？”"
c2role1 "“……嗯”"
nvl clear
narrator_nvl "我发现了，这时候无论我说什么都于事无补。"
c2role2 "“那，就这样吧。”"
nvl clear
narrator_nvl "她轻轻地叹息。"
c2role1 "“……嗯”"
nvl clear
narrator_nvl "除了这个字以外，我竟说不出其他的话，却只觉得自己好没用，"
narrator_nvl "眼睁睁地看着这通一开始就注定失败的挽回电话砸在了自己手里。"
c2role2 "“拜拜……（断线音，嘟……嘟……嘟……）”"
play sound "audio/sound_tel_busy.mp3"
nvl clear

hide screen time_display

## 音效控制
stop sound

$ renpy.pause(0.1, hard=True)

## 更换场景：床边的手机
window hide
scene bg13 with fade
pause 2.0
window show

narrator_nvl "那之后，我已确信，我们再也没有可能回去了。"
narrator_nvl "只是，我依然装作无事发生，"
narrator_nvl "还是会和她在社交网络上有一搭没一搭地，分享着或许是我的，又或许是她的日常。"
narrator_nvl "仿佛只要还可以这样，我便还没有完全失去她。"
nvl clear
narrator_nvl "是啊，我至今还没有接受自己已经失恋了的事实。"
narrator_nvl "这种关系哪怕是到了毕业后，刚进公司加班加到工伤的那两年也还保持了下来。"
narrator_nvl "直到我上次去上海。"
stop music fadeout 2.0
nvl clear

## 隐藏对话框，确保文字居中独立显示
scene black with fade
nvl clear
window hide
stop music fadeout 2.0
stop sound

## 时间指示器相关处理
show text "2019年，春" at fade_centered with fade
pause 3.0
hide text with fade
pause 2.0

## 显示窗口
play music "audio/bgm_xiangni.mp3"
scene bg20 with fade
pause 2.0

$ current_date = "2019年 5月 14日"
show screen time_display
window show

narrator_nvl "上次项目交付之后，有了一点窗口期。"
narrator_nvl "我于是跟公司请了年假把没来得及消化的带薪假花出去，顺便去上海看看老朋友。"
narrator_nvl "也许，还能跟她再见上一面。"
nvl clear
play sound "audio/sound_typing.mp3"
c2role1 "“我会在上海呆到后天，真的不能再见上一面吗？”"
play sound "audio/sound_popup.wav"
c2role2 "“我之前有没有跟你说过？其实我跟我先生领证了……”"
nvl clear
narrator_nvl "我木木地看着手机屏幕上那行文本，"
narrator_nvl "这些字，每个字我都认识，"
narrator_nvl "可是当它们聚在一起时，我却疑惑了起来，"
narrator_nvl "我知道这意味着什么，"
narrator_nvl "我本该知道的，"
narrator_nvl "可是我脑海里某个意识，某种强烈的思念，"
narrator_nvl "以近乎歇斯底里的方式"
narrator_nvl "一遍又一遍地打断我理性的思考瞬间得出的结果最终传递到它的归宿。"
nvl clear
narrator_nvl "我反反复复地读着这条信息。"
narrator_nvl "聊天框上一闪而过了“对方正在输入…”但马上消失了。"
narrator_nvl "我回过神来的时候发现眼泪止不住地从眼角溢出来，却不知为何。"
narrator_nvl "我把手指搭在软键盘上试图输入点什么，眼泪却把我的屏幕打湿。"
nvl clear
narrator_nvl "祝福你啊，亲爱的。"
narrator_nvl "祝福你啊！！"
narrator_nvl "操！这手机为什么不听我使唤！！操！！！！"
narrator_nvl "祝你幸福！！！"
nvl clear
narrator_nvl "我不为她感到高兴吗？"
narrator_nvl "我应该啊！"
narrator_nvl "不啊，"
narrator_nvl "我们已经结束了所以我，作为一个懂分寸的成年人，我应该送上祝福。"
narrator_nvl "我应该。"
nvl clear
narrator_nvl "于是我拂去手机屏幕上的泪水，"
play sound "audio/sound_typing.mp3"
c2role1 "“祝你幸福，我们不要再联系了吧。”"
nvl clear

stop sound
## 更换场景：廉价酒店
window hide
scene bg15 with fade
pause 2.0
window show

narrator_nvl "发完这条信息后，后续还发过几条信息过来，但我没有再看，"
narrator_nvl "我怕我再抑制不住自己的感情冲动。"
narrator_nvl "我把手机插上充电座，躺在酒店的大床上，把电视的音量开大了一点，"
narrator_nvl "好让自己的思绪可以忙一些以从刚才的失态逃出来。"
narrator_nvl "但是还是失败了。"
nvl clear
narrator_nvl "过去，从我们相知相遇，相互接近，"
narrator_nvl "再到表白，再到交往，再到吵架，"
narrator_nvl "闹分手，和好，再吵架，又分手，再和好，"
narrator_nvl "回忆中那些画面依然像昨天般清晰，"
narrator_nvl "而今天这一刻，回忆仅仅只是回忆，变成了禁忌的过去，"
narrator_nvl "变成了阻碍着我和她即将到来或许会美好的未来的不可触摸之禁忌。"
nvl clear
narrator_nvl "我不断告诉自己，不可以再去想了，"
narrator_nvl "但思绪并不受控，那些甜蜜的苦涩的过去像烈酒穿过喉咙，"
narrator_nvl "我试图睡去，但怎也无法睡去。"
nvl clear
narrator_nvl "感伤从四面八方袭来，"
narrator_nvl "击穿酒店那并不存在的隔音墙，"
narrator_nvl "盖过电视那点可怜的声音，"
narrator_nvl "甚至让我不再在意坏掉的空调。"
nvl clear

## 更换场景：手机
window hide
scene bg20  with fade
pause 2.0
window show

narrator_nvl "这里不能呆了。"
narrator_nvl "随着脑海内的这个声音逐渐变大，"
narrator_nvl "于是拿过手机，订了下午的高铁票，"
narrator_nvl "不顾朋友的挽留，我干脆地收拾了行李，匆匆结束了上海的旅程，"
narrator_nvl "回到了我们相遇的那个小镇。"

## 更换场景：自己的房间
window hide
scene bg16 with fade
pause 2.0
window show

## 时间指示器相关处理
$ current_date = "2019年 5月 15日"
show screen time_display

narrator_nvl "我已记不得我是怎样回到自己的家，自己的床上了，"
narrator_nvl "想必那样子一定难看至极。"
nvl clear
narrator_nvl "接下来的几天，我尝试着出门，"
narrator_nvl "但每每以我的情绪崩溃告终。"
nvl clear

## 更换场景：林业局的林荫道
window hide
scene bg17 with fade
pause 2.0
window show

## 时间指示器相关处理
$ current_date = "2019年 5月 16日"
show screen time_display

narrator_nvl "当我走在林业局夏天会开满喇叭花的林荫道上时，会想起那个夏天，"
narrator_nvl "穿着小司水手服的她撒娇说走累了"
narrator_nvl "然后“嘿呀~”一下子跳到我背上，"
narrator_nvl "我一个趔趄差点没站稳，还好勉强接住她，"
narrator_nvl "一直把她背回小区。"
narrator_nvl "耳边仿佛还听见她说的“不许嫌我重哦！”"
nvl clear

## 更换场景：黑屏
window hide
scene black with fade
pause 2.0
window show

narrator_nvl "这如果只是偶然的情景闪回的话还好，"
narrator_nvl "可我的病症却比这要严重得多。"
nvl clear

## 更换场景：母校
window hide
scene bg18 with fade
pause 2.0
window show

## 时间指示器相关处理
$ current_date = "2019年 5月 17日"
show screen time_display

narrator_nvl "当我走到曾经的我和她的母校，我会想起，"
narrator_nvl "我追她还在晚自习偷偷借好兄弟的手机聊QQ，"
narrator_nvl "有一次忍不住直接在考评员来清点人数之前溜下楼从单车棚取出单车，"
narrator_nvl "闯出校门飞奔到她在的网吧，"
narrator_nvl "还有我形迹可疑跑到她班上叫她出来的情景，"
narrator_nvl "又或者偶尔她因为被叫到校园广播站帮忙，"
narrator_nvl "我也被她拉进去广播室里，"
narrator_nvl "在她的姐妹们的一片调戏下，看着她一边憋笑一边念广播稿的样子。"
narrator_nvl "以及有段时间我们闹分手，"
narrator_nvl "我路过她年级的楼层偶遇她的时候，"
narrator_nvl "她故意“哼”的一下走过去，"
narrator_nvl "我也毫不逊色地“哼”了回去的样子。"
nvl clear

## 更换场景：小区前面的道路
window hide
scene bg21 with fade
pause 2.0
window show

## 时间指示器相关处理
$ current_date = "2019年 5月 18日"
show screen time_display

narrator_nvl "走到她曾经住的小区前面的道路时，"
narrator_nvl "会想起每天早上和中午上学的时候，我在她家楼下等她，"
narrator_nvl "而她姗姗来迟之后，小心翼翼却又略带一点小心思地问我"
narrator_nvl "“久等啦\~没有生气吧？”"
narrator_nvl "“没有。”"
narrator_nvl "“你生气了\~”"
narrator_nvl "“没有，你不要强奸我思想。”"
narrator_nvl "“我没有强奸你（坏笑）”"
narrator_nvl "“可恶！给我等着！”"
narrator_nvl "然后一边打闹一边去学校。"
nvl clear

## 更换场景：步行街
window hide
scene bg19 with fade
pause 2.0
window show

## 时间指示器相关处理
$ current_date = "2019年 5月 19日"
show screen time_display

narrator_nvl "走到繁华的步行街，经过街口的美食广场，"
narrator_nvl "会想起下午放学后我们有时会来到这里，"
narrator_nvl "趁晚自习开始之前的间隙吃一些炸串之类的垃圾食品。"
narrator_nvl "她总是会点一些油豆腐，乌贼触手，"
narrator_nvl "然后会跟老板要多一些纸巾，还有多撒辣椒面。"
narrator_nvl "有一次刚坐下没多久，商场的扬声器那边传来飞轮海的《只对你有感觉》，"
narrator_nvl "刚好那句歌词，两个人相视，我知道她在想什么，她肯定知道我在想什么，两个人傻傻地笑。"
narrator_nvl "步行街有一家西餐厅，虽然已经易主了，但是我记得我有一次生日，"
narrator_nvl "她特地穿上女仆装为我庆生。"
narrator_nvl "她捧着蛋糕说出那句“主人（狗修金撒嘛），生日快乐”的样子。"
nvl clear
narrator_nvl "我回过神来的时候，已经结完账，"
narrator_nvl "手里提着几罐啤酒和一堆垃圾食品。"
narrator_nvl "但我走出两步之后，冷静下来，又觉得不可以这样伤害自己的身体，"
narrator_nvl "把自己弄伤到最后还是要靠自己去疗伤。"
narrator_nvl "我不是不明白，但我走向最近的垃圾桶的时候，"
narrator_nvl "脑海里那些曾经的甜蜜就变得越发地大声，"
narrator_nvl "直到震耳欲聋的程度。"
narrator_nvl "我跑了起来，跑回家里。"
nvl clear

## 更换场景：自己的房间
window hide
scene bg16 with fade
pause 2.0
window show

narrator_nvl "那天晚上的记忆只剩我往嘴里灌酒和我打开航司官网改签机票，"
narrator_nvl "这个要用伤心溺死我的地方我是一刻也呆不下去了。"
narrator_nvl "第二天顶着个红眼圈跟家人说了一声便打车下广州了。"
nvl clear

## 更换场景：广州的酒店
window hide
scene bg23 with fade
pause 2.0
window show

## 时间指示器相关处理
$ current_date = "2019年 5月 22日"
show screen time_display

narrator_nvl "在广州的那两天也是，"
narrator_nvl "白天在酒店爆睡，"
narrator_nvl "晚上约人出来喝酒，"
narrator_nvl "喝到实在喝不下才回酒店。"
narrator_nvl "因为我发现，"
narrator_nvl "哪怕是广州，也时刻提醒着我刚刚失去了什么重要的东西。"
nvl clear

## 更换场景：广州塔远景
window hide
scene bg24 with fade
pause 2.0
window show

narrator_nvl "就像我回到家乡时候，"
narrator_nvl "同样的场景闪回在广州也没有消退。"
narrator_nvl "去游戏中心的时候，会想起之前在同一个地方约会的时候，一起玩跳舞机的情景。"
narrator_nvl "去吃饭的时候，会想起拿号排队等位的时候，她一直对我使用恶作剧，这样那样。"
narrator_nvl "去喝酒的时候，就算有酒，也还是会想起两人对饮时，她完全不输给我的豪爽劲。"
narrator_nvl "令我想起她总是自称萝莉身大叔心。"
narrator_nvl "睁眼是她，"
narrator_nvl "闭眼是她，"
narrator_nvl "只有半梦半醒朦胧中，才有那么一点廉价止痛药一般的效果。"
nvl clear

## 更换场景：飞机腾空而起
window hide
scene bg25 with fade
pause 2.0
window show

narrator_nvl "直到飞机腾空而起，"
narrator_nvl "冲破云层，"
narrator_nvl "下面广州的身影渐渐远去，祖国的海岸线渐渐离我远去，"
narrator_nvl "那些我想珍视却被我所失的那些终究是远去了。"
nvl clear

## 更换场景：飞机落地羽田机场
window hide
scene bg26 with fade
pause 2.0
window show

narrator_nvl "飞机落地羽田机场后走出飞机舱门走进廊桥的那一刻，"
narrator_nvl "打开蜂窝数据收到一堆工作上的邮件和数据之后，"
narrator_nvl "我大概是强行杀死了体内的某种东西，"
narrator_nvl "或者说至少让它睡去了。"
narrator_nvl "于是一头扎进工作，不再犹豫。"
stop music fadeout 2.0

# 章节切换处理
show screen next_chapter2_button
pause
hide screen time_display
jump chapter3
return