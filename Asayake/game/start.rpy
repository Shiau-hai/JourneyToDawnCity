screen next_chapter_button():
    vbox:
        xalign 0.5
        yalign 0.9  # 按钮位置调整到屏幕下方
        textbutton "按任意键，朝着朝霞照映的街道，进发。":
            text_size 60  # 调整字体大小
            text_color "#FFFFFF"  # 文字颜色
            action Return()  # 按钮点击后继续游戏
            at breathing_animation  # 应用呼吸闪烁动画

init:
    transform breathing_animation:
        alpha 0.2  # 开始时透明度降低
        linear 1.0 alpha 1.0  # 1秒内淡入
        linear 1.0 alpha 0.2  # 1秒内淡出
        repeat  # 无限循环

    transform fade_centered:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        linear 1.5 alpha 1.0  # 1.5 秒淡入
        
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label start:
scene bg01 with fade

narrator_nvl "这是一部关于孤独的小说。"
narrator_nvl "天际线在晨曦中逐渐晕染出蓝白交织的暖橙色，朝阳升起，万物复苏，一派美好的景象，"
narrator_nvl "然而这并没有给在深秋寒风中孤单伫立的你带来丝毫的撼动。"
narrator_nvl "异乡异客的你，抓着一罐已经喝空的柠檬堂，在模糊的视野中似乎看到了一条通往过去的路。"
narrator_nvl "——《朝着朝霞照映的街道进发》卷头语"
nvl clear
narrator_nvl "说起来，我为什么要写这部小说？"
narrator_nvl "我对异地恋所有美好的幻想，都在2015年彻底破灭。"
narrator_nvl "2015年9月，一段断断续续持续了7年的感情走到尽头，我失恋了。"
narrator_nvl "然而，时间越久，这段感情就像毒药一般，在我的记忆中愈发浓烈。"
nvl clear
narrator_nvl "当时我是这么想的，"
narrator_nvl "每天不管多鸡毛蒜皮的事情都好跟对方分享一下，聊聊最近在忙什么，热衷的事物，最后互相语音晚安，"
narrator_nvl "偶尔能互发自拍照，还挑逗说这就是你今晚的{rb}施法材料{/rb}{rt}Okazu{/rt}。"
narrator_nvl "到后来我发现，除了互道晚安，前面的所有都是写在待办清单上的一些废话。"
nvl clear
narrator_nvl "可我不甘心浪漫就这么死去。因为，我内心中还有一丝侥幸——"
narrator_nvl "也许我们相聚的那天，我从机场的到达口拖着拉杆箱出来，一眼就看到她。"
narrator_nvl "我们奔向对方，然后我把她抱起来，转上好几个圈圈。"
narrator_nvl "一起坐地铁回市区，一起去超市，挑了一堆杂七杂八的酒和下酒菜。"
narrator_nvl "然后就回酒店。接下来，或许这样，或许那样，都可以。"
narrator_nvl "靠着最后这点可怜的幻想撑了下来。"
narrator_nvl "最终，真正压垮我的，是跨越屏幕却始终无法触及的温度差。"
nvl clear
narrator_nvl "我们都好累，那些冰冷屏幕下的画面和声音，逐渐失去了温度——"
narrator_nvl "那是人，一个活人肌肤上该有的温度。"
narrator_nvl "好几次，没能打消对方的疑虑或者误解，却也累得不再多去辩解。"
narrator_nvl "只有苍白的晚安还在继续。"
narrator_nvl "我知道，这趟列车到站了，不会有下一站了。"
nvl clear
narrator_nvl "我校招进的公司加班很严重，使我身心俱疲。"
narrator_nvl "那段时间我常怀疑，这么劳累，到底是为了什么？"
narrator_nvl "也许，累一点可以少去想一些已经无济于事的事情，会好过一点？"
narrator_nvl "在极度疲惫时，我只想有个膝枕，或者有人可以抱抱我，摸摸我的头发，"
narrator_nvl "可就连这么简单的需求，都无法实现。"
nvl clear
narrator_nvl "2018年6月的某个周六，我喝了个烂醉，准备出门去吹吹晚风，醒醒酒。"
narrator_nvl "正如我刚来到新小岩时度过的无数个无眠之夜那样，我来到新小岩公园，看着公园里的一个电话亭发呆。"
narrator_nvl "我很想给她打个电话，告诉她我很后悔。"
narrator_nvl "但我知道，这是无法挽回的事情，成熟的大人就应该为自己的行为负责。"
nvl clear
narrator_nvl "像致幻剂一样的她，让我沉溺其中无法自拔。"
narrator_nvl "一个人待得越久，对爱的渴望就越强烈。"
narrator_nvl "有一段时间甚至觉得以前的雷点的病娇都可爱起来了，"
narrator_nvl "因为病娇换句话说就是太过爱了，爱过了火。"
narrator_nvl "而我的空洞不见得过火就能填上。"
nvl clear
narrator_nvl "我希望每个睡不好的夜晚，无数次闯入我梦乡的，不再是我再也见不到的人。"
narrator_nvl "我必须和我的过去说永别。"
narrator_nvl "明天在等待，我不能止步不前。"
narrator_nvl "正如我希望，这本小说不是我为自己施加的诅咒，而是对未到的未来的祝福。"
narrator_nvl "现在，就让我——"

show screen next_chapter_button
pause  # 让玩家可以点击按钮或按任意键继续

jump chapter1

return
