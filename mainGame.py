import pygame
from Wall import Wall
from MapGenerator import MapGenerator
from Tank import Tank

# init

pygame.init()
fps = 30
screen_w = 1400  # todo: leave a bit from above for score, and buttons
screen_h = 750
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Tank Trouble")
background_color = (233, 233, 233)
toolbar_color = (143, 200, 90)

map_generator = MapGenerator(screen, screen_w, screen_h - 100)
map_generator.generate_map()
yy = 110
xx = 110
tank1 = Tank(xx, yy, 'red tank.png', (xx, yy))


def game_loop():
    clock = pygame.time.Clock()
    game_run = True
    game_playing = True
    is_text = True
    rotate_angel = 0
    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            # if pygame.mouse.get_pressed():
            #     print(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rotate_angel = -1

                if event.key == pygame.K_LEFT:
                    rotate_angel = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    rotate_angel = 0
        tank1.update(rotate_angel)
        screen.fill(background_color)
        map_generator.draw_map()
        pygame.draw.rect(screen, toolbar_color, pygame.Rect(0, 0, screen_w, 50))  # Draw toolbar

        tank1.show(screen)


        pygame.display.update()
        clock.tick(fps)


game_loop()
pygame.quit()
quit()
