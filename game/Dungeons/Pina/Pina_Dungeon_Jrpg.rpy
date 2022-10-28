default doppel_hp = 37000
default pina_hp = 512
default pina_def = -10
default ray_hp = 1374
default ray_def = 20
default matt_hp = 972
default matt_def = 5
default tahv_hp = 741
default tahv_def = 10

default run_counter = 0

default ray_alive = True
default matt_alive = True
default tahv_alive = True
default pina_alive = True
default m_pina = False

default turn = 0
default ray_turn = True
default matt_turn = False
default tahv_turn = False
default pina_turn = False
default doppel_turn = False


image doppel:
    xalign 0.1
    yalign 0.5
    "Pina_Dungeon/Doppel/Monster1.png"
    0.3
    "Pina_Dungeon/Doppel/Monster2.png"
    0.3
    "Pina_Dungeon/Doppel/Monster3.png"
    0.3
    "Pina_Dungeon/Doppel/Monster4.png"
    0.3
    "Pina_Dungeon/Doppel/Monster5.png"
    0.3
    "Pina_Dungeon/Doppel/Monster6.png"
    0.3
    repeat
image apina:
    xalign 0.8
    yalign 0.4
    "Pina_Dungeon/Pina/Pina Idle/Pina Idle1.png"
    0.5
    "Pina_Dungeon/Pina/Pina Idle/Pina Idle2.png"
    0.5
    "Pina_Dungeon/Pina/Pina Idle/Pina Idle3.png"
    0.5
    "Pina_Dungeon/Pina/Pina Idle/Pina Idle4.png"
    0.5
    repeat
image apina_cast:
    xalign 0.81
    yalign 0.35
    "Pina_Dungeon/Pina/Pina Cast/Pina Cast1.png"
    0.4
    "Pina_Dungeon/Pina/Pina Cast/Pina Cast2.png"
    0.4
    "Pina_Dungeon/Pina/Pina Cast/Pina Cast3.png"
    0.4
    "Pina_Dungeon/Pina/Pina Cast/Pina Cast4.png"
    0.4
    "Pina_Dungeon/Pina/Pina Cast/Pina Cast4.png"
    0.4
    "Pina_Dungeon/Pina/Pina Cast/Pina Cast5.png"
    0.4
    repeat
image apina_def:
    xalign 0.81
    yalign 0.4
    "Pina_Dungeon/Pina/Pina Defense/Pina Defense1.png"
    0.4
    "Pina_Dungeon/Pina/Pina Defense/Pina Defense2.png"
    0.4
    "Pina_Dungeon/Pina/Pina Defense/Pina Defense3.png"
    0.4
    "Pina_Dungeon/Pina/Pina Defense/Pina Defense4.png"
    0.4
    "Pina_Dungeon/Pina/Pina Defense/Pina Defense5.png"
    0.4
    "Pina_Dungeon/Pina/Pina Defense/Pina Defense6.png"
    0.4
    repeat    
image mpina:
    xalign 0.8
    yalign 0.4
    "Pina_Dungeon/Pina/Magical Pina Idle/Magical Pina1.png"
    0.5
    "Pina_Dungeon/Pina/Magical Pina Idle/Magical Pina2.png"
    0.5
    repeat
image mpina_cast:
    xalign 0.81
    yalign 0.4
    "Pina_Dungeon/Pina/Magical Pina Cast/Magical Pina Cast1.png"
    0.5
    "Pina_Dungeon/Pina/Magical Pina Cast/Magical Pina Cast2.png"
    0.5
    "Pina_Dungeon/Pina/Magical Pina Cast/Magical Pina Cast3.png"
    0.5
    "Pina_Dungeon/Pina/Magical Pina Cast/Magical Pina Cast4.png"
    0.5
    repeat
image mpina_def:
    xalign 0.81
    yalign 0.4
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense1.png"
    0.25
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense2.png"
    0.25
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense3.png"
    0.25
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense4.png"
    0.25
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense5.png"
    0.25
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense6.png"
    0.25
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense7.png"
    0.25
    "Pina_Dungeon/Pina/Magical Pina Defense/Magical Pina Defense8.png"
    0.25
    repeat
image matt:
    xalign 0.63
    ypos 340
    "Pina_Dungeon/Matt/Matt Idle/Matt Idle1.png"
    0.5
    "Pina_Dungeon/Matt/Matt Idle/Matt Idle2.png"
    0.5
    repeat
image matt_attack:
    xalign 0.25
    ypos 440
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack1.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack2.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack3.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack4.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack5.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack6.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack7.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack8.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack9.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack10.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack11.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack12.png"
    0.1
    "Pina_Dungeon/Matt/Matt Attack/Matt Attack13.png"
    0.1
    repeat    
