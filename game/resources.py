import pyglet

pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

# image tools
def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2
    return image

def uncenter_image(image):
    image.anchor_x = 0
    image.anchor_y = 0
    return image
	
# IMAGES
players = [pyglet.resource.image("player.png"),
           pyglet.resource.image("player1.png"),
           pyglet.resource.image("player2.png"),
           pyglet.resource.image("player3.png")]
enemy = pyglet.resource.image("enemy.png")
enemy1 = pyglet.resource.image("enemy1.png")
enemyhu = pyglet.resource.image("enemyhu.png")
enemyhd = pyglet.resource.image("enemyhd.png")
enemyhl = pyglet.resource.image("enemyhl.png")
enemyhr = pyglet.resource.image("enemyhr.png")
bg = pyglet.resource.image("bg.png")