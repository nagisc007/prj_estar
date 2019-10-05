# -*- coding: utf-8 -*-
"""Story: chapter 04
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
THM = cnf.THEMES

# episodes
def ep_genuineghost(w: wd.World):
    return (w.chaptertitle("本物の幽霊？"),
                w.ryoma.explain(w.info("少年の問題を彼女と一緒に取り組む")),
                w.ryoma.explain(w.info("少年の問題が解決する")),
            )

def ep_oldmemory(w: wd.World):
    return (w.chaptertitle("小学校の思い出"),
                w.ryoma.explain(w.info("彼女に忘れ物を届けに行く")),
            )

def ep_vanishgirl(w: wd.World):
    return (w.chaptertitle("いなくなった少女"),
            # NOTE: 本物のゴーストを見つけてしまう、彼女を成仏させるために苦労する
                w.ryoma.explain(w.info("彼女が亡くなっていると知る")),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story-ch4", story(w), w.ryoma, w.miko),
            ]

def story_outline(w: wd.World):
    return [
            ("story-ch4", story(w),
                w.ryoma.explain(w.info("少年の問題を彼女と一緒に取り組む")),
                w.ryoma.explain(w.info("少年の問題が解決する")),
                w.ryoma.explain(w.info("彼女に忘れ物を届けに行く")),
                w.ryoma.explain(w.info("彼女が亡くなっていると知る")),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLES["ch04"]),
            ep_genuineghost(w),
            ep_oldmemory(w),
            ep_vanishgirl(w),
            )

def main(): # pragma: no cover
    from src.bghost.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

