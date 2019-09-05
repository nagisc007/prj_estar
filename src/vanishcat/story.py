# -*- coding: utf-8 -*-
"""Story: vanish cat
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.vanishcat import config as cnf
THM = cnf.THEMES


# scenes
def sc_catlife(w: wd.World):
    return w.scene("猫の居る生活",
            # NOTE: リビングで仕事をしながら、猫を愛でる、しかしそれは機械猫
            )

def sc_mywork(w: wd.World):
    return w.scene("仕事にて",
            )

def sc_lostcat(w: wd.World):
    return w.scene("猫のいない家",
            )

def sc_brokencat(w: wd.World):
    return w.scene("壊された猫",
            )

def sc_revivecat(w: wd.World):
    return w.scene("何度も蘇る猫",
            )

def sc_vanishing(w: wd.World):
    return w.scene("消える猫",
            )

def sc_waitcat(w: wd.World):
    return w.scene("待ちぼうけ",
            )

def sc_findword(w: wd.World):
    return w.scene("彼女が消えた意味、残した言葉",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_catlife(w),
            )

def ep_vanished(w: wd.World):
    return (w.chaptertitle("消えた猫"),
            sc_mywork(w),
            sc_lostcat(w),
            sc_brokencat(w),
            sc_revivecat(w),
            )

def ep_wating(w: wd.World):
    return (w.chaptertitle("待ち続ける"),
            sc_vanishing(w),
            sc_waitcat(w),
            )

def ep_knowreason(w: wd.World):
    return (w.chaptertitle("知る真実"),
            sc_findword(w),
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ]

def story_outlines(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The vanish cat")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("バイバイ・マイディア"),
            ep_intro(w),
            ep_vanished(w),
            ep_wating(w),
            ep_knowreason(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

