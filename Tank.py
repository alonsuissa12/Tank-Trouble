import pygame
import random
from pygame import Vector2

Tank_length = 50
Tank_width = 30
base_speed = 5


class Tank(object):
    def __init__(self, x: int, y: int, pic_name, pivot):
        self.x = x
        self.y = y
        self.ammunition = 4
        self.life = 1
        self.bullets = []
        self.angel = 0
        self.pivot = pivot
        self.offset = Vector2()
        self.offset.from_polar((0, self.angel))
        self.pos = pivot + self.offset
        self.orig_pic = pygame.image.load(pic_name).convert_alpha()
        self.pic = self.orig_pic

        self.rect = self.pic.get_rect(center=self.pos)
        self.center = self.rect.center

    def shoot(self):
        if self.ammunition > 0:
            self.ammunition -= 1
            self.bullets[self.ammunition].shoot()

    def show(self, screen):
        screen.blit(self.pic, self.rect)

    def update(self, dt):
        self.angel += 5 * dt
        self.pic, self.rect = self.rotate(self.orig_pic, self.angel, self.pivot, self.pos)

    def rotate(self, image, angel, pivot, origin):
        surf = pygame.transform.rotate(image, angel)

        offset = pivot + (origin - pivot).rotate(-angel)
        rect = surf.get_rect(center=offset)

        return surf, rect

        # pivot = self.center
        # rotate_pic = pygame.transform.rotate(self.pic, angel)
        # offset = pivot + (self.origin - pivot).rotate(-angel)
        # rect = rotate_pic.get_rect(center=offset)
        # self.rect = rect
        # self.pic = pic
        # self.center = self.rect.center
        # self.x = rect.x
        # self.y = rect.y
        # self.angel += angel

        # body_s = pygame.Surface((Tank_w, Tank_h))
        # body_s = pygame.transform.rotate(body_s, rotate_amount)
        # barrel_s = pygame.Surface(self.barrel.size)
        # barrel_s = pygame.transform.rotate(barrel_s, rotate_amount)

        # self.body = body_s.get_rect(center=self.body.center)
        # self.barrel = barrel_s.get_rect(center=self.barrel.center)
        # self.barrel.center = (self.body.centerx, self.body.top)  # middle of the top
