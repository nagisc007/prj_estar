# -*- coding: utf-8 -*-
"""Story: chapter 03
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
THM = cnf.THEMES

# episodes
def ep_neverrest(w: wd.World):
    return (w.chaptertitle("成仏しない幽霊"),
                w.ryoma.explain(w.info("少年の幽霊が嘘と発覚")),
                w.ryoma.explain(w.info("馬鹿らしくなって同好会は空中分解")),
            )

def ep_hisconfession(w: wd.World):
    return (w.chaptertitle("幽霊の告白"),
                w.ryoma.explain(w.info("少年の本当の悩みを聞く")),
            )

def ep_burstschool(w: wd.World):
    return (w.chaptertitle("旧校舎の崩壊"),
            # NOTE: それぞれがバラバラになる、ゴーストが嘘と発覚
                w.ryoma.explain(w.info("一人で少年の悩みを解決する")),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story-ch3", story(w), w.ryoma, w.miko),
            ]

def story_outline(w: wd.World):
    return [
            ("story-ch3", story(w),
                w.ryoma.explain(w.info("少年の幽霊が嘘と発覚")),
                w.ryoma.explain(w.info("馬鹿らしくなって同好会は空中分解")),
                w.ryoma.explain(w.info("少年の本当の悩みを聞く")),
                w.ryoma.explain(w.info("一人で少年の悩みを解決する")),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLES["ch03"]),
            ep_neverrest(w),
            ep_hisconfession(w),
            ep_burstschool(w),
            )

def main(): # pragma: no cover
    from src.bghost.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

