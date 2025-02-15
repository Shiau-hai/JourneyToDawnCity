screen next_chapter1_button():
    vbox:
        xalign 0.5
        yalign 0.9
        ## 闪烁文本内容
        textbutton "按任意键，进入记忆漩涡的中心。":
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

define role1 = Character('众人', color="#c8c8ff", image="role1")
define role2 = Character('新人', color="#c8c8ff", image="role2")
define role3 = Character('我', color="#c8c8ff", image="role3")
define role4 = Character('K桑', color="#c8c8ff", image="role4")
define role5 = Character('xx桑', color="#c8c8ff", image="role5")
define role6 = Character('谜之声', color="#c8c8ff", image="role6")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label chapter1:
## 章节初始化处理
hide screen next_chapter_button
scene black
nvl clear
window hide

## 音效控制
stop music fadeout 2.0
stop sound
stop audio
$ renpy.pause(0.1, hard=True)



## 时间指示器相关处理
show text "2021年，10月" at fade_centered with fade
pause 3.0
hide text with fade
pause 2.0

## 显示窗口
play music "audio/bgm_blues.mp3"
scene bg02 with fade
pause 2.0

$ current_date = "2021年 10月 17日"
show screen time_display
window show

narrator_nvl "这里是惠比寿，但凡年轻潮人名流之士都向往的地方。"
narrator_nvl "离日剧里面频频登场的一到春天盛开的樱花会把一条河都染成樱花色的目黑川也就稍微走走路的样子。"
narrator_nvl "这么潮的地方怎么都跟我搭不上吧？"
narrator_nvl "心里虽然这么想着，一时冲动答应同期的T君的相亲party，到头来还是来了啊。"
narrator_nvl "还能怎么办，现在再想打退堂鼓也来不及了吧。"
nvl clear

## 更换场景：酒吧
window hide
scene bg03 with fade
play sound "audio/element_party.mp3" loop
pause 2.0
window show

narrator_nvl "相亲的会场在某个行家之间评分颇高颇有气氛的，喝啤酒的露天音乐吧。"
narrator_nvl "不知名的上头的外国音乐，各种各样的客人，嘈杂的谈笑声——"
narrator_nvl "虽然还没开始喝，我竟有些酩酊的感觉。"
narrator_nvl "就在视线开始模糊之时，干事洪亮的一声把我拉回了现实。"
nvl clear
narrator_nvl "“既然饮料都到齐了，今天大家都尽兴啊，干杯！”"
role1 "“干杯！！”"
nvl clear
narrator_nvl "众人纷纷举杯碰杯。"
narrator_nvl "该说不愧是证券公司的营业备受瞩目的新人么，这身行头，这西装，这香水，这皮鞋，这言语谈吐，感觉对面的女生瞬间被他拿下一半了。我这么想。"
role2 "“那，咱们就直奔主题吧，自我介绍走一个，就从……角落开始吧！”"
nvl clear
narrator_nvl "这家伙绝对是故意的，他明明刚才在坏笑！虽然这么想着，我赶紧站了起来。"
role3 "“我叫晓，我是一名架构师，今年……呃，29岁，在第一赛博解决方案公司上班。请多关照！”"
nvl clear
narrator_nvl "然后坐下。是啊，为什么在年龄那里顿了一下，其实再没几天就是自己的生日了，马上就是30岁了，虽然跟已经是30岁没什么区别，这算我的一点最后的倔强吧。"
narrator_nvl "然后我之后其他人也一一做了自我介绍。"
role2 "“那，既然都一一做过了自我介绍，接下来的15分钟请好好享受跟对面的朋友的愉快交流吧！”"
nvl clear
narrator_nvl "呵，愉快，说得容易啊。我瞥了下拉我来的T君，这家伙早已进入状态了，丝毫没有跟进我这边进度的意思。看来我被队友卖了啊，哈哈哈哈。"
narrator_nvl "我跟对面的姑娘面面相觑，半晌，那姑娘好死不死偏偏抛出一句："
role4 "“欸，说起来，晓君的工作都是做些什么的呢？”"
nvl clear
narrator_nvl "我的理智极力阻止我接这个话茬，但是等我大脑的指令到达嘴巴时，嘴巴已经借着酒劲先走火了。"
role3 "“虽然在名片上，我被定义为系统工程师，这就有点太笼统了。"
role3 "这年头干系统工程师的人可太多了，而我们架构师，正确地说，是根据某种目的，按要求构筑某种情报系统的架构。同时呢，目的不一样，造出来的东西复杂程度也不一样。"
role3 "小到一个只有寥寥几行，甚至不如小学生的作文字数多的小程序，大到占地有一个东京巨蛋大小的建筑里容纳着上千台计算机和存储器，"
role3 "即使换算成超高清晰度的数字电影总时长也够一个人轮回好几百次的数据量每天从这座建筑吞进去吐出来的庞然大物。"
role3 "连这样的东西也能造出来的职业，单单一个系统工程师怎么说得完呢？对吧？“"
nvl clear
narrator_nvl "完了，我完了，枉我一世英名，毁于一旦。假酒害人啊。"
narrator_nvl "我真的宁可今天没有来过这里，如此般我即使是腐烂成一滩臭水，那这臭水也是清白的。"
narrator_nvl "我偏偏挑了最不适合的场合，说了最不美妙的话，而这已经从对面姑娘的尴尬神情窥见一二了。"
narrator_nvl "不过，我作为社会人的这几年也不是白混的，赶紧打圆场。"
role3 "“K桑，刚刚自我介绍时，有说在广告设计公司上班，对吗？我听说广告设计也挺辛苦的，对吧？”"
nvl clear
narrator_nvl "对方马上犹如“你这孙子终于开窍了”般醒悟过来，这天总算没有聊死。"
narrator_nvl "然后，我们就“甲方到底是不是傻逼”进行了15分钟愉快而没有建设性的交流。"
nvl clear

