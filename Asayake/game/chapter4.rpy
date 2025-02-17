screen next_chapter4_button():
    vbox:
        xalign 0.5
        yalign 0.9
        ## 闪烁文本内容
        textbutton "打卡，下班。":
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

define c4role1 = Character('我', color="#c8c8ff", image="c4role1")
define c4role2 = Character('课长', color="#c8c8ff", image="c4role2")
define c4role3 = Character('“她”', color="#c8c8ff", image="c4role3")
define c4role4 = Character('服务员', color="#c8c8ff", image="c4role4")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label chapter4:
## 章节初始化处理
scene black
nvl clear
window hide
stop sound
hide screen next_chapter3_button

## 时间指示器相关处理
show text "一夜过去了。" at fade_centered with fade
pause 3.0
hide text with fade
pause 2.0

## 显示窗口
play music "audio/bgm_iroaku.mp3"
play sound "audio/sound_alarm.ogg"
scene bg44 with fade
pause 2.0

$ current_date = "2021年 10月 18日"
show screen time_display
window show

narrator_nvl "早上，我在自己的手机夺命闹钟app下醒来，"
narrator_nvl "而一向没有裸睡习惯的我发现自己赤裸着全身，"
narrator_nvl "还有暖桌上没来得及收拾的计生用品的盒子，"
narrator_nvl "还有一张纸条，"
narrator_nvl "昨晚发生的事情终于有了些现实的味道。"
narrator_nvl "我爬起来坐在床边，拿过纸条，睁大朦胧的睡眼端详着上面的字。"
nvl clear
c4role1 "“多...谢...招...待...?...欸?”"
nvl clear
narrator_nvl "就这几个字。没有署名，没有更多的信息。"
narrator_nvl "打开LINE，置顶的只有之前的相亲群聊，那个妹子已经退群了。"
narrator_nvl "屏幕亮着，我盯着这几个字，好几秒才反应过来。"
nvl clear
narrator_nvl "她消失了。"
nvl clear
narrator_nvl "我当然可以把手机回滚到之前的某一个时间点来刨根问底，"
narrator_nvl "但面前的这个布局已经把她的立场阐述得非常明白，不需要再加任何的补充了。"
narrator_nvl "我愣了半晌，然后轻轻叹了一口气。"
nvl clear
c4role1 "“那要不然呢？”"
nvl clear
narrator_nvl "是啊。"
narrator_nvl "那要不然呢？"
nvl clear
narrator_nvl "然后就回到了一如既往的循环。"
narrator_nvl "打开电视，把麦片和速溶咖啡倒进马克杯里放进微波炉里，"
narrator_nvl "在嗡嗡作响的微波炉和早间新闻播报声中完成洗漱。"
narrator_nvl "边喝麦片边看天气预报，然后穿好衣服出门——"
narrator_nvl "本应该是这样的，监控系统不这么想。"
nvl clear
stop music fadeout 2.0

## 更换场景：和室
window hide
scene bg13 with fade
play sound "audio/sound_zabbix.ogg" loop
pause 2.0
window show

narrator_nvl "手机响了。"
narrator_nvl "是我职业生涯中最怕的那个提示音。"
narrator_nvl "Zabbix的警告有三种等级：info，warn，error。"
narrator_nvl "这个声音响起，就意味着——红色警戒。"
nvl clear

# 音效控制
stop music fadeout 2.0
stop sound
$ renpy.pause(1.0, hard=True)

play music "audio/bgm_tracer1.mp3" loop
c4role1 "“啊，狗操的一天开始了。”"
nvl clear
narrator_nvl "如果仅仅只是系统故障，只要修好就没事了。"
narrator_nvl "但这一天却比我想象得要漫长得多。"
narrator_nvl "比如——"
nvl clear

## 更换场景：
window hide
scene bg46 with fade
play sound "audio/element_kaisatu.mp3"
pause 2.0
window show

narrator_nvl "当我走到新小岩车站的时候，"
narrator_nvl "发现人已经从车站里堵到外面来。"
nvl clear
play sound "audio/sound_announce.ogg"
narrator_nvl "广播一遍遍循环着——"
narrator_nvl "“发生人身事故，”"
narrator_nvl "“电车恢复时间未知。”"
nvl clear
play sound "audio/sound_bubu.mp3"
narrator_nvl "而这边课长又夺命连环call问我几点才能到公司——"
narrator_nvl "明明我5分钟前刚刚答复过他同样的问题。"
nvl clear
c4role1 "【哔——（国骂）】……5分钟？我是能瞬移到你老婆床上，还是咋的？"
c4role1 "我是能瞬移到你老婆床上，"
c4role1 "还是咋的？"
c4role1 "【哔——（国骂）】"
nvl clear

