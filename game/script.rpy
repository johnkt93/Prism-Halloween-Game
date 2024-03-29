﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Hey, you aren't supposed to be seeing this. Stop staring at my shitty code. Go away.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
image white = "#ffffff"
image red = "#ff0000"

style ruby_style is default:
    size 12
    yoffset -20

style say_dialogue:
    line_leading 12
    ruby_style style.ruby_style

default difficulty = "Shiki"
default difficulties_unlocked = False
default game_cleared = False
default nia_in_party = False
default yura_in_party = False
default pina_in_party = False
default shiki_in_party = False
default hylo_in_party = False
default reiny_in_party = False
default iku_in_party = False

default pina_dungeon = True
default shiki_ear_press = 0
default corridor_forked = True
default inventory_tablet = True
default inventory_rope = False
default inventory_box = False
default inventory_plushie = False
default gottem = False
default hint_given = 0
default code = ""
default time_to_cheer_up_pina = False
default pina_tablet_viewed = False
default tablet_speech = False
default broguin_saved = False
default broguin_time = False

init python:
    def n(what, **kwargs):
        if nia_in_party:
            Nia(what, **kwargs)
        else:
            pass
    def y(what, **kwargs):
        if yura_in_party:
            Yura(what, **kwargs)
        else:
            pass

define a = Character("Aoi", image="Aoi")
image Aoi = "agents/aoi/aoi.png"
define iku = Character("Iku")
image Iku = "agents/iku/iku.png"
define l = Character("Luto")
image Luto = "agents/luto/luto.png"
define m = Character("Meno")
image Meno = "agents/meno/meno.png"
define r = Character("Rita")
image Rita = "agents/rita/rita.png"
define s = Character("Shiki", image="shiki")
image shiki = "agents/shiki/shiki.png"
image side shiki = "agents/shiki/shiki_side.png"
image side shiki scared = "agents/shiki/side_shiki_dead.png"
image side shiki happy = "agents/shiki/side_shiki_sparkle.png"
define n = Character ("Nia", image="nia")
image side nia = "agents/Nia/side_nia.png"
image side nia ponkotsu = "agents/Nia/side_nia_ponkotsu.png"
image side nia excited = "agents/Nia/side_nia_excited.png"
image side nia angry = "agents/Nia/side_nia_angry.png"
image side_nia_sad = "agents/Nia/side_nia_sad.png"
define y = Character ("Yura", image="yura")
image side yura = "agents/Yura/side_yura.png"
define p = Character("Pina", image="pina")
image Pina = "agents/Pina/pina.png"
image side pina = "agents/Pina/side_pina.png"

define re = Character("Reiny", image = "reiny")
image side reiny = "Miscellaneous/Reiny/side_reiny.png"
image side reiny shocked = "Miscellaneous/Reiny/side_reiny_what.png"
image side reiny cute = "Miscellaneous/Reiny/side_reiny_blush.png"
image side reiny surprise = "Miscellaneous/Reiny/side_reiny_surprise.png"
image side reiny mad = "Miscellaneous/Reiny/side_reiny_mad.png"

define h = Character("Hylo", image = "hylo")
image side hylo = "images/Miscellaneous/Hylo/side_hylo.png"
image side hylo neutral = "images/Miscellaneous/Hylo/side_hylo_neutral.png"
image side hylo happy = "images/Miscellaneous/Hylo/side_hylo_happy.png"
image side hylo sad = "images/Miscellaneous/Hylo/side_hylo_sad.png"
image side hylo scared = "images/Miscellaneous/Hylo/side_hylo_scared.png"

# The game starts here.
label splashscreen:
    scene black
    image movie = Movie(size =(1280,720), xpos=0, ypos=0, xanchor=0, yanchor=0)
    window hide
    play movie 'ProsmCord_Intro.webm'
    $ renpy.pause(6, hard=True)
    show movie
    $ renpy.set_return_stack([])
    return

label start:

    scene image "images/Yura_Dungeon/white.png":
        size(1280,720)
    menu:
        "Choose your difficulty setting"

        "Pina\nFor those who want to enjoy the story" if difficulties_unlocked == True:
            $ difficulty = "Pina"
            pass
        "Shiki\nFor those who want the normal escape experience":
            $ difficulty = "Shiki"
            pass
        "Reiny\nFor the true masochist.\nPuzzles will require all your brainpower" if difficulties_unlocked == True:
            $ difficulty = "Reiny"
            pass

    "Mysterious Voice""""
    The ritual demands a sacrifice. Powered by the lost souls gathered here.

    It is your choice to flee now, before the ritual starts. Or save the unfortunate souls.

    Should you choose to be the heroine of this story, if you wish to escape, free the lost souls enslaved by the mansion.

    What do you say [difficulty]?
    """

    menu:
        "Become the Heroine!":
            "IKZ!"
            jump prologue
        "Jump to Iku Dungeon":
            jump iku_dungeon
        "Haha, no. PeepoLeave":
            "Wow okay rood"
            centered "{color=#000000}Bad End{/color}"
            jump end_1
            return

label prologue:
    scene image "Backgrounds/manor.jpg"
    default shiki_dungeon = False
    """
    Today's the day!

    There's a carnival in town for Halloween and the girls and I decided
    to go together.

    Tonight's the night that they open their new haunted mansion
    attraction and I was extremely excited.

    It was essentially a giant escape room puzzle with horror elements.

    I almost had to drag the other to come with me.

    I waited outside the mansion, waiting for everyone to show up.

    A crowd slowly began to gather.

    After some time I began to get an ominous vibe from the crowd. A lot
    of them were wearing hooded robes, and I could get the sense that they
    were watching me.

    I sent a group message telling the others to hurry up.

    The crowd began to grow larger.

    They definitely weren't here for the haunted mansion.

    A more prominent figure stepped out from the crowd.
    """
    show image "Miscellaneous/Occultreats/Kknitro.png":
        xalign 0.5
        yalign 0.5
    voice "audio/Occultreats/Kknitro/kknitro1.mp3"
    "??" "Are you Shiki?"
    scene
    "I hesitated before responding."

    s "Yes I am. What of it?"

    "An indiscernible din erupted from the crowd."

    "Another figure emerged from the crowd."

    show image "Miscellaneous/Occultreats/Meateor.png":
        xalign 0.5
        yalign 0.5
    voice "audio/Occultreats/Meateor/Meateor1.wav"
    "?" "Silence brothers and sisters."

    "The crowd grew silent at his request."

    voice "audio/Occultreats/Meateor/Meateor2.wav"
    "?" "The time has come for you Shiki."

    "He rose his arms into the air theatrically."

    "The crowd once again burst with life at his motion."

    "I've got a bad feeling about this. I have to get out of here."

    "If I try to break through the crowd they'll definitely catch me, so I had no choice but to go into the haunted mansion and find another exit from there."
    scene
    "I made a dash for the attraction's doors."

    voice "audio/Occultreats/Kknitro/kknitro2.mp3"
    "??" "After her! Do not let her get away."

    "I could feel my heart pounding as I turned the doorknobs."

    s scared "Please be open."

    "The doorknobs turned easily, and I flung the door open with all my might."

    "The door shut behind me, leaving me alone in the dimly room. I have to find a hiding place."

    menu door_prologue:
        "There are doors to my left and right, as well as a door by the central staircase. Or I could check upstairs."
        "Left":
            "An emblem of what resembled a faceless man and a row of sharp teeth marked the door."
            jump enter_door_prologue
        "Right":
            $ shiki_dungeon = True
            "An emblem of a pallid child marked the door."
            jump enter_door_prologue
        "Staircase":
            "An emblem of red balloons marked the door."
            jump enter_door_prologue
        "Upstairs":
            "Instead of an emblem, a gash from a clawed creature was left on the door. It seemed fresh."
            jump enter_door_prologue

    menu enter_door_prologue:
        "Do you want to enter the door?"
        "Yes" if shiki_dungeon == False:
            "No matter how much I shook the handles, the door did not budge."
            jump door_prologue
        "Yes" if shiki_dungeon == True:
            "The doorknob turned easily in my hands. I thrusted the door open in a panic."
            jump shiki_dungeon
        "No":
            $ shiki_dungeon = False
            jump door_prologue

