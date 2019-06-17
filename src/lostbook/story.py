# -*- coding: utf-8 -*-
"""Story: Lost her book
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.lostbook import config as cnf
THM = cnf.THEMES


# scenes
# episodes

# test data
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.nako, w.saya),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.nako.think("全ての本を集める"),
                w.nako.know(w.i.vanishshop),
                w.nako.deal("本を集める"),
                w.nako.go(w.saya, "彼女に会う"),
                True),
            ]

# main
def world():
    w = wd.World("Lost her book")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("彼女の本が、消えます"),
            w.nako.be(w.stage.town, w.day.current),
            w.nako.know(w.i.vanishshop),
            w.nako.think("全ての本を集める"),
            w.nako.deal("本を集める"),
            w.nako.go(w.saya, "彼女に会う"),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

