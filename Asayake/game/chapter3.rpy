screen next_chapter3_button():
    vbox:
        xalign 0.5
        yalign 0.9
        ## 闪烁文本内容
        textbutton "去床上。":
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

define c3role1 = Character('广播', color="#c8c8ff", image="c3role1")
define c3role2 = Character('“xx桑”', color="#c8c8ff", image="c3role2")
define c3role3 = Character('我', color="#c8c8ff", image="c3role3")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label chapter3:
## 章节初始化处理
scene black
nvl clear
window hide
stop sound
hide screen next_chapter2_button

## 时间指示器相关处理
show text "2021年，如今" at fade_centered with fade
pause 3.0
hide text with fade
pause 2.0

## 显示窗口
play music "audio/bgm_blues.mp3"
play sound "audio/sound_shinkoiwa.ogg"
scene bg05 with fade
pause 2.0

$ current_date = "2021年 10月 17日"
show screen time_display
window show

c3role1 "“下一站，新小岩，新小岩，出口在右侧。”"
nvl clear
narrator_nvl "电车的报站将意识拉回现实，"
narrator_nvl "我看了看表，现在是晚上8点。"
narrator_nvl "头似乎没有刚刚那么沉了，我站起身把双肩包背在身上走到车门附近，"
nvl clear

## 音效控制
stop sound

$ renpy.pause(1.0, hard=True)

## 更换场景：新小岩月台
window hide
scene bg10 with fade
pause 2.0
window show

narrator_nvl "下车后，总之出了剪票口之后来到了新小岩的南口。"
nvl clear

## 更换场景：新小岩月台
window hide
scene bg37 with fade
play sound "audio/element_kaisatu.mp3" loop
pause 2.0
window show

narrator_nvl "我避让着行人找到一个不会阻碍到行人的柱子边上，"
narrator_nvl "靠墙掏出手机，点亮屏幕。"
narrator_nvl "并没有新的消息。"
narrator_nvl "百无聊赖的我四下张望。"
nvl clear

## 音效控制
stop sound
$ renpy.pause(1.0, hard=True)

## 更换场景：新小岩月台
window hide
scene bg39 with fade
play sound "audio/element_ekimae.mp3" loop
pause 2.0
window show

narrator_nvl "周日的8点，虽然说第二天还有工作，但时间还早，车站前依然人来人往非常热闹。"
narrator_nvl "有拿着吉他对着麦克风支架弹唱旁边还有坐着卡风在鼓点给节奏的街头艺人，"
narrator_nvl "举着手机录像的看起来是粉丝的几个女性。"
narrator_nvl "车站前的警察岗亭前两个警察拿着A4资料板在讨论着什么。"
narrator_nvl "巴士站和出租车上客点排了几个人在等车。"
narrator_nvl "远处红绿灯十字路口传来卖可丽饼的和小妹酒吧的小妹在揽客的招徕声。"
nvl clear
narrator_nvl "我觉得再这样等下去估计我会困到直接睡死在路边然后晒出一生都忘不掉的丑态，"
narrator_nvl "也算是为了醒酒，转身去车站商店买了一瓶解酒用的生姜萃取物安慰剂灌下，"
narrator_nvl "拿着上车前买的那瓶运动饮料，从北口出来朝新小岩公园走去。"
nvl clear

## 更换场景：新小岩月台
window hide
scene bg27 with fade
play sound "audio/element_autumn.mp3" loop
pause 2.0
window show

narrator_nvl "在公园入口的厕所解决了自然的召唤之后，走在没有路灯漆黑一片公园的林荫道上，"
narrator_nvl "偶尔有遛狗和夜跑的路人经过，手环和狗的颈链上的led灯非常显眼。"
nvl clear


## 音效控制
stop sound

$ renpy.pause(1.0, hard=True)

## 更换场景：电话亭
window hide
scene bg06 with fade
play sound "audio/element_roadside.ogg" loop
pause 2.0
window show