label shiki_dungeon:
    play music "<loop 0>shiki_bgm.wav"
    scene image "Backgrounds/darkroom.jpg"
    default shiki_dungeon_search = 0
    default bookcase_lifted = False
    default inventory_doorknob = False
    """
    The floorboards groaned as I entered. I could feel the floor sinking a
    bit with each step, but I hastily made my way inwards to flee from my
    pursuers.

    No sooner than a couple steps in, I heard a crash behind me. Startled,
    I looked behind me to see that the bookcase had fallen.

    I attempted to move the bookcase, but it wouldn't budge. There has to be something here that will help me escape.
    """
    $ renpy.notify ("Escape The Room")

    menu shiki_dungeon_escape:
        "What should I do?"
        "Leave" if inventory_doorknob == True:
            "There's no way I'm staying in a haunted room."
            s "Sayonara Ghosties!"
            jump escape_hub
        "Check the bookcase" if inventory_rope == False:
            """
            Despite the bookcase having just crashed violently behind me, it
            remained intact. No matter how much I tried to move the bookcase, it would not budge. I need to lift the bookcase somehow.
            """
            jump shiki_dungeon_escape

        "Check the bookcase" if inventory_rope == True and bookcase_lifted == False:
            "I tossed the rope over a pipe and wrapped it around the bookcase."
            "Hopefully the rope doesn't come undone as I try pulling it."
            "Well, here goes nothing."
            "I pulled the rope with all my might, but the bookshelf barely lifted off the ground."
            s "Please work."
            "I jumped up and pulled on the rope with my entire body."
            "The bookcase lifted fully."
            s "Yes!"
            "The bookcase rose to its full height and began tipping the other way."
            $ cont = 0
            $ counter = 0
            $ arr_keys = ["K_LEFT","K_RIGHT","K_SPACE"]
            call qte_setup(0.5,0.5, 0.01, renpy.random.choice(arr_keys), 0.5, 0.5) from _call_qte_setup
            while cont == 1 and counter == 0:
                $ counter = counter + 1

            if counter == 1:
                "I scrambled away from the falling bookshelf."
                "That was close."

                $ bookcase_lifted = True
                jump shiki_dungeon_escape
            else:
                s"{b}AAAH!{/b}"
                scene black:
                    size(1280,720)
                centered "{b}GAME OVER{/b}"
                scene image "images/Backgrounds/darkroom.jpg"
                jump shiki_dungeon_escape
        "Check the room" if shiki_dungeon_search == 0:
            """
            The dust in the room began to settle after the bookcase unceremoniously awoke the particles.

            The candelabras on the walls flickered with an eerie glow, but on closer inspection, they were electrical lights mimicking flames.

            Tucked away in the corner of the room was a door.
            """
            $ shiki_dungeon_search +=1
            jump shiki_dungeon_escape

        "Check the room" if shiki_dungeon_search == 1:
            """
            Since the only other thing in this room that I haven't checked was the door I made my way towards it.

            It was a shorter door, possibly to a broom closet.

            The doorknob was loose but it still turned freely in my hand.

            Inside was a tiny skeleton with rope strewn on its lap.

            I went to grab the rope.
            """

            s "AAAAAAAAAAAAAAA!!!"

            "I shrieked at the top of my lungs."

            "The skeleton fell on top of my arm as I removed the rope. Even though the skeleton was fake, it still startled me."

            $ inventory_rope = True
            $ renpy.notify ("Rope has been added to the inventory")
            $ shiki_dungeon_search += 1
            jump shiki_dungeon_escape

        "Check the room" if shiki_dungeon_search == 2 and bookcase_lifted == False:
            "There isn't anything else about the room that stands out."
            "The door is still blocked by the fallen bookcase, so I should deal with that."
            jump shiki_dungeon_escape

        "Check the room" if shiki_dungeon_search == 2 and bookcase_lifted == True:
            "Great!"
            "Now I can get out of here."
            "I reached for the door knob."
            s "What the heck!"
            "The doorknob was missing. Don't tell me that the bookcase took out the handle when it fell."
            s "What kinda game is this?!"
            s "Do you think this is funny?"
            "I shouted my fustratation to no one in particular."
            "I don't know how I missed it before, but there was a small vent near the ground."
            "Searching the vent I found that the doorknob had rolled inside."
            "I went to grab it, but it was slightly out of reach."
            s "Come on you son of a gun!"
            voice "audio/Miscellaneous/Reiny/urgh.mp3"
            "A small and cold hand grabbed me."
            voice "audio/Miscellaneous/Reiny/shiki.mp3"
            "?" "Shi-ki?"
            "AHHHHHHHHHHHHH! OH HELL NO!"
            "I snapped my arm away as quickly as I could."
            $ shiki_dungeon_search +=1
            $ inventory_doorknob = True
            jump shiki_dungeon_escape

