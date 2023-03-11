default wet_found = False
default rei_found = False
default wall_found = False
default climbing = False
default frame_count = 0
default climb_count = 0
default animation = "shiki_idle_right"
default state = None
define config.layers = [ 'master', 'transient', 'screens', 'sprite' , 'overlay' ]

image jail = "Iku_Dungeon/Dungeon Map/JailCell.png"
image door = "Iku_Dungeon/Dungeon Map/JailCellDoor.png"

image shiki_animated = ConditionSwitch(
    "animation == 'shiki_idle_left'", "Shiki_Idle_Left",
    "animation == 'shiki_walk_left'", "Shiki_Walk_Left",
    "animation == 'shiki_idle_right'", "Shiki_Idle_Right",
    "animation == 'shiki_walk_right'", "Shiki_Walk_Right",
    "animation == 'shiki_climb'", "Shiki_Climb",
)

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

image Shiki_Walk_Left = ConditionSwitch(
    "frame_count == 1","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft1.png",
    "frame_count == 2","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft2.png",
    "frame_count == 3","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft3.png",
    "frame_count == 4","Iku_Dungeon/Shiki Walk Left/ShikiWalkLeft4.png",
    "True", "Shiki_Idle_Left"
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

image Shiki_Walk_Right = ConditionSwitch(
    "frame_count == 1","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight1.png",
    "frame_count == 2","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight2.png",
    "frame_count == 3","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight3.png",
    "frame_count == 4","Iku_Dungeon/Shiki Walk Right/ShikiWalkRight4.png",
    "True", "Shiki_Idle_Right"
)

image Shiki_Climb = ConditionSwitch(
    "climb_count == 1", "Iku_Dungeon/Shiki Climb/ShikiClimb1.png",
    "climb_count == 2", "Iku_Dungeon/Shiki Climb/ShikiClimb2.png",
    "climb_count == 3", "Iku_Dungeon/Shiki Climb/ShikiClimb3.png",
    "climb_count == 4", "Iku_Dungeon/Shiki Climb/ShikiClimb4.png",
    "climb_count == 5", "Iku_Dungeon/Shiki Climb/ShikiClimb5.png",
    "climb_count == 6", "Iku_Dungeon/Shiki Climb/ShikiClimb6.png",
    "climb_count == 7", "Iku_Dungeon/Shiki Climb/ShikiClimb7.png",
    "climb_count == 8", "Iku_Dungeon/Shiki Climb/ShikiClimb8.png",
    "climb_count == 9", "Iku_Dungeon/Shiki Climb/ShikiClimb9.png",
    "True", "Iku_Dungeon/Shiki Climb/ShikiClimb1.png"
)

image 1-1:
    "Iku_Dungeon/Dungeon Map/1-1.png"

screen iku_dungeon():
    zorder -1
    modal False
    key "K_UP" action Return("u")
    key "repeat_K_UP" action Return("u")
    key "K_DOWN" action Return("d")
    key "repeat_K_DOWN" action Return("d")
    key "K_LEFT" action Return("l")
    key "repeat_K_LEFT" action Return("lr")
    key "K_RIGHT" action Return("r")
    key "repeat_K_RIGHT" action Return("rr")
    key "K_z" action Return("z")
  
    add "Iku_Dungeon/Dungeon Map/1-1.png" anchor(0,0) pos (xpos1, ypos1)

screen one_one_jail():
    zorder 10
    add "Iku_Dungeon/Dungeon map/JailCell.png" anchor(0, 0) pos (xpos1, ypos1+740)
    showif cell_door_locked == True:
        add "Iku_Dungeon/Dungeon map/JailCellDoor.png" anchor(0, 0) pos (xpos1, ypos1+740)

label iku_dungeon:
    $ screen = "one"
    $ quick_menu = False
    $ xpos1 = 0
    $ ypos1 = -720
    $ shiki_xpos1 = 0
    $ shiki_ypos1 = 1120
    show screen iku_dungeon
#    show screen one_one_jail
    show shiki_animated onlayer screens:
            xpos xpos1+shiki_xpos1
            ypos ypos1+shiki_ypos1

    label move_loop:
        $ res = ui.interact()
        show shiki_animated onlayer screens:
            xpos xpos1+shiki_xpos1
            ypos ypos1+shiki_ypos1
        if frame_count >= 4:
            $ frame_count = 1
        else:
            pass
        if climb_count >= 9:
            $ climb_count = 0
        elif climb_count < 1:
            $ climb_count = 9
        if res == "l":
            $ animation = "shiki_idle_left"
            $ frame_count = 0
            pass
        elif res == "lr":
            $ animation = "shiki_walk_left"
            $frame_count += 1
            if shiki_xpos1 >= 0:
                $ shiki_xpos1 -= 20
            if xpos1 <0:
                $ xpos1 += 20
            pause 0.1
            pass
        elif res == "r":
            $ animation = "shiki_idle_right"
            $ frame_count = 0
            pass
        elif res == "rr":
            $ animation = "shiki_walk_right"
            $ frame_count += 1
            pause 0.1
#            while cell_door_locked == True:
#                if x_pos1 
            if shiki_xpos1 <=2320:
                $ shiki_xpos1 += 20
            if xpos1 >-1280:
                $ xpos1 -= 20
                pass
        elif res == "u":
            $ animation = "shiki_climb"
            $ climb_count += 1
            if shiki_ypos1 >= -60:
                $ shiki_ypos1 -= 20
            if ypos1 <0:
                $ ypos1 += 20
            pass    
        elif res == "d":
            $ animation = "shiki_climb"
            $ climb_count -= 1
            if shiki_ypos1 < 1180:
                $ shiki_ypos1 += 20
            if ypos1 > -720:
                $ ypos1 -= 20
            pass
        elif res  == "z":
            call iku_party_menu
            pass
        pause 0.1
        jump move_loop