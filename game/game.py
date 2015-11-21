import pyglet

import player, resources

class Game(object):
    def __init__(self):
        self.window = pyglet.window.Window(width=800, height=600)
        self.batch = pyglet.graphics.Batch()
        self.player = player.Player(img=resources.player, x=50, y=50, batch=self.batch)
        self.window.push_handlers(self.player)
        self.window.push_handlers(self.on_draw)
        self.window.push_handlers(self.on_key_press)

        self.label_text = "The rag and bone man did not come today..."
        self.label_visible = True

    def on_key_press(self, symbols, modifiers):
    	if self.label_visible:
    		self.label_visible=False
        
    def on_draw(self):
    	from text import GameText # FIXME: the suck
        self.window.clear()
        self.batch.draw()
        if self.label_visible:
        	self.label = GameText(self.label_text)
        	self.label.draw()
        
    def execute(self):
        pyglet.app.run()
        
    
game = Game()