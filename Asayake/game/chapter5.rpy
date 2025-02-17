init python:
    # 定义黄褐色滤镜（老电影效果）
    sepia_matrix = im.matrix(
        [0.393, 0.769, 0.189, 0, 0,
         0.349, 0.686, 0.168, 0, 0,
         0.272, 0.534, 0.131, 0, 0,
         0,     0,     0,     1, 0])
    # 定义白飞效果
    white_fade = Fade(1.5, 1.0, 1.5, color="#FFFFFF")

init:
    # 定义一个较长的渐变转场
    define long_dissolve = Dissolve(1.5)

    # 定义模糊后的背景
    image blur_bg28 = im.Blur("bg28.jpg", 12)
    image blur_bg01 = im.Blur("bg01.jpg", 12)
    image blur_bg29 = im.Blur("bg29.jpg", 12)
    image blur_bg51 = im.Blur("bg51.jpg", 12)
    image blur_bg54 = im.Blur("bg54.jpg", 12)
    image blur_bg56 = im.Blur("bg56.jpg", 12)
    image blur_bg57 = im.Blur("bg57.jpg", 12)
    
    # 定义加了黄褐色滤镜的回忆背景
    image sepia_bg14 = im.MatrixColor("bg14.jpg", sepia_matrix)
    image sepia_bg21 = im.MatrixColor("bg21.jpg", sepia_matrix)
    image sepia_bg55 = im.MatrixColor("bg55.jpg", sepia_matrix)

    # 定义模糊的回忆背景
    image seblu_bg14 = im.Blur(im.MatrixColor("bg14.jpg", sepia_matrix), 10)
    image seblu_bg21 = im.Blur(im.MatrixColor("bg21.jpg", sepia_matrix), 10)
    image seblu_bg55 = im.Blur(im.MatrixColor("bg55.jpg", sepia_matrix), 10)

# 角色定义（必须放在 init 代码块外，或者单独用 init python:）
define c5role1 = Character('我', color="#c8c8ff", image="c5role1")
define c5role2 = Character('“她”', color="#c8c8ff", image="c5role2")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label chapter5:
## 章节初始化处理
scene black
nvl clear
window hide
stop sound
hide screen next_chapter4_button

## 时间指示器相关处理
show text "2021年，11月" at fade_centered with fade
pause 3.0
hide text with fade
pause 2.0

## 显示窗口
play music "audio/bgm_chapter5.mp3" loop
play sound "audio/element_kaze.mp3" loop
scene bg28 with fade
pause 2.0

$ current_date = "2021年 11月 22日"
show screen time_display
window show

narrator_nvl "秋意已深，早晨的气温冷到不穿毛衣都不敢出门。"
narrator_nvl "但作为广东人的矜持，我还是没穿长袖秋裤。"
narrator_nvl "一夜无眠，我坐在新小岩公园棒球场边的板凳上，面朝天空树。"
play sound "audio/sound_nomikomu.mp3"
narrator_nvl "干了三罐柠檬堂。"
nvl clear
c5role1 "\"震惊!旅日粤人竟对天空树做出那种事！"
c5role1 "……噗！哈哈哈哈哈哈……嗝儿！\""
c5role1 "“哎等等，我是不是还没吃早餐？哈哈哈哈……嗝儿！”"
c5role1 "“麦当劳薯条~屌~屌~屌~……哈哈……嗝儿！”"
nvl clear
narrator_nvl "酒精打开的毛孔，让黎明前的冷空气直钻进身体。"
narrator_nvl "我从似醉犹醒的飘飘然，变成了被寒风吹得直打哆嗦的狼狈样子。"
nvl clear
c5role1 "\"谁叫你讲烂gag的，你……活该！"
c5role1 "哈哈哈哈哈哈哈……嗝儿！\""
nvl clear
narrator_nvl "大秋天穿着卫衣半裤人字拖也就算了，"
narrator_nvl "还趁着醉酒讲一些冷笑话，"
narrator_nvl "谁见了这样的男人都会不自觉把他当成流浪汉吧。"
narrator_nvl "嘿，管他的呢。"
narrator_nvl "现在我感觉自己能穿梭在不同的时空中，感觉不能更棒了。"
nvl clear
# "现实开始变得模糊..."