label hylo_ministory:
    "Am I sure I should be checking out voices by myself?"
    menu:
        "Yes":
            "I couldn't just leave it alone."
            "It might bite me in the butt, but there's no way I can leave someone in trouble."
            "I know I'd want someone to do the same if I was in their position."
        "No":
            "Whatever that voice is and wherever it's coming from can't be good news."
            "As I made my way to the main section of the building a voice cried out to me."
    play music "<loop 0>hylo_bgm.wav"
    voice "audio/Miscellaneous/Hylo/hylo1.wav"
    h @ happy "Ah! You over there! How would you like the pleasure of aiding royalty? An honor normally reserved to the greatest knights of the kingdom."
    "There was a small girl trapped underneath some rubble. I almost wanted to leave her trapped there."
    s "What's in it for me?"
    voice "audio/Miscellaneous/Hylo/hylo2.wav"
    h @ neutral "I assure you as the princess of the Ayane family, saving me would be in your utmost interest."
    "Well, she doesn't seem dangerous at least. And it would be nice to have someone with me if something arises."
    "It took some effort but I was able to clear off some of the fallen debris and pull her out of the rubble."
    voice "audio/Miscellaneous/Hylo/hylo3.wav"
    h @ happy "Th-thanks for saving me. I will give you the honor of being one of my vassals."
    "She looked at me smugly, as if she had found a new toy to play with."
    s "Uh, no thanks."
    voice "audio/Miscellaneous/Hylo/hylo4.wav"
    h @ sad"Why wouldn't you want to be my vassal? When I take over this plane you'll definitely get preferential treatment. You could become head maid if you work hard enough!"
    s "What?! I don't want to be your maid. I can't believe I'm hearing this from some brat."
    voice "audio/Miscellaneous/Hylo/hylo5.wav"
    h @ neutral "Who are you calling a child? I am Ayane Hylo, of the Royal dragon family. For 3000 years have I held this title and this right!"
    s "There's no way you're older than I am. I'm 2525 years old."
    voice "audio/Miscellaneous/Hylo/hylo6.wav"
    h "You are but a young pup to me! Come back in a few centuries and maybe then you'll see how regal I truly am."
    "Well. I almost regret helping out now."
    "Time to leave before I get caught up in her shenanigans."
    voice "audio/Miscellaneous/Hylo/hylo7.wav"
    h @ scared "W-wait! Don't just leave me behind!"
    $ hylo_in_party = True
    jump escape_hub
label reiny_ministory:
    scene image "Backgrounds/darkroom.jpg"
    "We went back to the room I started in."
    s "I already searched this place. I don't think there's any way out."
    y "Hmmm."
    n @ sad "It's a bit chilly in here, isn't it?"
    p "It seems fine to me."
    n @ angry "You're a penguin! That doesn't count."
    y "There's definitely a draft in here."
    voice "audio/Miscellaneous/Reiny/urgh.mp3"
    s "AHHH IT'S THE GHOST!"
    y "Hmmmm."
    "Yura moved the bookcase and pushed on the ceiling."
    s "What are you"
    "She popped the ceiling open and stuck her head in."
    y "I found your ghost."
    "Yura came back down with someone on her shoulder."
    n @ excited "Is that..."
    p "Who I think it is?"
    s "A stray cat?"
    voice "audio/Miscellaneous/Reiny/notacat.mp3"
    re "I'm not a cat, I'm a dragon!"
    s "Oh, it's Reiny!"
    y "There's also a vent behind the bookcase here. I can see a computer on the other side."
    p "It might help us escape!"
    s "Finally!"
    n @ ponkotsu "It's a bit too small of a vent though."
    "We all turned to Reiny."
    voice "audio/Miscellaneous/Reiny/me.mp3"
    re "Me?"
    p "You're the only one that will fit. Please do this for us Reiny!"
    voice "audio/Miscellaneous/Reiny/on my own poi.mp3"
    re @ surprise "I have to go in there on my own? Well. Here goes nothing. Poi!"
    $ reiny_in_party = True
    jump escape_hub

label epilogue:
    scene image "Backgrounds/manor.jpg"
    s "I think we've lost them."
    voice "audio/Miscellaneous/Euro/line_1_euro.wav"
    "Captain?" "Oh, hello girls."
    s "Hi Cap."
    voice "audio/Miscellaneous/Euro/line_2_euro.wav"
    "Captain?" "What's wrong, looks like you're being haunted by ghosts."
    s "Something like that."
    voice "audio/Miscellaneous/Euro/line_3_euro.wav"
    "Captain?" "I see, I see. How are you enjoying the festival? Enough thrills for you all?"
    s "Enough thrills for a lifetime, honestly."
    voice "audio/Miscellaneous/Euro/line_4_euro.wav"
    "Captain?" "So, where are the other girls? I thought you all decided to go out together tonight?"
    s "Did we?"
    voice "audio/Miscellaneous/Euro/line_5_euro.wav"
    "Captain?" "Yes. Aoi, Iku, Meno, Rita, Luto, and you girls seemed all excited for tonight since it was one of the few times where you all could spend time together."
    "Ah, shit. Here we go again."
    jump end_game

label pina_rope_use:
    menu:
        "Tie the rope yourself":
            "I have some rope on me, but I have no idea how to tie a knot."
            "I'll have to get someone else to do it"
            jump pina_rope_use
        "Have Nia tie the rope" if nia_in_party:
            n @ ponkotsu "Ehhh, me? Why can't you do it?"
            s "I don't know how to tie a knot, okay?"
            $ renpy.notify ("Rope has been removed from your inventory")
            $ inventory_rope = False
            "Nia ties a simple knot with the rope on a nearby pipe."
            n "Simple, yeah?"
            "The rope falls a few feet short of the pool of water, but it makes the drop manageable."
            "We begin our descent into the cistern, the pipes groaning against our weight."
            n "Hey do you think that-"
            "At that moment the rope became undone and we plunged unceremoniously into the pool below."
            "Through the clear water I noticed that the pool wasn't as deep as expected. Standing up, the water reached only to my shoulders."
            "I could feel something thrashing in the water near me."
            "Panic set within me as I turned around."

            n @ ponkotsu "AHHH HELP ME! I CAN'T SWIM! CALL THE COAST GUARDS!"
            p "The water isn't that deep Nia! Just stand up."

            n @ sad "Oh. So it is. A-anyways, let's find a way out of here."
            "We retrieved the rope for future use."
            $ renpy.notify ("Rope has been added to your inventory.")
            return
        "Have Yura tie the rope" if yura_in_party:
            y "Hmmm."
            s "Something wrong Yura?"
            y "The rope is thicker than your would normally find inside of a household."
            y "This type of rope is more for mooring small boats to a dock."
            s "Eh?"
            y "You'd have to tie the rope a specific way so it won't untie itself."
            "The rope falls a few feet short of the pool of water, but it makes the drop manageable."
            "We begin our descent into the cistern, the pipes groaning against our weight."
            if nia_in_party == True:
                n "Hey do you think the rope will support all of our weight?"
                s "Come on now Nia, don't be a baby."
                n @ angry "I'm not a baby!"
                n "I just want to make sure we make it down safely, okay?"
                y "Don't worry. I'm confident that the rope can hold all of us."
            "We stopped at the end of the rope, a few feet above the pool of water beneath us."
            "From here we could see that the water wasn't as deep as we expected it to be, probably reaching only up to our shoulders."

            if nia_in_party == True:
                n "Hey. Maybe we should find another way to get down."
                s "We don't have time for that!"
                y "Do you want me to hold your hand, Nia?"
                n @ ponkotsu "W-what. N-no. What if Yura's flames go out? I'm just trying to be a considerate person."
                y "It'll be fine Nia. Just do it!"
                s "Yeah, or we'll leave you behind."
                y "Then last one in is a rotten egg!"
            "Yura did a cannonball into the pool"
            s "Geronimo!"
            "I dropped down into the pool. I pushed my bangs out of my face to see Nia clinging onto the rope for dear life."
            if nia_in_party == True:
                n @ ponkotsu "Oh god. Is this a bad time to mention I don't know how to swim?!"
                y "Water isn't that deep Nia. Just drop down and we'll bring you to the platform."
                n @ ponkotsu "ACKH!"
                "Nia either dropped herself from the rope and regretted it, or she lost her strength to hold on, as she flopped into the water."
                n @ ponkotsu "AHHH HELP ME! I CAN'T SWIM! CALL THE COAST GUARDS!"
                y "Come here you overgrown kitten."
                "Yura swam with Nia on her back to the platform. I followed suit."
            return
        "Return":
            jump save_pina

