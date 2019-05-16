# -*- coding: utf-8 -*-
"""Story: I am my mine
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.mymine import config as cnf
THM = cnf.THEMES


# episodes
def ep_intro(w: wd.World):
    k = w.kyoko
    return [w.chaptertitle("そして彼に出会った"),
            k.be(w.stage.univ, w.day.current),
            k.look(w.another),
            k.think(THM["problem"]),
            k.meet(w.shota),
            ]


def ep_parting(w: wd.World):
    k = w.kyoko
    return [w.chaptertitle("お別れという卒業"),
            k.deal("vanish", w.shota),
            ]


# main
def world():
    w = wd.World("I am my mine")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("わたしとワタシと私"),
            ep_intro(w),
            ep_parting(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