image matt_def:
    xalign 0.63
    ypos 340
    "Pina_Dungeon/Matt/Matt Defense/Matt Defense1.png"
    0.5
    "Pina_Dungeon/Matt/Matt Defense/Matt Defense2.png"
    0.5
    repeat
image ray:
    xalign 0.5
    ypos 420
    "Pina_Dungeon/Raylin/Ray Idle/Ray Idle1.png"
    0.5
    "Pina_Dungeon/Raylin/Ray Idle/Ray Idle2.png"
    0.5
    repeat
image ray_attack:
    xalign 0.25
    ypos 440
    "Pina_Dungeon/Raylin/Ray Attack/Ray Attack1.png"
    0.4
    "Pina_Dungeon/Raylin/Ray Attack/Ray Attack2.png"
    0.4
    "Pina_Dungeon/Raylin/Ray Attack/Ray Attack3.png"
    0.4
    "Pina_Dungeon/Raylin/Ray Attack/Ray Attack4.png"
    0.4
    "Pina_Dungeon/Raylin/Ray Attack/Ray Attack5.png"
    0.4
    repeat
image ray_def:
    xalign 0.5
    ypos 420
    "Pina_Dungeon/Raylin/Ray Defense/Ray Defense.png"
image tahv:
    xalign 0.65
    ypos 500
    "Pina_Dungeon/Tahvohck/Tahv Idle/Tahv Idle1.png"
    0.5
    "Pina_Dungeon/Tahvohck/Tahv Idle/Tahv Idle2.png"
    0.5
    "Pina_Dungeon/Tahvohck/Tahv Idle/Tahv Idle3.png"
    0.5
    "Pina_Dungeon/Tahvohck/Tahv Idle/Tahv Idle4.png"
    0.5
    repeat
image tahv_attack:
    xalign 0.65
    ypos 500
    "Pina_Dungeon/Tahvohck/Tahv Attack/Tahv Attack1.png"
    0.3
    "Pina_Dungeon/Tahvohck/Tahv Attack/Tahv Attack2.png"
    0.3
    "Pina_Dungeon/Tahvohck/Tahv Attack/Tahv Attack3.png"
    0.3
    "Pina_Dungeon/Tahvohck/Tahv Attack/Tahv Attack4.png"
    0.3
    repeat
image tahv_def:
    xalign 0.65
    ypos 500
    "Pina_Dungeon/Tahvohck/Tahv Defense/Tahv Defense.png"
image pointer:
    "Pina_Dungeon/Pointer/pointer1.png"
    0.25
    "Pina_Dungeon/Pointer/pointer2.png"
    0.25
    "Pina_Dungeon/Pointer/pointer3.png"
    0.25
    "Pina_Dungeon/Pointer/pointer4.png"
    0.25
    "Pina_Dungeon/Pointer/pointer5.png"
    0.25
    "Pina_Dungeon/Pointer/pointer6.png"
    0.25
    "Pina_Dungeon/Pointer/pointer7.png"
    0.25
    "Pina_Dungeon/Pointer/pointer8.png"
    0.25
    "Pina_Dungeon/Pointer/pointer9.png"
    0.25
    "Pina_Dungeon/Pointer/pointer10.png"
    0.25
    "Pina_Dungeon/Pointer/pointer11.png"
    0.25
    "Pina_Dungeon/Pointer/pointer12.png"
    0.25
    repeat

label pina_dungeon_jrpg:
    scene image "Pina_Dungeon/pina_jrpg_menu.png":
        size(1280,720)
    show apina
    show doppel
    show ray
    show matt
    show tahv
    show screen pina_jrpg_base
    jump ray_turn
    pass   

screen pina_jrpg_base():
    tag jrpg
    bar value ray_hp range 1374 xalign .9 ypos 575 xmaximum 200
    text "[ray_hp]/1374" xpos 1010 ypos 575
    text "Raylin" xpos 900 ypos 575
    bar value matt_hp range 972 xalign .9 ypos 610 xmaximum 200
    text "[matt_hp]/972" xpos 1010 ypos 610
    text "Matt" xpos 900 ypos 610
    bar value tahv_hp range 741 xalign .9 ypos 645 xmaximum 200
    text "[tahv_hp]/741" xpos 1010 ypos 645
    text "Tahv" xpos 900 ypos 645
    bar value pina_hp range 512 xalign .9 ypos 680 xmaximum 200
    text "[pina_hp]/512" xpos 1010 ypos 680
    text "Pina" xpos 900 ypos 680
    bar value doppel_hp range 3700 xpos 75 ypos 480 xmaximum 300
    text "???" xpos 200 ypos 480
    $ tooltip = GetTooltip()
    if tooltip:
        frame:
            xfill True
            text "[tooltip]"