label escape_hub:
    play music "shiki_bgm.wav"
    scene image "Backgrounds/hub.jpg"
    if hylo_in_party == False:
        "I heard a pained voice calling out. Should I go check it out?"
    menu:
        "What should I do?"
        "Check out the voice" if hylo_in_party == False:
            jump hylo_ministory
        "Check upstairs" if nia_in_party == False:
            "Instead of an emblem, a gash from a clawed creature was left on the door. It seemed fresh."
            jump nia_dungeon_start
            jump escape_hub
        "Check upstairs" if nia_in_party == True:
            n "Going for a catnap Shiki? I'd normally join you on this, but don't we have something more important to do?"
            jump escape_hub
        "Check this floor" if yura_in_party == False:
            "An emblem of what resembled a faceless man and a row of sharp teeth marked the door."
            jump yura_dungeon_start
        "Check the basement" if pina_in_party == False:
            jump pina_dungeon_it
        "Talk":
            call talk_with_party from _call_talk_with_party
            jump escape_hub
        "Check item":
            "Nothing to see here"
            jump escape_hub
        "Leave" if yura_in_party == False or pina_in_party == False or nia_in_party == False:
            jump end_1
        "Leave" if yura_in_party == True and pina_in_party == True and nia_in_party == True and reiny_in_party == False:
            jump end_3
        "Leave" if yura_in_party == True and pina_in_party == True and nia_in_party == True and reiny_in_party == True:
            jump end_2

label talk_with_party:
    menu party_menu:
        "Who do I talk with?"
        "Talk with Nia" if nia_in_party == True:
            jump nia_menu
        "Talk with Yura" if yura_in_party == True:
            jump yura_menu
        "Talk with Pina" if pina_in_party == True:
            jump pina_menu
        "Talk with Hylo" if hylo_in_party == True:
            jump hylo_menu
        "Talk with Reiny" if reiny_in_party == True:
            jump reiny_menu
        "Talk with self":
            jump shiki_menu
        "Return":
            return

label nia_menu:
    menu:
        n "You wanted to ask me something?"

        "Ask her about an item" if gottem == False:
            n "Hey what about these?"
            s "I haven't even shown you anything yet. What are you talking about?"
            show nia excited at center:
                zoom 1
                yalign 0
            n @ excited "{b}THESE NUTS!{/b}"
            hide nia
            "I hate this zoomer sometimes"
            $ gottem = True
            jump nia_menu
        "Ask her about an item" if gottem == True:
            call nia_inventory from _call_nia_inventory
            jump nia_menu
        "Talk with Nia":
            n @ sad "Sorry, I don't have anything to say at the moment"
            jump nia_menu
        "Return":
            jump talk_with_party

label yura_menu:
    menu:
        y "Yes, dear?"
        "Ask her about an item":
            y "Sorry [difficulty] I have nothing to say at the moment"
            jump yura_menu
        "Talk with Yura":
            y "Sorry [difficulty] I have nothing to say at the moment"
            jump yura_menu
        "Return":
            jump talk_with_party

label shiki_menu:
    menu:
        "What should I check?"
        "Check an item":
            "I don't have an inventory. My clothes don't have pockets.\nDang women's fashion."
            "I have some rope though."
            jump shiki_menu
        "Check self":
            "My ear hasn't been working properly since I got in here."
            call shiki_ear_menu from _call_shiki_ear_menu
            jump shiki_menu
        "Return":
            jump talk_with_party

label pina_menu:
    menu:
        p "Oh. Hey [difficulty]. What's up?"
        "Ask her about an item":
            call pina_inventory from _call_pina_inventory
            jump pina_menu
        "Talk with Pina":
            p "Gomenasai, I don't have anything to say at the moment."
            jump pina_menu
        "Return":
            jump talk_with_party

label hylo_menu:
    voice "audio/Miscellaneous/Hylo/Talk.wav"
    h "You asked me to grace you with my presence?"
    menu:
        "Ask her about an item":
            call hylo_inventory from _call_hylo_inventory
            jump hylo_menu
        "Talk with Hylo":
            "She's not responding."
            jump hylo_menu
        "Return":
            jump talk_with_party

label reiny_menu:
    voice "audio/Miscellaneous/Reiny/whatup.mp3"
    re "'Sup?"
    menu:
        "Ask her about an item":
            call reiny_inventory from _call_reiny_inventory
            jump reiny_menu
        "Talk with Reiny":
            "Maybe some other time, yeah?"
            jump reiny_menu
        "Return":
            jump talk_with_party

label shiki_ear_menu:
    window hide
    menu:
        "Press the ear button":
            if shiki_ear_press >=60:
                "I think I've used up all of my storage. My brain is starting to ache."
                jump shiki_ear_menu
            elif shiki_ear_press >=49:
                $ shiki_ear_press += 1
                "I pressed the button on my ear"
                window hide
                with flash
                $renpy.notify ("You have taken a screenshot")
                jump shiki_ear_menu
            else:
                "I pressed the button on my ear"
                "..."
                "Nothing happened"
                $ shiki_ear_press +=1
                jump shiki_ear_menu
        "Return":
            return

label pina_dungeon_it:
    "There is a door with an emblem Red Balloon on it."

    if pina_dungeon  == True:
        menu:
            "Do you want to open the door?"
            "Yes":
                jump pina_escape_start
            "No":
                jump escape_hub
    else:
        "There's nothing else for us to do down there."
        jump escape_hub

