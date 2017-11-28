import sprites
import random
import pygame


class EnemyHeli(object):

    shoot = False
    shoot_counter = 0
    bullets = []



    current = sprites.enemy_heli

    crash_counter = 0

    wreck_start = False
    wrecked = False

    speed = 10

    x = 500
    y = 200

    y_stop = random.randint(200, 600)

    moving_up = True
    moving_left = False
    moving_down = False
    moving_right = False

    next_0 = True
    next_1 = False
    next_2 = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def movement(self):
        if self.x > 400:
            self.x -= 10
        else:
            if self.y > 100 and self.moving_up:
                self.y -= 2
            else:
                self.moving_up = False
                self.moving_down = True

            if self.y < 400 and self.moving_down:
                self.y += 2
            else:
                self.moving_down = False
                self.moving_up = True

    def shoot(self):

            self.shoot_counter += 1

            if self.shoot_counter >= 30:
                if not self.x > 600 and not self.x < 400:
                    self.bullets.append([self.x, self.y])
                    self.shoot_counter = 0

    def init(self):
        self.movement()
        self.shoot()
