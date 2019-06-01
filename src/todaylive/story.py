# -*- coding: utf-8 -*-
"""Story: Today I've lived
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.todaylive import config as cnf
THM = cnf.THEMES


# scenes
def sc_ruinworld(w: wd.World):
    ito = w.ito
    return w.scene("荒廃した町",
            ito.look(w.stage.ruintown, w.day.current),
            ito.hear(w.i.broadcast),
            ito.think("彼に会いたい"),
            )

def sc_towertown(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("鉄塔のある町",
            ito.go(w.stage.tower),
            ito.meet(shima),
            )

def sc_inthetower(w: wd.World):
    ito = w.ito
    return w.scene("鉄塔にて",
            )

def sc_truth(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("知らされる真実",
            ito.know(w.i.george_gone),
            )

def sc_myreport(w: wd.World):
    ito = w.ito
    return w.scene("私の生存報告",
            ito.talk(THM["alive"]).d("$meの報告だった"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_ruinworld(w),
            )

def ep_towerplace(w: wd.World):
    return (w.chaptertitle("鉄塔の立つ場所"),
            sc_towertown(w),
            sc_inthetower(w),
            )

def ep_hisreport(w: wd.World):
    return (w.chaptertitle("生存報告"),
            sc_truth(w),
            sc_myreport(w),
            )

# main
def world():
    w = wd.World("The golden girld")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("生存報告、今日も私は生きてます"),
            ep_intro(w),
            ep_towerplace(w),
            ep_hisreport(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