narrator_nvl "也就几十来步路，走到了藏前桥大道边上一个电话亭旁边。"
narrator_nvl "我脑海里浮现出一组数字，是她的手机号码。"
narrator_nvl "我当然知道是她的手机号码，"
narrator_nvl "可是，此情此景让我想起这种无关紧要的东西到底什么意思啊？"
nvl clear
narrator_nvl "我走进电话亭，抚摸着公用电话绿色的塑料外壳。"
narrator_nvl "大概是误触了按键。电话的LED显示屏显示了几个点阵字——它告诉我“可以使用”，"
narrator_nvl "我刚好钱包里还有一张Windows7萌娘的电话卡，"
narrator_nvl "记得还是她说她喜欢水树奈奈，水树刚好又给那个Win7娘配过音，我就爱屋及乌买了这玩意。"
narrator_nvl "如今这玩意虽然会让我想起她，但我还是从实用防灾角度出发，把电话卡塞进了我的钱包里。"
narrator_nvl "也就是说这一刻，只要我想，我可以打个长途给她，"
narrator_nvl "虽然走蜂窝数据的即时通讯软件的语音聊天显然更经济实惠，没必要整这滑稽的一出。"
nvl clear
narrator_nvl "可是，退一万步，"
narrator_nvl "就算接通了，要我跟她说什么？"
narrator_nvl "国内现在是7点多吧？"
narrator_nvl "她在做什么呢？"
nvl clear
narrator_nvl "拿起听筒的手，最后还是放下了。"
narrator_nvl "我坐在电话亭的栏杆上，依靠着玻璃，"
narrator_nvl "电话亭在这秋夜竟有些闷热。"
narrator_nvl "外面车来车往明明应该很吵才对，"
narrator_nvl "然而电话亭里安静得只剩我自己酒后砰砰直跳的心跳声和自己的耳鸣声。"
nvl clear
narrator_nvl "她这个时候还在上海吗？"
narrator_nvl "结婚这么久了，孩子应该有了吧？"
narrator_nvl "这个时候应该吃完饭一边带孩子一边在客厅和丈夫享受宁静的生活吧？"
narrator_nvl "不可能，以我认识她这么久对她的了解，"
narrator_nvl "她估计还在要么接活画画,要么在外面跟姐妹嗨皮——"
narrator_nvl "她不是能在家静若处子的主。"
nvl clear
narrator_nvl "可那又怎么样呢？"
narrator_nvl "我难道要拿起电话打给她，"
narrator_nvl "“哟！是我啊！"
narrator_nvl "你之前跟我说结婚其实是骗我的吧？”，"
narrator_nvl "不对，"
narrator_nvl "还是说，"
narrator_nvl "“那个，如果你改变主意了我会等你的。”"
nvl clear
narrator_nvl "去他妈的吧，"
narrator_nvl "怎么不想下万一是别人，比如说她丈夫接电话我该说什么。"
narrator_nvl "“158xxxxxxxx，你的快递，我放快递柜子里了记得拿！”"
narrator_nvl "嗯，很合理，不会引起怀疑。"
narrator_nvl "不对，我还没原谅这孙子凭什么，"
narrator_nvl "“你是她老公？"
narrator_nvl "那正好，我是她前男友哦，哈哈哈！”"
narrator_nvl "那会不会气到她老公啊？"
nvl clear
narrator_nvl "我情不自禁嘴角上扬了。"
narrator_nvl "但我明白，我还没醉到那种地步，今晚我还没有到位。"
nvl clear

## 音效控制
stop sound

$ renpy.pause(1.0, hard=True)

## 更换场景：新小岩月台
window hide
scene bg28 with fade
play sound "audio/element_autumn.mp3" loop
pause 2.0
window show

narrator_nvl "从电话亭出来，走到棒球场外围的板凳上坐下。"
narrator_nvl "外面的凉风让我稍微清醒了一些，"
narrator_nvl "我喝了一口运动饮料，把手插在上衣的兜里，稍微发了会儿呆。"
play sound "audio/sound_bubu.mp3"
narrator_nvl "这时候手机又震了几下。"
nvl clear
play sound "audio/sound_popup.wav"
c3role2 "“快到了！”"
play sound "audio/sound_popup.wav"
c3role2 "“现在龟户！”"
nvl clear
narrator_nvl "让人久等可不好，"
play sound "audio/sound_walk.mp3"
narrator_nvl "我于是朝车站稍微加快脚步走去。"
nvl clear

## 音效控制
stop sound

$ renpy.pause(1.0, hard=True)

## 更换场景：新小岩改札
window hide
scene bg37 with fade
play sound "audio/element_kaisatu.mp3" loop
pause 2.0
window show

narrator_nvl "在我回到剪票口外几乎同时，"
narrator_nvl "我感到背后被人拍了一下。"
narrator_nvl "转身，是她。"
nvl clear
c3role2 "“哟！”"
c3role3 "“哦哦哦是你啊，吓我一跳”"
narrator_nvl "还不等我反应过来，手里的运动饮料被她抢了过去，"
play sound "audio/sound_nomikomu.mp3"
narrator_nvl "她拧开瓶盖后抿了一口，好像很难喝似的皱着眉吐着舌头还给我。"
nvl clear
c3role3 "“等等，这，”"
c3role2 "“好难喝~咦？这并不是酒嘛！”"
c3role3 "“不是啊，”"
c3role2 "“那是什么？”"
c3role3 "“就，运动饮料啊？”"
c3role2 "“为什么喝那种东西啊，"
c3role2 "比起那个，"
c3role2 "我们去买酒吧！"
c3role2 "然后就去晓君的家里，"
c3role2 "{rb}在家喝酒！{/rb}{rt}TAKUNOMI{/rt}"
c3role2 "嘻嘻嘻~”"
nvl clear
narrator_nvl "她的样子看起来绝对是喝高了那种兴奋，"
narrator_nvl "因此声音也几乎是完全不在乎周围的那种，"
narrator_nvl "我仅剩的理智不想引起太多注目，"
narrator_nvl "于是决定还是把她稳住。"
c3role3 "“好好好走走走。”"
play sound "audio/sound_walk.mp3"
nvl clear

