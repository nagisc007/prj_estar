# -*- coding: utf-8 -*-
"""Story: The night umbrella
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.umbrella import config as cnf
THM = cnf.THEMES


# scenes
def sc_standroof(w: wd.World):
    miyu = w.miyu
    return w.scene("屋上に立つ者",
            w.miyu.be(w.stage.rooftop, w.day.current),
            w.miyu.feel(w.i.worklimit),
            w.miyu.think(w.i.myfinish),
            miyu.look("都会のビル群"),
            miyu.be("時間帯は夜"),
            miyu.look(w.i.starlight),
            )

def sc_mysteryousman(w: wd.World):
    miyu, ryu = w.miyu, w.ryuichi
    return w.scene("謎の男性",
            ryu.talk("最初の言葉"),
            w.miyu.meet(w.ryuichi),
            miyu.look("傘持つ男"),
            miyu.ask(w.umbrella, w.i.feature.flag()),
            )

def sc_lookback(w: wd.World):
    miyu, ryu = w.miyu, w.ryuichi
    return w.scene("私の回想",
            miyu.remember("仕事の失敗"),
            miyu.remember("上司との関係"),
            miyu.remember("同僚との関係"),
            )

def sc_umbrella(w: wd.World):
    miyu, ryu = w.miyu, w.ryuichi
    return w.scene("傘の意味",
            w.miyu.know(w.i.meaning),
            )

def sc_truth(w: wd.World):
    miyu, ryu = w.miyu, w.ryuichi
    return w.scene("真実は",
            ryu.explain("自分はAI教師"),
            ryu.talk(w.i.feature.deflag()),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_standroof(w),
            )

def ep_lighting(w: wd.World):
    return (w.chaptertitle("街を照らす光"),
            sc_mysteryousman(w),
            sc_lookback(w),
            )

def ep_meaning(w: wd.World):
    return (w.chaptertitle("傘の意味"),
            sc_umbrella(w),
            sc_truth(w),
            )

# test data
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.miyu, w.ryuichi),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.miyu.think(w.i.myfinish),
                w.miyu.feel(w.i.worklimit),
                w.miyu.meet(w.ryuichi),
                w.miyu.know(w.i.meaning),
                True),
            ]

# main
def world():
    w = wd.World("The night umbrella")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("宵の傘"),
            ep_intro(w),
            ep_lighting(w),
            ep_meaning(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