## 更换场景：
window hide
scene bg35 with fade
play sound "audio/element_kosaten.mp3"
pause 2.0
window show

narrator_nvl "而我权衡利弊之下最后决定搭巴士，"
narrator_nvl "好不容易挤着上座率远超平时的巴士，到丸之内的时候，时间已经来到了上午10点半。"
narrator_nvl "我已经尽全力跑了起来，汗水把汗衫和白衬衫湿到透，"
narrator_nvl "都这样了，也还是没能免得了到工位之后，课长和一堆帮不上忙干着急的人在我耳边聒噪。"
nvl clear

# 音效控制
stop music fadeout 2.0
stop sound
$ renpy.pause(1.0, hard=True)

## 更换场景：
window hide
scene bg33 with fade
play music "audio/bgm_tracer2.mp3" loop
play sound "audio/element_office.ogg" loop
pause 2.0
window show

narrator_nvl "故障排除的那个小时，就像被肾上腺素冲垮的幻觉，"
narrator_nvl "过程已经模糊不清，只剩下指尖在键盘上飞舞的残影。"
narrator_nvl "帮不上忙的课长只管守在座机前跟客户那边稳住客户的情绪，"
nvl clear
narrator_nvl "我这时大约是在肾上腺素加持下很快找到了问题的所在。"
narrator_nvl "对着黑漆漆的终端界面手指飞快在键盘上飞舞。"
nvl clear
narrator_nvl "终于，系统恢复上线。"
narrator_nvl "终端上的日志流动了几行，"
narrator_nvl "任务结束了。"
nvl clear
narrator_nvl "办公室里响起一阵轻微的叹息声，所有人都松了口气。"
narrator_nvl "我靠回椅背，手臂垂落在扶手上，像泄了气的气球瘫在椅子里。"
narrator_nvl "眼前的屏幕依旧滚动着系统日志，但我已经完全没心思再去读它了。"
nvl clear
c4role2 "“是..."
c4role2 "是..."
c4role2 "是的，您说得非常有道理，非常抱歉。"
c4role2 "给贵司添了如此麻烦，真是万分抱歉。"
c4role2 "“今天下午3点，我们两人会到贵司拜访，届时还请您多多关照。”"
nvl clear

# 音效控制
stop music fadeout 2.0
$ renpy.pause(1.0, hard=True)

play music "audio/bgm_tracer3.mp3" loop
narrator_nvl "课长打完电话，长舒一口气。"
narrator_nvl "他看了看表："
nvl clear
c4role2 "“哦哟，这个点了，"
c4role2 "走，吃饭去，陪我一下。"
c4role2 "反正你也该歇会儿了，对吧？”"
narrator_nvl "我知道这家伙想的是什么，"
narrator_nvl "一半是为了找机会再聊聊我的离职，"
narrator_nvl "一半是因为那家餐馆能抽烟，咖啡无限续杯，一举两得。"
nvl clear
narrator_nvl "我当然不情愿，但碍于他是课长，"
narrator_nvl "又帮我顶了锅，拒绝也显得太不近人情。"
narrator_nvl "吃人嘴软，"
narrator_nvl "想想还是算了。"
nvl clear

# 音效控制
stop music fadeout 2.0
stop sound
$ renpy.pause(1.0, hard=True)

## 更换场景：
window hide
scene bg42 with fade
play music "audio/bgm_guitar.mp3" loop
play sound "audio/element_party.mp3" loop
pause 2.0
window show

narrator_nvl "那家中餐馆在读卖新闻大厦的地下，某个入口正对着卫生间的位置。"
narrator_nvl "入口虽然摆着几张等位用的椅子，但从来没用到过。"
narrator_nvl "门口的黑板立牌上，今天的轮换套餐是麻婆豆腐和拉面套餐。"
narrator_nvl "和上周没什么区别。"
nvl clear
narrator_nvl "这地方我是绝不会自己来的。"
narrator_nvl "所谓的‘中华料理’，在我这个广东人看来，实在不敢恭维。"
narrator_nvl "更何况，来这里吃饭，还得冒着碰见课长的风险。"
narrator_nvl "他几乎把这地方当作食堂，而我能避开就避开。"
narrator_nvl "只有今天这种情况，我才会勉强坐在这里，"
narrator_nvl "这也意味着——"
narrator_nvl "这顿他请。"
nvl clear

