label retry :
    $points=0
    scene bg_dev with dissolve
    show devchar at center with moveinleft
    dev "So..."
    dev "Unfortunately you have not passed..."
    dev "But since your still young I'll give you a second chance"

    menu:
        dev "What do you do when there is ample rain water?"
        
        "Dance in the rain":
            dev "Well you got sick the next day, too bad"

        "Collect the rain water":
            dev "Well well, you got it right"
            $points=points+10

        "Go sleep under the blanket":
            dev "Got a funny bone huh?"
            dev "Not right tho"
    
    dev "Moving on..."

    menu:
        dev "You finish eating a candy and want to throw away the wrapper..."

        "Throw it into a water body":
            dev "No No No, thats the last thing you should do!!!"

        "Throw it on the ground":
            dev "Why not just throw it into the dustbin then?"

        "Throw it into the dustbin":
            dev "Impressive, that's the right thing to do!!"
            $points=points+10

    dev "Well you got [points]/20"


###################################################################################################################################

label game_over :
    dev "Game Over!!"
    #have not passed with succifienct score
    scene bg_gameover with fade:
        pause (1.0)

###################################################################################################################################

label passed :
    dev "The End!!"
    #succesfully passed with the highscore
    scene bg_end with fade:
        pause (1.0)