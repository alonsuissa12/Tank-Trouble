import math

import pygame
import random
from pygame import Vector2


class BoostManager:
    def __init__(self):
        pass


Tank_length = 55
Tank_width = 31
base_speed = 5


class Tank(object):
    def __init__(self, pic_name, pivot):

        self.ammunition = 4
        self.life = 1
        self.bullets = []
        self.angel = 0  # note: angel 0 is upward!
        self.regular_angel = (self.angel + 90) % 360
        self.pivot = pivot
        self.offset = Vector2()
        self.offset.from_polar((0, self.angel))
        self.pos = pivot + self.offset
        self.orig_pic = pygame.image.load(pic_name).convert_alpha()
        self.pic = self.orig_pic
        self.BM = BoostManager()
        self.rect = self.pic.get_rect(center=self.pos)
        self.center = self.rect.center

        # self.right_dot_offset = Vector2()
        # self.offset.from_polar(((Tank_width + 1) / 2, self.angel))

    def shoot(self):
        if self.ammunition > 0:
            self.ammunition -= 1
            self.bullets[self.ammunition].shoot()

    def show(self, screen):
        screen.blit(self.pic, self.rect)
        print("offset =", self.offset)
        print("center =", self.center)
        print("pivot =", self.pivot)
        pygame.draw.circle(screen, (200, 200, 100), self.center, 5.0, 10)
        pygame.draw.circle(screen, (200, 200, 100), (self.center[0] + Tank_width / 2, self.center[1]), 3.0, 3)
        # pygame.draw.circle(screen, (200, 200, 100), (self.center[0] - Tank_width / 2, self.center[1]), 3.0, 3)

    def update(self, dt, move_speed):
        # rotate
        if dt != 0:
            rotate_speed = 5
            self.angel += rotate_speed * dt
            self.angel = self.angel % 360
            self.regular_angel = (self.angel + 90) % 360
            self.pic, self.rect = self.rotate(self.orig_pic, self.angel, self.pivot, self.pos)

        # move
        if move_speed != 0:
            x, y = self.move(move_speed)
            self.center = (self.center[0] + x, self.center[1] - y)
            self.rect.center = self.center
            self.pivot = self.center
            self.pos = self.pivot + self.offset

    def rotate(self, image, angel, pivot, origin):
        surf = pygame.transform.rotate(image, angel)

        offset = pivot + (origin - pivot).rotate(-angel)
        rect = surf.get_rect(center=offset)

        # self.right_dot_offset = pivot + (origin - pivot).rotate(-angel)

        return surf, rect

    def move(self, speed):
        # Todo: check for boost and add to speed
        radian_angel = math.radians(self.regular_angel)
        x = Tank_length * math.cos(radian_angel) * speed
        y = Tank_length * math.sin(radian_angel) * speed
        return x, y