hide screen time_display
show blur_bg28 with long_dissolve

## 音效控制
stop sound fadeout 2.0
$ renpy.pause(1.0, hard=True)

$ current_date = "2017年 07月 7日"
show screen time_display

## 更换场景：手机
window hide
# 过渡到回忆场景（老电影风格）
scene sepia_bg14 with white_fade
pause 2.0
window show

c5role1 "“昨天不好意思，加班加到12点，打的回来之后直接睡了忘记回你信息了。”"
c5role2 "“没关系，我也在赶稿。”"
c5role1 "“不要这样拼好吗？大不了我回去养你啊。”"
hide screen time_display
show seblu_bg14 with long_dissolve
nvl clear

$ current_date = "2021年 11月 22日"
show screen time_display

## 更换场景：朝霞
window hide
scene bg01 with white_fade
pause 2.0
window show

narrator_nvl "抬起手环看了看表，差不多到日出的时候了，"
narrator_nvl "该回去了。"
narrator_nvl "我把空的易拉罐都扔到自贩机旁边的回收箱，"
narrator_nvl "拿着最后一罐还没喝完的柠檬堂往家走去。"
nvl clear
narrator_nvl "已记不得是什么时候以来了，"
narrator_nvl "像今天这般感到自由，却又感到失落。"
nvl clear
narrator_nvl "天空渐渐变亮，朝霞染出一抹漂亮的渐变色。"
play sound "audio/sound_walk.mp3"
narrator_nvl "我朝朝霞射来的方向迎面走去，"
narrator_nvl "那是家的方向。"
nvl clear
# "现实开始变得模糊..."
hide screen time_display
show blur_bg01 with long_dissolve

## 音效控制
stop sound fadeout 2.0
$ renpy.pause(1.0, hard=True)

$ current_date = "2008年 6月 7日"
show screen time_display

## 更换场景：手机
window hide
# 过渡到回忆场景（老电影风格）
scene sepia_bg21 with white_fade
pause 2.0
window show

c5role1 "“我们这样到底算什么关系？”"
c5role2 "“嗯……就，兄妹？”"
c5role1 "“那你叫一声{rb}哥哥{/rb}{rt}Oniichan{/rt}来听听？”"
c5role2 "“{rb}不要{/rb}{rt}Iyada{/rt}！”"

hide screen time_display
show seblu_bg21 with long_dissolve

$ current_date = "2021年 11月 22日"
show screen time_display

## 更换场景：朝霞
window hide
scene bg29 with white_fade
play sound "audio/element_morning.ogg" loop
pause 2.0
window show

narrator_nvl "走在一个人都没有的住宅街的路上，"
narrator_nvl "耳边只听到渐渐多起来的鸟鸣声，"
narrator_nvl "还有偶尔的一两声异常凄厉的乌鸦叫。"
nvl clear

## 更换场景：新小岩月台
window hide
scene bg30 with fade
play sound "audio/element_shotengai.ogg"  loop
pause 2.0
window show

narrator_nvl "路过了商店街，"
narrator_nvl "这里再过两小时会有垃圾车开进来回收垃圾，"
narrator_nvl "紧闭着的卷闸门也会一扇接着一扇地拉开。"
nvl clear

stop sound fadeout 0.5
## 更换场景：新小岩月台
window hide
scene bg51 with fade
play sound "audio/element_kosaten.mp3"  loop
pause 2.0
window show

narrator_nvl "我站在车站前的十字路口信号灯处等了半天红绿灯，"
narrator_nvl "发现红绿灯这时是黄闪，才快步通过。"
narrator_nvl "而在我身后，红绿灯从黄闪变成了红灯。"
nvl clear

