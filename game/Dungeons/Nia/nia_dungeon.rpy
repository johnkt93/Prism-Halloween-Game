label nia_dungeon_start:
    default inventory_control_key = False
    default gabut_roll = False
    scene image "Backgrounds/bedroom.jpg"
    """
    I opened the door to a small bedroom.

    In comparison to the rest of the manor, the room looked well lived in. There was a lack of dust on the walls, and the room was neatly organized. In the corner of the room was a small vanity table.

    Set against the middle of a wall, next to the vanity table was a canopy bed. It looked like there was someone on the bed.
    """

    menu:
        "Part the curtains?"
        "Yes":
            "As I moved the curtains out of the way, I noticed a familiar sight"
            pass
        "No":
            "I had no idea what was pass the curtain, and I had the feeling that it would be better not to find out."
            "?"  "Please, just 15 more minutes. I'll get up, I swear."
            "Wait, I recognize that voice."
            "I threw open the curtains."
            pass

    s "Nia?!"
    "Nia laid on the bed, fast asleep."
    s """
    Nia, now is not the time to be sleeping.

    There's something weird going on and I think it's best for us to
    get out of here.

    N-{w}nia?
    """

    "I gently shook her{w} but she barely budged."
    s "If you're trying to scare me, I'm going to be mad."
    "No response."
    "I began shaking her harder."
    s "Nia, wake up you lazy cat."
    "A loud thump came from behind me."
    "I turned around to find a book open on the table."
    "It was opened to a page describing a being that puts people to sleep to eat their dreams."
    s "Oh no."
    "I looked back to Nia. She looked so peaceful, but what if?"
    s "There has to be something in the book that would help me save Nia."
    "It says here that the only way to escape from the dream-like state is to remove it from the dream."
    s "Yes, but remove it how!"
    """
    There was no other information in the book, and the rest of the
    pages were blank.

    This writing sucks.

    I laid down next to Nia to contemplate what to do next.

    The bed was actually very comfy.

    I could see why Nia wouldn't want to get up from this.

    The sheets were so soft, and the pillow had the right amount of fluff.

    I could feel myself sinking gently into the bed.
    """
    scene image "Backgrounds/warehouse.jpg"
    play music "<loop 0>nia_dungeon.wav"
    "When I opened my eyes, I found myself on the cold metallic floor of a room I did not recognize."

    n "Well, good morning sleepyhead!"
    n @ ponkotsu "Wait, is it morning? I have no idea."
    "I got off the ground and dusted off my clothing."
    s "Where are we?"
    n "Some kind of warehouse."
    n "There was this scary guy chasing me and I made my way into this place."
    n "Seems abandoned though."
    n @ angry "Did you see that creepy guy too?"
    s "No, when I woke up I was already here."
    n "Alrighty. Let me know if you see him."
    s "So what have you been up to in here?"
    n "I've been trying to find a key to use the crane and move some boxes. It should help us out."
    s "Do you even know how to operate a crane?"
    n @ ponkotsu "Eh. How hard could it be? You press buttons and it moves. It moves too far and you press some other buttons. Pretty simple."
    s "I admire your optimism."
    n "Thanks! Would you mind helping me find the key? I'll check the control room, if you don't mind checking the other places."
    s "Sure."

    menu control_room:
        "What should I do?"
        "Press a button" if gabut_roll == False:
            voice "audio/CatnipCartel/Gabut/GabutRoll.wav"
            "Never gonna give you up. Never gonna let you down. Never gonna run around and desert you."
            s "Really now?"
            $ gabut_roll = True
            jump control_room
        "Ask Nia for help" if lost == 3 and nia_in_party == False:
            n "Hey Shiki, did you find the key?"
            s "Yes, but the guy who has it won't give it to me."
            n "Have you tried taking it and running away."
            s "Well, he challenged me to an arm-wrestling contest. And I lost."
            n "Alright, I'll come help you."
            $ nia_in_party = True
        "Talk with Nia" if inventory_control_key == False:
            n "Any luck finding that key?"
            s "No, nothing yet."
            n "Let me know when you find it."
            jump control_room
        "Talk with Nia" if inventory_control_key == True:
            n "Great! Hand over the key and let's get things started."
            $ renpy.notify ("Control key has been removed from your inventory")
            jump nia_dungeon_end
        "Leave the control room":
            jump nia_dungeon

