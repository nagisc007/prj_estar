# -*- coding: utf-8 -*-
"""Story: chapter 05
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
THM = cnf.THEMES

# episodes
def ep_lookforher(w: wd.World):
    return (w.chaptertitle("彼女を探して"),
            )

def ep_lastwork(w: wd.World):
    return (w.chaptertitle("最後の仕事"),
            )

def ep_goodbyegirl(w: wd.World):
    return (w.chaptertitle("そして、さよなら"),
            )

def ep_epilogue(w: wd.World):
    return (w.chaptertitle("エピローグ"),
            # NOTE: 彼女との別離、大人になること
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLES["ch05"]),
            ep_lookforher(w),
            ep_lastwork(w),
            ep_goodbyegirl(w),
            ep_epilogue(w),
            )

def main(): # pragma: no cover
    from src.bghost.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

