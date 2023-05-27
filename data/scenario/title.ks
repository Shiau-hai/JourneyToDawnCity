
[cm]

/*
	タイトル：背景画像を読み込み
*/
@clearstack
@bg storage ="title.jpg" time=100
@wait time = 200

*start 
;.\data\image\title
[button x=364 y=286 graphic="title/button_start.png" target="gamestart"] ;最初から
[button x=364 y=386 graphic="title/button_load.png"  role="load" ] ;続きから
;一部の端末のため全画面表示を設定
[button x=364 y=486 graphic="title/button_fullwin.png" role="fullscreen" ]
[button x=364 y=586 graphic="title/button_config.png" role="sleepgame" storage="config.ks" ] ;設定

[s]

*gamestart
;一番最初のシナリオファイルへジャンプする
@jump storage="scene1.ks"



