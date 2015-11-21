from random import randint

import pyglet

import player, resources
from enemy import Enemy

class Game(object):

    framerate = 1/60.

    def __init__(self):
    	from text import GameText # FIXME: the suck
        self.window = pyglet.window.Window(width=800, height=600)
        self.batch = pyglet.graphics.Batch()
        self.player = player.Player(img=resources.player, x=50, y=50, batch=self.batch)
        self.window.push_handlers(self.player)
        self.window.push_handlers(self.on_draw)
        self.window.push_handlers(self.on_key_press)
        self.entities = []
        for _ in range(3):
            self.add_entity(Enemy(img=resources.enemy, 
                                  x=randint(100, 500), 
                                  y=randint(100, 500), 
                                  batch=self.batch))

        self.label_text = "The rag and bone man did not come today..."
        self.label_visible = True
        self.label = GameText(self.label_text, self.window.width, self.window.height)
        
        pyglet.clock.schedule_interval(self.update, self.framerate)

    def on_key_press(self, symbols, modifiers):
    	if self.label_visible:
    		self.label_visible=False
        
        
    def on_draw(self):
        self.window.clear()
        self.batch.draw()
        if self.label_visible:
        	self.label.draw()
        
    def add_entity(self, entity):
        self.entities.append(entity)
        
    def update(self, dt):
        for e in self.entities:
            e.update(dt)
        
    def execute(self):
        pyglet.app.run()
