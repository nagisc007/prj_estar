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
    ito, uncle = w.ito, w.uncle
    return w.scene("荒廃した町",
            w.tag.comment("生存放送。名前など重要項目とフレーズ"),
            ito.hear(w.i.broadcast),
            ito.have(w.portableradio),
            ito.look("3時"),
            ito.look("sky"),
            ito.look("海の色"),
            ito.look(w.stage.ruintown, w.day.voyage),
            ito.look("高台", w.i.suicide.flag()),
            )

def sc_decision(w: wd.World):
    ito, uncle = w.ito, w.uncle
    return w.scene("旅立ちの決意",
            ito.come(w.stage.home),
            uncle.talk("あまり外には"),
            ito.reply("ラジオがよく入らない"),
            uncle.talk("電波障害"),
            ito.think("世界がどうなったか"),
            ito.think("彼に会いたい"),
            ito.do("調べる", "電波のこと"),
            uncle.deal("噂を教える"),
            ito.think("決意"),
            uncle.talk("昔登山をよくしていた"),
            ito.have(w.mybag),
            ito.ask("本当に行っても？"),
            uncle.talk("今の目は信じられる"),
            ito.go(w.stage.tower),
            )

def sc_towertown(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("鉄塔のある町",
            ito.move("三日歩く"),
            ito.look("道中埋まった建物を見た"),
            ito.deal(w.mybag, "非常食"),
            ito.deal("寝袋"),
            ito.go(w.stage.city, w.day.current),
            ito.look("多くが沈んだ都市"),
            ito.ask(w.man1),
            w.man1.talk(shima, "タワーにいる"),
            ito.go(w.stage.tower),
            ito.look("タワー前の状況"),
            ito.look(shima),
            ito.meet(shima),
            ito.ask("放送"),
            ito.deal(shima, w.i.myalive),
            shima.reply("ジョージじゃない"),
            ito.ask(w.george),
            shima.go("鉄塔の中"),
            )

def sc_inthetower(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("鉄塔にて",
            ito.move("階段を上がる"),
            shima.explain("タワーについて"),
            ito.come(w.stage.broadroom),
            ito.look("放送室の内装"),
            shima.look(ito, w.broadbox),
            w.tag.comment("ジョージは生存者探しの旅に出た"),
            shima.talk(w.i.george_gone),
            ito.know(w.i.george_gone),
            )

def sc_histalk(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("彼の話",
            ito.come(w.stage.barrack, w.day.current),
            ito.look("ボロ小屋"),
            ito.look("ドラム缶風呂"),
            shima.deal("料理"),
            shima.talk(w.i.george_gone),
            shima.talk("自分も助けられたんだ"),
            ito.know(w.i.george_gone),
            ito.behav("泣いた"),
            ito.look(shima, "困ってる風"),
            ito.explain("涙の理由"),
            )

def sc_truth(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("私の真実",
            ito.talk(shima, w.i.suicide),
            ito.talk("災害と両親の死"),
            ito.talk("孤独"),
            ito.talk("生存報告との出逢い"),
            ito.talk("３時は生まれた時間", "両親が死んだ時間"),
            ito.know(w.i.george_gone),
            ito.talk(shima, w.i.suicide.deflag()),
            ito.think(w.george, w.i.myalive),
            ito.deal(shima, w.i.radio, "使い方"),
            )

def sc_myreport(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("私の生存報告",
            ito.be("wake", "夜の三時"),
            ito.go("tower"),
            ito.move("階段"),
            ito.feel("彼は黙ったまま"),
            shima.talk("外で待ってる"),
            ito.come(w.stage.broadroom, w.day.reporting),
            ito.talk(w.i.reporting, w.i.myalive),
            ito.talk(THM["alive"]).d("$meの報告だった"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_ruinworld(w),
            sc_decision(w),
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

