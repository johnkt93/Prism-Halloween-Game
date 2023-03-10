default wet_found = False
default rei_found = False
default wall_found = False
default climbing = False
default frame_count = 0
default shiki_left_frame = 0
default shiki_right_frame = 0

define config.layers = [ 'master', 'transient', 'screens', 'sprite' , 'overlay' ]

image jail = "Iku_Dungeon/Dungeon Map/JailCell.png"
image door = "Iku_Dungeon/Dungeon Map/JailCellDoor.png"

image Shiki_Idle_Left:
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft1.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft2.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft3.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft4.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft5.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft6.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft7.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft8.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft9.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft10.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft11.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft12.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft13.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft14.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Left/ShikiIdleLeft15.png"
    pause 0.1
    repeat

image shiki_walk_left = ConditionSwitch(
    "shiki_right_frame == 0", "Shiki_Idle_Left",
    "shiki_right_frame == 1","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft1.png",
    "shiki_right_frame == 2","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft2.png",
    "shiki_right_frame == 3","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft3.png",
    "shiki_right_frame == 4","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft4.png"
)

image Shiki_Idle_Right:
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight1.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight2.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight3.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight4.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight5.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight6.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight7.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight8.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight9.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight10.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight11.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight12.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight13.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight14.png"
    pause 0.1
    "Iku_Dungeon/Shiki Idle Right/ShikiIdleRight15.png"
    pause 0.1
    repeat

image shiki_walk_right = ConditionSwitch(
    "shiki_right_frame == 0", "Shiki_Idle_Right",
    "shiki_right_frame == 1","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight1.png",
    "shiki_right_frame == 2","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight2.png",
    "shiki_right_frame == 3","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight3.png",
    "shiki_right_frame == 4","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight4.png"
)


image 1-1:
    "Iku_Dungeon/Dungeon Map/1-1.png"

screen one_one():
    zorder -1
    key "K_UP" action Return("u")
    key "repeat_K_UP" action Return("u")
    key "K_DOWN" action Return("d")
    key "repeat_K_DOWN" action Return("d")
    key "K_LEFT" action Return("l")
    key "repeat_K_LEFT" action Return("l")
    key "K_RIGHT" action Return("r")
    key "repeat_K_RIGHT" action Return("r")
    key "K_z" action Return("z")
    
    add "Iku_Dungeon/Dungeon Map/1-1.png" anchor(0,0) pos (x_pos1, y_pos1)

screen one_one_jail():
    zorder 10
    add "Iku_Dungeon/Dungeon map/JailCell.png" anchor(0, 0) pos (x_pos1, y_pos1+740)
    showif cell_door_locked == True:
        add "Iku_Dungeon/Dungeon map/JailCellDoor.png" anchor(0, 0) pos (x_pos1, y_pos1+740)

label iku_dungeon:
    $ screen = "one"
    $ quick_menu = False
    $ x_pos1 = 0
    $ y_pos1 = -720
    $ shiki_xpos = 0
    $ shiki_ypos = 1120
    show screen one_one
    show screen one_one_jail
    show Shiki_Idle_Right onlayer screens:
        xpos x_pos1+shiki_xpos
        ypos y_pos1+shiki_ypos
    label move_loop:
        $ res = ui.interact()
        if frame_count >= 4:
            $ frame_count = 0
        else:
            pass
        if res == "l":
            if x_pos1 <0:
                $ x_pos1 += 20
                $ shiki_xpos += 20
        elif res == "r":
#            while cell_door_locked == True:
#                if x_pos1 
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
        elif res  == "z":
            call iku_party_menu
        $ frame_count += 1
        jump move_loop