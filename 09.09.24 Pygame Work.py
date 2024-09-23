import pygame
import random

icon = pygame.image.load("bob.PNG")
pygame.display.set_icon(icon)

bg = pygame.image.load("nyan.jpg")
bg = pygame.transform.scale (bg,[1200,800])

cat = pygame.image.load("nyancat-removebg-preview.png")
frog = pygame.image.load("1.png")
bullet = pygame.image.load("big.jpg")


cat = pygame.transform.scale(cat,[100,62])
frog = pygame.transform.scale(frog,[50,50])
bullet = pygame.transform.scale(bullet,[150,30])



################################################################################################
class Minigun (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([80,10])
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        miniguns.add(self)


        
miniguns = pygame.sprite.Group()


################################################################################################
class Wall (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20,800])
        self.image.fill([0,250,0])
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 0
        players.add(self)
    def gravity(self):
        self.rect.y += 0
      

walls = pygame.sprite.Group()







        

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
        

        
    def moveup(self):
        self.rect.y -= 19.8
        if self.rect.top < 0:
            self.rect.top = 0

            
    def movedown(self):
        self.rect.y +=10
        if self.rect.bottom > 800:
            self.rect.bottom = 800

            
    def moveleft(self):
        self.rect.x -=10
        if self.rect.left< 0:
            self.rect.left = 0

            
    
    def moveright(self):
        self.rect.x +=10
        if self.rect.right > 1200:
            self.rect.right = 1200

    def gravity(self):
        self.rect.y += 9.8
        if self.rect.bottom > 800:
            self.rect.bottom = 800

    #jumping code 
    
 
    



bullets = pygame.sprite.Group()
           
#################################################################


class Bullet(pygame.sprite.Sprite):
    def __init__(self,rany,col1,col2,col3):                         #__init__ will make box
        super().__init__()

        self.image = pygame.Surface([20,10])
        self.image = frog
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = rany
        bullets.add(self)
    def move(self):
        self.rect.x +=10














#####################################################################
screen = pygame.display.set_mode([1200,800])

players = pygame.sprite.Group()
rany = random.randint (0,800)
col1 = random.randint (0,250)
col2 = random.randint (0,250)
col3 = random.randint (0,250)
#####################################################################
minigun = Minigun ()
wall = Wall()
player = Player()
player2 = Player()
bullet = Bullet(rany,col1,col2,col3)
#####################################################################



clock = pygame.time.Clock()
done = False
while not done:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True






            
    #############################
    rany = random.randint (0,800)
    col1 = random. randint (0,250)
    col2 = random. randint (0,250)
    col3 = random. randint (0,250)
    Bullet(rany,col1,col2,col3)









    
    #############################
    for b in bullets:
        b.move()
    for x in players:
        x.gravity()





        
    #############################
    collide = pygame.sprite.spritecollide(player, bullets,False)
    for obj in collide:
        obj.rect.x -=15

        
    collide = pygame.sprite.spritecollide(player2, bullets,False)
    for obj in collide:
        obj.rect.x -=15

        
    collide = pygame.sprite.spritecollide(wall, bullets, False)
    for obj in collide:
        pygame.sprite.Sprite.kill (obj)
    








     
 
   # pygame.display.flip()

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
    
    if keys [pygame.K_w]:
        player2.moveup()
        
    if keys [pygame.K_s]:
        player2.movedown()
        
    if keys [pygame.K_a]:
        player2.moveleft()

    if keys [pygame.K_d]:
        player2.moveright()

    #######################

 

#####################################################################

    

    screen.blit(bg,(0,0))
    players.draw(screen)
    bullets.draw(screen)
    walls.draw(screen)
    miniguns.draw(screen)
  
    pygame.display.flip()
    screen.fill((0, 0, 0))
pygame.quit()
        





