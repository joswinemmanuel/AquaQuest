# Declare characters used by this game.
define e = Character("")
image bg background = im.Scale("bg-pond.jpg",1920,1080)
# Define the draggable and droppable images.
image circle = im.Scale("circle.png",100,100)
image triangle = im.Scale("triangle.png",100,100)
image square = im.Scale("square.png",100,100)
image drop_box = im.Scale("drop-box.png",200,200)

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
label start:
    scene bg background  # Show the background image

    # Show the initial drag-and-drop screen
    show screen drag_and_drop

    e "Drag the shapes into the trash can. They will disappear when dropped."

    window hide
    pause
    
    # Wait until all items are dropped
    while not all_items_dropped():
        pause 0.1
        
    # Continue the game after all items are dragged and dropped
    e "Great job! You've dropped all the shapes into the trash can."
    
    return

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
            child "drop_box"
            xpos 1550
            ypos 650
            draggable False
            droppable True
            drag_raise True