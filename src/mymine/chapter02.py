# -*- coding: utf-8 -*-
"""Story: chapter 02: I am my mine
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.mymine import config as cnf
THM = cnf.THEMES


# scenes
def sc_visited(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("彼の訪問",
            shota.come(w.stage.apart, w.day.encounter),
            )

def sc_canlook(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("見える人",
            shota.look(w.another),
            kyoko.think(shota, "知りたい"),
            )

def sc_mymeeting(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("わたし会議",
            )

def sc_hisvisit(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("彼の再訪",
            )

def sc_livewith(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("同棲",
            kyoko.deal("一緒に暮らす"),
            )

def sc_hispropose(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("プロポーズ",
            kyoko.deal(shota, w.i.proposed),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("ワタシが見える人"),
            sc_visited(w),
            sc_canlook(w),
            )

def ep_rebellion(w: wd.World):
    return (w.chaptertitle("ワタシの反乱"),
            sc_mymeeting(w),
            sc_hisvisit(w),
            sc_livewith(w),
            )

def ep_confess(w: wd.World):
    return (w.chaptertitle("彼の告白"),
            sc_hispropose(w),
            )

# main
def story(w: wd.World):
    return [w.maintitle("わたしと彼"),
            ep_intro(w),
            ep_rebellion(w),
            ep_confess(w),
            ]


def main(): # pragma: no cover
    from src.mymine.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

