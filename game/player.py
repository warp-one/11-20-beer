import pyglet
from pyglet.window import key

import resources, unit

from enemy import Enemy

class Player(unit.Unit):

    step = 5
    images = resources.players

    def __init__(self, *args, **kwargs):
        self.game=kwargs.pop('game')
        super(Player, self).__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.current_image = 0
        
    def update(self, dt):
        dx, dy = 0, 0
        if self.key_handler[key.UP]:
            dy = self.step
        if self.key_handler[key.DOWN]:
            dy = -self.step
        if self.key_handler[key.LEFT]:
            dx = -self.step
        if self.key_handler[key.RIGHT]:
            dx = self.step
        if self.key_handler[key.SPACE]:
            for e in self.get_colliding_baddies():
                e.freeze(100)
                
        self.move(dx, dy)
        
        
    def advance_image(self):
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[self.current_image]

    def get_colliding_baddies(self):
        from game import get_distance
        for e in self.game.entities:
            if isinstance(e,Enemy) and get_distance(self, e) < 20:
                yield e
       