## 音效控制
stop sound

$ renpy.pause(1.0, hard=True)

## 更换场景：新小岩月台
window hide
scene bg07 with fade
play sound "audio/element_konbini.mp3" loop
pause 2.0
window show

narrator_nvl "于是在十字路口边上的罗森我们进去准备买些酒菜。"
narrator_nvl "她进去以后径直朝酒类冰柜走去拿了好几罐度数很高的烧酒，"
narrator_nvl "其他的看都没看，"
narrator_nvl "找到正在买下酒菜的我，把酒全部放进我手里的购物篮，"
narrator_nvl "然后笑眯眯地看着我。"
c3role2 "“不可以哦，才喝这么一点，再喝点嘛”"
nvl clear
narrator_nvl "我苦笑，"
narrator_nvl "我不知道眼前这个醉美人到底酒量几何，"
narrator_nvl "但我肯定她这么说的时候"
narrator_nvl "她今晚肯定不会轻易放过我的。"
nvl clear
c3role3 "“那，我跟你分吧，"
c3role3 "你喝多少我陪你喝多少，"
c3role3 "要是喝完的话我家对面就是卖酒的自贩机，"
c3role3 "陪你尽兴为止”"
nvl clear
narrator_nvl "她高兴地挽住我的手臂"
c3role2 "“这才像话，嘻嘻”"
nvl clear

## 音效控制
stop sound

$ renpy.pause(1.0, hard=True)

## 更换场景：新小岩月台
window hide
scene bg36 with fade
play sound "audio/element_walk_jutaku_night.mp3" loop
pause 2.0
window show

narrator_nvl "我有些难为情，"
narrator_nvl "虽然我很明白，我这是在占她便宜，"
narrator_nvl "占一个喝醉了的美女的便宜，"
narrator_nvl "但意外地感觉不坏，"
nvl clear
## 更换场景：新小岩月台
window hide
scene bg45 with fade
pause 2.0
window show

## 音效控制
stop sound

$ renpy.pause(1.0, hard=True)
nvl clear
narrator_nvl "于是就这样保持这个姿势一直到家。"
narrator_nvl "我掏出钥匙打开门。打开灯。"
c3role3 "“我回来了”"
c3role2 "“打扰啦”"
nvl clear
narrator_nvl "我自己一个人回来的时候从来不说，"
narrator_nvl "今天有其他人在的时候不说感觉有点怪，于是说了。"
play sound "audio/sound_shoes.mp3"
narrator_nvl "我从鞋柜里找出一双拖鞋给她。"
c3role2 "“谢谢，嘿嘿~”"
nvl clear
narrator_nvl "她看起来还是很开心。"
narrator_nvl "我把购物袋放到暖桌上，把墙角灯打开，"
narrator_nvl "恰到好处的暖光包围了暖桌的周围。"
narrator_nvl "把一切安排妥当之后，招呼她在暖桌边坐下。"
nvl clear

## 更换场景：新小岩月台
window hide
scene bg40 with fade
pause 2.0
window show

c3role3 "“不好意思，"
c3role3 "男人的破狗窝是这个样子，"
c3role3 "你随意就好不用太拘……嗯呣……！！？”"
play sound "audio/sound_kiss.mp3"
nvl clear
narrator_nvl "嘴唇上两片柔软的感触传了过来，"
narrator_nvl "随之而来就是一股带着烧酒和香水味的浓烈气息。"
narrator_nvl "我还没反应过来怎么回事，"
narrator_nvl "但我似乎又有些理解了这一切。"
narrator_nvl "我似乎想说些什么，嘴唇却被她用手指按下。"
nvl clear
c3role2 "“现在你要是吐出一个字，我马上回去。”"
narrator_nvl "我被她震住了，"
narrator_nvl "然后她再一次凑近，"
narrator_nvl "额头贴到我的额头上，额头传递着她的体温，"
narrator_nvl "我感受到我们的呼吸渐渐加快。"
play sound "audio/sound_kiss.mp3"
narrator_nvl "然后好像是同时，我们再次温柔地接吻，"
nvl clear

## 更换场景：和室
window hide
scene bg38 with fade
pause 2.0
window show

narrator_nvl "片刻后。稍微分开。"
narrator_nvl "暖色的灯光下的她这时却有些害羞了起来，"
narrator_nvl "我忍不住笑场了，她看到我笑了也忍不住笑了。"
narrator_nvl "然后一拳捶到我胸口上，那可是实打实的一拳啊。"

nvl clear
c3role2 "“呐，去床上吧。”"
c3role3 "“嗯”"

stop music fadeout 2.0

# 章节切换处理
show screen next_chapter3_button
pause
hide screen time_display
jump chapter4
return