label story1:
    scene black with dissolve
    show grannychar at left with moveinleft
    
    if points>50: #out of 75
        jump passed
    elif points>25:
        jump retry
    else:
        jump game_over