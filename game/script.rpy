﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default points=0

label splashscreen:
    scene black
    with Pause(1)

    show text "{b}Tech Titans Presents{/b}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Aqua-Quest" with dissolve
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

    scene bg_dev with advtrans1
    show devchar with moveinright
    dev "Oh, Hey there. Welcome to Aqua-Quest"
    dev "A game made for the sole purpose of teaching children about water management!!"
    dev "Enjoy the graphic contents and the mini-games!!"
    dev "It is also advised to wear earphone for immersed gameplay"

    scene bg_ with dissolve
    show char with movein
    bro "Grandma, why is the well running dry? It’s so hot, and everyone looks worried!"]
    gran "Yes, dear. This summer’s heat teaches water care."
    bro "What can we do? Everyone's just waiting for rain."
    gran "Let’s show them water conservation. Small steps, big impact."
    bro "Absolutely! Let’s do something fun to get everyone excited about saving water!"
    gran "That's the spirit, Leo! Together, we’ll turn this challenge into an adventure."

    scene bg_ with dissolve
    show char with movein
    gran "Oh, it looks like it might rain soon! Let’s get the rain barrels ready, shall we?"
    sis "Rain barrels? Why do we need those, Grandma? Isn’t there plenty of water in the well?"
    gran "Not today. We'll use rainwater later; every drop counts."
    sis "But it’s just rain. How can that help us?"
    gran "Every time it rains, we can collect enough water to last us for days. It’s like nature’s gift."
    sis "I see! Can I help?"
    gran "Of course! You can hold the funnel while I position the barrels."
    sis "Yay! Let’s catch that rain!"

    scene bg_ with dissolve
    show char with movein
    gran "Look at this mess. People forget that littering here affects our water supply."
    sis "But it’s just a little garbage. It won't make that much difference, right?"
    gran "Every bit helps. Cleaning up keeps the river healthy and clean."
    sis "Alright, I’ll help! This looks bad."
    gran "Thank you, sweetheart! Clean water is precious. If we neglect it, it won’t be there later."
    sis "I’ll tell my friends to help next time too!"

    scene bg_ with dissolve
    show char with movein
    gran "Oh dear, look at this! What a waste of water!"
    sis "What can we do, Grandma?"
    gran "We need to connect these broken pipes—the water that’s leaking here could fill our barrels many times!"
    sis "But it looks complicated. Can we fix it?"
    gran "Of course, we can try! It may take some work, but working together is the best way to learn."
    sis "Let’s do it! I want to help save the water!"
    gran "That’s the spirit. Remember, every effort we make today ensures we'll have clean water for tomorrow!"

    scene bg_ with dissolve
    show char with movein
    sis "Look, Grandma! We got so much rainwater!"
    gran "Yes, we did, darling. It’s all because we took the time to collect it."
    sis "And we cleaned the river and fixed the pipes. I get it now! Water is super important!"
    gran "Exactly! It’s our responsibility to conserve it."
    sis "I’m going to tell everyone in the village how we can save water!"
    gran "That's great! Let's all be water guardians, learning and sharing to protect our precious resource."
    sis "I promise, Grandma! Together, we’ll make a difference!"


    jump story1