screen pina_jrpg_ray():
    tag turns
    frame:
        xpos 15
        ypos 569
        xfill True
        xmaximum 135
        ymaximum 137
        background Null()
        button:
            xfill True
            ypos -5
#            text "Attack"
            action [Hide("ray_skill"), Call("ray_attack")]
            tooltip("A standard attack")
        button:
            xfill True
            ypos 30
#            text "Skill"
            action Show("ray_skill")
            tooltip("Open the character's skill list")
        button:
            xfill True
            ypos 65
#            text "Guard"
            action [Hide("ray_skill"), Call("ray_guard")]
            tooltip ("Guards against an upcoming attack. Reduces incoming damgage by 50%")
        button:
            xfill True
            ypos 100
#            text "Run"
            action [Hide("ray_skill"), Call("run")]
            tooltip("Attempt to escape from the fight")

screen ray_skill():
    tag skill
    frame:
        xfill True
        yfill True
        xpos 165
        ypos 569
        xmaximum 725
        ymaximum 137
#        background Null()
        textbutton ("Bash"):
            ypos -5
            tooltip "Strikes the enemy with your shield"
            action [Hide("pina_jrpg_ray"), Hide("ray_skill"), Call("ray_skill_bash")]
        textbutton ("Guard"):
            ypos 30
            tooltip "Protects your allies for the next turn"
            action [Hide("pina_jrpg_ray"), Hide("ray_skill"), Call("ray_skill_guard")]
        textbutton ("Back") action Hide("ray_skill"):
            xpos 650
            ypos 100
            tooltip "Close the menu"
label ray_skill_bash:
    "Raylin slammed his shield into the side of the monster"
    hide ray
    show ray_attack
    $damage = renpy.random.randint(103, 174)
    "It does [damage] damage to the monster"
    hide ray_attack
    show ray
    $doppel_hp -= damage
    voice "audio/PenPals/Raylin/LeaveAMark.wav"
    "Raylin" "That's going to leave a mark"
    $ray_turn = False
    $matt_turn = True
    jump matt_turn
    pass
label ray_skill_guard:
    voice "audio/PenPals/Raylin/BehindMe.wav"
    "Raylin" "Get behind me."
    "Raylin put up his shield to block the monster's blow"
    hide ray
    show ray_def
    $ray_def = (100+ray_def)/2
    $pina_def = (100+pina_def)/2
    $matt_def = (100+matt_def)/2
    $tahv_def = (100+tahv_def)/2
    $ray_turn = False
    $matt_turn = True
    jump matt_turn
    pass
label ray_attack:
    voice "audio/PenPals/Raylin/Hyaaa.wav"
    "Raylin does a basic slice with his sword"
    hide ray
    show ray_attack
    $damage = renpy.random.randint(54, 72)
    "It does [damage] damage to the monster"
    hide ray_attack
    show ray
    $doppel_hp -= damage
    $ray_turn = False
    $matt_turn = True
    jump matt_turn
    pass
label ray_guard:
    voice "audio/PenPals/Raylin/Shield.wav"
    "Raylin" "My shield will protect me!"
    hide ray
    show ray_def
    "Raylin braces himself for the next attack"
    $ray_def = (100+ray_def)/2
    $ray_turn = False
    $matt_turn = True
    jump matt_turn
    pass
screen pina_jrpg_matt():
    tag turns
    frame:
        xpos 15
        ypos 569
        xfill True
        xmaximum 135
        ymaximum 137
        background Null()
        button:
            xfill True
            ypos -5
#            text "Attack"
            action [Hide("matt_skill"), Call("matt_attack")]
            tooltip("A standard attack")
        button:
            xfill True
            ypos 30
#            text "Skill"
            action Show("matt_skill")
            tooltip("Open the character's skill list")
        button:
            xfill True
            ypos 65
#            text "Guard"
            action [Hide("matt_skill"), Call("matt_guard")]
            tooltip ("Guards against an upcoming attack. Reduces incoming damgage by 50%")
        button:
            xfill True
            ypos 100
#            text "Run"
            action [Hide("matt_skill"), Call("run")]
            tooltip("Attempt to escape from the fight")
screen matt_skill():
    tag skill
    frame:
        xfill True
        yfill True
        xpos 165
        ypos 569
        xmaximum 725
        ymaximum 137