label nia_dungeon:
    default warehouse_search = False
    default prison_found = False
    menu nia_dungeon_hub:
        "I looked around the warehouse."
        "Return to the control room":
            jump control_room

        "Search the warehouse" if warehouse_search == False:
            "From what I could tell the warehouse itself hadn't been used in a long time. A thick layer of dust had settled on most of the boxes."
            "A plaque laid on top of one of the boxes."
            "It read"
            centered "{size=60}Beware La Matrona" (what_outlines=[(5,"#ff0000",0,0)])
            "The plaque depicted a beast with fierce eyes and claws. It looked like a fox."

            $ warehouse_search = True
            jump nia_dungeon_hub

        "Search the warehouse" if warehouse_search == True and prison_found == False:
            "I took another look around the warehouse. Something about some of the boxes struck me as odd."
            "It looked just like the other boxes in the warehouse, but there was almost no dust on the box whatsoever. There was also some scratch marks on the floor, hinting that the box was dragged or pushed here."
            "I tried to open one of the boxes when a voice shouted out at me."
            show image "images/Nia_Dungeon/Gabut.png"
            voice "audio/CatnipCartel/Gabut/Line1.wav"
            "Gabut" "Hey! Don't touch that."
            "A voice yelled at me"
            voice "audio/CatnipCartel/Gabut/Line2.wav"
            "Gabut" "Boss will get angry with you if you mess with the storage."
            voice "audio/CatnipCartel/Gabut/Line3.wav"
            "Gabut" "Wait. I haven't seen you around before. You new here?"
            s "Uhh, you could say that."
            voice "audio/CatnipCartel/Gabut/Line4.wav"
            "Gabut" "Hmm."
            "He looked me up and down."
            voice "audio/CatnipCartel/Gabut/Line5.wav"
            "Gabut" "Aren't you kinda small to be doing work in the warehouse?"
            s "I'm just looking around. You know anything about the key for the control room."
            voice "audio/CatnipCartel/Gabut/Line6.wav"
            "Gabut" "Now that you mention it, I think I heard talk about that in the mess hall. Go check in with our second in command then and he'll assign you to somewhere more, uhhh, fitting."
            hide image "images/Nia_Dungeon/Gabut.png"
            $ prison_found = True
            jump nia_dungeon_hub

        "Search the warehouse" if warehouse_search == True and prison_found == True:
            "I don't think they would appreciate it if I poked my nose around"
            "I should check somewhere else."
            jump nia_dungeon_hub

        "Go to the mess hall" if prison_found == True and inventory_control_key == False and lost == 0:
            "Following the directions given to me, I found myself outside of a barred gate."
            "Off to the side was a man slumped over on the ground."
            "I shook the gate, and unsurprisingly it was locked."
            show image "images/Nia_Dungeon/Noseless.png"
            voice "audio/CatnipCartel/Noseless/line1.wav"
            "Noseless" "HUH?! who goes there."
            "He wiped the drool off his face before rising to his feet."
            voice "audio/CatnipCartel/Noseless/line2.wav"
            "Noseless" "Wait, who are you?"
            s "Uhhh, new recruit? Sent here to get the key and bring it to Boss."
            "He looked me up and down."
            voice "audio/CatnipCartel/Noseless/line3.wav"
            "Noseless" "Yeah, I don't think so."
            voice "audio/CatnipCartel/Noseless/line4.wav"
            "Noseless" "But that's above my paygrade so."
            "He pulled out a key from his pocket and unlocked the gates."
            voice "audio/CatnipCartel/Noseless/line5.wav"
            "Noseless" "Here you go"
            s "Wait, just like that?"
            voice "audio/CatnipCartel/Noseless/line6.wav"
            "Noseless" """
            Yeah, just like that.

            To be honest the second-in-command is bossier than Boss is.

            I'd rather just pretend that I'm doing something.

            It's why I was given guard duty.

            And between you and me. {w} I think our second-in-command is getting big for his britches since Boss likes him a little bit more than the rest of us.

            But, you didn't hear that from me.
            """
            hide image "images/Nia_Dungeon/Noseless.png"
            jump waffles #Lel syntax
        "Go to the mess hall" if lost > 0 and nia_in_party == False:
            "There's no point in going back there at the moment. I should talk with Nia."
            jump nia_dungeon_hub
        "Go to the mess hall" if lost > 0 and nia_in_party == True:
            jump waffles_fight

