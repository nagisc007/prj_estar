# -*- coding: utf-8 -*-
"""Story: the golden girl
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.golden import config as cnf


# episodes
def ep_intro(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    scenes = [
            w.scene("黄金になる娘",
                kana.be(w.i.goldsyndrome, w.stage.home, w.day.current),
                f.deal("guard", kana),
                f.come(w.stage.kanaroom),
                f.look(kana, "黄金化"),
                kana.talk("きれい"),
                f.talk(hiroko),
                ),
            w.scene("黄金化症候群",
                f.go(w.stage.hospital),
                kana.deal("診察"),
                w.medic1.talk("大きな病院で診てもらった方が"),
                f.go(w.stage.univhospital),
                w.medic2.talk("専門の機関を紹介"),
                f.go(w.stage.labo),
                doc.talk(f, "黄金化症候群"),
                f.know("不治の病"),
                doc.talk("莫大な研究費"),
                doc.talk("国の助成金が少ない"),
                ),
            w.scene("治療",
                f.deal(w.fund),
                hiroko.talk("娘の細胞を売るべき"),
                doc.come(w.stage.home),
                doc.deal(w.i.heal),
                doc.talk("我々に任せて下さい"),
                f.deal("研究所に預ける決断"),
                f.look(hiroko, "渋っているよう"),
                f.deal(kana, "預ける", w.stage.labo),
                kana.deal("奪われる", w.kanacell),
                ),
            ]
    return [w.chaptertitle("黄金の娘"),
            *scenes,
            ]


def ep_unfortune(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    scenes = [
            w.scene("奪われる黄金細胞",
                ),
            w.scene("研究される娘",
                f.look("tv", "取り上げられる"),
                f.think(kana, "guard"),
                kana.deal(w.kanacell, "奪われる"),
                ),
            w.scene("有名になる",
                ),
            w.scene("更なる強奪",
                ),
            w.scene("家に引き取る",
                f.be(kana, w.stage.home, "匿う"),
                f.come(w.kana, w.stage.home, "連れ帰る", w.day.takehome),
                hiroko.talk("反対だった"),
                f.look("毎日見張り"),
                f.be("睡眠不足"),
                kana.deal("奪われる", w.kanacell),
                ),
            w.scene("限界点",
                hiroko.talk(f, "もう限界"),
                hiroko.be(w.i.neurosis),
                ),
            ]
    return [w.chaptertitle("不幸の始まり"),
            *scenes,
            ]


def ep_decision(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    scenes = [
            w.scene("決断",
                f.think(w.kanacell, "資金集めに使う"),
                hiroko.think(w.i.killkana),
                f.do("stop", hiroko),
                f.deal(hiroko, w.i.golden),
                ),
            w.scene("そして神が生まれた",
                f.deal("案内", w.stage.home, w.day.goddess),
                f.deal(kana, w.i.god),
                ),
            ]
    return [w.chaptertitle("決断の時"),
            *scenes,
            ]


# main
def world():
    w = wd.World("The golden girld")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("不幸の黄金少女"),
            ep_intro(w),
            ep_unfortune(w),
            ep_decision(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

