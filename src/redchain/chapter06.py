# -*- coding: utf-8 -*-
"""Chapter 06: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.redchain import config as cnf
THM = cnf.THEMES


# scenes
def sc_deathanniv(w: wd.World):
    ma, mam, dad = w.masuda, w.mam, w.dad
    return w.scene("祖母の三回忌にて",
            ma.go(w.stage.home, w.day.anniversary),
            mam.talk("結婚は？"),
            dad.talk("農家継げばいい"),
            ma.ask(w.hideko),
            dad.talk("秀子の話"),
            dad.talk(w.movie, "ここが舞台のモデルだった"),
            )

def sc_meaning(w: wd.World):
    ma, miki = w.masuda, w.miki
    return w.scene("赤い繋がり",
            ma.come(w.stage.temple, w.day.summer),
            ma.deal("お参り"),
            ma.think(w.hideko),
            miki.come(),
            miki.talk(w.hideko, "彼女について"),
            miki.ask("仕事続けるの？"),
            ma.reply("もう少しがんばってみます"),
            )

# episode
def ep_epilogue(w: wd.World):
    return [w.chaptertitle("エピローグ"),
            sc_deathanniv(w),
            sc_meaning(w),
            ]

# main
def story(w: wd.World):
    return ep_epilogue(w)


def main(): # pragma: no cover
    from src.redchain.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

