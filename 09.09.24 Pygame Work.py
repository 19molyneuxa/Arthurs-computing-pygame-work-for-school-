import pygame
import random

icon = pygame.image.load("bob.PNG")
pygame.display.set_icon(icon)

bg = pygame.image.load("nyan.jpg")
bg = pygame.transform.scale (bg,[1200,800])

cat = pygame.image.load("sprite.jpg")
frog = pygame.image.load("1.png")
bullet = pygame.image.load("big.jpg")


cat = pygame.transform.scale(cat,[100,62])
frog = pygame.transform.scale(frog,[50,50])
bullet = pygame.transform.scale(bullet,[150,30])






run = True 
#bullet spawning position 
playerx = 0
playery = 0
################################################################################################
































################################################################################################







        

###################################################################################################


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
        self.rect.y -= 10 ### change to 19.8 if gravity used 
       
        if self.rect.top < 0:
            self.rect.top = 0
        

            
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
    
 
    



           
#################################################################



   
#####################################################################
































#####################################################################
screen = pygame.display.set_mode([1200,800])

players = pygame.sprite.Group()


#####################################################################

player = Player ()



#####################################################################



clock = pygame.time.Clock()
done = False
while not done:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True





            
    #############################
  
   

  






    
    #############################

   # for x in players:                                     gravity code 
  #      x.gravity()





        
    #############################
    








     
 
  
    keys = pygame.key.get_pressed()
    
                
    if keys [pygame.K_UP]:
       
        player.moveup ()
        
        
        
    if keys [pygame.K_DOWN]:
        player.movedown()
      
       
       

       
    if keys [pygame.K_LEFT]:
        player.moveleft()
    
    if keys [pygame.K_RIGHT]:
        player.moveright()
    ########################        
  

    #######################

 

#####################################################################

    

    screen.blit(bg,(0,0))
    players.draw(screen)
  
  
    pygame.display.flip()
    screen.fill((0, 0, 0))
pygame.quit()
        





