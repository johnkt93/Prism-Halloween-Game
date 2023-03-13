default Nolia_Needs_Water = False
default petal_name = False
default petal_knows = False
default nolia_hint = False
default food_count = 0
default cell_key_in_inventory = False
default cell_door_locked = True
default wetty_encountered = False
default rei_key_in_inventory = False
default Nolia_in_party = False
default Wetty_in_party = False
default Rei_in_party = False
default Wall_in_party = False
default screen = None
default location = "cell"

label iku_dungeon_script:
    background "black"
    "As you open the door, you feel some resistance and hear the sound of fungal tendrils snapping."
    "The ground beneath you is uneven, and though you try your best to keep your footing, you slip while going down a slope and start picking up speed"
    "As you try to slow down your descent, you see someone peeking out from behind some tall sunflowers"
    "You are almost certainly going to hit her at this rate"

    menu:
        "Do you?"
        "Scream at her to get out of the way?":
            "You muster up as much energy as you can and shout{nw}"
            s "{b}LOOK OUT!{/b}"
            pass
        "Say nothing, and hope for the best?":
            "At this speed, nothing you can say or do will stop you from colliding with her"
            "You brace yourself as best you can"
            pass

    "The woman lets out a screech as you careen into her, knocking her off her feet"
    "The two of you entangle and your momentum carries the two of you forward a bit"
    "Colors fade from your vision as the world grows dark"
    "With the last of your energy you can make out some voices"
    "?" "No! Let go of me!"
    "???" "Don't be like that, my princess. Soon you will have everything you can want."
    "???" "Get rid of the dog, I have no use for her"
    pause 3.0
    "Your senses return to you and your vision begins to refocus"
#   show screen 1_1
#   show shiki_sprite_idle
    "You find yourself in a jail cell"
    "As you go to the cell door, you shake it with all your muster"
#   Door noises
    "Expectedly, the door does not budge"
    s "Hey! Let me out of here"
    "You shout at the top of your lungs, while clamoring with the bars"
    "After some time, seeing as your words were getting you nowhere, you devolve into barking"
    "You hear to seound of soft footsteps slowly approaching, and almost instinctively, you back away from the door"
#   show iku_sprite_idle with fade in
    "In front of you is the most beautiful alien creature you've ever seen"
    "You wipe the drool from your mouth, and rub your eyes to better focus your thoughts"
    iku "Shiki"
    "The utterance of your name breaks your out of your reverie and you notice that the alien in front of you is actually Iku"
    s "S-senpai?!"
    "Iku responds unenthused, and as if she had rehearsed the lines over and over"
    iku "Welcome trespasser, to the newly founded Kinoko Kingdom"
    iku "We have no intention of letting you go free to trample on our children, so you'll be staying here"
    "She slides a dog bowl filled with a brown mush into your cell"
    iku "I got you some food"
    iku "Please {i}enjoy{/i} it {i}slowly{/i}"
    s scared "Senpai wait, what's going on?!"
    "Without saying another word, she leaves you alone in the cell"
#   call the platformer code here
#label interaction_menu:
#    if location == "cell_door":
#        call cell_door
#        return
#    elif location == "cell_nolia":
#        call cell_nolia
#        return
#    elif location == "dog_bowl":
#        call dog_bowl
#        return
#    else:
#        return
label cell_door:
    if cell_key_in_inventory == True:
        "The door is shut tight. Rattling the bars does nothing for you"
        "You put the key into its slot and turn. You push on the door, but it doesn't budge"
        "You then realize its a slidng door, and drag it open"
        $ cell_door_locked = False
        "As you leave the cell, you see a flash of blue on the periphery of your vision"
        "Turning your head to the sight, you see a nearby bush"
        return
    else:
        "The door is shut tight. Rattling the bars does nothing for you"
        return

label cell_nolia:
    if Nolia_Needs_Water == False:
        "In the corner of the cell, you find what looks to be a shriveled wooden ball"
        "As you approach it, you can hear a faint sound"
        "?" "Wa-er"
        $ Nolia_Needs_Water = True
        call water_menu
        return

label water_menu:
    menu:
        "Pour your water on it":
            "You pour the water on the ball"
            "It doesn't seem to do much, until you see it moving"
            "Taking a step back, it begins to rise"
#           show nolia_sapling_sprite
            "It turns around, and does what you can only assume to be stretching"
            "?" "Ah, thanks for that"
            "It wobbles around the cell, before sitting back down"
            "?" "It's been so long since someone came by, I thought I would be a fossil when someone found me"
            call nolia_sapling_menu
            return
        "Do nothing":
            return

