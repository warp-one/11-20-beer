
import pyglet
import random


class GameText(pyglet.text.Label):

    def __init__(self, text, w, h, **kwargs):
        super(GameText, self).__init__(
            text,
            font_size=12,
            anchor_x=kwargs.pop('anchor_x', 'center'),
            anchor_y=kwargs.pop('anchor_y', 'center'),
            x=w//2,
            y=h//2,
            font_name="Times New Roman",
            **kwargs
        )
        print text, w, h, kwargs

class EnemyText(GameText):

    TEXTS = [
        'Frances did not eat her egg.',
        'She sang a little song to it.',
        'She sang the song very softly:',
        '"I do not like the way you slide,',
        'I do not like your soft inside,',
        'I do not like you lots of ways,',
        'And I could do for many days',
        'Without eggs."',
    ]

    def __init__(self, enemy):
        t = self.get_text()
        super(EnemyText, self).__init__(text=t, w=enemy.x, h=enemy.y, 
            anchor_x="left", anchor_y="top", batch=enemy.batch, color=(100,100,100,255), group=enemy.group)

    def get_text(self):
        return random.choice(self.TEXTS)