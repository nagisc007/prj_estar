# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.s100 import config as cnf


# episodes
def ep_intro(w: wd.World):
    return [w.chaptertitle("冒頭"),
            w.hero.be(w.stage.apart, w.day.current),
            ]


def ep_middle(w: wd.World):
    return [w.chaptertitle("展開"),]


def ep_climax(w: wd.World):
    return [w.chaptertitle("これ以上書けない"),]


def ep_end(w: wd.World):
    return [w.chaptertitle("最後の作品"),]


# main
def world():
    w = wd.World("100 stories project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS)
    return w


def story(w: wd.World):
    return [w.maintitle("百妄想騙り"),
            ep_intro(w),
            ep_middle(w),
            ep_climax(w),
            ep_end(w),
            ]


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

