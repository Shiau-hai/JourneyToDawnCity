label splashscreen:

    scene black  # 先让屏幕变黑
    play sound "audio/logo_sound.mp3"  # 播放 Logo 音效（可选）

    show logo with fade  # 显示 Logo，使用 fade 淡入
    pause 3.0  # 显示 3 秒

    hide logo with fade  # 淡出 Logo
    pause 1.0  # 停顿 2 秒

    show notice1 with fade  # 显示 Logo，使用 fade 淡入
    pause 3.0  # 显示 3 秒

    hide notice1 with fade  # 淡出 Logo
    pause 1.0  # 停顿 2 秒


    return  # 进入主菜单