## 更换场景：
window hide
scene bg47 with fade
pause 2.0
window show

narrator_nvl "汗在空调的冷风里干得差不多了， "
narrator_nvl "但背后仍然黏糊糊的，怎么都不舒服。"
narrator_nvl "即使坐下之后，也完全无法集中。"
nvl clear
narrator_nvl "服务员递来热毛巾和冰水，只说一句中国味浓郁的日语"
nvl clear
c4role4 "“决定好了点什么您吩咐”，"
nvl clear
narrator_nvl "刚要转身，课长赶紧叫住她"
nvl clear
c4role2 "“来份每日套餐，啊，还有烟灰缸”"
nvl clear
narrator_nvl "服务员歪头向厨房用洪亮的中文嚷道——"
nvl clear
c4role4 "“日替一个——！”"
nvl clear
narrator_nvl "声音穿过店里，和锅铲翻炒的声音混在一起。"
nvl clear
narrator_nvl "然后她又一语不发地看着我。"
narrator_nvl "她的表情与其说是不耐烦或者生气，倒不如说是麻木。"
narrator_nvl "这种表情，我再熟悉不过了。"
narrator_nvl "倒不如说，我跟她其实没区别。"
nvl clear
c4role1 "“木须肉定食，米饭半碗”"
nvl clear
narrator_nvl "我随口说道，甚至懒得抬头。"
narrator_nvl "她也依旧是面不改色直接把我原话嚷给厨房，然后问。"
nvl clear
c4role4 "“就这些吗？”"
c4role1 "“嗯，就这些了。”"
nvl clear
narrator_nvl "她很快拿过烟灰缸，之后便忙别的去了。"
narrator_nvl "课长掏出烟盒和打火机摆在桌上，开始跟我例行聊起了我的离职，都是些场面话了。"
nvl clear
c4role2 "“晓君，了不得啊。"
c4role2 "又会日语又会中文，"
c4role2 "要换做是我让我去中国挣钱养家什么的，我怕是活不下去。”"
nvl clear
c4role1 "“得了吧课长，有话您直说吧。”"
nvl clear
c4role2 "“哎呀哎呀，不要这么无情嘛，"
c4role2 "是不是最近的工作负担太重了？"
c4role2 "但你知道吧？公司很快要上市了。"
c4role2 "只要上市，你的期权要是换成日元那可是个大数字啊。”"
nvl clear
c4role1 "“我知道，可是，我已经决定了。"
c4role1 "课长，你的心意我领了。”"
nvl clear
c4role2 "“哎，既然你都这么说了。"
c4role2 "不过我可把话说在前头。"
c4role2 "我一直很欣赏你。"
c4role2 "你是我带过这么多下属里不说最优秀的也是名列前茅的孩子了。”"
nvl clear
narrator_nvl "我笑了，甚至笑得太露骨了，觉得会不会让课长尴尬的程度。"
nvl clear
c4role1 "“别逗了课长，我几斤几两我自己清楚。"
c4role1 "不过，您这么抬爱我，我倒也是非常感激您的。”"
nvl clear

## 更换场景：
window hide
scene bg41 with fade
pause 2.0
window show

narrator_nvl "还好并没有等多久，服务员就上菜了，给这段尴尬的对话告了一个段落。"
narrator_nvl "课长看我丝毫没有动摇地埋头吃饭，加上午休时间宝贵，也就只好默默吃饭。"
nvl clear

## 更换场景：
window hide
scene bg48 with fade
pause 2.0
window show

narrator_nvl "吃完饭，他抽烟，我喝咖啡。"
nvl clear
c4role2 "“说来，晓君今年30了吧？"
c4role2 "结婚什么的，有考虑过吗？”"
nvl clear
narrator_nvl "我有些诧异他这么问，不过并没有动摇。"
nvl clear
c4role1 "“是29，明年30。"
c4role1 "结婚什么的，暂时没有这个打算。”"
nvl clear
c4role2 "“是吗。”"
nvl clear
narrator_nvl "他又接着抽了一口，仰头把烟吐出后，缓缓地说——"
nvl clear
c4role2 "“原来这样啊……所以才……”"
nvl clear
narrator_nvl "他顿了一下，换了种语气。"
nvl clear
c4role2 "“不过，怎么样都好……"
c4role2 "不要后悔啊。”"
nvl clear
c4role1 "“好。”"
nvl clear
narrator_nvl "我低头搅了搅杯子里的咖啡，没再说话。"
narrator_nvl "是不是我让他想起了什么？"
narrator_nvl "但我不关心。"
nvl clear

