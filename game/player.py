import pyglet

class Player(pyglet.sprite.Sprite0):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        
    def on_key_press(self, symbol, modifiers):
        pass