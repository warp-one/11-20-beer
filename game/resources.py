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
player = pyglet.resource.image("player.png")