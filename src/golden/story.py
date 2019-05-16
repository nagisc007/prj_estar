# -*- coding: utf-8 -*-
"""Story: the golden girl
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.golden import config as cnf


# episodes
def ep_intro(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    scenes = [
            w.scene("黄金になる娘",
                kana.be(w.i.goldsyndrome, w.stage.home, w.day.current),
                f.deal("guard", kana),
                ),
            w.scene("奪われる黄金の肌",
                ),
            w.scene("治療費用",
                f.deal(w.fund),
                hiroko.talk("娘の細胞を売るべき"),
                ),
            ]
    return [w.chaptertitle("黄金の娘"),
            *scenes,
            ]


def ep_decision(w: wd.World):
    f, kana = w.fukuo, w.kana
    scenes = [
            w.scene("決断",
                f.think(w.kanacell, "資金集めに使う"),
                ),
            ]
    return [w.chaptertitle("決断の時"),
            *scenes,
            ]


# main
def world():
    w = wd.World("The golden girld")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("不幸の黄金少女"),
            ep_intro(w),
            ep_decision(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