# "现实开始变得模糊..."

hide screen time_display
show blur_bg51 with long_dissolve

## 音效控制
stop sound fadeout 2.0
$ renpy.pause(1.0, hard=True)

$ current_date = "2015年 3月 1日"
show screen time_display

## 更换场景：手机
window hide
# 过渡到回忆场景（老电影风格）
scene sepia_bg55 with white_fade
pause 2.0
window show

c5role2 "“话说回来，我们这样真的好老夫老妻哦~！”"
c5role1 "“听你这么一说好像确实……”"
c5role2 "“对啊，好像以前我们在一起的时候，就算什么也不说，只要牵着手就好了”"
c5role1 "“嗯。……嗯。（重新握住）”"

hide screen time_display
show seblu_bg55 with long_dissolve
nvl clear

$ current_date = "2021年 11月 22日"
show screen time_display

## 更换场景：朝霞
window hide
scene bg51 with white_fade
play sound "audio/element_kosaten.mp3"  loop
pause 2.0
window show

narrator_nvl "路过的罗森前的栏杆处靠着两个穿着工装的看起来是土木工人，"
narrator_nvl "拿着一罐咖啡在一边抽烟一边说着什么。"
nvl clear
stop sound fadeout 0.5

## 更换场景：新小岩月台
window hide
scene bg52 with fade
play sound "audio/element_morning.ogg"  loop
pause 2.0
window show

narrator_nvl "往前走过几个路口后是一座小学，"
narrator_nvl "再过两个小时，充满朝气的小学生们会排成一队朝着校门进发。"
nvl clear

## 更换场景：新小岩月台
window hide
scene bg54 with fade
pause 2.0
window show

narrator_nvl "然后就是平时一直路过却没有怎么进去过的小公园。"
narrator_nvl "我环顾了公园一周，"
narrator_nvl "但又仔细想想觉得有些滑稽——"
narrator_nvl "好像能在这里遇到谁似的。"
nvl clear

# "现实开始变得模糊..."

hide screen time_display
show blur_bg54 with long_dissolve

## 音效控制
stop sound fadeout 2.0
$ renpy.pause(1.0, hard=True)

$ current_date = "2008年 3月 26日"
show screen time_display

## 更换场景：手机
window hide
# 过渡到回忆场景（老电影风格）
scene sepia_bg21 with white_fade
pause 2.0
window show

c5role1 "“咦？原来你也知道《幸运星》？”"
c5role2 "“对啊我超喜欢的，"
c5role2 "还有《反叛的鲁路修》，"
c5role2 "还有《银魂》，"
c5role2 "还有《蔷薇少女》，"
c5role2 "还有……”"

hide screen time_display
show seblu_bg21 with long_dissolve
nvl clear

$ current_date = "2021年 11月 22日"
show screen time_display

## 更换场景：朝霞
window hide
scene bg53 with white_fade
play sound "audio/element_morning.ogg"  loop
pause 2.0
window show

narrator_nvl "终于，到了家楼下的一排自动贩卖机前面。"
narrator_nvl "我把喝剩的柠檬堂一口气灌下，"
narrator_nvl "把空罐放进自贩机旁的回收箱，"
play sound "audio/sound_jihanki.mp3"
narrator_nvl "又掏出零钱袋，从自贩机买了瓶冰露，"
pause 3.0
play sound "audio/sound_nomikomu.mp3"
narrator_nvl "吨吨吨吨牛饮几口，"
narrator_nvl "呛到把卫衣弄湿了。"
nvl clear

## 更换场景：新小岩月台
window hide
scene bg56 with fade
play sound "audio/element_morning.ogg"  loop
pause 2.0
window show

narrator_nvl "然后推开公寓大门，"
narrator_nvl "走到信箱前，打开信箱，"
narrator_nvl "把里面的广告传单全部扔进墙角的废纸篓。"
narrator_nvl "然后上楼。"
nvl clear
narrator_nvl "是啊，"
narrator_nvl "我在期待个什么劲呢？"
nvl clear

