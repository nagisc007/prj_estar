# -*- coding: utf-8 -*-
"""Story: chapter 05: I am my mine
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.mymine import config as cnf
THM = cnf.THEMES


# scenes


# episodes
def ep_parting(w: wd.World):
    k = w.kyoko
    return [w.chaptertitle("お別れという卒業"),
            k.deal("vanish", w.shota),
            ]

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            w.kyoko.be(w.stage.apart, w.day.current, w.shota),
            ep_parting(w),
            ]


def main(): # pragma: no cover
    from src.mymine.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