#        background Null()
        textbutton ("Slice"):
            ypos -5
            tooltip "Quickly strikes the target with both blades"
            action [Hide("pina_jrpg_matt"), Hide("matt_skill"), Call("matt_skill_slice")]
        textbutton ("Overdrive"):
            ypos 30
            tooltip "Strikes the target with a flurry of slashes"
            action [Hide("pina_jrpg_matt"), Hide("matt_skill"), Call("matt_skill_overdrive")]
        textbutton ("Back") action Hide("matt_skill"):
            xpos 650
            ypos 100
            tooltip "Close the menu"
label matt_skill_slice:
    voice "audio/PenPals/Mattdoss/TakeThis.wav"        
    "Matt" "Take this!"
    hide matt
    show matt_attack
    "Matt swipes the monster with both of his daggers"
    $damage = renpy.random.randint(150, 170)
    "It does [damage] damage to the monster"
    hide matt_attack
    show matt
    $doppel_hp -= damage
    $matt_turn = False
    $tahv_turn = True
    jump tahv_turn
    pass
label matt_skill_overdrive:
    voice "audio/PenPals/Mattdoss/DontPush.wav"
    "Matt" "Don't push me, because I'm close to the edge"
    hide matt
    show matt_attack
    "Matt rushes in and does swipes at the monster furiously"
    hide matt_attack
    show matt
    $damage = renpy.random.randint(372,786)
    $doppel_hp -= damage
    $matt_turn = False
    $tahv_turn = True
    jump tahv_turn
    pass
label matt_attack:
    voice "audio/PenPals/Mattdoss/OffTheTop.wav"
    "Matt" "Just a little off the top"
    hide matt
    show matt_attack
    "Matt does a basic slice with a dagger"
    hide matt_attack
    show matt
    $damage = renpy.random.randint(54, 72)
    "It does [damage] damage to the monster"
    $doppel_hp -= damage
    $matt_turn = False
    $tahv_turn = True
    jump tahv_turn
    pass
label matt_guard:
    voice "audio/PenPals/Mattdoss/TakingCover.wav"
    "Matt" "Taking cover"
    hide matt
    show matt_def
    "Matt braces himself for the next attack."
    $matt_def = (100+matt_def)/2
    $matt_turn = False
    $tahv_turn = True
    jump tahv_turn
    pass
screen pina_jrpg_tahv():
    tag turns
    frame:
        xpos 15
        ypos 569
        xfill True
        xmaximum 135
        ymaximum 137
        background Null()
        button:
            xfill True
            ypos -5
#            text "Attack"
            action [Hide("tahv_skill"), Call("tahv_attack")]
            tooltip("A standard attack")
        button:
            xfill True
            ypos 30
#            text "Skill"
            action Show("tahv_skill")
            tooltip("Open the character's skill list")
        button:
            xfill True
            ypos 65
#            text "Guard"
            action [Hide("tahv_skill"), Call("tahv_guard")]
            tooltip ("Guards against an upcoming attack. Reduces incoming damgage by 50%")
        button:
            xfill True
            ypos 100
#            text "Run"
            action [Hide("tahv_skill"), Call("run")]
            tooltip("Attempt to escape from the fight")
screen tahv_skill():
    tag skill
    frame:
        xfill True
        yfill True
        xpos 165
        ypos 569
        xmaximum 725
        ymaximum 137
        textbutton ("Unload"):
            ypos -5
            tooltip "Fires a barrage of bullets into the monster"
            action [Hide("pina_jrpg_tahv"), Hide("tahv_skill"), Call("tahv_skill_unload")]
        textbutton ("Analysis"):
            ypos 30
            tooltip "Scan the enemy for a vital point, and shoots"
            action [Hide("pina_jrpg_tahv"), Hide("tahv_skill"), Call("tahv_skill_analysis")]
        textbutton ("Back") action Hide("tahv_skill"):
            xpos 650
            ypos 100
            tooltip "Close the menu"
label tahv_attack:
    voice "audio/Penpals/Tahvohck/pew.wav"
    "Tahv fires a shot at the monster"
    hide tahv
    show tahv_attack
    $damage = renpy.random.randint(112,140)
    "The monster takes [damage] damage"
    hide tahv_attack
    show tahv
    $doppel_hp -= damage
    $tahv_turn = False
    $pina_turn = True
    jump pina_turn
    pass
label tahv_skill_unload:
    voice "audio/Penpals/Tahvohck/Unload.wav"
    "Tahv" "Laying down covering fire!"
    hide tahv
    show tahv_attack
    $damage = renpy.random.randint(712,1079)
    "The monster takes [damage] damage"
    hide tahv_attack
    show tahv
    $doppel_hp -= damage
    $tahv_turn = False
    $pina_turn = True
    jump pina_turn
    pass