## 更换场景：
window hide
scene bg35 with fade
play sound "audio/element_kaisatu.mp3" loop
pause 2.0
window show

narrator_nvl "之后，便结了帐，回公司收拾收拾就去客户那里赔不是，顺便说明情况了。"
nvl clear


# 音效控制
stop music fadeout 2.0
stop sound
$ renpy.pause(1.0, hard=True)

## 更换场景：
window hide
scene bg49 with fade
play music "audio/bgm_hanzawa.mp3" loop
play sound "audio/element_meeting.ogg" loop
pause 2.0
window show

narrator_nvl "客户还算冷静，没有歇斯底里。"
narrator_nvl "可会议室里乌泱乌泱地挤着十几号技术部的老油条，外加一群刚入职的新人，"
narrator_nvl "西装领带绑得跟吊颈绳似的，一个个站得笔直，神情肃穆。"
narrator_nvl "喂，诸位小兄弟，你们站的是旁听席，不是被告席吧？"
narrator_nvl "虽然见过这场面不止一次，但面对这股“法庭自辩”的空气，我心里还是有点发虚。"
nvl clear
narrator_nvl "还好，我提前找到了一个足够稳妥的事故原因——"
narrator_nvl "既能保全大人物的颜面，也能堵住客户的嘴，同时给出一个可行的技术方案。"
nvl clear
narrator_nvl "发言结束，会议室短暂沉默，"
narrator_nvl "随后技术部的老手们接过话茬，一连抛出几个问题，"
narrator_nvl "语速不快不慢，却字字精准。"
narrator_nvl "我一边应对，一边稳住节奏，"
narrator_nvl "攻防之间不疾不徐。"
nvl clear
narrator_nvl "客户方负责人翻着报告，一页页地看，像是在翻开市客的折扣广告，生怕错过什么蛛丝马迹。"
narrator_nvl "空气里弥漫着一种无形的紧迫感，像是所有的故障都是可以用人力换取时间的事。"
narrator_nvl "哪怕问题已经解决，客户仍然想要确认‘是否能再多做点什么’。"
narrator_nvl "视线在我们和自家技术团队之间游移，等待最终定论。"
narrator_nvl "新人们机械地做着记录，偶尔偷看上司表情，察言观色。"
nvl clear
narrator_nvl "等到最后一个技术问题确认无误，技术部主管点了点头，"
narrator_nvl "客户交换了个眼神，低声交谈几句，散会的信号随之而来。"
narrator_nvl "人群陆续起身。"
narrator_nvl "椅子挪动的声响、文件合上的啪嗒声、低语交谈声交织在一起，"
narrator_nvl "空气中的沉闷感终于开始消散。"
nvl clear
narrator_nvl "我叹了口气，身体微微前倾，不再坐得那么笔直。"
narrator_nvl "顺手摸起手机，看了眼时间。"
narrator_nvl "时间过得倒是挺快"
narrator_nvl "可惜……不是我的时间。"
nvl clear
narrator_nvl "屈指敲了敲桌面，合上笔记本。"
narrator_nvl "弯腰拔掉插座，顺手卷好电线。"
narrator_nvl "站起身，理了理衬衫下摆。"
nvl clear
narrator_nvl "赔不是环节结束，客户满意地点头，我的工作也算暂时告一段落。"
narrator_nvl "课长走过来，拍拍我的肩膀，说了句：“小子，撤了。”"
nvl clear
narrator_nvl "他的手掌落在肩膀上，力度不大。"
narrator_nvl "但带着某种无言的默契。"
narrator_nvl "这种默契，不需要多说。"
nvl clear
narrator_nvl "这一刻，我才意识到，这一天最难熬的部分，总算过去了。"
nvl clear

# 音效控制
stop music fadeout 2.0
stop sound
$ renpy.pause(1.0, hard=True)

## 更换场景：
window hide
scene bg31 with fade
play music "audio/bgm_yuuhiyaro.mp3" loop
pause 2.0
window show

narrator_nvl "回到公司，已经过了钟。"
narrator_nvl "打卡机滴滴作响，几个同事陆续收拾东西，"
narrator_nvl "“我先走了”“辛苦了啊”的声音此起彼伏，办公室里人越来越少。"
nvl clear

## 更换场景：
window hide
scene bg33 with fade
pause 2.0
window show

