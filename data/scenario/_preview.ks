[_tb_system_call storage=system/_preview.ks ]

[mask time=10]
[mask_off time=10]
*start

[cm  ]
[clearfix]

[start_keyconfig]

[bg  storage="room.jpg"  time="100"  ]
[showmenubutton]

[position layer="message0" left=20 top=400 width=920 height=200 page=fore visible=true]

[position layer=message0 page=fore margint="45" marginl="50" marginr="70" marginb="60"]

[layopt layer=message0 visible=true]

[ptext name="chara_name_area" layer="message0" color="white" size=24 x=50 y=410]

[chara_config ptext="chara_name_area"]

[chara_new  name="akane" storage="chara/akane/normal.png" jname="あかね"  ]

[chara_face name="akane" face="angry" storage="chara/akane/angry.png"]

[chara_face name="akane" face="doki" storage="chara/akane/doki.png"]

[chara_face name="akane" face="happy" storage="chara/akane/happy.png"]

[chara_face name="akane" face="sad" storage="chara/akane/sad.png"]

[chara_new  name="yamato"  storage="chara/yamato/normal.png" jname="やまと" ]

#
さて、ゲームが簡単に作れるというから、来てみたものの[p]
誰もいねぇじゃねぇか。[p]
……[p]
帰るか。。。[p]


[font  size="30"  ]
#?
ちょっとまったーーーーー[p]


[resetfont  ]
#
誰だ！？[p]


[chara_show  name="akane"  ]
#?
こんにちは。[p]
私の名前はあかね。[p]
#あかね
もしかして、ノベルゲームの開発に興味があるの？[p]


[glink  color="blue"  storage="scene1.ks"  size="20"  x="260"  width="400"  y="100"  text="はい。興味あります"  target="*selectinterest"  ]
[glink  color="blue"  storage="scene1.ks"  size="20"  x="260"  width="400"  y="170"  text="興味あります！"  target="*selectinterest"  ]
[glink  color="blue"  storage="scene1.ks"  size="20"  x="260"  width="400"  y="240"  text="どちらかと言うと興味あり"  target="*selectinterest"  ]
[s  ]
*selectinterest

[chara_mod  name="akane"  face="happy"  ]
#あかね
わー。興味あるなんて、嬉しいなー。[p]
#
・・・・・[p]
まぁ、作ってみたい気持ちはあるけど、むずかしいんでしょ？[p]
プログラミングとかやったことないし、、、[p]


[chara_mod  name="akane"  face="default"  ]
#あかね
そんな君に、耳寄りな情報があるんだけど[p]
ききたい？　ききたいよね？[p]
#
いや、べつに[p]
#あかね


[cm  ]
[font  size="40"  ]
[delay  speed="160"  ]
ティラノスクリプトー[p]


[delay  speed="30"  ]
[resetfont  ]
#
・・・・[p]
#あかね
ティラノスクリプトを使うと、簡単に本格的なノベルゲームが簡単に作れてしまうのよ。[p]
#
へぇー。それはちょっと興味あるね。[p]


[chara_mod  name="akane"  face="happy"  ]
#あかね
ほ、ほんと！？[p]
このゲームをプレイするだけで、ティラノスクリプトの機能を確認することができるから[p]
ぜひ、最後までつきあってね[p]
まず、ティラノスクリプトの特徴として[p]


[font  color="red"  ]
「HTML5」[p]


[resetfont  ]
で動作するよ[p]
#
つ、つまり？[p]
#あかね
一度ティラノスクリプトで作ったゲームは多くの環境で動作させることができるってこと！[p]
#
へぇー。それはいいね。[p]
せっかく作ったらたくさんの人に遊んでもらいたいもんね。[p]
#あかね
ウィンドウズ用のPCアプリケーションはもちろん。[p]
マック用のアプリケーションにだって対応するわよ。[p]
あと、HTML5だから、ブラウザゲームとしても発表できるわよ。[p]
ウェブサイトに貼り付けて遊んでもらえるから、気軽にゲームをプレイしてもらうことができるね。[p]
主要なブラウザはすべてサポートしているから、安心してね。[p]
#
やるなぁ。。[p]
でも、最近スマホが復旧してて、僕のサイトにもスマホで訪れる人が増えたんだけど[p]
スマホからは遊べない？[p]
#あかね
ティラノスクリプトで作ったゲームはスマートフォンからでも遊べるよ！[p]
アイフォーン、アンドロイドはもちろん。アイパッドとかのタブレットでも問題ないわ。[p]
#
おぉー。[p]
#あかね
AppStoreやGooglePlayに向けてアプリ化して販売することもできるから[p]
#
おぉぉ、、やっとの貧困生活から脱出できるかも[p]
#あかね
まぁ、おもしろいゲームつくらないと、売れもしないけどな！[p]
#
くっ。。[p]
#あかね
じゃあ、次に場面を移動してみるね[p]
廊下に移動するよ[p]


[bg  time="3000"  method="crossfade"  storage="rouka.jpg"  ]
#
お、廊下に移動したね。[p]
#あかね
寒いよぉ〜。はやく教室に戻ろう。[p]