label tahv_skill_analysis:
    voice "audio/Penpals/Tahvohck/Analysis.wav"
    "Tahv" "Kowalski, analysis"
    "A drone approaches the monster and beeps, while a shot rings out"
    $damage = renpy.random.randint(224,280)
    $doppel_hp -= damage
    $tahv_turn = False
    $pina_turn = True
    jump pina_turn
    pass
label tahv_guard:
    voice "audio/Penpals/Tahvohck/Defend.wav"
    "Tahv" "Hunkering down"
    hide tahv
    show tahv_def
    "Tahv prepares himself for the next attack"
    $tahv_def = (100+tahv_def)/2
    $tahv_turn = False
    $pina_turn = True
    jump pina_turn
    pass
screen pina_jrpg_pina():
    tag turns
    frame:
        xpos 15
        ypos 569
        xfill True
        xmaximum 135
        ymaximum 137
        background Null()
        button:
            xfill True
            ypos -5
#            text "Attack"
            action [Hide("pina_skill"), Call("pina_attack")]
            tooltip("Pina looks apprehensive...")
        button:
            xfill True
            ypos 30
#            text "Skill"
            action Show("pina_skill")
            tooltip("Open the character's skill list")
        button:
            xfill True
            ypos 65
#            text "Guard"
            action [Hide("pina_skill"), Call("pina_guard")]
            tooltip ("Guards against an upcoming attack. Reduces incoming damgage by 50%")
        button:
            xfill True
            ypos 100
#            text "Run"
            action [Hide("pina_skill"), Call("run")]
            tooltip("Attempt to escape from the fight")
screen pina_skill():
    tag pina
    frame:
        xfill True
        yfill True
        xpos 165
        ypos 569
        xmaximum 725
        ymaximum 137
        textbutton ("Heal"):
            ypos -5
            tooltip "Fills a target part member with light magic"
            action [Hide("pina_jrpg_pina"), Hide("pina_skill"), Call("pina_skill_heal")]
        textbutton ("Mass Heal"):
            ypos 30
            tooltip "Call upon the power of a harpy-penguin to fill the party with light magic"
            action [Hide("pina_jrpg_pina"), Hide("pina_skill"), Call("pina_skill_massheal")]
        if tahv_alive == matt_alive == ray_alive == False:
            textbutton ("Disaresta"):
                ypos 65
                tooltip "The ultimate spell of the Harpy Penguins."
                action [Hide("pina_jrpg)pina"), Hide("pina_skill"), Call("pina_skill_disaresta")]
        textbutton ("Back") action Hide("tahv_skill"):
            xpos 650
            ypos 100
            tooltip "Close the menu"
label pina_attack:
    "Pina" "..."
    "Pina refuses to attack"
    jump pina_turn
    pass
label pina_guard:
    "Pina prepares herself for the next blow"
    if tahv_alive == matt_alive == ray_alive == False:
        hide mpina
        show mpina_def
    else:
        hide apina
        show apina_def
    $pina_def += (100+pina_def)/2
    $pina_turn = False
    $doppel_turn = True
    jump doppel_turn
    pass
label pina_skill_heal:
    "Choose a party member to heal"
    python:
        alive = []
        if ray_alive == True:
            alive.append("Raylin")
        if matt_alive == True:
            alive.append("Matt")
        if ray_alive == True:
            alive.append("Tahv")
        if pina_alive == True:
            alive.append("Pina")
    if tahv_alive == matt_alive == ray_alive == False:
        hide mpina
        show mpina_cast
    else:
        hide apina
        show apina_cast        
    $ heal = renpy.random.randint(57,98)
    menu:
        "Ray" if ray_alive == True:
            $ray_hp += heal
            "Raylin healed for [heal]"
            hide apina_cast
            show apina
            $doppel_turn = True
            $pina_turn = False
            jump doppel_turn
            pass
        "Matt" if matt_alive == True:
            $matt_hp += heal
            "Matt healed for [heal]"
            hide apina_cast
            show apina
            $doppel_turn = True
            $pina_turn = False
            jump doppel_turn
            pass
        "Tahv" if tahv_alive == True:
            $tahv_hp += heal
            "Tahv healed for [heal]"
            hide apina_cast
            show apina
            $doppel_turn = True
            $pina_turn = False
            jump doppel_turn
            pass
        "Pina":
            $pina_hp += heal
            "Pina healed for [heal]"
            hide apina_cast
            hide mpina_cast
            if len(alive)==1:
                show mpina
            else:
                show apina
            $doppel_turn = True
            $pina_turn = False
            jump doppel_turn
            pass