# 音效控制
stop sound
stop audio
$ renpy.pause(1.0, hard=True)

## 更换场景：散场
window hide
play sound "audio/element_townnight.mp3" loop
scene bg04 with fade
pause 2.0
window show

narrator_nvl "之后，轮换了几次座位，跟所有人都交换了联系方式，便到了一次会解散的时间。"
narrator_nvl "虽然T君礼节性地挽留了一下我，但我很识趣地找了个非常随便的理由开溜了。"
narrator_nvl "反正都二次会了就算只剩他们5个，按T君和那个超级精英证券公司营业新人君那个派对动物的特质来看，也能玩得很尽兴的吧。"
nvl clear
narrator_nvl "至于我？相亲什么的，见鬼去吧。"
play sound "audio/sound_nomikomu.mp3"
narrator_nvl "我把相亲这个设定完全抛到脑后，只管把店里的精酿啤酒各个牌子都喝了个遍。"
play sound "audio/sound_heartbeats.mp3"
narrator_nvl "这时候，不用照镜子摸自己的胸口量心跳都能猜到我脸已经红成猴子屁股了。"
play sound "audio/sound_walk.mp3"
narrator_nvl "我听着自己粗粗的呼吸声朝电车站走去。"
stop sound
nvl clear

## 更换场景：自动贩卖机
window hide
scene bg09 with fade
play sound "audio/sound_jihanki.mp3"
pause 3.0
window show

play sound "audio/sound_nomikomu.mp3"
narrator_nvl "路上，路过了一个不知道什么自动贩卖机，买了瓶宝矿力，吨吨吨了几口"
narrator_nvl "摸出手机，才8点不到，晚上才刚刚开始呢。"
narrator_nvl "这之后我摇摇晃晃地掏出交通卡过了剪票口，上了月台，等车来了以后，勉强找到位子坐下。"
nvl clear

# 音效控制
stop sound
stop audio
$ renpy.pause(1.0, hard=True)

## 更换场景：电车
window hide
scene bg05 with fade
play sound "audio/element_train.ogg" loop
pause 2.0
window show