label nolia_sapling_menu:
    menu:
        "Ask her name" if petal_name == False:
            "?" "My name? My name..."
            "?" "Hmmm"
            "?" "Well I promise to tell you eventually, but how about you pick a name for me?"
            s "How about Petal, on account of your petals"
            "Petal" "Oh! That sounds lovely! Petal it is then. Pleased to meet you."
            s "My name is Shiki, by the way"
            "Petal" "Oh, I already knew that"
            s scared "What?! How?"
            "Petal" "I err... overheard your friend earlier. Yeah!"
            $ petal_name = True
            jump nolia_sapling_menu
        "Ask her if she knows what is going on" if petal_knows == False:
            if petal_name == True:
                "Petal" "Well you see, I was minding my own business"
                "Petal" "Just tending to the garden, you know"
                "Petal" "La la la la~ and all that when this guy comes up to me, all banged up"
                "Petal" "Poor guy looked like he was in pain, so I was taking care of him. Few weeks later..."
                "Petal" "BAM!"
                "Petal" "Boxes me head in, left me dazed on the ground."
                "Petal" "I come to and I'm stuck in this cell."
                $ petal_knows = True
                jump nolia_sapling_menu
            if petal_name == False:
                "?" "Well you see, I was minding my own business"
                "?" "Just tending to the garden, you know"
                "?" "La la la la~ and all that when this guy comes up to me, all banged up"
                "?" "Poor guy looked like he was in pain, so I was taking care of him. Few weeks later..."
                "?" "BAM!"
                "?" "Boxes me head in, left me dazed on the ground."
                "?" "I come to and I'm stuck in this cell."
                $ petal_knows = True
                jump nolia_sapling_menu
        "Ask her what to do next" if petal_name == petal_knows == True:
            s "Any ideas on how to get out of here?"
            "Petal" "I heard your friend from earlier. Sounds like she left something behind to help us escape."
            s "She left some brown mush"
            "Petal" "Maybe something is in the mush?"
            $ nolia_hint = True
            return

label dog_bowl:
    "It's a plastic bowl with some brown mush. It doesn't smell like much, but it looks unappetizing"
    if nolia_hint == True:
        menu:
            "Take a bite?"
            "Yes" if food_count == 0:
                "Your stomach rumbles"
                "You have no idea when food will come again, so you take a bite"
                "And immediately spit it back out"
                s scared "Oh God, this is disgusting! Its so mushy"
                $ food_count += 1
                jump dog_bowl
            "Continue eating" if food_count == 1:
                "You continue shoveling the goop into your mouth, struggling to swallow and keep the vile concoction down"
                $ food_count += 1
                jump dog_bowl
            "Continue eating" if food_count == 2:
                "Eventually, you bite into something solid"
                "You pull a small metal key from your mouth"
                s scared "Oh thank God!"
                s scared "I thought I was going to pass out from how terrible that was"
                "Petal" "Why didn't you just dig through the bowl, I don't think you had to eat anything"
                s scared "..."
                "You quickly go to unlock the cell doors"
                $ Nolia_in_party = True
                return
            "No":
                return
    else:
        return

label wetty_encounter:
    "Petal" "Not to alarm you Shiki but I think we're being followed. Just don't look behi-"
    s scared "WE'RE BEING FOLLOWED?!"
    "You immediately turn around just in time to see a blue blob go into a nearby bush"
    "Petal" "Maybe we should leave while we still have the chance."
    $ wetty_encountered = True
    return

label Wetty:
    "As you approach the bush, you notice a blue blob sticking out of the bush"
    "Petal" "What do you think it is?"
    s "I dont know..."
    s "Let's find out!"
    "Petal" "Wait!{nw}"
    menu:
        "Slap it":
            $ wetty = "slap"
            pass
        "Poke it":
            $ wetty = "poke"
            pass
    "Taking your chance, you [wetty] it."
    voice "audio/Ikumin/WetFloor/Wetty1.wav"
    "Wetty" "AAAHHHHHH"
    "The blue blob screams out, and emerges from the bushes."
    voice "audio/Ikumin/WetFloor/Wetty2.wav"
    "Wetty" "What was that for?!"
    "In front of you seems to be some sort of slime creature that seems to be constantly melting."
    s scared "Sorry!"
    s scared "I didn't know what it was-"
    voice "audio/Ikumin/WetFloor/Wetty3.wav"
    "Wetty" "{b}SO YOU JUST HIT ME?!{/b}"
    s scared "I didn't mean to!"
    voice "audio/Ikumin/WetFloor/Wetty4.wav"
    "Wetty" "Wait"
    "The blob regains her composure and looks you up and down"
    "Wetty" "You're the dog that was talking to Hime earlier."
    "Wetty" "What have you done with her?"
    "Wetty" "I swear if you've hurt her..."
    "She starts hopping around and shadowboxing, before taking in the height difference between the two of you."
    "Wetty" "I'll punch your knees!"
    "She jabs the air in front of you"
    "Petal" "Calm down there. We're friends. I think."
    s "Hime?"
    "Wetty" "Yes! Hime. The most beautiful, funny and sexy woman to have graced our planet! She's my owner but don't tell her I said that."
    "Her eyes begin sparkling"
    s "Hime..."
    "Suddenly you think of someone"
    s happy "Oh! You mean Iku-senpai!"
    "Wetty" "Yes!"
    "She jumps up in joy at the mention of Iku's name"
    s "Well, I think she is being held captive. Do you think you could help me save her?"
    "Wetty" "As if you had to ask! We should find the other Ikumin"
    $ renpy.notify("Wetty has joined your party")
    $ Wetty_in_party = True
    return

