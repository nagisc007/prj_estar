# -*- coding: utf-8 -*-
"""Story: the emperor 100
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.emperor100 import config as cnf


# episodes
def ep_intro(w: wd.World):
    h, lion = w.hero, w.lion
    return [w.chaptertitle("皇帝の死"),
            h.be(w.stage.castle, w.day.ceremony),
            h.be(w.i.throne, "次期皇帝"),
            h.be("皇帝の息子"),
            lion.be("dead"),
            h.know(w.i.throne),
            ]


def ep_preparation(w: wd.World):
    h, milea, garneth = w.hero, w.milea, w.garneth
    return [w.chaptertitle("儀式の準備"),
            h.be(w.stage.castle, w.day.dead),
            garneth.talk(h, w.i.throne),
            h.be(w.i.throne, "$must"),
            h.know(w.i.lion_dead),
            h.talk(garneth, w.i.throne),
            h.be(w.i.throne, w.i.emperor100),
            h.remember(w.i.murder_mam),
            h.talk(milea, w.i.emperor_bug),
            h.know(w.i.milea_mind),
            ]


def ep_ceremony(w: wd.World):
    h, milea, garneth, child = w.hero, w.milea, w.garneth, w.child
    return [w.chaptertitle("百代目のバグ"),
            h.be(w.stage.hisroom, w.day.ceremony),
            h.think("whether", w.i.throne),
            h.be(w.i.ceremony, "時間が迫る"),
            h.do(w.i.his_mind),
            w.hero.do(w.i.enthrone),
            w.hero.be(w.i.portchara, "強制的に"),
            w.hero.do(w.milea, "殺害"),
            h.ask(garneth, "儂は皇帝か？"),
            garneth.reply("yes"),
            h.look(child),
            h.talk(child, "お前もいずれ最愛の者を殺す"),
            ]


# main
def world():
    w = wd.World("100 characters")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("皇帝百代のバグ"),
            ep_intro(w),
            ep_preparation(w),
            ep_ceremony(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

