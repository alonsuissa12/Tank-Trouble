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
walls = map_generator.generate_map()
red_start_y = 600
red_start_x = 1200
blue_start_y = 110
blue_start_x = 110
red_tank = Tank('red tank.png', (red_start_x, red_start_y))
blue_tank = Tank('blue tank.png', (blue_start_x, blue_start_y))


def game_loop():
    clock = pygame.time.Clock()
    game_run = True
    game_playing = True
    is_text = True
    rotate_angel_red = 0
    move_speed_red = 0
    rotate_angel_blue = 0
    move_speed_blue = 0
    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rotate_angel_red = -1
                if event.key == pygame.K_LEFT:
                    rotate_angel_red = 1
                if event.key == pygame.K_UP:
                    move_speed_red = 0.1
                if event.key == pygame.K_DOWN:
                    move_speed_red = -0.1
                if event.key == pygame.K_d:
                    rotate_angel_blue = -1
                if event.key == pygame.K_a:
                    rotate_angel_blue = 1
                if event.key == pygame.K_w:
                    move_speed_blue = 0.1
                if event.key == pygame.K_s:
                    move_speed_blue = -0.1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    rotate_angel_red = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    move_speed_red = 0
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    rotate_angel_blue = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    move_speed_blue = 0

        red_tank.update(rotate_angel_red, move_speed_red)
        blue_tank.update(rotate_angel_blue,move_speed_blue)
        screen.fill(background_color)
        map_generator.draw_map()
        pygame.draw.rect(screen, toolbar_color, pygame.Rect(0, 0, screen_w, 50))  # Draw toolbar

        red_tank.show(screen)
        blue_tank.show(screen)

        pygame.display.update()
        clock.tick(fps)


game_loop()
pygame.quit()
quit()
