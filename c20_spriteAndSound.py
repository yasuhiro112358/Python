import pygame, sys, time, random
# from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
# WINDOWWIDTH = 400
# WINDOWHEIGHT = 400

# VGA size (4 : 3)
# WINDOWWIDTH = 640
# WINDOWHEIGHT = 480

# Gameboy size (10 : 9)
# WINDOWWIDTH = 160
# WINDOWHEIGHT = 144

# # Gameboy Advance size (3 : 2)
# WINDOWWIDTH = 240
# WINDOWHEIGHT = 160

# # Nintendo DS size (4 : 3)
WINDOWWIDTH = 256
WINDOWHEIGHT = 192

# Nintendo switch size (16 : 9)
# WINDOWWIDTH = 1280
# WINDOWHEIGHT = 720




windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

# Set up the colors.
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the block data structures.
# player = pygame.Rect(300, 100, 40, 40)
player = pygame.Rect(0, 0, 40, 40)
playerImage = pygame.image.load('files/player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('files/cherry.png')

foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

foodCounter = 0
NEWFOOD = 40

# Set up keyboard variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Set up the music.
pickUpSound = pygame.mixer.Sound('files/pickup.wav')
pygame.mixer.music.load('files/background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# Ran the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        # Check for the QUIT event.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Change the keyboard variables.
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moveRight = False
                moveLeft = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moveLeft = False
                moveRight = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                moveDown = False
                moveUp = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moveUp = False
                moveDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moveLeft = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moveRight = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                moveUp = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moveDown = False
            if event.key == pygame.K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == pygame.K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == pygame.MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player.
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Draw the block onto the surface.
    windowSurface.blit(playerStretchedImage, player)

    # Check whether the player has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()
    
    # Draw the food.
    for food in foods:
        windowSurface.blit(foodImage, food)
        
    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40)
    # mainClock.tick(24)
    # mainClock.tick(120)


            
        
