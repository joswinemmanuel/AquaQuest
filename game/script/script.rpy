# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define points=0
define only_game_var = False

label splashscreen:
    scene black
    with Pause(1)

    show text "{b}Tech Titans Presents{/b}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "{b}{i}Aqua-Quest{/i}{/b}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return

#blur fn
image devchar = At('dev', sprite_highlight('dev'))

image grannychar = At('granny', sprite_highlight('granny'))

image sischar main= At('sis main', sprite_highlight('eileen'))
image sischar = At('sis', sprite_highlight('eileen'))

image brochar main= At('bro main', sprite_highlight('keith'))
image brochar = At('bro', sprite_highlight('keith'))

image userchar = At('no_char', sprite_highlight('me'))

image santachar = At('santa', sprite_highlight('santa'))
image santachar_shadow = At('santa_shadow', sprite_highlight('santa'))


image bullychar = At('bully', sprite_highlight('bully'))

image mrsgraychar = At('mrsgray', sprite_highlight('mrsgray'))

image storeownerchar = At('storeowner', sprite_highlight('storeowner'))

image mrwickchar = At('mrwick', sprite_highlight('mrwick'))

#char intro
define dev = Character("Dev",image='devchar',callback=name_callback, cb_name='dev')
define Granny = Character('Granny')
define gran = Character("Granny",image='granchar',callback=name_callback, cb_name='granny')
define sis = Character("Eileen",image='sischar',callback=name_callback, cb_name='eileen')
define bro = Character("Keith",image='brocahr',callback=name_callback, cb_name='keith')
define user = Character("Me",image='userchar',callback=name_callback, cb_name='me')
define santa = Character("Santa",image='santachar',callback=name_callback, cb_name='santa')
define bully = Character("Bully", image='bullychar',callback=name_callback, cb_name='bully')
define storeowner = Character("Store Owner", image='storeownerchar',callback=name_callback, cb_name='storeowner')
define mrsgray = Character("Mrs.Gray", image='mrsgraychar',callback=name_callback, cb_name='mrsgray')
define mrwick = Character("Mr.Wick", image = 'mrwickchar', callback=name_callback, cb_name='mrwick')


# The game starts here.

label start:
    $points = 0

    scene bg_dev with advtrans1
    show devchar with moveinright

    dev "Oh, Hey there. Welcome to Aqua-Quest"
    dev "A game made for the sole purpose of teaching children about water management!!"
    dev "Enjoy the graphic contents and the mini-games!!"
    dev "It is also advised to wear earphone for immersed gameplay"
    menu:
        dev "Before we start would you like to [points]:"

        "Progress Only with the Games":
            $only_game_var=True
            jump only_games

        "Progress Along with Story Mode":
            pass

    scene bg_village with dissolve
    show brochar at right with moveinright
    bro "Grandma, why is the well running dry? It’s so hot, and everyone looks worried!"
    show grannychar at left with moveinleft
    gran "I know, dear. The sun is relentless this summer, and we need to be careful with how we use our water. It's a real lesson for all of us."
    bro "But what can we do to help? It feels like everyone is just waiting for the water to come back."
    gran "Well, we can start by showing them how to conserve water. Small changes can make a big difference. Are you up for the challenge?"
    bro "Absolutely! Let’s do something fun to get everyone excited about saving water!"
    gran "That's the spirit, Keith! Together, we’ll turn this challenge into an adventure."

    scene rain with dissolve
    show grannychar at right with moveinright
    gran "Oh, it looks like it might rain soon! Let’s get the rain barrels ready, shall we?"
    show sischar at left with moveinleft
    sis "Rain barrels? Why do we need those, Grandma? Isn’t there plenty of water in the well?"
    gran "Not today, my dear. We’ll use the rainwater to water the plants and wash up later. Every drop counts, especially now that the well is running low."
    sis "But it’s just rain. How can that help us?"
    gran "Every time it rains, we can collect enough water to last us for days. It’s like nature’s gift."
    sis "I see! Can I help?"
    gran "Of course! You can hold the funnel while I position the barrels."
    sis "Yay! Let’s catch that rain!"

    jump fish_catcher
    label s1:
        pass
    
    show sischar at left with moveinleft
    sis "Look, Grandma! We got so much rainwater!"
    gran "Yes, we did, darling. It’s all because we took the time to collect it."


    scene bg_river with dissolve
    show grannychar at left with moveinleft
    gran "Look at this mess. People forget that littering here affects our water supply."
    show sischar at right with moveinright
    sis "But it’s just a little garbage. It won't make that much difference, right?"
    gran "Every little bit adds up. See all this? It ends up in the river and makes the water dirty. If we clean it up, we help our river stay healthy."
    sis "Alright, I’ll help! This looks bad."
    gran "Thank you, sweetheart! Remember, clean water is precious. If we don’t take care of it, we won’t have it when we need it."
    sis "I’ll tell my friends to help next time too!"

    jump waste_game
    label s2:
        pass

    scene bg_river with dissolve
    show grannychar at left with moveinleft
    gran "Oh dear, look at this! What a waste of water!"
    show sischar at right with moveinright
    sis "What can we do, Grandma?"
    gran "We need to connect these broken pipes—the water that’s leaking here could fill our barrels many times!"
    sis "But it looks complicated. Can we fix it?"
    gran "Of course, we can try! It may take some work, but working together is the best way to learn."
    sis "Let’s do it! I want to help save the water!"
    gran "That’s the spirit. Remember, every effort we make today ensures we'll have clean water for tomorrow!"

    #jump game
    label s3:
        pass

    scene drought with dissolve
    show sischar at right with moveinright
    show grannychar at left with moveinleft
    sis "And we cleaned the river and fixed the pipes. I get it now! Water is super important!"
    gran "Exactly! It’s our responsibility to conserve it."
    sis "I’m going to tell everyone in the village how we can save water!"
    gran "That’s wonderful! We can all be guardians of our precious water. Let's promise to keep learning and sharing what we know."
    sis "I promise, Grandma! Together, we’ll make a difference!"

    jump story1