label waffles:
    "I made my way into the mess hall, and I saw a key on one of the tables."
    "As I got further into the room, I could hear the gate closing behind me."
    voice "audio/CatnipCartel/Noseless/line7.wav"
    "Noseless" "Sorry, just doing my job."
    "I was trapped in here."
    "But that's fine. I just needed to grab the key and I can find another way out."
    show image "images/Nia_Dungeon/Pancakes.png"
    voice "audio/CatnipCartel/Waffles/line1.wav"
    "Waffles" "So we've finally caught the sewer rat sneaking around our base."
    "I looked up to see a younger looking man on the second floor railing."
    "He leapt over the edge and landed on his feet."
    voice "audio/CatnipCartel/Waffles/line2.wav"
    "Waffles" "We don't take kindly to those who jeopardize our operations."
    s "Look, I have no idea what you guys are doing here. I just need that key and I'll be on my way, and out of your hair."
    voice "audio/CatnipCartel/Waffles/line3.wav"
    "Waffles" "A likely story!"
    voice "audio/CatnipCartel/Waffles/line4.wav"
    "Waffles" "But unfortunately for you, that key is for Boss. And Boss has given the order to deal with you."
    s "Wait! But this is supposed to be a family-friendly game."
    voice "audio/CatnipCartel/Waffles/line5.wav"
    "Waffles" "I was only going to challenge you to an arm-wrestling contest. I don't think Boss would approve of anything violent."
    s "Well then prepared to get your butt whooped!"
    voice "audio/CatnipCartel/Waffles/line6.wav"
    "Waffles" "Great!"
    "He pounded his fist into an open palm, and tossed his neck making a loud cracking sound reverberate in the otherwise empty room"
    voice "audio/CatnipCartel/Waffles/line7.wav"
    "Waffles" "Then let's get started."
    voice "audio/CatnipCartel/Waffles/line8.wav"
    "Waffles" "But first {w} could you help me get to the table? I hurt my legs jumping down here."
    hide image "images/Nia_Dungeon/Pancakes.png"
    jump waffles_fight

