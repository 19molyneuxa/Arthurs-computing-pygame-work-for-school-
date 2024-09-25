import pygame
import random

screen = pygame.display.set_mode([1200,800])

icon = pygame.image.load("bob.PNG")
pygame.display.set_icon(icon)

bg = pygame.image.load("nyan.jpg")
bg = pygame.transform.scale (bg,[1200,800])

cat = pygame.image.load("sprite.jpg")
cat = pygame.transform.scale(cat,[100,62])

isjump = False
velocity = 5
mass = 1
##################################################################### player sprite

class Player(pygame.sprite.Sprite):
    def __init__(self):                         #__init__ will make box
        super().__init__()

        self.image = pygame.Surface([100,60])
        self.image = cat
        
        
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        players.add(self)
        global playerx 
        global playery 

        
    def moveup(self):
        isjump = True
    def moveupjump(self):
        self.rect.y -= force 

            
    def movedown(self):
        self.rect.y +=10
        playerx = self.rect.x 
        playery = self.rect.y
        if self.rect.bottom > 800:
            self.rect.bottom = 800
            

            
    def moveleft(self):
        self.rect.x -=10
        playerx = self.rect.x 
        playery = self.rect.y
        if self.rect.left< 0:
            self.rect.left = 0

            
    
    def moveright(self):
        self.rect.x +=10
        playerx = self.rect.x 
        playery = self.rect.y
        if self.rect.right > 1200:
            self.rect.right = 1200

    def gravity(self):
        self.rect.y += 9.8
        playerx = self.rect.x 
        playery = self.rect.y
        if self.rect.bottom > 800:
            self.rect.bottom = 800

    #jumping code 
    
 
##################################################################### sprite groups and induvidual sprites

players = pygame.sprite.Group()
player = Player ()

##################################################################### game loop setup

clock = pygame.time.Clock()
done = False
while not done:
    
    clock.tick(6)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



##################################################################### player 1 inputs

    keys = pygame.key.get_pressed()
               
    if keys [pygame.K_UP]:
        player.moveup()
    if isjump == True:
            force = (1/2)*mass*(velocity**2)
            player.moveupjump()
            velocity = velocity -1
            if velocity < 0:
                mass = -1
            if velocity == -6:
                isjump == False
                velocity = 5
                mass = 1
    pygame.time.delay(10)






            
    if keys [pygame.K_DOWN]:
        player.movedown()
      
    if keys [pygame.K_LEFT]:
        player.moveleft()
    
    if keys [pygame.K_RIGHT]:
        player.moveright()

##################################################################### drawing stuff

    

    screen.blit(bg,(0,0))
    players.draw(screen)
    pygame.display.flip()
    screen.fill((0, 0, 0))
pygame.quit()
        