label pina_skill_massheal:
    if tahv_alive == matt_alive == ray_alive == False:
        hide mpina
        show mpina_cast
    else:
        hide apina
        show apina_cast 
    "A warm light fills the entire party."
    $massheal = renpy.random.randint(12,34)
    if ray_alive == True:
        $ray_hp += massheal
        pass
    if matt_alive == True:
        $matt_hp += massheal
        pass
    if tahv_alive == True:
        $tahv_hp += massheal
        pass
    $pina_hp += massheal
    "The party healed for [massheal]"
    hide apina_cast
    hide mpina_cast
    if tahv_alive == matt_alive == ray_alive == False:
        hide mpina_cast
        show mpina
    else:
        hide apina_cast
        show apina
    $pina_turn = False
    $doppel_turn = True
    jump doppel_turn
    pass
label pina_skill_disaresta:
    "Pina begins to glow"
    hide mpina
    show mpina_cast
    "Pina" "I can feel my magic surging inside me"
    "Pina" "Thank you Penpals for keeping me safe."
    "Pina" "Because penpals are my guiding light"
    "Pina" "I won't let your belief in me go unrewarded"
    "Pina" "This light..."
    "Pina" "Shall be proof of our friendship!"
    "The entire area fills with light magic"
    hide mpina_cast
    show mpina
    $doppel_hp -= doppel_hp
    return
label run:
    if run_counter <3:
        if run_counter == 0:
            p "I can't run away and leave my friends behind"
            $ run_counter += 1
            jump ray_turn
            return
        if run_counter == 1:
            p "But"
            p "Maybe they'd be better off without me around."
            $ run_counter += 1
            jump ray_turn
            return
        if run_counter == 2:
            p "..."
            p "I turn around and begin running as fast as I can."
            p "I'm so sorry."
            p "I'm not strong enough to deal with this."
            p "I hope you'll forgive me."
            p "It's okay to be selfish sometimes."
            p "Right?"
            $ run_counter += 1
            jump ray_turn
            return
    if run_counter == 3:
        "There's no more text, but the dialogue will reset for testing purposes"
        "You can't actually run from this fight, but will probably add some sort of achievement here in the future"
        $ run_counter = 0
        jump ray_turn
        pass
label doppel_basic:
    $damage = renpy.random.randint(102,250)
    if tahv_alive == matt_alive == ray_alive == False:
                "A magical force prevents Pina from being hurt"
                pass
    python:
        alive = []
        if ray_alive == True:
            alive.append("Raylin")
        if matt_alive == True:
            alive.append("Matt")
        if tahv_alive == True:
            alive.append("Tahv")
        if pina_alive == True:
            alive.append("Pina")
        Penpal = renpy.random.choice(alive)
    "The monster attacks [Penpal]"
    if Penpal == "Raylin":
        if ray_alive == True:
            if damage >= ray_hp:
                "Ray collapses from the attack"
                voice "audio/PenPals/Raylin/DontGiveUp.wav"
                "Raylin""Don't... give up."
                $ray_hp = 0
                $ray_alive = False
                $alive.remove("Raylin")
                hide ray_def
                hide ray
                pass
            else:
                $ray_damage = int(damage*(1-(ray_def*.01)))
                "Ray takes [ray_damage] damage"
                $ray_hp -= ray_damage
                pass
    if Penpal == "Matt":
        if matt_alive == True:
            if damage >= matt_hp:
                "Matt collapses from the attack"
                voice "audio/PenPals/Mattdoss/IDidMyBest.wav"
                "Matt""Don't... give up."
                $matt_hp = 0
                $matt_alive = False
                $alive.remove("Matt")
                hide matt_def
                hide matt
                pass
            else:
                $matt_damage = int(damage*(1-(matt_def*.01)))
                "Matt takes [matt_damage] damage"
                $matt_hp -= matt_damage
                pass
    if Penpal == "Tahv":
        if tahv_alive == True:
            if damage >= tahv_hp:
                "Tahv collapses from the attack"
                voice "audio/PenPals/Tahvohck/SemperFi.wav"
                "Tahv""Semper...fi"
                $tahv_hp = 0
                $tahv_alive = False
                $alive.remove("Tahv")
                hide tahv_def
                hide tahv
                pass
            else:
                $tahv_damage = int(damage*(1-(tahv_def*.01)))
                "Tahv takes [tahv_damage] damage"
                $tahv_hp -= tahv_damage
                pass
    if Penpal == "Pina":
        if pina_alive == True:
            if damage >= pina_hp:
                if len(alive) > 1:
                    python:
                        alive.remove("Pina")
                        Penpal = renpy.random.choice(alive)
                    "[Penpal] jumps in front and blocks for Pina"
                    pass
                if Penpal == "Raylin":
                    if ray_alive == True:
                        if damage >= ray_hp:
                            "Ray collapses from the attack"
                            voice "audio/PenPals/Raylin/DontGiveUp.wav"
                            "Raylin""Don't... give up."
                            $ray_hp = 0
                            $ray_alive = False
                            $alive.remove("Raylin")
                            pass
                        else:
                            $ray_damage = int(damage*(1-(ray_def*.01)))
                            "Ray takes [ray_damage] damage"
                            $ray_hp -= ray_damage
                            pass
                if Penpal == "Matt":
                    if matt_alive == True:
                        if damage >= matt_hp:
                            "Matt collapses from the attack"
                            voice "audio/PenPals/Mattdoss/IDidMyBest.wav"
                            "Matt""Don't... give up."
                            $matt_hp = 0
                            $matt_alive = False
                            $alive.remove("Matt")
                            pass
                        else:
                            $matt_damage = int(damage*(1-(matt_def*.01)))
                            "Matt takes [matt_damage] damage"
                            $matt_hp -= matt_damage
                            pass
                if Penpal == "Tahv":
                    if tahv_alive == True:
                        if damage >= tahv_hp:
                            "Tahv collapses from the attack"
                            voice "audio/PenPals/Tahvohck/SemperFi.wav"
                            "Tahv""Semper...fi"
                            $tahv_hp = 0
                            $tahv_alive = False
                            $alive.remove("Tahv")
                            pass
                        else:
                            $tahv_damage = int(damage*(1-(tahv_def*.01)))
                            "Tahv takes [tahv_damage] damage"
                            $tahv_hp -= tahv_damage
                            pass
            else:
                $pina_damage = int(damage*(1-(pina_def*.01)))
                "Pina takes [pina_damage] damage"
                $pina_hp -= pina_damage
                pass
    $doppel_turn = False
    $ray_turn = True
    jump ray_turn
    pass
