# import sys
# import pygame
# from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYUP

# pygame.init()





# class Character(pygame.sprite.Sprite):

#     ACTIONS = [
#          'Idle', 'Dead', 'Jump', 'Run', 'Slide'
#               ]

#     def __init__(self, action='Idle', x=400, y=100, frame=0):
#         super().__init__()
#         self.rect = pygame.Rect((0, 0), (588, 600))
#         self.action = action
#         self.x = x
#         self.y = y
#         self.frame = frame
#         self.deltatime = 0
#         self.direction = 1       

#     def left(self):
#         self.x -= 10
#         self.action = 'Run'
#         self.direction = -1

#     def right(self):
#         self.x += 10
#         self.action = 'Run'
#         self.direction = 1
        
#     def stand(self):
#         self.y = 100
#         self.action = 'Idle'
        
#     def slide(self):
#         if self.direction == -1:
#             self.x -= 13
#             self.y = 200
#             self.action = 'Slide'
            
#         elif self.direction == 1:
#             self.x += 13
#             self.y = 200
#             self.action = 'Slide'
            
#     def jump(self):
#         self.y -= 20
#         self.y = 20
#         self.action = 'Jump'
        
#     def dead(self):
#         self.action = 'Dead'
        
        

#     def update(self, deltatime):
#         self.deltatime += deltatime
#         if self.deltatime >= 30:
#             self.deltatime -= 30
#             self.frame = (self.frame+1)%10

#     def blit(self, screen):
#         image = pygame.image.load("cutegirlfiles/png/Run (1).png")
#         self.rect = self.image.get_rect()  # รับค่า rect ของภาพตัวละคร
#         self.rect.topleft = (300, 250)  # ตำแหน่งเริ่มต้นของตัวละคร
#         if  self.direction == -1:
#             image = pygame.transform.flip(image, True, False)
#         self.rect.topleft = self.x, self.y
#         screen.blit(image, self.rect)
        
# clock = pygame.time.Clock()        
# screen_width = 1100
# screen_height = 700
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Test game")
# background = pygame.image.load("pygame/picture/bg.jpg")
# bg_rect = background.get_rect()
# font = pygame.font.Font('pygame/NotoSerifThai.ttf/static/black.ttf', size=50)
# background = pygame.transform.scale(background, (screen_width, screen_height))
# player = Character()
# game_over = False   
# animation = None

     
# while not game_over:
    
#     screen.blit(background, (0, 0))  
#     pygame.display.update() 
    

#     for event in pygame.event.get():              
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
                           
#         if event.type == KEYUP:
#             player.stand()
            
            
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_LSHIFT] or keys[pygame.K_SPACE]:
#         if keys[pygame.K_a]:
#             player.left()
#         if keys[pygame.K_d]:
#             player.right()
#         if keys[pygame.K_LSHIFT]:
#             player.slide()
#         if keys[pygame.K_SPACE]:
#             player.jump()
#     elif keys[pygame.K_k]:
#             player.dead()
            
    
# screen.blit(background, bg_rect)
# text = f'{clock.get_fps():.2f} FPS'
# msg = font.render(text, True, (0,150,0))
# screen.blit(msg, msg.get_rect())
# player.blit(screen)
# deltatime = clock.tick(60)
# player.update(deltatime)
# if animation: 
#     animation.update(screen, deltatime)
# pygame.display.update()


import sys
import pygame
from pygame.locals import QUIT, KEYUP

pygame.init()

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"pygame/cutegirlfiles/png/Run (1).png")  # โหลดภาพตัวละคร
        new_width = 100  # ขนาดใหม่ของความกว้าง
        new_height = 100  # ขนาดใหม่ของความสูง
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()  # รับค่า rect ของภาพตัวละคร
        self.rect.topleft = (500, 569)  # ตำแหน่งเริ่มต้นของตัวละคร
        

    def left(self):
        self.rect.x -= 10

    def right(self):
        self.rect.x += 10

    def stand(self):
        self.y = 100
        self.action = 'Idle'
        
            
    def jump(self):
        self.y -= 20
        self.y = 20
        self.action = 'Jump'
        
    def dead(self):
        self.action = 'Dead'

class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()

    def update(self, screen, deltatime):
        pass

    def draw(self, screen):
        pass

clock = pygame.time.Clock()
screen_width = 1100
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test game")
background = pygame.image.load("pygame/picture/bg.jpg")
bg_rect = background.get_rect()
font = pygame.font.Font(None, 36)
background = pygame.transform.scale(background, (screen_width, screen_height))
player = Character()
game_over = False
animation = Animation()

while not game_over:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_LSHIFT] or keys[pygame.K_SPACE]:
        if keys[pygame.K_a]:
            player.left()
        if keys[pygame.K_d]:
            player.right()
        if keys[pygame.K_LSHIFT]:
            player.slide()
        if keys[pygame.K_SPACE]:
            player.jump()
    elif keys[pygame.K_k]:
            player.dead()

    screen.blit(background, bg_rect)
    player_rect = screen.blit(player.image, player.rect)
    animation.draw(screen)
    text = f'FPS: {clock.get_fps():.2f}'
    fps_text = font.render(text, True, (0, 255, 0))
    screen.blit(fps_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
