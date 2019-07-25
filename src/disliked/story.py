# -*- coding: utf-8 -*-
"""Story: The disliked you
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.disliked import config as cnf
THM = cnf.THEMES


# scenes
# episodes
# outline
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.satomi, w.bot),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.satomi.be(),
                w.satomi.be(),
                w.satomi.be(),
                w.satomi.be(),
                True),
            ]

# main
def world():
    w = wd.World("The disliked you")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("背景、あなたが嫌いです"),
            w.satomi.be(w.stage.myhome, w.day.current, w.bot),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

