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
            ito.look(w.stage.ruintown, w.day.voyage),
            ito.look("高台", w.i.suicide.flag()),
            ito.hear(w.i.broadcast),
            ito.think("彼に会いたい"),
            ito.do("調べる", "電波のこと"),
            w.uncle.deal("噂を教える"),
            ito.think("決意"),
            ito.have(w.mybag),
            ito.go(w.stage.tower),
            )

def sc_towertown(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("鉄塔のある町",
            ito.go(w.stage.tower, w.day.current),
            ito.meet(shima),
            ito.deal(shima, w.i.myalive),
            shima.reply("ジョージじゃない"),
            ito.ask(w.george),
            shima.go("鉄塔の中"),
            )

def sc_inthetower(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("鉄塔にて",
            ito.come(w.stage.broadroom),
            shima.look(ito, w.broadbox),
            ito.know(w.i.george_gone),
            )

def sc_histalk(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("彼の話",
            ito.come(w.stage.barrack, w.day.current),
            shima.talk(w.i.george_gone),
            ito.know(w.i.george_gone),
            )

def sc_truth(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("私の真実",
            ito.know(w.i.george_gone),
            ito.talk(shima, w.i.suicide.deflag()),
            ito.think(w.george, w.i.myalive),
            ito.deal(shima, w.i.radio, "使い方"),
            )

def sc_myreport(w: wd.World):
    ito = w.ito
    return w.scene("私の生存報告",
            ito.come(w.stage.broadroom, w.day.reporting),
            ito.talk(w.i.reporting, w.i.myalive),
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
            sc_histalk(w),
            )

def ep_hisreport(w: wd.World):
    return (w.chaptertitle("生存報告"),
            sc_truth(w),
            sc_myreport(w),
            )

# test data
def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.ito.think("彼に会いたい"),
                w.ito.hear(w.i.broadcast),
                w.ito.go(w.stage.tower),
                w.ito.know(w.i.george_gone),
                True),
            ]

def episode_outlines(w: wd.World):
    return [
            ("episode1", ep_intro(w),
                w.ito.think("彼に会いたい"),
                w.ito.hear(w.i.broadcast),
                w.ito.do("調べる"),
                w.ito.go(w.stage.tower),
                True),
            ("episode2", ep_towerplace(w),
                w.ito.deal(w.shima, w.i.myalive),
                w.ito.meet(w.shima),
                w.ito.ask(w.george),
                w.shima.talk(w.i.george_gone),
                True),
            ("episode3", ep_hisreport(w),
                w.ito.think(w.george, w.i.myalive),
                w.ito.know(w.i.george_gone),
                w.ito.deal(w.shima, w.i.radio),
                w.ito.talk(w.i.reporting, w.i.myalive),
                True),
            ]

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

