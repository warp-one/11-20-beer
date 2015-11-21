import pyglet
from pyglet.window import key

import resources

class Player(pyglet.sprite.Sprite):

    step = 5
    images = resources.players

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.current_image = 0
        
    def update(self, dt):
        if self.key_handler[key.UP]:
            self.y += self.step
        if self.key_handler[key.DOWN]:
            self.y -= self.step
        if self.key_handler[key.LEFT]:
            self.x -= self.step
        if self.key_handler[key.RIGHT]:
            self.x += self.step
        
    def advance_image(self):
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[self.current_image]
       