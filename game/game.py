import pyglet

class 

class Game(object):
    def __init__(self):
        self.window = pyglet.window.Window(width=800, height=600)
        self.batch = pyglet.graphics.Batch()
        
    def execute(self):
        pyglet.app.run()
    
if __name__ == '__main__':
    game = Game()
    game.execute()