label pina_escape_start:
    scene image "Backgrounds/Aqueduct.jpg"
    image monster = "Pina_Dungeon/Pina_Monster.png"
    """
    Upon opening the door, you find yourself in a small room with no distinguishable features, and no lighting.

    In front of you are metal bars that descend further down.

    As you begin descending further down, the sound of flowing water begins to surround you.
    """

    s "Must be nice to have your own water supply."

    "You continue down the corridor until you find a large cistern depressed into the floor."
    "Peering over the edge, you notice one of your companions."

    s "Pina?!"

    p "[difficulty]! [difficulty], help I'm stuck down here."

    s "Don't worry Pina! I'll get you out."

    menu save_pina:
#        hide window
        "Dive into the water":
            s "Don't worry Pina, I'll save you!"
            p "Shiki, wait!"
            "..."
            "..."
            "..."
            "I could feel a warmth radiating thorughout my body."
            "Slowly, my senses returned to me."
            s "Five more minutes mom. I don't feel so good."
            p "I wouldn't be feeling so good either, if I jumped into shallow water too."
            p "What were you thinking?"
            s "P-pina?"
            "As my vision began refocusing, I saw Pina with here eyes closed and her hands placed on my forehead."
            s "Ugh. Sorry for troubling you Pina. My body moved faster than my brain."
            p "It's no problem. It's what I do."
            pass
        "Tie a rope" if inventory_rope == True and yura_in_party == True and nia_in_party== True:
            call pina_rope_use from _call_pina_rope_use
            pass
        "Leave":
            "I'll have to come back later"
            jump escape_hub
    $ pina_in_party = True
    $ location = "Pina Dungeon"
    play music "<loop 0>pina_dungeon.wav"
    "Nia was carefully grooming herself with her tongue. I just shook as much of the water off of me as I could."
    n @ angry "HEY!"
    "Nia hissed at me but I paid her no mind."

    "I could see some steam rising off of Yura as her flames flickered."
    s "You okay over there Yura?"
    y "I'm just drying myself off."
    s "I thought your flames were body temperature."
    y "With some effort I can raise the temperature."
    s "Can you dry me off too?"
    y "Of course darling."
    "Yura opened her arms for an embrace."
    y "Come as close as you'd like and get yourself nice and dry."
    "Yura felt like being wrapped in a towel fresh from the dryer."
    "The transient scent of lilacs filled my nose."

    p "Thanks for coming. I've been having trouble getting out."
    s "What about that corridor over there?"
    p "I've tried, but it just leads you in circles back to here."
    s "Hmmm"

    menu pina_escape_menu:
        "What can we do?"
        "Search the area" if inventory_box == False and inventory_plushie == False:
            p "I've already searched as much as I could. This was all i could find."
            "Pina hands you an ornate box"
            $ renpy.notify("Ornate Box has been added to your inventory")
            p "I can't get it open, but maybe you'll have better luck."
            $ inventory_box = True
            jump pina_escape_menu
        "Search the area" if inventory_box == True or inventory_plushie == True:
            "We searched the area as much as we could. But nothing else stood out."
            jump pina_escape_menu
        "Check the corridor" if corridor_forked == True:
            call corridor_view from _call_corridor_view
            jump pina_escape_menu
        "Check the corridor" if corridor_forked == False and broguin_saved == False and broguin_time == False:
            "There is no need to stay here any longer than we need to."
            "It's time to start hauling butt."
            "As we made our way down the corridor a pervasive laugh filled our ears"
            "???" "AHAHEHEHE WHERE DO YOU THINK YOU'RE GOING?"
            p "No... no.. no. no!"
            p "Not this again."
            "???" "Did you think you'd escape so easily? hehehe What's the rush? If you're trying to reach the top, stay a while. We all float down here AHAHAHA"
            "Pina was hunched over and was covering her ears"
            p "Here it comes."
            "Before I got the chance to comfort Pina, a wave of darkness ran over us."
            s "Pina?! Where are you? I can't see a thing."
            p "Shiki!"
            "Her voice grew fainter as if the darkness was drowning her out."
            s "Pina!"
            "After the oppressive darkness dissipated, I noticed that Pina had gone missing."
            "I began to panic when suddenly"
            p "I-"
            p "I'm alright! I just got swept away in the waves."
            "Waves?"
            "The water laid still at my feet."
            "Did something else drag Pina away?"
            "The thought of something else being in here with us unnerved me."
            "I made my way back to where Pina was."
            "She laid on her back, looking at the ceiling."
            s "You okay Pina?"
            "She laid there unresponsive."
            "Her chest gently rose and fell, as if she were in a trance."
            s "Pina?"
            "I gently shook her."
            p "Hey Shiki. Sorry."
            "She rose up off the ground."
            p "It hasn't happened in a while but whenever I hear that voice. I just feel this overwhelming force push me back."
            "I wonder if I have something to get her out of this funk."
            $ broguin_time = True
            jump pina_escape_menu
        "Check the corridor" if broguin_time == True:
            "There's no point in dragging Pina there if she's not ready for it."
            jump pina_escape_menu
        "Check the corridor" if broguin_saved == True:
            "We rushed down the corridor as fast as our legs would carry us."
            "???""""
            What's the rush?

            Here I thought I was being a gracious host.

            Are you really going to turn your back on my hospitality?

            Maybe I didn't make things comfortable enough for you.
            """

            "A mass of darkness dropped down from the ceiling, impeding our way forward."
            show monster:
                xalign 0.1
                yalign 0.5
                zoom 0.6
            "The black mass quickly sprung toward us, wrapping us in a writhing black mass."
            "I struggled against the mass as much as I could, but it would not yield."
            s "I can't break free."
            n @ sad "Yeah. I'm stuck too."
            y "Same here. Can't even get my head free"
            p "I... {w} I WON'T LET YOU WIN!"
            "Pina glowed with a bright light that caused the writhing mass to retreat."
            p "As long as I stand, I won't let anything get in the way of my dreams anymore!"
            "Pina held the tablet in front of her like a magic grimoire"
            "A light shined from the tablet and three PenPals appeared in front of her"
            p "Let's show this monster the power of family!"
            play music "<loop 0>audio/PenPals/rhythm.mp3"
            voice "audio/PenPals/Mattdoss/ForPina.wav"
            "Mattdoss" "For Pina!"
            voice "audio/PenPals/Raylin/ForPenPals.wav"
            "Raylin" "For the PenCult!"
            voice "audio/PenPals/Tahvohck/ForTheBioreactor.wav"
            "Tahvohck" "For the BioReactor!"

            call pina_dungeon_jrpg from _call_pina_dungeon_jrpg

            stop music fadeout 2.0
            "???" "RARGH!"
            hide monster with dissolve
            "As the light shone around the monster, it began retreating into itself, releasing its grip on us."
            p "Nothing is keeping us here anymore. Let's go."
            $ renpy.notify ("You've freed Pina from the dungeon")
            $ pina_dungeon = False
            jump escape_hub

        "Check Inventory":
            call shiki_inventory from _call_shiki_inventory
            jump pina_escape_menu
        "Talk with party":
            call talk_with_party from _call_talk_with_party_1
            jump pina_escape_menu