label Rei:
    "You find another jail cell"
    "Inside is a pink blob with a harmonica"
    "Wetty" "Mama!"
    "Rei" "Wetty!"
    "The cookie looking blob comes to the cell door"
    "Rei" "You should get out of here while you can. The mushrooms could be back at any time"
    "Wetty" "We have something more important though"
    "You are about to ask about Iku's location when Wetty continues her thought"
    "Wetty" "Why are you playing the harmonica?"
    "Rei" "Pretty neat, huh?"
    "He plays a sour note"
    "Rei" "I figured since I was stuck in this cell, you know how they're always playing the harmonica on TV, when they're in jail?"
    s "Wait, that's not important! We need to find Iku!"
    "Rei" "Well, I'd help you but"
    "He shakes the cell door for effect"
    "Rei" "I'm stuck in here"
    s "Do you know how we can get you out?"
    "Rei" "Hmmm. I heard Wall said he was going to look for a key, but he hasn't come back yet. Maybe try finding him?"
    return

label Rei_Jailed:
    "Rei" "Did you find the key yet?"
    if rei_key_in_inventory:
        "Rei" "Thanks for getting me out of there!"
        "He happily shakes your hand as a sign of thanks"
        "As you regain your hand, you smell a faint scent of cookies emanating from your hand"
        "You suddenly get hungry"
        "Rei" "So where's Wall?"
        "You pull out the letter and show it to him"
        "Rei" "I see..."
        "He hands you back the letter"
        s "So what's it say?"
        "Rei" "No idea. I don't speak German"
        "Wetty grabs the note."
        "Wetty" "It says he's broken out and will meet up with us later"
        "Rei" "You know German?"
        "Wetty" "Nein!"
        "Wetty" "Let's hurry up and save Hime!"
        s happy "You're right, we can't keep them waiting"
        "Rei" "I'm right behind you"
        "Wetty" "No!{nw}"
        "Wetty" "I want to beat up the mushrooms so Hime will praise me!"
        "Rei" "Hime already praises you Wetty"
        "Wetty" "Well...{w} I want more"
        $ renpy.notify("Rei has joined your party")
        $ Rei_in_party = True
        return
    else:
        "You are still missing the key to this cell."
        return

label Wall_jailed:
    "While searching for the last Sunflower, you come across an empty cell"
    "Searching the cell, all you can find is a letter"
    centered """
    Eh Jo, wenn ihr das hier lesen könnt, haben mich die penner in ne neue zelle gebraucht... die Pisser.\n    Ich hab ne paar sachen da gelassen damit ihr ihr mich findet könnt.\n    Null ahnung ob die Pilze englisch können also schreib ich einfach in Deutsch\n    Ich glaube an euch Sonnenblumen! Viel Glück
    """
    "Attached to the back of the letter is a key"
    $ renpy.notify("You have found a cell key")
    $ rei_key_in_inventory = True
    "You have no idea what the letter says, so you stash it away"
    return

label Wall_found:
    "As you search the room where the letter once was, you hear a voice come from behind"
    "Wall" "Jo!"
    "As you turn towards the source of the sound, you notice that two of your companions have gone to hug the red blob"
    "Wall" "Hello Rei, hello daughter"
    "Wetty" "Hi Father!"
    "Rei" "Hey Wall"
    "Wall" "You guys found the letter I left!"
    s "Yeah! Thanks for getting us that key, it saved us some trouble"
    "Wall" "Have you all found my Hime yet?"
    "Rei" "You mean {i}our{/i} Hime?"
    "Wall shoots a glare at Rei"
    "Wetty" "No, we haven't found her yet, but there's probably only a few more places to check"
    "Wall" "Then let's go! No point in wasting time here"
    $ renpy.notify("Wall has joined your party")
    $ Wall_in_party = True
    return

label nolia_drrdrrdrr:
    "Petal" "Oh it's pretty comfy here."
    s "I don't want to leave you behind."
    "Petal" "Don't worry about it! I'll just be right here"
    s "What if its a trap?"
    "Petal" "I dont think so. I can feel it! This is my hole! This is the hole that was meant for me!"
    "Petal" "Yawns"
    "Petal" "I haven't felt so relaxed in a long while. I'll catch up with you after a short nap."
    $ renpy.notify("Petal has left your party")
    return
    