c4role2 "“议事录我来写，你赶紧把修正补丁做出来，争取明天远程会议能让客户看到。”"
c4role1 "“明白了。”"
nvl clear
narrator_nvl "我侧了侧身随口应了一句，回过头继续盯着终端界面，手指飞快地敲击键盘。"
nvl clear
narrator_nvl "半小时后，天彻底黑了。课长站在衣架旁穿风衣，一边套袖子一边喊了我一声："
nvl clear
c4role2 "“怎么样？搞得定吗？”"
c4role1 "“啊……大概还要个把小时，吧。”"
c4role2 "“嗨，昨天才睡 4 小时，真扛不住了，我先撤。议事录我回头再写，你这边别拖太晚啊。”"
c4role1 "“好，您慢走。”"
nvl clear
narrator_nvl "等他走了，办公室瞬间安静下来，剩下几个运维的哥们各忙各的，敲键盘的声音此起彼伏。"
narrator_nvl "我扫了一眼控制台上的报错数，原本想重新评估一下还得多久才能收工。"
narrator_nvl "可恶，脑子像风干的水泥，完全纹丝不动，别说算时间了，就连思考都快成奢侈品了。"
narrator_nvl "唉，算了，先去便利店随便垫几口，回来再慢慢收拾吧。"
narrator_nvl "我伸了个懒腰，站起身，拿起钱包、手机和门禁卡，头也不回地喊了句——"
nvl clear
c4role1 "“我去便利店一趟。”"
nvl clear
narrator_nvl "没人搭理，我也没期待什么。只是规矩如此，我也只是习惯了照做。"
nvl clear

## 更换场景：
window hide
scene bg08 with fade
pause 2.0
window show

narrator_nvl "从办公室出来，"
narrator_nvl "短暂地呼吸了一口外面的空气，"
c4role1 "“啊……”"
c4role1 "“社畜加班的夜景真好看。”"
c4role1 "“真特么想一走了之啊。”"
c4role1 "“操。”"

## 更换场景：
window hide
scene bg34 with fade
pause 2.0
window show

narrator_nvl "顺手带回了"
narrator_nvl "一份炸鸡君、"
narrator_nvl "一瓶复合维生素果汁"
narrator_nvl "还有蛋白质能量棒。"

nvl clear
## 更换场景：
window hide
scene bg33 with fade
pause 2.0
window show

narrator_nvl "等着开发环境跑程序的时候，我撕开能量棒，机械地咀嚼着，"
narrator_nvl "一边随手翻着手机相册，一边走神，"
narrator_nvl "想着昨晚的事，还有一些有的没的。"
nvl clear
narrator_nvl "很多照片，早就删了。"
narrator_nvl "不想再翻到的，那些太直接的，已经从网盘里彻底清空。"
narrator_nvl "但有些东西，删不掉。"
nvl clear
narrator_nvl "翻着相册时，偶尔会看到街角的一张风景照，学校门口的晨雾，深夜书桌上的一杯咖啡……"
narrator_nvl "它们本身没什么特别的意义，却总能让我想起些什么。"
narrator_nvl "如果当初做了不同的选择，某个熟悉的对话框会不会毫无预兆地弹出来？"
narrator_nvl "就像那年我在晚自习借着好兄弟的手机聊QQ时，屏幕忽然亮起，她发来的那张让我逃课赶到她身边的自拍一样。"
nvl clear
narrator_nvl "当然，也仅限于想想而已。"
narrator_nvl "时间并不会怜悯我，"
narrator_nvl "给我指出一条回到过去的路。"
nvl clear
narrator_nvl "目光落在工位上的日历，离离职只剩三天。"
narrator_nvl "三天后，这张办公桌就不再属于我。"
narrator_nvl "三天后，这些熟悉的会议、系统报警、客户催促，都和我再无关系。"
narrator_nvl "三天后，我会真正离开这里。"
narrator_nvl "……大概吧。"
nvl clear
narrator_nvl "周五之后，就是带薪假的消化期。"
narrator_nvl "再之后，去新东家报道，见见新团队。"
narrator_nvl "然后，整整两个月的空档，我可以去任何我想去的地方——"
narrator_nvl "毕竟，银行账户里还躺着那些没日没夜加班挣来的钱，"
narrator_nvl "一笔可观的、没来得及花的钱。"
nvl clear
narrator_nvl "补丁比预期完成得更快，意外地和暂存环境的契合度很好。"
narrator_nvl "如果维持这个状态，明天交给客户也不会有怨言吧。"
nvl clear
narrator_nvl "于是打卡，收拾工位。"
nvl clear
c4role1 "“我先下班了，各位辛苦了。”"
nvl clear
stop music fadeout 2.0

# 章节切换处理
show screen next_chapter4_button
pause
hide screen time_display
jump chapter5
return