label doppel_slam:
    python:
        alive = []
        if ray_alive == True:
            alive.append("Raylin")
        if matt_alive == True:
            alive.append("Matt")
        if tahv_alive == True:
            alive.append("Tahv")
        if pina_alive == True:
            alive.append("Pina")
    "The monster slams down its tentacle on the party"
    $ damage = renpy.random.randint(33,96)
    if ray_alive == True:
        if damage >= ray_hp:
            "Ray collapses from the attack"
            voice "audio/PenPals/Raylin/DontGiveUp.wav"
            "Raylin""Don't... give up."
            $ray_hp = 0
            $ray_alive = False
            $alive.remove("Raylin")
            hide ray
            pass
        else:
            $ray_damage = int(damage*(1-(ray_def*.01)))
            "Ray takes [ray_damage] damage"
            $ray_hp -= ray_damage
            pass
    if matt_alive == True:
        if damage >= matt_hp:
            "Matt collapses from the attack"
            voice "audio/PenPals/Mattdoss/IDidMyBest.wav"
            "Matt""Don't... give up."
            hide matt
            $matt_hp = 0
            $matt_alive = False
            $alive.remove("Matt")
            pass
        else:
            $matt_damage = int(damage*(1-(matt_def*.01)))
            "Matt takes [matt_damage] damage"
            $matt_hp -= matt_damage
            pass
    if tahv_alive == True:
        if damage >= tahv_hp:
            "Tahv collapses from the attack"
            voice "audio/PenPals/Tahvohck/SemperFi.wav"
            "Tahv""Semper...fi"
            $tahv_hp = 0
            $tahv_alive = False
            $alive.remove("Tahv")
            hide tahv
            pass
        else:
            $tahv_damage = int(damage*(1-(tahv_def*.01)))
            "Tahv takes [tahv_damage] damage"
            $tahv_hp -= tahv_damage
            pass
    if pina_alive == True:
        if damage >= pina_hp:
            if tahv_alive == matt_alive == ray_alive == False:
                "A magical force prevents Pina from being hurt"
                pass
            if len(alive) > 1:
                "[Penpal] jumps in front and blocks for Pina"
                pass
            if Penpal == "Raylin":
                if ray_alive == True:
                    if damage >= ray_hp:
                        "Ray collapses from the attack"
                        voice "audio/PenPals/Raylin/DontGiveUp.wav"
                        "Raylin""Don't... give up."
                        $ray_hp = 0
                        $ray_alive = False
                        $alive.remove("Raylin")
                        hide ray_def
                        hide ray
                        pass
                    else:
                        $ray_damage = int(damage*(1-(ray_def*.01)))
                        "Ray takes [ray_damage] damage"
                        $ray_hp -= ray_damage
                        pass
            if Penpal == "Matt":
                if matt_alive == True:
                    if damage >= matt_hp:
                        "Matt collapses from the attack"
                        voice "audio/PenPals/Mattdoss/IDidMyBest.wav"
                        "Matt""Don't... give up."
                        $matt_hp = 0
                        $matt_alive = False
                        $alive.remove("Matt")
                        hide matt_def
                        hide matt
                        pass
                    else:
                        $matt_damage = int(damage*(1-(matt_def*.01)))
                        "Matt takes [matt_damage] damage"
                        $matt_hp -= matt_damage
                        pass
            if Penpal == "Tahv":
                if tahv_alive == True:
                    if damage >= tahv_hp:
                        "Tahv collapses from the attack"
                        voice "audio/PenPals/Tahvohck/SemperFi.wav"
                        "Tahv""Semper...fi"
                        $tahv_hp = 0
                        $tahv_alive = False
                        $alive.remove("Tahv")
                        hide tahv_def
                        hide tahv
                        pass
                    else:
                        $tahv_damage = int(damage*(1-(tahv_def*.01)))
                        "Tahv takes [tahv_damage] damage"
                        $tahv_hp -= tahv_damage
                        pass            
        else:
            $pina_damage = int(damage*(1-(pina_def*.01)))
            "Pina takes [pina_damage] damage"
            $pina_hp -= pina_damage
            pass
    $doppel_turn = False
    $ray_turn = True
    jump ray_turn
    pass
