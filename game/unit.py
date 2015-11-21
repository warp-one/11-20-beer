import pyglet

class Unit(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Unit, self).__init__(*args, **kwargs)
        
    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x > 0 and new_x < self.game.window.width:
            self.x = new_x
        if new_y > 0 and new_y < self.game.window.height:
            self.y = new_y
        
        