label corridor_view:
    if pina_tablet_viewed == False and time_to_cheer_up_pina == False:
        "As we approached the corridor, there laid a forked path in front of us."
        p "I've tried navigating both of the paths, but they both seem to lead back to here."
        s "Hmmmm. Well we won't know unless we try."
        "..."
        "We tried to find the exit as best as we could, but like Pina said, it seemed that we were going nowhere."
        s "I'm sure that the last time we took that third turn, we didn't have to go down a corridor that long."
        p "It's probably best if you leave me. I don't want to keep you all here. I'll find a way out eventually."
        s "No way! We'll definitely get out of this together!"
        "Pina smiled"
        p "Yeah! There's nothing we can't overcome together!"
        """
        Even with her cheerful voice I could tell that she was faking it.

        It's painful to see Pina like this.

        I wonder if I have something that could cheer her up.
        """
        $ time_to_cheer_up_pina = True
        return
    elif pina_tablet_viewed == True:
        "We approached the corridor again with renewed fervor. But to our surprise the path no longer forked. In front of us, was a singular path that lead back upstairs."
        s """
        That.

        That wasn't like that before right?

        Didn't we drop down here?

        How is the entrance in front of us?
        """
        p "I don't know, but let's get out of here while we still can"
        $ corridor_forked = False
        return
    else:
        "I don't think we're going to make much progress with Pina like this."
        return

label inventory:
    menu shiki_inventory:
        "Tablet" if inventory_tablet == True:
            "A tablet that was given to us by Captain. It helps us communicate back home."
            jump shiki_inventory
        "Rope" if inventory_rope == True:
            "A sturdy piece of rope. It's fairly heavy."
            jump shiki_inventory
        "Ornate Box" if inventory_box == True:
            "A fancily decorated box."
            jump box_puzzle
            jump shiki_inventory
            return
        "Broguin Plushie" if inventory_plushie == True:
            "A doll that was made in the likeness of Broguin. Despite the chiseled musculature, it is soft and squeezable."
            jump shiki_inventory
        "Return":
            return

    menu pina_inventory:
        p "What item did you want to ask about?"
        "Tablet" if inventory_tablet == True and time_to_cheer_up_pina == True:
            p "That's the tablet given to us by Cap isn't it?"
            s "Yeah, do you still have yours?"
            "Pina pulls out her tablet."
            p "Of course I do. Why do you mention it?"
            s "Didn't you want to be an idol?"
            p "I still do"
            s "Well then hold on to that feeling."
            s "Even if you lose your way every now and then, it won't be too hard to get back on track as long as you focus on your goals."
            s """
            Run towards the finish line!

            And if you can't run, then walk.

            And if you can't walk, then crawl.

            And if you can't crawl, then we'll carry you there!

            No matter how far you think your dream may be, never lose sight of your goals.
            """

            p "Shiki-chan"
            "Pina wrapped her arms around me"
            p "Arigatou"

            $ tablet_speech = True
            $ pina_tablet_viewed = True
            $ time_to_cheer_up_pina = False
            jump pina_inventory
        "Tablet" if inventory_tablet == True and time_to_cheer_up_pina == False:
            p "That's the tablet given to us by Cap isn't it?"
            jump pina_inventory
        "Rope" if inventory_rope == True:
            p "I don't know what you want me to do with that, but it looks pretty hefty"
            jump pina_inventory
        "Ornate Box" if inventory_box == True:
            if hint_given == 3:
                p "What are you waiting for Shiki. The code is sep1986. I'm sure of it."
                jump pina_inventory
            if hint_given == 2:
                p "I've got it! The code is sep1986! That's the release date of Stephen King\'s IT novel."
                $ hint_given += 1
                jump pina_inventory
            if hint_given == 1:
                p "Hmmm. That phrase 'We all float down here' sounds familiar. Does it ring a bell for you Shiki-chan?"
                $ hint_given += 1
                jump pina_inventory
            if hint_given == 0:
                p "There's a clue written on the box. Does it make any sense to you?"
                $ hint_given += 1
                jump pina_inventory
        "Broguin Plushie" if inventory_plushie == True and broguin_time == True:
            s "Pina, I know you're in a bit of a funk right now, but I wanted to show you this."
            "I held out the plushie of Broguin"
            p "A plushie of Broguin?"
            s "Yeah!"
            s "Sometimes, when I'm feeling down or when I have nothing else to do, I like to think of the occultreats and the memories we've made together."
            s "Sure they bully me{w}\n\nLIKE A LOT"
            s "But I'll never forget how much they mean to me and even if it's a little bit selfish I want them to see how cool I am!"
            s "Even if I have to try different things, I'm sure I'll find my stride and everyone will cheer my name from the sidelines!"
            p "You're right Shiki!"
            p "I haven't finished showing off to the PenPals yet!"
            p "They're waiting for me and I can't disappoint them."
            $ broguin_saved = True
            $ broguin_time = False
            jump pina_inventory
        "Broguin Plushie" if inventory_plushie == True and broguin_time == False:
            p "OMG."
            p "That's such a cute plushie of Broguin!"
            p "Would you mind if I-"
            "She takes the plushie from my hands and hugs it tightly."
            p "It's so soft."
            "She hands the plushie back to you"
            jump pina_inventory
        "Return":
            return
    menu nia_inventory:
        "Tablet" if inventory_tablet == True:
            n"""
            That's the tablet that Cap gave us when we joined right?

            I have mine {w}...somewhere in my room.

            {w}

            {w}

            Probably.
            """
            jump nia_inventory
        "Rope" if inventory_rope == True:
            n @ angry "I don't like what you're insinuating."
            s "What makes you think I'm insinuating anything?"
            jump nia_inventory
        "Ornate Box" if inventory_box == True:
            n "That's a fancy looking box."
            n @ excited "How much do you think we'd get if we sold it?"
            s "We aren't selling the box, especially if we're stuck down here."
            n "You're probably right."
            s "Any idea on how to open it?"
            n @ excited "Have you tried throwing it really hard?"
            jump nia_inventory
        "Broguin Plushie" if inventory_plushie == True:
            n @ excited "That's adorable!"
            n @ excited "I want one of the Catnip Cartel!"
            jump nia_inventory
        "Return":
            return
    menu reiny_inventory:
        "Tablet" if inventory_tablet == True:
            voice "audio/Miscellaneous/Reiny/ooo.mp3"
            re "Oooh!"
            re "Wait. Shouldn't you leave that at home?"
            s "You know. I thought I did."
            jump reiny_inventory
        "Rope" if inventory_rope == True:
            voice "audio/Miscellaneous/Reiny/kimoi.mp3"
            re "Why are you caarrying that around with you?"
            s "You never know when you might need some rope."
            re @ mad "Ugh, kimoi"
            jump reiny_inventory
        "Broguin Plushie" if inventory_plushie == True:
            "I held out the plushie of Broguin"
            voice "audio/Miscellaneous/Reiny/cute.mp3"
            re "That's cute!"
            "She petted Broguin."
            jump reiny_inventory
        "Return":
            return
    menu hylo_inventory:
        "Tablet" if inventory_tablet == True:
            h "Did you want me to do something with that?"
            s "No, just wanted to see what you would say."
            voice "audio/Miscellaneous/Hylo/hylo_disgusted.wav"
            h "Gross."
            jump hylo_inventory
        "Rope" if inventory_rope == True:
            "I held out some rope."
            h "Wait! I didn't do anything wrong!"
            s "Huh? I'm not going to use it on you."
            h "Sorry. Bad experience."
            s "???"
            jump hylo_inventory
        "Broguin Plushie" if inventory_plushie == True:
            voice "audio/Miscellaneous/Hylo/hylo_excited.wav"
            h @ happy "OMG!"
            "She snatched the plushie out of my hand."
            h @ happy "He's such a cutie!"
            jump hylo_inventory
        "Return":
            return
