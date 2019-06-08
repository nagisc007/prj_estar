# -*- coding: utf-8 -*-
"""Story: chapter 03: I am my mine
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.mymine import config as cnf
THM = cnf.THEMES


# scenes
def sc_proposed(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("彼のプロポーズから",
            kyoko.deal(shota, w.i.proposed, w.stage.apart, w.day.proposed),
            kyoko.think(w.i.proposed),
            )

def sc_meeting1(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("私会議その1",
            kyoko.come(w.stage.living),
            kyoko.deal(w.i.meeting),
            )

def sc_meeting2(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("私会議その2",
            kyoko.go(w.stage.univ),
            kyoko.come(w.stage.classroom),
            kyoko.deal(w.i.meeting),
            )

def sc_meeting3(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("私会議その3",
            kyoko.come(w.stage.famires),
            kyoko.deal(w.i.meeting),
            shota.come("前の席"),
            shota.deal(w.i.proposed),
            )

def sc_birthanother(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("私、誕生",
            kyoko.come(w.stage.living),
            kyoko.look(w.another),
            kyoko.be(w.i.birth_another),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("今日子、逃亡す"),
            sc_proposed(w),
            )

def ep_meeting(w: wd.World):
    return (w.chaptertitle("私会議"),
            sc_meeting1(w),
            sc_meeting2(w),
            )

def ep_4thanother(w: wd.World):
    return (w.chaptertitle("四番目の今日子"),
            sc_meeting3(w),
            sc_birthanother(w),
            )

# outline
def base_info(w: wd.World):
    return ("chapter3", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return ("chapter3", story(w),
            w.kyoko.think(w.i.proposed),
            w.kyoko.deal(w.i.proposed, w.shota),
            w.kyoko.deal(w.i.meeting),
            w.kyoko.be(w.i.birth_another),
            True)

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            ep_intro(w),
            ep_meeting(w),
            ep_4thanother(w),
            ]


def main(): # pragma: no cover
    from src.mymine.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

