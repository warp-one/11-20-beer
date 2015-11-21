import pyglet
from pyglet.window import key


class Player(pyglet.sprite.Sprite0):

    step = 5

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.y += self.step
        if symbol == key.DOWN:
            self.y -= self.step
        if symbol == key.LEFT:
            self.x -= self.step
        if symbol == key.RIGHT:
            self.x += self.step
        