import pyglet

import player, resources

class Game(object):
    def __init__(self):
        self.window = pyglet.window.Window(width=800, height=600)
        self.batch = pyglet.graphics.Batch()
        self.player = player.Player(img=resources.player, x=50, y=50, batch=self.batch)
        self.window.push_handlers(self.player)
        self.window.push_handlers(self.on_draw)
        
    def on_draw(self):
        self.window.clear()
        self.batch.draw()
        
    def execute(self):
        pyglet.app.run()
        
    
if __name__ == '__main__':
    game = Game()
    game.execute()