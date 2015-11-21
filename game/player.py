import pyglet
from pyglet.window import key


class Player(pyglet.sprite.Sprite):

    step = 5

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        
    def update(self, dt):
        if self.key_handler[key.UP]:
            self.y += self.step
        if self.key_handler[key.DOWN]:
            self.y -= self.step
        if self.key_handler[key.LEFT]:
            self.x -= self.step
        if self.key_handler[key.RIGHT]:
            self.x += self.step
        