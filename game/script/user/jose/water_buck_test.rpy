init:
    image bg background = im.Scale("images/bucket_minigame/background1.jpg", 1920, 1080)
    
    python:
        import random
        import pygame
                
        class Fish():
            def __init__(self):
                self.image = Image("images/bucket_minigame/water1.png")
                self.active = False
                self.dimensions = [100, 150]
                self.position = [0, 0]
                self.speed = [0, 10]
                self.maxY = 700
            
            def createNew(self):
                self.position[0] = random.randrange(2, 18) * 100
                self.position[1] = 2 - self.dimensions[1]  # Start off-screen
                self.speed[1] = random.randrange(2, 10)
                self.active = True
            
            def update(self, deltaTime):
                if self.active:
                    self.position[1] += self.speed[1]
                
                if self.position[1] > self.maxY:
                    self.active = False
            
            def isCaught(self, playerPosition, playerDimensions):
                if (playerPosition[0] < self.position[0] + self.dimensions[0] and
                        playerPosition[0] + playerDimensions[0] > self.position[0] and
                        playerPosition[1] < self.position[1] + self.dimensions[1] and
                        playerPosition[1] + playerDimensions[1] > self.position[1]):
                    self.active = False
                    return True
                
                return False
            
            def render(self, renderer, shownTimebase, animationTimebase):
                if self.active:
                    r = renpy.render(self.image, 1600, 900, shownTimebase, animationTimebase)
                    renderer.blit(r, (self.position[0], self.position[1]))
        
        class Player():
            def __init__(self):
                self.image = Image("images/bucket_minigame/bucket1.png")
                self.dimensions = [100, 150]
                self.position = [500, 750]
                self.speed = [100, 10]
                self.grabCounter = 0
                self.grabCounterMax = 20
                self.action = "NONE"
                self.score = 0
            
            def handleInput(self, action):
                if self.grabCounter <= 0:
                    self.action = action
            
            def update(self, deltaTime):
                if self.grabCounter > 0:
                    if self.grabCounter > self.grabCounterMax/2:
                        self.position[1] -= self.speed[1] * deltaTime
                    else:
                        self.position[1] += self.speed[1] * deltaTime
                    
                    self.grabCounter -= 1
                    if self.grabCounter == 0:
                        self.position[1] = 750
                        
                else:
                    if self.action == "LEFT" and self.grabCounter <= 0:
                        self.position[0] -= self.speed[0] * deltaTime
                    
                    elif self.action == "RIGHT" and self.grabCounter <= 0:
                        self.position[0] += self.speed[0] * deltaTime
                    
                    elif self.action == "GRAB" and self.grabCounter <= 0:
                        self.grabCounter = self.grabCounterMax
                    
                    # Adjust position - can't go off screen!
                    if self.position[0] < 0:
                        self.position[0] = 0
                    elif self.position[0] > 1850 - self.dimensions[0]:
                        self.position[0] = 1850 - self.dimensions[0] 
                
                self.action = "NONE"
            
            def render(self, renderer, shownTimebase, animationTimebase):
                r = renpy.render(self.image, 1600, 900, shownTimebase, animationTimebase)
                renderer.blit(r, (self.position[0], self.position[1]))
        
        class FishCatcherGame(renpy.Displayable):
            def __init__(self):
                renpy.Displayable.__init__(self)
                
                self.background = renpy.display.image.ImageReference("bg background")
                self.player = Player()
                
                self.debug = []
                self.counter = 0
                
                self.fish = []
                self.fishCaught = 0
                
                self.lastStart = None   
                self.frameRate = 90
                
                self.clock = pygame.time.Clock()
                self.countdown = 10
                self.milliseconds = 0
                
                self.gameover = False
                self.game_over = False
            
            def event(self, ev, x, y, st):
                if self.game_over:
                    return True  # Tell Ren'Py to end interaction
                
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_UP:
                        self.player.handleInput("GRAB")
                    elif ev.key == pygame.K_LEFT:
                        self.player.handleInput("LEFT")
                    elif ev.key == pygame.K_RIGHT:
                        self.player.handleInput("RIGHT")
                
                raise renpy.IgnoreEvent()
            
            def update(self, shownTimebase, animationTimebase):
                delta = self.getDelta(shownTimebase)
                rate = 1000 / self.frameRate
                speedAdjust = delta * rate
                
                if not self.gameover:
                    chance = random.randrange(0, 20)
                    if chance == 0 and len(self.fish) < 5:
                        fish = Fish()
                        fish.createNew()
                        self.fish.append(fish)
                    
                    removalList = []
                    for fish in self.fish:
                        fish.update(1)
                        
                        if fish.isCaught(self.player.position, self.player.dimensions):
                            self.player.score += 1
                        
                        if not fish.active:
                            removalList.append(fish)
                    
                    for fish in removalList:
                        self.fish.remove(fish)
                        
                    self.player.update(1)
                    
                    if self.milliseconds > 1000:
                        self.countdown -= 1
                        self.milliseconds = 0
                    
                    self.milliseconds += self.clock.tick_busy_loop(60)
                    if self.countdown <= 0:
                        self.gameover = True
                    
                    # Debug info
                    del self.debug[:]
                    self.debug.append("Debug")
                    self.debug.append("Random: " + str(chance))
                    self.debug.append("Bucket Position: " + str(self.player.position[0]) + ", " + str(self.player.position[1]))
                    for fish in self.fish:
                        self.debug.append("Water Position: " + str(fish.position[0]) + ", " + str(fish.position[1]) + ", Active: " + str(fish.active))
                    self.debug.append("Delta: " + str(delta))
            
            def render(self, width, height, shownTimebase, animationTimebase):
                self.update(shownTimebase, animationTimebase)
                renderer = renpy.Render(width, height)

                bg_render = renpy.render(self.background, width, height, shownTimebase, animationTimebase)
                renderer.blit(bg_render, (0, 0))
                
                if not self.gameover:
                    for fish in self.fish:
                        fish.render(renderer, shownTimebase, animationTimebase)
                    
                    self.player.render(renderer, shownTimebase, animationTimebase)
                    
                    counter = 0
                    for debug in self.debug:
                        txt = Text(_(debug), size=10)
                        textRender = renpy.render(txt, 800, 600, shownTimebase, animationTimebase)
                        renderer.blit(textRender, (0, 10 * counter))
                        counter += 1
                else:  # Gameover
                    self.game_over = True
                    renpy.timeout(2)
                
                txtScore = Text(_("Time : " + str(self.countdown)), size=20)
                renderer.blit(renpy.render(txtScore, 1600, 900, shownTimebase, animationTimebase), (1820, 0))
                
                txtScore = Text(_("Score: " + str(self.player.score)), size=20)
                renderer.blit(renpy.render(txtScore, 1600, 900, shownTimebase, animationTimebase), (1820, 20))
                
                renpy.redraw(self, 0)
                
                return renderer

            def is_game_over(self):
                return self.game_over
            
            def per_interact(self):
                renpy.timeout(0)
            
            def getDelta(self, shownTimebase):
                if self.lastStart is None:
                    self.lastStart = shownTimebase
                        
                delta = shownTimebase - self.lastStart
                self.lastStart = shownTimebase
                
                return delta

# Define a screen for the fish catcher game
screen fish_catcher_screen(game):
    modal True
    
    add game
    
    if game.is_game_over():
        timer 1 action Return()

# Label to start the fish catcher game
label fish_catcher:
    $ game = FishCatcherGame()
    call screen fish_catcher_screen(game=game)
    $ points = game.player.score  # Store the score
    jump water_buck_over

# Label for after the game
label water_buck_over:
    scene bg_white with dissolve
    show grannychar at right with moveinright
    gran "Well done, you've collected [points] points from the mini-game!"
    # Continue with your visual novel...    