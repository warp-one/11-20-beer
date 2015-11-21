from random import randint

import pyglet

class Enemy(pyglet.sprite.Sprite):

    step = 5

    def __init__(self, *args, **kwargs):
        super(Enemy, self).__init__(*args, **kwargs)
        
    def update(self, dt):
        self.x += randint(-self.step, self.step)
        self.y += randint(-self.step, self.step)