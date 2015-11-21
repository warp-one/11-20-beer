from random import randint

import pyglet

import player, resources
from enemy import Enemy

class Game(object):

    framerate = 1/60.

    def __init__(self):
        self.window = pyglet.window.Window(width=800, height=600)
        self.batch = pyglet.graphics.Batch()
        self.player = player.Player(img=resources.player, x=50, y=50, batch=self.batch)
        self.window.push_handlers(self.player)
        self.window.push_handlers(self.on_draw)
        
        self.entities = []
        for _ in range(3):
            self.add_entity(Enemy(img=resources.enemy, 
                                  x=randint(100, 500), 
                                  y=randint(100, 500), 
                                  batch=self.batch))
        
        pyglet.clock.schedule_interval(self.update, self.framerate)
        
    def on_draw(self):
        self.window.clear()
        self.batch.draw()
        
    def add_entity(self, entity):
        self.entities.append(entity)
        
    def update(self, dt):
        for e in self.entities:
            e.update(dt)
        
    def execute(self):
        pyglet.app.run()
        
    
if __name__ == '__main__':
    game = Game()
    game.execute()