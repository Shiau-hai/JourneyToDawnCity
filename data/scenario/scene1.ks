*start

;各設定項目初期化
[cm  ]
[clearfix]
[start_keyconfig]
[bg storage="bg01.jpg" time="100"]
;メニューボタンの表示
@showmenubutton
;メッセージウィンドウの設定
[position layer="message0" left=20 top=530 width=1330 height=200 page=fore visible=true]
[position layer=message0 page=fore margint="45" marginl="50" marginr="70" marginb="60"]
;メッセージウィンドウの表示
@layopt layer=message0 visible=true

;キャラクターの名前が表示される文字領域
[ptext name="chara_name_area" layer="message0" color="white" size=24 x=50 y=540]
[chara_config ptext="chara_name_area"]

;-------------------------------------------------------------------------
;キャラクター定義
;-------------------------------------------------------------------------
;akane
[chara_new  name="tomomi" storage="chara/tomomi/tujo.png" jname="アイナ"  ]
;表情登録
[chara_face name="tomomi" face="tujo" storage="chara/tomomi/tujo.png"]
[chara_face name="tomomi" face="nissisi" storage="chara/tomomi/nissisi.png"]
[chara_face name="tomomi" face="tere" storage="chara/tomomi/tere.png"]
[chara_face name="tomomi" face="honto" storage="chara/tomomi/honto.png"]
[chara_face name="tomomi" face="gekiko" storage="chara/tomomi/gekiko.png"]
[chara_face name="tomomi" face="ase" storage="chara/tomomi/ase.png"]
[chara_face name="tomomi" face="yay" storage="chara/tomomi/yay.png"]
;ヒロイン好感度定義
[eval exp="sf.heroin_koukando = 0"] 
#
我叫Hiro，[l]这里是御台场海滨公园，[l]今天是12月24日，[p]
又是一年平安夜，[l]就读于都内私立大学的哥，都大三的人了到现在连个女朋友都没有。[p]
没有女朋友也就算了吧，还逞嘴上一时之快把研究室的忘年会随便编了个“真不巧今晚有约哥几个吃好喝好哈”之类的理由推掉之后，[l]来到了本来的话不会来的御台场。[p]
明明没有女朋友，耍什么风流啊。[p]
不，[l]不是的。[p]
我今天来到这里并不是偶然。[l]来了无数次，[l]看了无数次这有着治愈人们的不可思议的力量的海滨景色的我明白——[p]
[bg  time="3000"  method="crossfade" storage="bg02.jpg"  ]
御台场在召唤着我！今天这是要发生奇迹的节奏啊！[p]
[font  size="30"   ]
#?
“……一下～”[p]
[resetfont  ]
#
哎？[l]年方21之际年龄跟没有女朋友的年数画等号[l]这种经历都能炫出来的我，在这个“平安夜的御台场”的情景下，[l]也终于失去理智产生了自己有个空气做的女朋友的幻觉了吗。[p]

;キャラクター登場
[chara_show  name="tomomi" left="340" top="110" ]

#?
“你好～打扰一下～”[p]
#
随着清晰的声音回到现实，[l]眼前出现了一位年纪相仿的少女。[p]
#主人公
“唉不好意思，[l]您叫我吗？”[p]
#
说着被少女递过来一个包着可爱的手机壳的手机。[p]
#?
“能请您帮忙拍个照吗？”[p]
#
“好啊没问题。”[p]

[chara_mod  name="tomomi" face="nissisi"  ]
#?
“太谢谢您了！”[p]

[chara_mod  name="tomomi" face="tujo"  ]
#
少女靠过来，[l]伸出手熟练地解锁手机点开了相机应用，[l]手指细长而白，指甲上涂着可爱的纹样。[l]一瞬间闻到了一股淡淡的香气。[p]
#?
“摁一下这边的快门键就好的，那[l]就拜托啦！”[p]
她朝我做了个拜托了的手势，[l]然后一边确认背后的视野一边后退到拍照的位置，[l]摆好了姿势看着我这边。[p]
倒是没说要怎么拍，我也忘了问，[l]总之怎么拍好呢？[p]
[glink  graphic="button/button_selection.png"  size="32" x="220"  y="135" width="800" text="哎呀妹子客气了，一起拍吧！"  target="*ev1_select1"  ]
[glink  graphic="button/button_selection.png"  size="32" x="220"  y="255" width="800" text="那必须是把妹子拍得美美的啊"  target="*ev1_select2"  ]
[glink  graphic="button/button_selection.png"  size="32" x="220"  y="375" width="800" text="把妹子跟背景一起拍进去"  target="*ev1_select3"  ]
[s  ]
*ev1_select1
;好感度変化
[eval exp="sf.heroin_koukando = sf.heroin_koukando -1 "]
#
原来如此，是想跟我一起拍照啊，[l]这妹子真客气哈哈。[p]
#
“那我就恭敬不如从命……”[p]
#
当我走向少女的方向时，[l]少女一脸困惑地叫我停一下。[p]
[chara_mod  name="tomomi" face="ase"  ]
#?
“啊，不是这样的，[l]是想请您从您现在的位置为我拍一张这样的……”[p]
#
咦？我怎么自作多情以为是妹子想跟我一起拍呢？[l]哎呀失态失态。[p]
#
「哦~原来这样啊，[l]哎呀你看我这，[l]真不好意思哈哈~」[p]
#?
「不会~请别在意。」[p]
#
（少女的好感度，稍微下降了。）[p]
@jump target=*common 
*ev1_select2
[chara_mod  name="tomomi" face="tere"  ]
#
选择了第二个选项哦[p]
@jump target=*common 
*ev1_select3
[chara_mod  name="tomomi" face="nissisi"  ]
#
选择了第三个选项哦[p]
@jump target=*common 

*common
#
[chara_mod  name="tomomi" face="yay"  ]
开发进度目前到这里为止。更多内容敬请期待哟。[p]
test.
[cm]
[s]

