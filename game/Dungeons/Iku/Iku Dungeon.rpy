default wet_found = False
default rei_found = False
default wall_found = False

define config.layers = [ 'master', 'transient', 'screens', 'sprite' , 'overlay' ]

image Shiki_Idle_Right:
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight1.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight2.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight3.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight4.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight5.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight6.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight7.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight8.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight9.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight10.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight11.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight12.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight13.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight14.png"
    0.1
    "Iku_Dungeon/Shiki Idle Right Side/ShikiIdleRight15.png"
    0.1
    repeat
image Shiki_Climbing:


image 1-1:
    "Iku_Dungeon/Dungeon Map/1-1.png"

screen one_one():
    key "K_UP" action Return("u")
    key "repeat_K_UP" action Return("u")
    key "K_DOWN" action Return("d")
    key "repeat_K_DOWN" action Return("d")
    key "K_LEFT" action Return("l")
    key "repeat_K_LEFT" action Return("l")
    key "K_RIGHT" action Return("r")
    key "repeat_K_RIGHT" action Return("r")
    
    add "Iku_Dungeon/Dungeon Map/1-1.png" anchor(0,0) pos (x_pos1, y_pos1)

label iku_dungeon:
    $ screen = "one"
    $ quick_menu = False
    $ x_pos1 = 0
    $ y_pos1 = -720
    $ shiki_xpos = 0
    $ shiki_ypos = 1120
    show screen one_one
    show Shiki_Idle_Right onlayer screens:
        xpos x_pos1+shiki_xpos
        ypos y_pos1+shiki_ypos
    label move_loop:
        $ res = ui.interact()
        if res == "l":
            if x_pos1 <0:
                $ x_pos1 += 20
                $ shiki_xpos += 20
        elif res == "r":
            if x_pos1 >-1280:
                $ x_pos1 -= 20
                $ shiki_xpos += 20
                pass
        elif res == "u":
            if y_pos1 <0:
                $ y_pos1 += 20
        elif res == "d":
            if y_pos1 > -720:
                $ y_pos1 -= 20
                pass
        jump move_loop
    "Well here it is"
    pause
    hide window