label nolia_tree:
    "Petal is rooted in the ground"
    "She looks serene and peaceful"
    "It's best to leave her be"
    return

label iku_saved:
    "Sunflowers" "Hime!"
    iku "Ikumins?! How did you get out of your cages?"
    "Wall" "Shiki helped us escape!"
    "Wetty" "Hey, I helped too! Praise me!"
    "Rei" "You ran away as soon as everything started!"
    "Wetty" "I was just waiting for the right moment. No point in getting us all caught"
    iku "Thank you Shiki-chan for saving the ikumins!"
    iku "Did you find an exit? I'll catch up with you all after you escape"
    iku "Hurry! We don't have a lot of time"
    s "We won't leave with you Senpai!"
    "King" "Well, well, if it isn't the misfits and their mangy dog!"
    s "Mangy?!"
    s "I'll have you know I shower everyday!"
    "King" "A dog is a dog, and you should know your place!"
    "Now darling, let's not get caught up in bad company"
    "The guards will be here to take care of them"
    "The trio emerge behind the king"
    "Wall" "Thanks for keeping him distracted"
    "Ikumins attack!"
    "The three of them attempt to subdue the king, but are quickly thrown off"
    "They scuttle to Iku's side, and look up at her"
    "Rei" "I guess it's time for our last resort"
    "Wetty gives Iku a look of childlike innocence and acceptance"
    "Wetty" "Do what you must Hime"
    "Iku nods, and the bends down and scoop the ikumin into her free arm"
    iku "Wall-E furifuri, YEET!"
    "She tosses Wall at the unsuspecting king"
    "Wall" "FOR HIME!"
    "A loud thwack is heard when he collides"
    "King" "What is this?"
    iku "Rei Nana furifuri, YEET!"
    "She tosses Rei next"
    "Rei" "FOR HIME!"
    "Another thwacking sound is heard when the two collide"
    "King" "Cease this tomfoolery at once!"
    iku "Wetty furifuri, YEET!"
    "A soft plapping noise is heard when she lands on him"
    "She slowly oozes down and falls to the floor"
    "King" "Disgusting"
    "This is no way for a future queen to act"
    "Now, if you're done, we have more important matters to tend to"
    s "Hold it right there, buster!"
    "Iku steps behind you and puts a hand on your shoulder"
    "You turn your head"
    s "Don't worry Iku-senpai! I'm part guarddog!"
    iku "I'm sorry for this Shiki-chan."
    "Iku picks you up by the waist."
    s scared "S-senpai?!"
    iku "Thank you Shiki-chan! OtsuFuri! YEET!"
    "The world flashes by you as you are sent flying towards the king."
    "A loud {b}CRACK!{/b} is all you hear before things turn dark."
    pause 3.0
    "When you come to, you find yourself being tended to by a tiny sapling."
    "It notices you wake up, and leaves the room that you are in"
    "As you sit up, you hear a familiar voice"
    "Petal" "Ah Shiki! Thanks for getting rid of the mushroom guy."
    "Wha? Who- who are you?"
    "Petal" "It's me Shiki!"
    "P-petal? I must have died, I dont remember you being this pretty"
    "Petal" "P-pretty? Huh? Buh, hu-bubu!"
    "Petal clears her throat."
    "Petal" "I just wanted to thank you and your friends before you left. Thanks for helping me get the forest back to normal!"
    "Petal" "So now that everything is dealt with, I should tell you the truth. For starters, my name is actually Nolia, and I may have started all this by insulting the little dude's cooking."
    "Nolia" "Gregory should have cleared the hill of the remaining fungus by now, you all should be able to leave."
    "Nolia" "Buh-bye! Feel free to visit!"
    return

label iku_party_menu:
    menu:
        "Speak with Hylo":
            call iku_hylo_menu
            jump iku_party_menu
        "Speak with Petal" if Nolia_in_party == True:
            call nolia_noises
            jump iku_party_menu
        "Return":
            return

label iku_hylo_menu:
    menu:
        "Ask Hylo for advice":
            jump iku_hylo_menu
            pass
        "Return":
            return

label nolia_noises:
    menu:
        "I may have forgotten what I originally intended these lines to be used for, so have a free soundboard for Nolia noises"
        "Ask her what to do next":
            "Petal" "I don't know what to do. Maybe we should look around some more."
            jump nolia_noises
            pass
        "Alternate line":
            "Petal" "There was one thing that caught my interest."
            jump nolia_noises
            pass
        "Idea Accepted":
            "Petal" "You got it!"
            jump nolia_noises
            pass
        "Idea Rejected":
            "Petal" "No, I don't think so."
            jump nolia_noises
            pass
        "Return":
            return