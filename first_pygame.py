import pygame
import sys 

#creating the screen
pygame.init()
pygame.display.set_caption("first game")
SCREEN_HIGTH = 400
SCREEN_WIDGH = 800
screen = pygame.display.set_mode((SCREEN_WIDGH,SCREEN_HIGTH))
clock = pygame.time.Clock()
font_title = pygame.font.Font("font/Pixeltype.ttf",50)

scoor = 0
passed = 0
player_gravity=0
jumped = 0
game_over = 0

#creating the basic background
img_sky = pygame.image.load("graphics/Sky.png").convert_alpha()
img_ground = pygame.image.load("graphics/ground.png").convert_alpha()

#bringing the objects
img_snail1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
rec_snail1 = img_snail1.get_rect(midbottom = (800,300))
img_player_walk1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
rec_player1_walk1 = img_player_walk1.get_rect(midbottom = (70,300))


#running the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space DOWN")
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_SPACE:
                print("space UP")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not jumped and not game_over :
                print("space UP")
                player_gravity = -20
                jumped = 1

        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(img_sky,(0,0))
    screen.blit(img_ground,(0,300))

    #snail
    if rec_snail1.left < -100:
        rec_snail1.left = 800
        passed = 0
    screen.blit(img_snail1,rec_snail1)
    rec_snail1.left-=5

    #player
    player_gravity+=1
    rec_player1_walk1.bottom += player_gravity
    screen.blit(img_player_walk1,rec_player1_walk1)
    if rec_player1_walk1.bottom > 300:
        rec_player1_walk1.bottom = 300
        jumped = 0
        player_gravity = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and not game_over:
        rec_player1_walk1.left += 4
    if keys[pygame.K_LEFT] and not game_over:
        rec_player1_walk1.left -= 4

    #scoor
    if rec_snail1.right < 70 and not passed :
        scoor += 1
        passed = 1

    #game over 
    if rec_player1_walk1.colliderect(rec_snail1):
        rec_snail1.left+=5
        game_over = 1

        font_title_game_over = pygame.font.Font("font/Pixeltype.ttf",90)
        text_game_over = font_title_game_over.render("GAME OVER ",0,'black')
        rec_game_over = text_game_over.get_rect(center = (400,140))
        screen.blit(text_game_over,rec_game_over)

        text_game_scoor = font_title.render(f"YOUR SCOOR : {scoor} ",0,'black')
        rec_game_scoor = text_game_scoor.get_rect(center = (400,200))
        screen.blit(text_game_scoor,rec_game_scoor)
    
    text_scoor = font_title.render(str(scoor),0,'black')
    rec_scoor = text_scoor.get_rect(center = (750,50))
    pygame.draw.rect(screen,"green",rec_scoor)
    screen.blit(text_scoor,rec_scoor)
    rec_mouse= pygame.Rect(20,20,20,20)
    rec_mouse.center = pygame.mouse.get_pos()
    pygame.draw.ellipse(screen,"gold",rec_mouse,100)

    pygame.display.update()
    clock.tick(60)