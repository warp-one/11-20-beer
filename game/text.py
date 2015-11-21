
import pyglet

from game import game


class GameText(pyglet.text.Label):

	def __init__(self, text):
		super(GameText, self).__init__(
			text,
			font_size=12,
			anchor_x="center",
			anchor_y="center",
			x=game.window.width//2,
			y=game.window.height//2,
			font_name="monospace"
		)