from random import randint

import pyglet

from text import EnemyText

class Enemy(pyglet.sprite.Sprite):

    step = 5

    def __init__(self, *args, **kwargs):
        super(Enemy, self).__init__(*args, **kwargs)
        self.text = EnemyText(self)
        
    def update(self, dt):
        self.x += randint(-self.step, self.step)
        self.y += randint(-self.step, self.step)
        self.text.x = self.x
        self.text.y = self.y