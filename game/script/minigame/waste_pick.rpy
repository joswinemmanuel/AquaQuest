image bg background2 = im.Scale("images/bg/bg-pond.jpg",1920,1080)

# Define the draggable and droppable images.
image circle = im.Scale("images/bg/circle.png",100,100)
image triangle = im.Scale("images/bg/triangle.png",100,100)
image square = im.Scale("images/bg/square.png",100,100)
image drop_box = im.Scale("images/bg/drop-box.png",200,200)

# Initialize store variables for tracking drag-and-drop interactions
init python:
    store.draggable = None
    store.droppable = None

    store.dropped_items = {
        "circle": False,
        "triangle": False,
        "square": False
    }

    def drag_placed(drags, drop):
        if not drop:
            return

        # Record which item was dragged and which drop area it was placed in
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        # Check if the item is successfully placed into the drop box
        if drop.drag_name == "drop_box":
            # Mark the draggable item as dropped
            if store.draggable in store.dropped_items:
                store.dropped_items[store.draggable] = True

        return True

    def all_items_dropped():
        return all(store.dropped_items.values())

# The game starts here.
label waste_game:
    play music "Game.mp3"
    scene bg background2  # Show the background image

    # Show the initial drag-and-drop screen
    show screen drag_and_drop

    show grannychar at left with moveinleft
    gran "Drag the waste into the trash can. They will disappear when dropped."
    hide grannychar with moveinleft

    window hide
    pause
    
    # Wait until all items are dropped
    while not all_items_dropped():
        pause 0.1
        
    # Continue the game after all items are dragged and dropped
    show grannychar at left with moveinleft
    gran "Great job! You've dropped all the shapes into the trash can."
    hide grannychar with moveinleft

    jump waste_over

# Define the drag-and-drop screen
screen drag_and_drop:
    # Define draggable items
    draggroup:
        # Circle
        drag:
            drag_name "circle"
            xpos 130
            ypos 700
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            if not store.dropped_items["circle"]:
                child "circle"

        # Triangle
        drag:
            drag_name "triangle"
            xpos 480
            ypos 750
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            if not store.dropped_items["triangle"]:
                child "triangle"

        # Square
        drag:
            drag_name "square"
            xpos 680
            ypos 720
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            if not store.dropped_items["square"]:
                child "square"

        # Define droppable area (trash can)
        drag:
            drag_name "drop_box"
            xpos 1550
            ypos 650
            draggable False
            droppable True
            drag_raise True
            if not all_items_dropped():
                child "drop_box"

label waste_over:
    scene bg_river with dissolve
    show grannychar at left with moveinleft
    gran "You have done well in collecting all the waste in the river"
    play music "main-menu-music.mp3"
    $points=points+25
    if only_game_var==True:
        jump l2
    else:
        jump s2