label ray_turn:
    if ray_alive == True:
        if ray_turn == True:
            hide ray_def
            show ray
            $ray_def = 20
            show pointer:
                xalign 0.5
                ypos 260
            call screen pina_jrpg_ray
            pass
    else:
        $matt_turn = True
        pass
label matt_turn:
    if matt_alive == True:
        if matt_turn == True:
            hide matt_def
            show matt
            $matt_def = 5
            show pointer:
                xalign 0.63
                ypos 160
            call screen pina_jrpg_matt
            pass
    else:
        $tahv_turn = True
        pass
label tahv_turn:
    if tahv_alive == True:
        if tahv_turn == True:
            hide tahv_def
            show tahv
            $tahv_def = 10
            show pointer:
                xalign 0.63
                ypos 330
            call screen pina_jrpg_tahv
            pass
    else:
        $pina_turn = True
        pass
label pina_turn:
    if doppel_hp >0:
        if pina_alive == True:
            if pina_turn == True:
                $pina_def = -10
                if matt_alive ==False:
                    if tahv_alive==False:
                        if ray_alive==False:
                            if m_pina == False:
                                "As her last comrade succumbs to the onslaught, Pina begins to shine and transform"
                                $m_pina = True
                                hide apina_def
                                hide apina
                            hide mpina_def
                            show mpina
                else:
                    hide apina_def
                    show apina
                show pointer:
                    xalign 0.775
                    yalign 0.25
                call screen pina_jrpg_pina
                pass
label doppel_turn:
    if doppel_turn == True:
        jump expression renpy.random.choice(['doppel_basic','doppel_slam'])
        pass
label pina_dungeon_jrpg_end:
    return
#label testing_menu:
#        if ray_hp <= 0:
#            hide ray
#        else:
#            show ray
#        if matt_hp <= 0:
#            hide matt
#        else:
#            show matt
#        if tahv_hp <= 0:
#            hide tahv
#        else:
#            show tahv
#        menu:
#            "Textbutton wasn't working":
#                return
#            "Testing secondary menu item":
#                return
#            "This sets the hp to 0 and should end the fight.":
#                $doppel_hp = 0
#                pass
#            "Ray passes out":
#                $ray_hp = 0
#                $ray_alive = False
#                jump testing_menu
#                pass
#            "Matt passes out":
#                $matt_hp = 0
#                $matt_alive = False
#                jump testing_menu
#                pass
#            "Tahv passes out":
#                $tahv_hp = 0
#                $tahv_alive = False
#                jump testing_menu
#                pass
#            "Reset the fight":
#                $doppel_hp = 37000
#                $ray_hp = 1374
#                $ray_alive = True
#                $ray_turn = True
#                $matt_hp = 972
#                $matt_alive = True
#                $matt_turn = True
#                $tahv_hp = 741
#                $tahv_alive = True
#                $tahv_turn = True
#                $pina_hp = 512
#                $pina_turn = True
#                jump testing_menu
#                pass
