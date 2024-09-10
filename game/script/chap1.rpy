label story1:
    scene black with dissolve
    show grannychar at left with moveinleft
    gran "Hello my child"
    show sischar at right with moveinright
    sis "Hello granny"
    sis "Such a good day right"
    gran "It would have been a better day if there was rain my child..."
    $points=points+30
    jump retry
    
    if points>50: #out of 100
        jump passed
    elif points>25:
        jump retry
    else:
        jump game_over