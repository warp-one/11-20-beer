
import pyglet


class GameText(pyglet.text.Label):

    def __init__(self, text, w, h):
        super(GameText, self).__init__(
            text,
            font_size=12,
            anchor_x="center",
            anchor_y="center",
            x=w//2,
            y=h//2,
            font_name="monospace"
        )