# "现实开始变得模糊..."

hide screen time_display
show blur_bg56 with long_dissolve

## 音效控制
stop sound fadeout 2.0
$ renpy.pause(1.0, hard=True)

$ current_date = "2008年 7月 10日"
show screen time_display

## 更换场景：手机
window hide
# 过渡到回忆场景（老电影风格）
scene sepia_bg21 with white_fade
pause 2.0
window show

nvl clear
c5role2 "“你对我真的很好呢，"
c5role2 "你真的只是想和我做普通的朋友吗？”"
c5role1 "“被你发现了啊，"
c5role1 "其实我想说——"
c5role1 "做我女朋友好吗？”"
c5role2 "“嗯……"
c5role2 "让我回去好好考虑一下"
c5role2 "好吗？”"
nvl clear

hide screen time_display
show seblu_bg21 with long_dissolve
nvl clear

$ current_date = "2021年 11月 22日"
show screen time_display

## 更换场景：朝霞
window hide
scene bg44 with white_fade
play sound "audio/element_morning.ogg"  loop
pause 2.0
window show

narrator_nvl "我拿出一罐肝肾脏提取物的营养剂药片，"
narrator_nvl "或者说安慰剂药片，"
narrator_nvl "端详了一会儿。"
nvl clear
narrator_nvl "她比我还能喝，我这点真不够她看的。"
nvl clear
play sound "audio/sound_nomikomu.mp3"
narrator_nvl "拿出两片，用水服下。"
nvl clear

## 更换场景：新小岩月台
window hide
scene bg57 with fade
pause 2.0
window show

narrator_nvl "虽然太阳在这会儿刚刚升起，"
narrator_nvl "洗漱完的我看着太阳投射在窗户的毛玻璃上的光斑，"
narrator_nvl "却只剩睡意。"
nvl clear
narrator_nvl "我想起了那年夏天，和她坐在江边，"
narrator_nvl "看着夕阳将整座城市染上回忆感伤的金黄，"
narrator_nvl "我想起我承诺过的，"
narrator_nvl "等我来了日本，我要把她也接来，"
narrator_nvl "带着她远走高飞。"
nvl clear
narrator_nvl "我们去京都，"
narrator_nvl "去北海道，"
narrator_nvl "去濑户内海，"
narrator_nvl "去美术馆，"
narrator_nvl "去水族馆，"
narrator_nvl "去天象馆，"
narrator_nvl "去迪斯尼，"
narrator_nvl "去富士急，"
narrator_nvl "去环球影城，"
narrator_nvl "去滑雪，"
narrator_nvl "去潜水，"
narrator_nvl "去花火大会，"
narrator_nvl "去新年的神社，"
narrator_nvl "去海边，"
narrator_nvl "去山里，"
narrator_nvl "去很多很多没有去过的地方。"
nvl clear
# "现实开始变得模糊..."

hide screen time_display
show blur_bg57 with long_dissolve

## 音效控制
stop sound fadeout 2.0
$ renpy.pause(1.0, hard=True)

$ current_date = "2008年7月10日"
show screen time_display

## 更换场景：手机
window hide
# 过渡到回忆场景（老电影风格）
scene sepia_bg21 with white_fade
pause 2.0
window show

c5role2 "“关于你刚刚说的话，我考虑过了。”"
c5role1 "“嗯，可以吗？”"
c5role2 "“可以哦。”"
c5role1 "“太好了！"
c5role1 "呜……太好了！”"
nvl clear

hide screen time_display
show seblu_bg21 with long_dissolve
nvl clear

$ current_date = "2021年 11月 22日"
show screen time_display

## 更换场景：朝霞
window hide
scene bg01 with white_fade
pause 2.0
window show

narrator_nvl "而今天我，"
narrator_nvl "独自一人，"
narrator_nvl "在这朝霞照映的街道，"
narrator_nvl "沉沉睡去。"
nvl clear
narrator_nvl "（完）"

return