label box_puzzle:
    if hint_given > 1:
        "I know that the code has to do with the release date with Stephen King's IT."

    if hint_given > 2:
        "The book was released on September of 1986."

    if hint_given:
        """
        Let's see.

        What was the hint again?

        To find your answer for this gear\nLook for the release\nWe all float down here\nAnd the lock will cease
        """
        $ code = renpy.input("Please type in your answer, MMMYYYY Format", length = 7)
        if code.lower() == "sep1986":
            $ inventory_plushie = True
            $ renpy.notify("Broguin Plushie has been added to you inventory")
            $ inventory_box = False
            "Seemed like that worked!"
            "Upon entering the last digit, the lock clicks and the top is left ajar."
            "Opening the lid, you find a plushie of Broguin"
            jump pina_escape_menu
        else:
            "Hmmm. The box is still locked. Did I mess up somewhere? It accepts three letters, and then four numbers."
            jump box_puzzle
    else:
        "It's a fancy looking box. That's about all I can tell from it."
        jump pina_escape_menu

label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    # can change to "call screen qte_button" to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return

label end_1:
    s "Wait. What do you mean that this is all there is to the game. When is it going to be done?"
    "Pang" "Soon. (read as never)"
    re "Am I late?!"
    "Pang" "Yes"
    s "Oh, I gave Reiny the wrong time to show up."
    call end_game from _call_end_game
    # This ends the game.

    return

label end_2:
    scene image "Backgrounds/manor.jpg"
    "We all made it out of the mansion in once piece."
    "There were still some people waiting for us outside, but they weren't paying attention."
    "We slowly crept along the side of the manor to escape their gaze."
    "Nia scrunched up her face, as if she was about to sneeze."
    "I whispered to her."
    s "Hold it in Nia!"
    "Reiny moved to block Nia's face before she could sneeze."
    "I breathed a sigh of relief"
    #reiny sneeze here
    voice "audio/Miscellaneous/Reiny/bonus sneeze TSKR.mp3"
    re @ cute "~Choo."
    p "Bless you, Reiny."
    show image "Miscellaneous/Occultreats/Kknitro.png":
        xalign 0.2
        yalign 0.5
    show image "Miscellaneous/Occultreats/Meateor.png":
        xalign 0.5
        yalign 0.5
    show image "Miscellaneous/Occultreats/Pang.png":
        xalign 0.8
        yalign 0.5
    voice "audio/Occultreats/Meateor/Meateor3.wav"
    "?" "We knew you'd make it out of there eventually."
    voice "audio/Occultreats/Kknitro/kknitro3.mp3"
    "??" "Honestly, I bet against her. Didn't you also say we should find a way in to save her?"
    voice "audio/Occultreats/Meateor/Meateor4.wav"
    "?" "Brother Nitro, not in front of her."
    voice "audio/Occultreats/Meateor/Meateor5.wav"
    "?" "Shiki!"
    "The man pulled down his hood. I recognized his face from my streams. It was none other than..."
    voice "audio/Occultreats/Meateor/Meateor6.wav"
    "Meateor" "The time has come for you to atone for your sins! You will answer for your crimes in front of all the Occultreats that you have slighted!"
    voice "audio/Occultreats/John/john1.wav"
    "John" "Actually, I agreed with most of her tierlist"
    voice "audio/Occultreats/Meateor/Meateor7.wav"
    "Meateor" "SILENCE BROTHER JOHN! What will the other members think if we let her get away with this. Do we need to send you back to Luto?"
    voice "audio/Occultreats/John/john2.wav"
    "John" "Please don't! I just got my body back."
    voice "audio/Occultreats/Kknitro/kknitro4.mp3"
    "Kknitro" "I actually also don't care one way or another about her opinion. We all have our own beliefs."
    voice "audio/Occultreats/Meateor/Meateor8.wav"
    "Meateor" "Yeah, but what about her hot takes? Are we going to let those slide?"
    voice "audio/Occultreats/Kknitro/kknitro5.mp3"
    "Kknitro" "Those were pretty out there. She will have to repent for that."
    s "Well then I'm sorry guys."
    "A smile began forming on their faces. A happy murmur could be heard from the crowd."
    s "SORRY I'M BASED AND THAT YOU GUYS ARE WRONG!"
    voice "audio/Occultreats/Kknitro/kknitro6.mp3"
    "Kknitro" "Alright guys, get her!"
    s "You guys aren't the only one here you know."
    "The other girls stood with me, as well as the Catnip Cartel, Yuragumis, and PenPals"
    voice "audio/Occultreats/Meateor/Meateor9.wav"
    "Meateor" "Did you really think that would be enough to take us all on?"
    "The Occultreats formed a large crowd in front of us."
    s "No, but we have a special technique."
    "I took a deep breath."
    s "Joestar Family secret technique {w} RUN AWAY!"
    "We began running in different directions"
    voice "audio/Occultreats/Kknitro/kknitro7.mp3"
    "Kknitro" "After them!"
    scene image "Backgrounds/manor.jpg"
    jump bonus_epilogue

