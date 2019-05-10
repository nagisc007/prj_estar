# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.s100 import config as cnf


# episodes
def ep_intro(w: wd.World):
    h, osaki = w.hero, w.osaki
    scenes = [
            w.scene("冒頭",
                h.be(w.stage.apart, w.day.current),
                h.do("phone", w.osaki, "原稿締め切り"),
                h.deal(w.fear_mail),
                h.do("write", "$must"),
                h.do("write", w.i.novel),
                h.have(w.terminal),
                h.have(w.i.future_mail),
                ),
            ]
    return [w.chaptertitle("冒頭"),
            *scenes,
            ]


def ep_middle(w: wd.World):
    h, fuyumi = w.hero, w.fuyumi
    scenes = [
            w.scene("未来からの警告",
                h.be(w.stage.apart, w.day.current),
                h.think(w.i.future_mail),
                h.have(fuyumi, w.i.fuyumi_call),
                h.talk(fuyumi, "別離"),
                h.talk("説得", fuyumi),
                h.look(fuyumi, "自分の小説", "彼女に自分の才能を示す"),
                h.have(w.i.help_mail),
                ),
            ]
    return [w.chaptertitle("展開"),
            *scenes,
            ]


def ep_climax(w: wd.World):
    h = w.hero
    scenes = [
            w.scene("そして自分が死ぬ",
                h.be(w.stage.apart, w.day.current),
                h.think(w.i.help_mail),
                h.do("help", w.futureman),
                h.know(w.futureman, "dead"),
                h.do(w.futureman, "小説を書く"),
                h.be("dead"),
                ),
            ]
    return [w.chaptertitle("これ以上書けない"),
            *scenes,
            ]


def ep_end(w: wd.World):
    h = w.hero
    scenes = [
            w.scene("過去の自分",
                h.be("dead"),
                h.deal(w.terminal),
                h.go("過去に戻る", w.day.schoolday),
                h.go(w.stage.school),
                h.meet(w.pastman),
                ),
            w.scene("小説を書く意味",
                h.know(w.i.his_reason),
                ),
            ]
    return [w.chaptertitle("最後の作品"),
            *scenes,
            ]


# main
def world():
    w = wd.World("100 stories project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS)
    return w


def story(w: wd.World):
    return [w.maintitle("百妄想騙り"),
            ep_intro(w),
            ep_middle(w),
            ep_climax(w),
            ep_end(w),
            ]


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

