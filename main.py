import pygame
import sys
from pygame.locals import *

def final_screen(win:bool):
        rect_width, rect_height = 900, 700
        rect_x = 0
        rect_y = 0
        


  
        pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_width, rect_height))
        
        if win == True:
            result = font.render("YOU WIN", True, (0, 102, 0))
        else:
            result= font.render("YOU LOSE",True,(102,0,0))
   
        result_rectangle = result.get_rect()
        

        result_rectangle.center = (rect_x + rect_width // 2, rect_y + rect_height // 2)
        

        screen.blit(result, result_rectangle)


pygame.init()

clock = pygame.time.Clock()

window_size = (900, 700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Evil Wizard")
font = pygame.font.Font(None, 44)


player_image = pygame.image.load("idle/idle0.png")
player_x = 250
player_width  = player_image.get_width()
player_height = player_image.get_height()
player_y = 0
player_speed = 0
player_acceleration = 0.2
heart_image= pygame.image.load('heart.png')



tile_image = pygame.image.load("wall/tomb0.png")
tile_width, tile_height = tile_image.get_size()


platforms = [

    pygame.Rect(100, 300, tile_width*10, tile_height),

    pygame.Rect(100, 266, tile_width*2, tile_height),

    pygame.Rect(356, 266, tile_width*2, tile_height),

    pygame.Rect(520, 400, tile_width * 10, tile_height),  

    pygame.Rect(500, 150, tile_width * 7, tile_height),
    pygame.Rect(500, 116, tile_width , tile_height),
    pygame.Rect(692, 116, tile_width , tile_height),
    
    pygame.Rect(50, 600, tile_width * 12, tile_height),
    pygame.Rect(50, 566, tile_width , tile_height),    
    pygame.Rect(402, 566, tile_width , tile_height),   
       # Upper right

]

#gems
gem_img = pygame.image.load('gems/gems0.png')
new_size = (24,24)
gem_image = pygame.transform.scale(gem_img, new_size)
gem_height = gem_image.get_height()
gem_width  = gem_image.get_width()

gems=[
    pygame.Rect(120,230,gem_width,gem_height),

    pygame.Rect(395,230,gem_width,gem_height),

    pygame.Rect(505,83,gem_width,gem_height),

    pygame.Rect(697,83,gem_width,gem_height),

    pygame.Rect(522,367,gem_width,gem_height),

    pygame.Rect(808,367,gem_width,gem_height),

    pygame.Rect(55,533,gem_width,gem_height),

    pygame.Rect(407,533,gem_width,gem_height)

]

#enemies
flame_img = pygame.image.load("flames/flames0.png")
flamesize= (32,32)
flame_image = pygame.transform.scale(flame_img,flamesize)
flame_width= flame_image.get_width()
flame_height = flame_image.get_height()

flames = [
    pygame.Rect(170,266,flame_width,flame_height),
    pygame.Rect(320,266,flame_width,flame_height),
    pygame.Rect(670,366,flame_width,flame_height),
    pygame.Rect(630,366,flame_width,flame_height),
    pygame.Rect(710,366,flame_width,flame_height),
    pygame.Rect(365,566,flame_width,flame_height),
    pygame.Rect(85,566,flame_width,flame_height),
    pygame.Rect(230,566,flame_width,flame_height),
    pygame.Rect(535,116,flame_width,flame_height),
    pygame.Rect(660,116,flame_width,flame_height),
    pygame.Rect(170,266,flame_width,flame_height),
]


moving_left = False
moving_right = False
moving_up = False
score = 0 
lives=3

while True:
    screen.fill((6, 25, 5))

#rendering map
    for p in platforms:
        # Calculate the number of tiles needed to fill the rectangle
        tiles_x = p.width // tile_width
        tiles_y = p.height // tile_height
        
        # Blit the tile images to cover the platform rectangle
        for i in range(tiles_x):
            for j in range(tiles_y):
                screen.blit(tile_image, (p.x + i * tile_width, p.y + j * tile_height))


    new_player_x = player_x
    new_player_y = player_y

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_UP:
                moving_up = True

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


        if event.type == pygame.KEYUP:
        
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_UP:
                moving_up = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    if moving_left:
        if new_player_x>0:
            new_player_x -=4
    if moving_right:
        if new_player_x + player_width < window_size[0]:
            new_player_x +=4
    if moving_up:
        if player_y > 0:
            if player_ground:
               player_speed = -8

    
    
    
    new_player_rect = pygame.Rect(new_player_x,player_y,player_width,player_height)
    x_collision = False

    #...check against every platform
    for p in platforms:

        if p.colliderect(new_player_rect):
            x_collision = True
            break

    if x_collision == False:
        player_x = new_player_x
    player_speed += player_acceleration
    new_player_y += player_speed

    new_player_rect = pygame.Rect(player_x,new_player_y,player_width,player_height)
    
    
    y_collision = False
    player_ground = False
    #...check against every platform
    
    
    
    for p in platforms:

        if p.colliderect(new_player_rect):
            y_collision = True
            player_speed = 0

            if p[1] > new_player_y:
                player_y = p[1]-player_height
                player_ground = True
            break

    if y_collision == False:
        player_y = new_player_y
    
    
    new_player_rect=pygame.Rect(player_x,player_y, player_width,player_height)

    for gem in gems:

        screen.blit(gem_image,(gem.x,gem.y))

        if gem.colliderect(new_player_rect):
            gems.remove(gem)
            score +=1

    new_player_rect=pygame.Rect(player_x,player_y, player_width,player_height)

    for flame in flames:

        screen.blit(flame_image,(flame.x,flame.y))
        if flame.colliderect(new_player_rect):
            lives -= 1
            player_x = 250
            player_y = 0
            player_speed = 0

    screen.blit(player_image, (player_x, player_y))    

    #score
    score_text = font.render('Score = ' + str(score), True, (102,102,0) )
    score_text_rect = score_text.get_rect()
    score_text_rect.topleft = (10,10)
    screen.blit(score_text,score_text_rect) 

    #lives
    a=0
    for life in range(lives):
        screen.blit(heart_image,((300+a,0)))
        a +=50


    if  player_y+player_height >= window_size[1]:
        final_screen(False)
    if lives == 0:
        final_screen(False)
    if score >= 8:
        final_screen(True)

    pygame.display.flip()
    clock.tick(60)
