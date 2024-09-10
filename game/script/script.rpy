# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label splashscreen:
    scene black
    with Pause(1)

    show text "Team 8 Interactive Productions Presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Rights-Quest" with dissolve
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

    jump story1

    return