[bg  time="1000"  method="slide"  storage="room.jpg"  ]
#
あれ、今、場面の移動がちょっと違ったね。[p]
#あかね
うん。急いでたからね。[p]
ティラノスクリプトでは、いろいろな演出を加える事ができて[p]
画面を切り替えるだけでも１０種類以上の演出がつかえるよ。[p]
#
ふむ。便利だ[p]
#あかね
次にメッセージの表示方法を変えてみるね[p]
ティラノスクリプトでは、今みたいなアドベンチャーゲームの他に[p]


[r]

ビジュアルノベルのような全画面表示のゲームもつくれるよ。[p]
#


[chara_hide  name="akane"  ]
[position layer="message0" left=20 top=40 width=920 height=560 page=fore visible=true ]

どうかな? 物語をじっくり読ませたい場合はこの方式が便利ですね[p]


[l  ]
[r]

ティラノスクリプトは非常に強力で、柔軟な表現が可能です。[p]


[l  ]
[cm  ]
[font  size="40"  ]
文字のサイズを変更したり[p]


[l  ]
[r]

[resetfont  ]
[font  color="pink"  ]
色を変更したり[p]


[resetfont  ]
[l  ]
[r]

[ruby text=る]

ル[p]


[ruby text=び]

ビを[p]


[ruby text=ふ]

振ることだって[p]


[ruby text=かん]

簡[p]


[ruby text=たん]

単にできます[p]


[l  ]
[cm  ]
[position vertical=true layer=message0 page=fore margint="45" marginl="0" marginr="70" marginb="60"]

このように縦書きで記述することもできます。[p]


[r]

[l  ]
縦書きでも、横書きの時と同じ機能を使うことができます。[p]


[r]

[l  ]
[position vertical=false]

横書きと縦書きをシーンによって使い分けることもできます[p]


[r]

[l  ]
じゃあ、アドベンチャー形式に戻しますね[p]


[position layer="message0" left=20 top=400 width=920 height=200 page=fore visible=true]

[chara_show  name="akane"  ]
#akane
メッセージボックスは、自分の好きな画像を使うこともできるよ[p]


[font  color="0x454D51"  ]
[deffont color="0x454D51"]

[free name="chara_name_area" layer="message0"]

[position layer=message0 width=960 height=210 top=430 left=0]

[position layer=message0 page=fore frame="frame.png" margint="45" marginl="50" marginr="70" marginb="60" opacity=230 ]

[ptext name="chara_name_area" layer="message0"  color="0xFAFAFA"  size=24 x=40 y=435]

[chara_config ptext="chara_name_area"]

どうかな？[p]
ゲームに合わせて自分の好きなデザインを作ってくださいね[p]
あと、デフォルトだとセーブやロードは画面右下のボタンからできるけど[p]
ウィンドウをカスタマイズすれば、、、、[p]


[hidemenubutton]

[button  name="role_button"  role="skip"  graphic="button/skip.png"  enterimg="button/skip2.png"  x="35"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="auto"  graphic="button/auto.png"  enterimg="button/auto2.png"  x="110"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="save"  graphic="button/save.png"  enterimg="button/save2.png"  x="185"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="load"  graphic="button/load.png"  enterimg="button/load2.png"  x="260"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="quicksave"  graphic="button/qsave.png"  enterimg="button/qsave2.png"  x="335"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="quickload"  graphic="button/qload.png"  enterimg="button/qload2.png"  x="410"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="backlog"  graphic="button/log.png"  enterimg="button/log2.png"  x="485"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="window"  graphic="button/close.png"  enterimg="button/close2.png"  x="560"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="fullscreen"  graphic="button/screen.png"  enterimg="button/screen2.png"  x="635"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="menu"  graphic="button/menu.png"  enterimg="button/menu2.png"  x="710"  y="610"  storage=""  target=""  ]
[button  name="role_button"  role="sleepgame"  graphic="button/sleep.png"  enterimg="button/sleep2.png"  x="785"  y="610"  storage="config.ks"  target=""  ]
[button  name="role_button"  role="title"  graphic="button/title.png"  enterimg="button/title2.png"  x="860"  y="610"  storage=""  target=""  ]
こんな風にゲームに必要な機能を画面の上に持たせることも簡単にできるよ[p]
これはロールボタンといって、ボタンに特別な機能を持たせる事ができます。[p]
標準で用意されているのは、[p]


[l  ]
セーブ、[p]


[l  ]
ロード、[p]


[l  ]
[cm  ]
タイトルへ戻る、[p]
メニュー表示、[p]
メッセージ非表示、[p]
スキップ、[p]
バックログ、[p]
フルスクリーン切り替え、[p]
クイックセーブ、[p]
クイックロード、[p]
オートモード！[p]
はぁ、はぁ[p]
#
大丈夫？[p]
これだけあれば、ゲームを作るには困らなそうだね[p]
#あかね
さて、もちろん音楽を鳴らすこともできるよ[p]