narrator_nvl "当我在电车的暖气全开的座位上蜷缩到一个刚刚好的姿势，并在酒精的作用下昏昏欲睡时，手机忽然震动了一下。"
narrator_nvl "一般来说这时候我大概会犹豫一下要不要确认是什么通知，"
narrator_nvl "但这一次有些不一样。"
play sound "audio/sound_bubu.mp3"
narrator_nvl "因为，正当我犹豫的时候，马上就接二连三地发来了第二条第三条。"
nvl clear
stop sound
narrator_nvl "我只好睁开睡眼点开，发现是LINE的新消息通知。心想——"
narrator_nvl "不是吧？二次会都没结束就开始给刚交换联络方式的相亲对象发消息，"
narrator_nvl "现在的相亲party这么卷的吗？"
narrator_nvl "然后点开LINE，果然是刚才三个女生中的其中一个。我回忆了一下，是个短发妹子。"
play sound "audio/sound_popup.wav"
role5 "“二次会好无聊~”"
play sound "audio/sound_popup.wav"
role5 "“可以去你家吗？”"
play sound "audio/sound_popup.wav"
role5 "“我们再喝过吧~”"
play sound "audio/sound_popup.wav"
role5 "“[[一张集体照片，二次会的卡拉OK包厢和各种艺术字]”"
nvl clear
narrator_nvl "要是一般人看到这种来势汹汹的妹子的话估计就怂了，但我刚好已经脱离了一般人的范畴，再加上酒精的驱使，我给她回复了。"
play sound "audio/sound_typing.mp3"
role3 "“喂喂，这才二次会吧？”"
play sound "audio/sound_typing.mp3"
role3 "“自己答应留下来还说无聊什么的，对一起去的人有些不礼貌哟”"
play sound "audio/sound_typing.mp3"
role3 "“我家？我家啥也没有啊，xx桑来了大概也会感到无聊，这样也没问题吗？”"
nvl clear
stop sound
narrator_nvl "发完这些字以后我便锁上屏幕往座位后靠了靠，"
narrator_nvl "电车的玻璃忠实地传递着铁轨上细微的颠簸，"
narrator_nvl "我想我这时候真的是醉了。"
nvl clear
narrator_nvl "说起来，并想不起那个妹子长什么样子。"
narrator_nvl "嗨，我本来就没有认真去参加的意思，只是同期T君盛情难却，姑且是来了，"
narrator_nvl "倒也没有通过这次相亲达成什么的意思。"
narrator_nvl "虽说吧，我单身一事属实，"
narrator_nvl "但要论及改变现状，我其实是没有准备的。"
nvl clear
play sound "audio/sound_bubu.mp3"
narrator_nvl "（手机震动声，连续震动声）"
narrator_nvl "回过神来，解锁手机，刚才那个妹子发来了信息。"
stop sound
play sound "audio/sound_popup.wav"
role5 "“不会哦，有啤酒和薯条就好了”"
play sound "audio/sound_popup.wav"
role5 "“比起这个，最近的车站在哪里？”"
play sound "audio/sound_popup.wav"
role5 "“（表情包，wakuwaku）”"
nvl clear
stop sound
narrator_nvl "我以为妹子是喝醉了所以说玩笑话的。却不曾想妹子好像真的有来的意思。"
narrator_nvl "怎么办？回绝吗？"
narrator_nvl "我关上手机抬头，把视线投向上方的电车车厢广告。"
nvl clear
narrator_nvl "如今我孑然一身，"
narrator_nvl "既没有扯不清的前任，"
narrator_nvl "也没有热恋中的现任，"
narrator_nvl "更没有需要回应的表白。"
narrator_nvl "想来，似乎并无负心之可能，"
narrator_nvl "况且今宵的酒尚未尽欢，"
narrator_nvl "似醉犹醒，"
narrator_nvl "反而难过。"
narrator_nvl "对影小酌虽无不可，有美人与我对饮则更是美妙，"
narrator_nvl "于是我非常轻而易举地输给了自己的冲动，决心给她回消息。"
play sound "audio/sound_typing.mp3"
role3 "“JR新小岩”"
play sound "audio/sound_typing.mp3"
role3 "“我去剪票口接你吧，这边剪票口只有一个，还挺好找的。”"
nvl clear
narrator_nvl "发完这条消息后，锁上手机，我把视线投向列车窗户外面。"
narrator_nvl "电车在黑夜的铁道上飞驰，外面不断掠过各种或独栋住宅或集体住宅或商业楼或广告牌电线杆什么的。"
narrator_nvl "酒精作用下有点困，我强打起精神。"
narrator_nvl "脑海中不断重复着某个人的声音，我试图去听清。"
role6 "“你……以冷……一下？”"
nvl clear
narrator_nvl "什么？"

# 音效控制
stop music fadeout 2.0
stop sound
stop audio
$ renpy.pause(1.0, hard=True)

play music "audio/bgm_bocchi.mp3"
role6 "“……就算了吧。像个电子宠物”"
nvl clear
narrator_nvl "你是谁？为什么我知道你的声音。"
role6 "“嫁给我好不好？”"
nvl clear
narrator_nvl "不行啊，我听不清你说什么。"
nvl clear
narrator_nvl "我甩了甩头，试图让自己回过神来。"
narrator_nvl "我拿出手机下意识看了看时间，现在是2021年，我已经在日本了。"
narrator_nvl "刚刚那个声音来自过去。但很熟悉。我试图追溯这股熟悉的声音。"
narrator_nvl "电车驶入隧道，透过车窗玻璃，我看着反光里的自己喝醉后的样子，有些不堪的记忆涌上心头。"

# 章节切换处理
show screen next_chapter1_button
pause
hide screen time_display
jump chapter2
return