import pygame


class Wall(object):
    def __init__(self, start: tuple[2], end: tuple[2], color=(140, 140, 140), width=1):
        self.start = start
        self.end = end
        self.color = color
        self.width = width
        self.rect = (0, 0, 0, 0)

    def draw(self,screen):
        self.rect = pygame.draw.line(screen, self.color, self.start, self.end, width=self.width)

    def get_rect(self):
        return self.rect
