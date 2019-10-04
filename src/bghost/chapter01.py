# -*- coding: utf-8 -*-
"""Story: chapter 01
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
THM = cnf.THEMES

# scenes

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            )

def ep_oldschool(w: wd.World):
    return (w.chaptertitle("旧校舎"),
            )

def ep_boyghost(w: wd.World):
    return (w.chaptertitle("少年の幽霊"),
            )

def ep_lastwork(w: wd.World):
    return (w.chaptertitle("同好会最後の仕事"),
            # NOTE: 小学校が廃校になり、同窓会に集まる仲良しメンバ、そこにイレギュラーな彼女
            # NOTE: 地縛霊という少年を見つける、本物？　少年ホームレス？
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
    return (w.maintitle(cnf.TITLES["ch01"]),
            ep_intro(w),
            ep_oldschool(w),
            ep_boyghost(w),
            ep_lastwork(w),
            )

def main(): # pragma: no cover
    from src.bghost.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

