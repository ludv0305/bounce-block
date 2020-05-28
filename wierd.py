import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

on = True

down_right = True

down_left = False

up_right = False

up_left = False

player_pos = [300, 300]

while on:

    screen = pygame.display.set_mode((600, 600))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            on = False

    x = player_pos[0]
    y = player_pos[1]

    if x >= 580:
        down_left = True
        down_right = False
        up_right = False
        up_left = False

    if down_left:
        x = player_pos[0]
        y = player_pos[1]

        x -= 7
        y += 4

        player_pos = [x, y]

    if y >= 580:
        up_left = True
        down_left = False
        down_right = False
        up_right = False

    if up_left:
        x = player_pos[0]
        y = player_pos[1]

        x -= 3
        y -= 10

        player_pos = [x, y]

    if x <= 0:
        up_right = True
        up_left = False
        down_right = False
        down_left = False

    if up_right:
        x = player_pos[0]
        y = player_pos[1]

        x += 8
        y -= 3
        player_pos = [x, y]

    if y <= 0:
        down_right = True
        up_right = False
        up_left = False
        down_left = False

    if down_right:
        x = player_pos[0]
        y = player_pos[1]

        x += 5
        y += 4

        player_pos = [x, y]

    screen.fill((76, 153, 0))
    player = pygame.draw.rect(screen, (51, 255, 255), (player_pos[0], player_pos[1], 30, 30))

    clock = pygame.time.Clock()

    clock.tick(30)

    pygame.display.update()
