import pygame

# Initilization + Configuration
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Some Random Game")

# Weapon Variables
weaponx = 225
weapony = 400
weaponspeed = 10
shot = False

running = True

# Game Loop
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        weaponx -= weaponspeed
    if keys[pygame.K_RIGHT]:
        weaponx += weaponspeed
    if keys[pygame.K_UP]:
        shot = True
    
    # Ammo Variables
    bulletx = weaponx + 12
    bullety = weapony - 50

    # Out of bound check
    if weaponx <= 0:
        weaponx = 0
    elif weaponx >= 455:
        weaponx = 455

    pygame.draw.rect(screen, (2, 222, 240), (0, 0, 500, 500)) # Sky
    pygame.draw.rect(screen, (0, 255, 0), (0, 450, 600, 50)) # Grass / Ground
    pygame.draw.rect(screen, (127, 127, 127), (weaponx, weapony, 50, 75)) # Weapon
    if shot == True:
        firstbulletanim = pygame.draw.rect(screen, (5, 0, 0), (bulletx, bullety, 25, 37))
    print(bullety)
    pygame.display.update()

pygame.quit()