[l  ]
[cm  ]
それじゃあ、再生するよ？[p]


[l  ]
[cm  ]
[link target=*playmusic]

【１】うん。再生してください[p]


[endlink]

[r]

[link target=*noplay]

【２】いや。今は再生しないで！[p]


[endlink]

[s  ]
*playmusic

[cm  ]
よし、再生するよ。[p]


[l  ]
[playbgm  time="3000"  storage="music.ogg"  loop="true"  ]
徐々にフェードインしながら再生することもできるんだ[p]


[l  ]
[cm  ]
[jump  target="*common_bgm"  storage=""  ]
*noplay

[cm  ]
うん。わかった。再生はしないね。[p]


[l  ]
[cm  ]
また、試してみてね[p]


[l  ]
[cm  ]
*common_bgm

あ、そうそう[p]


[l  ]
[cm  ]
今みたいな選択肢で物語を分岐することも、簡単にできるよ。[p]


[l  ]
[cm  ]
#あかね
ここらで、別のキャラクターに登場してもらいましょうか[p]


[l  ]
[cm  ]
やまとー[p]


[chara_show  name="yamato"  ]
こんな風に。簡単です。[p]


[l  ]
[r]

キャラクターは何人でも登場させることができるから、試してみてね。[p]
#yamato
おい、俺もう、帰っていいかな？[p]


[l  ]
[cm  ]
#akane
あ、ごめんごめん。ありがとう[p]


[l  ]
[cm  ]
[chara_hide  name="yamato"  ]
#akane
これでティラノスクリプトの基本機能の説明は終わりだけど[p]
どうだったかな？[p]
#
うん、これなら自分でも作れそうな気がしてきたよ[p]
#あかね
よかった！[p]
最初は、ティラノスクリプト公式ページのチュートリアルをやってみると良いと思うよ！[p]
もちろん、このゲームもティラノスクリプトで動いてるから、参考になると思うし。[p]
ぜひ、ゲーム制作にチャレンジしてみてね[p]
プレイしてくれてありがとう。[p]
最後にティラノスクリプトで役立つ情報へのリンクを表示しておくから[p]
確認してみてね。[p]


[cm  ]
*button_link

[layopt layer=message0 visible=false]

[layopt layer=fix visible=false]

[anim  name="akane"  left="600"  time="1000"  ]
[glink  text="ティラノビルダーの紹介"  size="20"  width="500"  x="30"  y="100"  color="blue"  target="tyranobuilder"  ]
[glink  text="制作事例"  size="20"  width="500"  x="30"  y="160"  color="blue"  target="example"  ]
[glink  text="応用テクニック"  size="20"  width="500"  x="30"  y="220"  color="blue"  target="tech"  ]
[glink  text="役に立つ情報源"  size="20"  width="500"  x="30"  y="280"  color="blue"  target="info"  ]
[glink  text="タグリファレンス"  size="20"  width="500"  x="30"  y="340"  color="blue"  target="tagref"  ]
[s  ]
*tyranobuilder

[cm  ]
[layopt layer=message0 visible=true]

[layopt layer=fix visible=true;]

[font  color-red=""  ]
「ティラノビルダー」[p]


[resetfont  ]
という無料の開発ツールもあります。[p]


[image layer=1 page=fore visible=true top=10 left=50 width=560 height=400  storage = builder.png]

これは、グラフィカルな画面でノベルゲームを作れるツールです[p]
スクリプトが苦手な人でもゲーム制作を行うことができるからぜひ試してね。[p]


[freeimage layer=1]

[jump  target="button_link"  storage=""  ]
[s  ]
*example

[layopt layer=message0 visible=true]

[layopt layer=fix visible=true]

これまで、ティラノスクリプトを使って沢山のゲームが作成されています。[p]
一部の制作事例を公式サイトに乗せているのでよければ確認してくださいね。[p]


[iscript]
window.open("http://tyrano.jp/home/example");
[endscript]

[jump  target="button_link"  storage=""  ]
[cm  ]
[s  ]
*tech

[layopt layer=message0 visible=true]

[layopt layer=fix visible=true]

このサンプルでは、ティラノスクリプトのごく一部の機能しか紹介できていません[p]
さらに出来ることを知りたい場合、スクリプトを丸ごとダウンロードできるようになっているので[p]
そのサンプルを触ってみることをオススメします！[p]


[iscript]
window.open("http://tyrano.jp/home/demo");
[endscript]

[jump  target="button_link"  storage=""  ]
*info

[layopt layer=message0 visible=true]

[layopt layer=fix visible=true]

ティラノスクリプトでわからないことがあったら[p]
公式掲示板で質問したり、Wikiなどもありますので参考にしてみてください[p]


[jump  target="button_link"  storage=""  ]
*tagref

[layopt layer=message0 visible=true]

[layopt layer=fix visible=true]

タグは詳細なリファレンスページが用意されています。[p]
このページでさらに詳細な使い方を身につけてください[p]


[iscript]
window.open("http://tyrano.jp/home/tag");
[endscript]

[jump  target="*button_link"  storage=""  ]
[s  ]
