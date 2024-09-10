#blinking transition

transform blink:
    "eye_half.png"
    .1
    "eye_close.png" 
    .1
    "eye_open.png"
    .2
    "eye_half.png"
    .1
    "eye_close.png"
    .1
    "eye_open.png"
    .2
    "eye_half.png"
    .1
    "eye_close.png"
    .1
    "eye_open.png"
    alpha 0.0

#######################################################################################################################################
#auto-blurring and auto-speech

define sprite_focus = {}
default speaking_char = None

transform sprite_highlight(sprite_name):
    function SpriteFocus(sprite_name)

define sounds = ['audio/type/A1.ogg', 'audio/type/A2.ogg', 'audio/type/A3.ogg', 'audio/type/A4.ogg', 'audio/type/A5.ogg', 'audio/type/B1.ogg', 'audio/type/B2.ogg', 'audio/type/B3.ogg', 'audio/type/B4.ogg', 'audio/type/B5.ogg']
define sounds2 = ['audio/type/A5.ogg', 'audio/type/B4.ogg', 'audio/type/B5.ogg']

init -10 python:
    import math

    def name_callback(event, interact=True, name=None, **kwargs):
        global speaking_char
        if event == "begin":
            speaking_char = name
        if event == "show":
            renpy.sound.queue(renpy.random.choice(sounds2), loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    class SpriteFocus(object):
        def __init__(self, char_name):
            self.char_name = char_name

        def __call__(self, trans, start_time, anim_time):
            def get_ease(t):
                return .5 - math.cos(math.pi * t) / 2.0

            global sprite_focus, speaking_char
            char_name = self.char_name

            if char_name not in sprite_focus:
                sprite_focus[char_name] = False
            anim_length = 0.2       # How long (in seconds) the animation will last
            bright_change = 0.5   # How much the brightness changes
            sat_change = 0.2        # How much the saturation changes
            zoom_change = 0.0025    # How much the zoom changes
           
            y_change = 1

            is_talking = speaking_char == char_name

            if isinstance(sprite_focus[char_name], (int, float)) and anim_time < sprite_focus[char_name]:
                sprite_focus[char_name] = is_talking
            if sprite_focus[char_name] != is_talking and isinstance(sprite_focus[char_name], bool):
                sprite_focus[char_name] = anim_time
                if renpy.is_skipping() or renpy.in_rollback():
                    sprite_focus[char_name] = is_talking

            curr_time = max(anim_time - sprite_focus[char_name],0) 
            curr_ease = 1.0
            if curr_time < anim_length and not isinstance(sprite_focus[char_name], bool):
                curr_ease = get_ease(curr_time/anim_length)
            else:
                sprite_focus[char_name] = is_talking
            if is_talking:
                trans.matrixcolor = SaturationMatrix((1.0-sat_change) + curr_ease * sat_change) * BrightnessMatrix(-bright_change + curr_ease * bright_change)
                trans.zoom = min(curr_ease * zoom_change + (1.0-zoom_change), 1.0)
                trans.yoffset = y_change - curr_ease * y_change 
            else:           
                trans.matrixcolor = SaturationMatrix(1.0 - curr_ease * sat_change) * BrightnessMatrix(curr_ease * -bright_change)
                trans.zoom = max(1.0 - curr_ease * zoom_change, (1.0-zoom_change))
                trans.yoffset = y_change * curr_ease            
            return 0

#######################################################################################################################################
#interactable map

screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")

label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map/bg_map.png"

    imagebutton:
        xpos 671
        ypos 316
        idle "map/santa_idle.png"
        hover "map/santa_hover.png"
        action Jump("end")

    imagebutton:
        xpos 1448
        ypos 746
        if L1complete==False:
            idle "map/L1_idle.png"
            hover "map/L1_hover.png"
        else:
            idle "map/L1_idle.png"
            hover "map/L1_hover.png"
        action Jump("L1")
        
    imagebutton:
        xpos 1475
        ypos 232
        if L2complete==False:
            idle "map/L2_idle.png"
            hover "map/L2_hover.png"
        else:
            idle "map/L2_idle.png"
            hover "map/L2_hover.png"
        action Jump("L2")

    imagebutton:
        xpos 415
        ypos 754
        if L3complete==False:
            idle "map/L3_idle.png"
            hover "map/L3_hover.png"
        else:
            idle "map/L3_idle.png"
            hover "map/L3_hover.png"
        action Jump("L3")

#######################################################################################################################################
#advanced transition

init:
    $ advtrans1 = ImageDissolve("images/transition/038.jpg", 1.0, 8) #dev interaction
    $ advtrans3 = ImageDissolve("images/transition/19.jpg", 1.0, 8) #lvl start
    $ advtrans4 = ImageDissolve("images/transition/12.jpg", 1.0, 8) #lesson start n end
    $ advtrans5 = ImageDissolve("images/transition/20.jpg", 1.0, 8) #after before game
    $ advtranssnake = ImageDissolve("images/transition/snake2.png", 1.0, 8) 
    $ advtransbite = ImageDissolve("images/transition/bites.jpg", 1.0, 8) #snacks break

#######################################################################################################################################
#pointer cursor

init:
    $ config.mouse = {
        'default' : [ ( "gui/cursor/cursor_idle.png", 0, 0) ],
        'pressed_default' : [ ( "gui/cursor/cursor_click.png", 0, 0) ],
        "button" : [ ( "gui/cursor/cursor_idle.png", 0, 0) ],
        'pressed_button' : [ ( "gui/cursor/cursor_click.png", 0, 0) ],
    }


#######################################################################################################################################
#snowfall

init python:
    
    import random
    
    random.seed()
    
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    class SnowFactory(object):
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):

            self.max_particles = max_particles
            
            self.speed = speed
            
            self.wind = wind
            
            self.xborder = xborder
            self.yborder = yborder
            
            self.depth = kwargs.get("depth", 10)
            
            self.image = self.image_init(image)
            

        def create(self, particles, st):

            if particles is None or len(particles) < self.max_particles:
                
                depth = random.randint(1, self.depth)
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                self.speed*depth_speed,  # the vertical speed of the particle
                random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                random.randint(self.yborder[0], self.yborder[1]), # vertical border
                ) ]
        
        
        def image_init(self, image):

            rv = [ ]
            
            for depth in range(self.depth):
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):

            return self.image
            
    class SnowParticle(object):

        def __init__(self, image, wind, speed, xborder, yborder):
            
            self.image = image
            
            if speed <= 0:
                speed = 1
                
            self.wind = wind
            
            self.speed = speed

            self.oldst = None
                      
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None
                
            return int(self.xpos), int(self.ypos), st, self.image


##################################################################################################################################################
#