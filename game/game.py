from random import randint

import pyglet

import player, resources, window_dressing
from enemy import Enemy

class Game(object):

    framerate = 1/60.

    def __init__(self):
    	from text import GameText # FIXME: the suck
        self.entities = []
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)
        
        self.window = pyglet.window.Window(width=800, height=600)
        self.batch = pyglet.graphics.Batch()
        self.player = player.Player(img=resources.player, x=50, y=50, batch=self.batch, group=self.foreground)
        self.add_entity(self.player)
        self.window.push_handlers(self.player.key_handler)
        self.window.push_handlers(self.on_draw)
        self.window.push_handlers(self.on_key_press)
        for _ in range(3):
            e = Enemy(img=resources.enemy, 
                                  x=randint(100, 500), 
                                  y=randint(100, 500), 
                                  batch=self.batch,
                                  group=self.foreground)
                                  
            self.add_entity(e)
            self.add_entity(e.text)
        self.bg = window_dressing.Background(img=resources.bg, x=0, y=0, batch=self.batch, group=self.background)

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
            if hasattr(e, 'update'):
                e.update(dt)
        
    def execute(self):
        pyglet.app.run()
