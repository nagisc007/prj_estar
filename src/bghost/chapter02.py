# -*- coding: utf-8 -*-
"""Story: chapter 02
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
THM = cnf.THEMES

# episodes
def ep_aboutghost(w: wd.World):
    return (w.chaptertitle("幽霊って何だ？"),
            )

def ep_howtorestsoul(w: wd.World):
    return (w.chaptertitle("成仏の方法"),
            )

def ep_ghostmemory(w: wd.World):
    return (w.chaptertitle("幽霊の思い出"),
            # NOTE: ゴーストを成仏させることになる、それが元同好会の最後の成果
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
    return (w.maintitle(cnf.TITLES["ch02"]),
            ep_aboutghost(w),
            ep_howtorestsoul(w),
            ep_ghostmemory(w),
            )

def main(): # pragma: no cover
    from src.bghost.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

