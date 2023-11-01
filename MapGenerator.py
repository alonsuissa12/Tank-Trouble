import pygame
import random
from Wall import Wall

map_walls_1 = [
    ((2, 750), (2, 0)),
    ((0, 52), (1400, 52)),
    ((1400 - 2, 0), (1400 - 2, 750)),
    ((1400, 750 - 2), (0, 750 - 2)),

    ((100, 96), (100, 300)),
    ((100, 150), (300, 150)),
    ((100, 100), (0, 100)),
    ((380, 150), (380, 50)),
    ((0, 390), (400, 390)),
    ((250, 390), (250, 230)),
    ((250, 308), (400, 308)),
    ((100, 460), (100, 575)),
    ((100, 570), (0, 570)),
    ((0, 655), (190, 655)),
    ((190, 660), (190, 540)),
    ((190, 470), (190, 390)),
    ((450, 520), (900, 520)),
    ((580, 750), (580, 600)),
    ((640, 55), (640, 308)),
    ((900, 150), (490, 150)),
    ((780, 520), (780, 650)),
    ((1240, 750), (1240, 250)),
    ((1100, 50), (1100, 308)),
    ((1105, 308), (800, 308)),
    ((980, 650), (1240, 650)),
    ((1040, 520), (1240, 520)),

]



max_len = 200
min_len = 50
jump = 50


class MapGenerator:
    def __init__(self, screen, width, height, wall_width=10):
        self.screen = screen
        self.width = width
        self.height = height
        self.wall_width = wall_width
        self.walls = []

    def generate_map(self):
        # Randomly select one of the predefined maps
        map_options = [map_walls_1]
        selected_map = random.choice(map_options)

        # Create walls based on the selected map
        for wall_coords in selected_map:
            start, end = wall_coords
            wall = Wall(start, end, width=self.wall_width)
            self.walls.append(wall)
        return self.walls

    def draw_map(self):
        for wall in self.walls:
            wall.draw(self.screen)