label waffles_fight:
    default lost = 0
    while cont == 1:
        $ cont = 0
        $ arr_keys = ["K_LEFT","K_RIGHT","K_SPACE"]
        call qte_setup(0.2,0.5, 0.01, renpy.random.choice(arr_keys), 0.5, 0.5) from _call_qte_setup_2

    if lost == 1 and nia_in_party == False and inventory_control_key == False:
        "I'm getting nowhere with this."
        "I have to find another way to get the key off of him."
        "Maybe Nia has an idea?"
        jump nia_dungeon_hub
    if lost == 1 and nia_in_party == True:
        "I came back to the room, ready for my revenge."
        n "Is this where the guy you wanted me to beat up is?"
        s "No, just beat him. Don't beat him up."
        n "Same thing."
        show image "images/Nia_Dungeon/CatnipCartel.png"
        "Waffles" "Back for more are we?"
        "Waffles" "I don't mind the light workout."
        n "Oh, hey guys."
        n "Any luck finding that key?"
        "Waffles" "Boss! We weren't expecting you. We did find that key, and we also found that intruder you were looking for."
        n @ excited "Great! Where is she!?"
        "Waffles" "Actually, she's right next to you."
        n @ ponkotsu "Huh?"
        "Nia turned to look at me."
        s "Are we the baddies?"
        n @ angry "What are you talking about. That's my friend Shiki."
        "Gabut" "Hey, don't look at me, blame Waffles."
        n @ ponkotsu "Who's Waffles?"
        voice "audio/CatnipCartel/Waffles/line9.wav"
        "Waffles" "Boss... I'm Waffles."
        n @ sparkles "Oh! Pfannkuchen!"
        n "Why'd you change your name? Trying to sound tough?"
        voice "audio/CatnipCartel/Waffles/line10.wav"
        "Waffles" "I'M NOT A PANCAKE!"
        hide image "images/Nia_Dungeon/Pancakes.png"
        $ inventory_control_key = True
        $ renpy.notify("The control key has been added to your inventory.")
        n "Well since that's settled, I'll meet you back at the control room."
        $ nia_in_party = False
    elif nia_in_party == False:
        show image "images/Nia_Dungeon/Pancakes.png"
        "Waffles" "AHA! Another victory for the cartel."
        "Waffles" "Care to go again little missy?"
        $ lost += 1
        hide image "images/Nia_Dungeon/Pancakes.png"
        jump waffles_fight

    "Great! I have the key and now all I need to do is to meet Nia in the control room and we can get out of here."
    jump nia_dungeon_hub

    label nia_dungeon_end:
    n "Great! Let me just."
    "She inserted and turned the key which caused the machinery to whir to life."
    "I could hear some grunting sounds coming from the crane."
    "Eventually a silhouette pass by the window and a thud could be heard from the platform outside."
    n @ angry "Ah! You bitch!"
    "Nia quickly began running out of the room"
    n "Shiki take care of the crane while I deal with some unfinished business."
    s "But."
    "She was already gone. I could hear her clamoring down the metal stairs."
    n @ angry "Get your ass back here, I'ma beat you up."
    "I operated the crane to the best of my abilities, clearing the boxes away from the exit."
    "I searched around for Nia before leaving, but she was nowhere to be seen."
    "I'm sure she's fine. Can't say the same for whoever she's chasing though."
    $ nia_in_party = True
    "..."
    show image "images/Backgrounds/bedroom.jpg"
    "As I opened my eyes, my vision was blurry."
    "I rubbed my eyes to help re-focus."
    "As my vision cleared up I noticed I was back in the bedroom."
    "Sleeping next to me was Nia"
    "I shook her aggressively."
    n "Huh, is it time for food?"
    n "Oh, Shiki. I had the weirdest dream about the Catnip Cartel. You were there!"

    play music "shiki_bgm.wav"
    scene image "Backgrounds/hub.jpg"
    h "Well, well. Look who's finally awake!"
    h "Had a nice rest, princess?"
    s "I don't even remember falling asleep. I just went to lie down next to Nia, and then I was out like a light."
    h "Ex-cuses!"
    h "Did you expect me to do all the work while you rest your lazy bones?"
    s @ scared "I mean it'd help if did something other than bark orders at me."
    h "You think I'm only ordering you around?"
    h "My dear, as my retainer I'm offering you something kingdoms have risen and fallen over."
    s "And what would that be?"
    h """
    That would be the pact with a dragon of course!

    Do you know how much evil magic is being held at bay just by having me around?

    Do you know how scared those creepy crawlies in the dark are to approach you?

    Be lucky I'm not charging you for this service!
    """

    s @ happy "You know I do feel a bit luckier recently. I suppose it was wrong of me to accuse you of doing nothing. I apologize."
    h "Heh. Sucker."
    

    jump escape_hub
