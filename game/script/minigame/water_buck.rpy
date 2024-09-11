init:
    image bg background = im.Scale("images/bucket_minigame/background1.jpg", 1920, 1080)
    
    python:
        import random
        import pygame
                
        class Fish():
            def __init__( self ):
                self.image = Image( "images/bucket_minigame/water1.png" )
                self.active = False
                self.dimensions = [ 100, 150 ]
                self.position = [ 0, 0 ]
                self.speed = [ 0, 10 ]
                self.maxY = 700
            # __init__
            
            def createNew( self ):
                self.position[0] = random.randrange( 2, 18 ) * 100
                self.position[1] = 2 - self.dimensions[1]                  # Start off-screen
                self.speed[1] = random.randrange( 2, 10 )
                self.active = True
            # createNew
            
            def update( self, deltaTime ):
                if ( self.active ):
                    self.position[1] += self.speed[1]
                
                if ( self.position[1] > self.maxY ):
                    self.active = False
            # update
            
            def isCaught( self, dogPosition, dogDimensions ):
                if ( dogPosition[0] < self.position[0] + self.dimensions[0] and
                        dogPosition[0] + dogDimensions[0] > self.position[0] and
                        dogPosition[1] < self.position[1] + self.dimensions[1] and
                        dogPosition[1] + dogDimensions[1] > self.position[1] ):
                    self.active = False
                    return True
                
                return False
            # isCaught
            
            def render( self, renderer, shownTimebase, animationTimebase ):
                if ( self.active ):
                    r = renpy.render( self.image, 1600, 900, shownTimebase, animationTimebase )
                    renderer.blit( r, ( self.position[0], self.position[1] ) )
            # render 
        # Fish
    
        class Player():
            def __init__( self ):
                self.image = Image( "images/bucket_minigame/bucket1.png" )
                self.dimensions = [ 100, 150 ]
                self.position = [ 500, 750 ]
                self.speed = [ 100, 10 ]
                self.grabCounter = 0
                self.grabCounterMax = 20
                self.action = "NONE"
                self.score = 0
            # __init__
            
            def handleInput( self, action ):
                if ( self.grabCounter <= 0 ):
                    self.action = action
            # handleInput
            
            def update( self, deltaTime ):
                if ( self.grabCounter > 0 ):
                    if ( self.grabCounter > self.grabCounterMax/2 ):
                        self.position[1] -= self.speed[1] * deltaTime
                    else:
                        self.position[1] += self.speed[1] * deltaTime
                        
                    self.grabCounter -= 1
                    if ( self.grabCounter == 0 ):
                        self.position[1] = 750
                        
                else:
                    if ( self.action == "LEFT" and self.grabCounter <= 0 ):
                        self.position[0] -= self.speed[0] * deltaTime
                    
                    elif ( self.action == "RIGHT" and self.grabCounter <= 0 ):
                        self.position[0] += self.speed[0] * deltaTime
                    
                    elif ( self.action == "GRAB" and self.grabCounter <= 0 ):
                        self.grabCounter = self.grabCounterMax
                    
                    # Adjust position - can't go off screen!
                    if ( self.position[0] < 0 ):
                        self.position[0] = 0
                    elif ( self.position[0] > 1850 - self.dimensions[0] ):
                        self.position[0] = 1850 - self.dimensions[0] 
                
                self.action = "NONE"
            # update
            
            def render( self, renderer, shownTimebase, animationTimebase ):
                r = renpy.render( self.image, 1600, 900, shownTimebase, animationTimebase )
                renderer.blit( r, ( self.position[0], self.position[1] ) )
            # render
        # Player
    
        class FishCatcherGame( renpy.Displayable ):
        
            def __init__( self ):
                renpy.Displayable.__init__( self )
                
                # Maybe I'll write a sub-class for this stuff
                self.player = Player()
                
                self.debug = []
                self.counter = 0
                
                self.fish = []
                self.fishCaught = 0
                
                self.lastStart = None   
                self.frameRate = 90
                
                self.clock = pygame.time.Clock()
                self.countdown = 30
                self.milliseconds = 0
                
                self.gameover = False
                self.game_over = False
            # __init__
            
            def event( self, event, x, y, shownTimebase ):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.handleInput( "GRAB" )
                    # Up Key
                    
                    if event.key == pygame.K_LEFT:
                        self.player.handleInput( "LEFT" )
                    # Left Key
                    
                    if event.key == pygame.K_RIGHT:
                        self.player.handleInput( "RIGHT" )
                    # Right Key
                # KEYDOWN
                         
            # event
            
            def update( self, shownTimebase, animationTimebase ):
                delta = self.getDelta( shownTimebase )
                rate = 1000 / self.frameRate
                speedAdjust = delta * rate
                
                if ( self.gameover == False ):
                
                    chance = random.randrange( 0, 20 )
                    if ( chance == 0 and len( self.fish ) < 5 ):
                        fish = Fish()
                        fish.createNew()
                        self.fish.append( fish )
                    
                    removalList = []
                    # TODO: There is probably a more Python-idiomatic way to do this
                    for fish in self.fish:
                        fish.update( 1 )
                        
                        if ( fish.isCaught( self.player.position, self.player.dimensions ) ):
                            self.player.score += 1
                        
                        if ( fish.active == False ):
                            removalList.append( fish )
                    
                    for fish in removalList:
                        self.fish.remove( fish )
                        
                    self.player.update( 1 )
                    
                    if ( self.milliseconds > 1000 ):
                        self.countdown -= 1
                        self.milliseconds = 0
                    
                    self.milliseconds += self.clock.tick_busy_loop( 60 )
                    if ( self.countdown <= 0 ):
                        self.gameover = True
                    
                    # TODO: Remove
                    del self.debug[:]
                    self.debug.append( "Debug" )
                    self.debug.append( "Random: " + str( chance ) )
                    self.debug.append( "Bucket Position: " + str( self.player.position[0] ) + ", " + str( self.player.position[1] ) )
                    for fish in self.fish:
                        self.debug.append( "Water Position: " + str( fish.position[0] ) + ", " + str( fish.position[1] ) + ", Active: " + str( fish.active ) )
                    self.debug.append( "Delta: " + str( delta ) )
                    
                # Run while game is not over
            # update
            
            def render( self, width, height, shownTimebase, animationTimebase ):
                self.update( shownTimebase, animationTimebase )
                renderer = renpy.Render( width, height )
                
                if ( self.gameover == False ):
                    for fish in self.fish:
                        fish.render( renderer, shownTimebase, animationTimebase )
                    
                    self.player.render( renderer, shownTimebase, animationTimebase )
                    
                    counter = 0
                    for debug in self.debug:
                        txt = Text( _( debug ), size=10 )
                        textRender = renpy.render( txt, 800, 600, shownTimebase, animationTimebase )
                        renderer.blit( textRender, ( 0, 10 * counter ) )
                        counter += 1
                else:  # Gameover
                    self.game_over = True # Jump to the game-over label
                                       
                       
                txtScore = Text( _( "Time : " + str( self.countdown ) ), size=20 )
                renderer.blit( renpy.render( txtScore, 1600, 900, shownTimebase, animationTimebase ), ( 1820, 0 ) )
                
                txtScore = Text( _( "Score: " + str( self.player.score ) ), size=20 )
                renderer.blit( renpy.render( txtScore, 1600, 900, shownTimebase, animationTimebase ), ( 1820, 20 ) )
                
                    
                renpy.redraw( self, 0 )
                
                return renderer
            # render

            def is_game_over(self):
                return self.game_over
            
            def per_interact( self ):
                renpy.timeout( 0 )
                renpy.redraw( self, 0 )
            # per_interact
            
            def getDelta( self, shownTimebase ):
                if self.lastStart is None:
                    self.lastStart = shownTimebase
                        
                delta = shownTimebase - self.lastStart
                self.lastStart = shownTimebase
                
                return delta
            # updateRate
        # FishCatcherGame

label fish_catcher:    
    window hide None
    
    scene bg background
    with fade
    
    $ game = FishCatcherGame()
    $ ui.add(game)
    $ ui.interact(suppress_overlay=True, suppress_underlay=True)

    if game.is_game_over():
        jump water_buck_over

label water_buck_over:
    scene bg_white with dissolve
    show grannychar at right with moveinright
    gran "Well done, you've collected [points] points from the mini-game"
    pass