label end_3:
    "When we got to the main corridor we all rushed for the door."
    "I swung open the glowing door and made my way outside"
    y "Ah!"
    "We turned back to see yura with an exasperated look on her face."
    y "Guys I think I'm stuck here."
    n "Just walk through the door 4head."
    y "Oh sure yeah let me just walk through, like I just tried."
    "She stuck her tongue out at Nia."
    "We moved back into the main room where I noticed a seal on the door."
    p "Well, what do we do now?"
    s "Well with my understanding of occultology, this seal is definitely  arcane in nature."
    n "It's a seal to trap demons or spirits."
    "We all looked at Nia incredulously."
    n "Yeah. Look, it's a modified form of the Kabbalistic tree of life. Some of it isn't exact, but there's Malkuth, Chokhmah, Binah, Chesed, Tiferet, Netzach."
    n "If I had to offer an rough idea it means 'Victory and kingship over the spirits through knowledge and understanding for beauty and kindness.'"
    n @ ponkotsu "Why are you all looking at me like that?"
    y "Whose brain did you take, where's the real Nia."
    n @ sad "Eh?! Come on. don't be like that. It's just some stuff they teach during shrine maiden training. Warding spirits and stuff, you know?"
    s "You actually paid attention though?"
    n @ angry "Excuse you. I'm a wonderful student."
    y "Yeah, if the teacher is alcohol."
    p "You shouldn't drink so much."
    n @ ponkotsu "A-anyways. We can probably overload the seal with magic, or I can dispel it (probably)."
    s "Which one's easier for you?"
    n "Oh. I don't know any magic. Pina should be able to do it though."
    p "One of us is going to have to stay behind, while the rest escape."

    menu menu_sacrifice:
        "Sacrifice Yura":
            y "It's okay. I'll find another way out."
            s "Sorry Yura. We'll find a way to help from the outside."
            y "Eww gross. You think I need help?"
            p "Well it would be faster if we help, right?"
            y "I'm not Nia. I can do this by myself."
            n @ angry "What? I didn't even say anything."
            y "Git gud."
            jump end_1
        "Sacrifice Pina":
            p "Alright. I can do this!"
            s "We'll wait for you Pina!"
            n "See ya Pina!"
            y "Take care of yourself Pina."
            p "I'll never forget the time we spent together!"
            s "Why is everyone writing off Pina?!"
            jump end_1
        "Sacrifice Nia":
            n @ ponkotsu "Ah, gee Rick. I don't know if I can do this."
            s "We can find another way."
            n "No. I got this."
            "Nia takes a deep breath"
            jump nia_chant
        "Sacrifice No One" if reiny_in_party == False:
            "No way we came all the way here to give up now."
            s "There has to be another way out."
            p "What about that room over there."
            s @ dead "I'm pretty sure that room is empty. Also it's haunted."
            y "What? Don't be a baby Shiki. Come on."
            jump reiny_ministory
        "Sacrifice No One" if reiny_in_party == True:
            jump end_2
label nia_chant:
    n"""
    Kregi safade slehiya tunoleba

    Watumi yufiniya

    Waituno se saifiszaiya

    Faituno se naidizaiya
    """
    menu:
        "Continue listening":
            pass
        "Leave":
            jump end_1
    n"""
    Shejumani Ifuritias

    Krasa meyu sheina ifil

    Krezu mani putisala

    Krasa seidu fleina

    Shejumani Ifuritias

    Prasa feinu sheina

    Ikimasi

    A sheinu fleina

    Arumateria
    """
    menu:
        "Continue listening":
            pass
        "Leave":
            jump end_1
    n"""
    Wadi kyufede faisii witoliye

    Watumi yufiniyasu

    Shanti fase omilaya

    Shanti fase

    Somikana

    Apeyumetumi ya
    """
    menu:
        "Continue listening":
            pass
        "Leave":
            jump end_1
    n"""
    Flajimani Eyruathsi

    Plasa meyu neina ifil

    Arumani yurifala

    Prasa leinu fleina

    Flajimani Eyruathsi

    Krasa meinu neina

    Ikimasi

    A leinu neina

    Arumateria
    """

    "We all started aplauding"
    n @ ponkotsu "Eh. Why are you guys still here."
    s "Because you have a beeautiful voice."
    n @ excited "Th-thanks. But I have to start over now. So please go away."
    jump end_1


label bonus_epilogue:
    s  "-panting- I think we've lost them."
    voice "audio/Miscellaneous/Euro/line_1_euro.wav"
    "Captain?" "Oh, hello girls."
    s  "Hi Cap."
    voice "audio/Miscellaneous/Euro/line_2_euro.wav"
    "Captain?" "What's wrong, looks like you're being haunted by ghosts."
    s  "Something like that."
    voice "audio/Miscellaneous/Euro/line_3_euro.wav"
    "Captain?" "I see, I see. How are you enjoying the festival? Enough thrills for you all?"
    s  "Enough thrills for a lifetime, honestly."
    voice "audio/Miscellaneous/Euro/line_4_euro.wav"
    "Captain?" "Where's the other girls? I thought you all decided to go out together tonight?"
    s  "Did we?"
    voice "audio/Miscellaneous/Euro/line_5_euro.wav"
    "Captain?" "Yes. Aoi, Iku, Meno, Rita, Luto, and you girls seemed all excited for tonight since it was one of the few times where you all could spend time together."
    s  "Ah, shit. Here we go again."
    jump end_game

label end_game:
    play music "Prism Ending Scuff.wav"
    $ persistent.credits = True
    $ _dismiss_pause = False
    $ _skipping = False
    $ _rollback = False
    $ credits_speed = 58 #scrolling speed in seconds
    scene black:
        size(1280,720)#replace this with a fancy background
    show cred at Move((0.5, 6.8), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    with dissolve
    with Pause(credits_speed -4)
    show splash
    with dissolve
    with Pause(3)
    hide splash
    with dissolve
    with Pause(.75)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4.5)
    hide thanks
    with dissolve

init python:
    credits =('Backgrounds', 'Yura Dungeon: John'),('Backgrounds', 'Unsplash (sourced by Baka)'),('Artwork', 'Wet Floor/Lil Bucket'),('Artwork', 'Sera Nyan'),('Sprites','Airborne Cat'),('Writing', 'John'),('Additional Story','Renfield'),('Programming', 'John'),('Opening Theme:\nI Ran(So Far Away)', 'Peen Matsuri'),('Closing Theme:\nYou\'ll Be In My Heart', 'John'),('Voice Acting', '\n\nOccultreats:\nJohn\nkknitro\nMeateor'),('Voice Acting', '\n\nCatnip Cartel:\nWaffles\nGabut\nNoseless'),('Voice Acting', '\n\nYuragumis:\nQtini\nAlicerez\nFroze'),('Voice Acting', '\n\nPenPals:\nMattdoss\nTahvohck\nRaylin'),('Voice Acting', '\n\nIkumins:\nLil Bucket\nWall-E\nRei Nana'),('Featuring','Reiny (as herself)'),('Featuring','Hylo (as herself)'),('Featuring','Nolia (as herself)')
    credits_s = "{size=80}PrismCord Halloween\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()

init:
    image splash = Text("{size=90}Happy Halloween!", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
#    image splash = "images/Company-Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
