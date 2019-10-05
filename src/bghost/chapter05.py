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
                w.ryoma.explain(w.info("彼女が幽霊になった事情を知る")),
            )

def ep_lastwork(w: wd.World):
    return (w.chaptertitle("最後の仕事"),
                w.ryoma.explain(w.info("彼女は成仏できない")),
                w.ryoma.explain(w.info("彼女の心残りは良馬だと知る")),
            )

def ep_goodbyegirl(w: wd.World):
    return (w.chaptertitle("そして、さよなら"),
                w.ryoma.explain(w.info("彼女を成仏させる")),
            )

def ep_epilogue(w: wd.World):
    return (w.chaptertitle("エピローグ"),
            # NOTE: 彼女との別離、大人になること
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.ryoma, w.miko),
            ]

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.ryoma.explain(w.info("彼女が幽霊になった事情を知る")),
                w.ryoma.explain(w.info("彼女は成仏できない")),
                w.ryoma.explain(w.info("彼女の心残りは良馬だと知る")),
                w.ryoma.explain(w.info("彼女を成仏させる")),
                True),
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

