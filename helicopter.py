import sprites


class Helicopter(object):

    health = 3

    counter = 0
    current = sprites.helicopter

    crash_counter = 0

    damaged_counter = 0
    damaged = False

    wreck_start = False
    wrecked = False

    x = 0
    y = 0

    moving_up = False
    moving_left = False
    moving_down = False
    moving_right = False


    def __init__(self, x, y):
        self.x = x
        self.y = y


    def movement(self):

        speed = 10

        if not self.wreck_start:

            if (self.moving_up and self.moving_left) or (self.moving_down and self.moving_left):
                speed *= 0.707
            if (self.moving_up and self.moving_right) or (self.moving_down and self.moving_right):
                speed *= 0.707

            if self.moving_up:
                self.y -= speed
            if self.moving_left:
                self.x -= speed
            if self.moving_down:
                self.y += speed
            if self.moving_right:
                self.x += speed*2

            if self.x > 200:
                self.x -= speed*2
            elif self.x > 100:
                self.x -= speed/2

            if self.x < 0:
                self.x += speed
            elif self.x < 100:
                self.x += speed/2

        if self.y < 0:
            self.y = 0

        if self.y > 430:
            self.health = 0



    def player_init(self):
        self.movement()

