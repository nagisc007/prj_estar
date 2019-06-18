# -*- coding: utf-8 -*-
"""Story: The night umbrella
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.umbrella import config as cnf
THM = cnf.THEMES


# scenes

# episodes
# test data
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.miyu, w.gentleman),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.miyu.think(w.i.myfinish),
                w.miyu.feel(w.i.worklimit),
                w.miyu.meet(w.gentleman),
                w.miyu.know(w.i.meaning),
                True),
            ]

# main
def world():
    w = wd.World("The night umbrella")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("宵の傘"),
            w.miyu.be(w.stage.rooftop, w.day.current),
            w.miyu.feel(w.i.worklimit),
            w.miyu.think(w.i.myfinish),
            w.miyu.meet(w.gentleman),
            w.miyu.know(w.i.meaning),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

