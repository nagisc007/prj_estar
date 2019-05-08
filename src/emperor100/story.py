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


# main
def world():
    w = wd.World("100 characters")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("皇帝百代のバグ"),
            w.hero.be(w.stage.castle, w.day.ceremony),
            w.lion.be("dead"),
            w.hero.talk(w.garneth, w.i.throne),
            w.hero.be(w.i.throne, w.i.emperor100),
            w.hero.do(w.i.enthrone),
            w.hero.be(w.i.portchara),
            w.hero.do(w.milea, "殺害"),
        )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

