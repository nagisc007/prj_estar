# -*- coding: utf-8 -*-
"""Story: lv1 yusha.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from . import config as cnf

# episodes


# main
def world():
    w = wd.World("lv1 yusha project")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w


def story(w: wd.World):
    return (w.maintitle("レベル１勇者の旅立ち"),
            w.hero.be("live", w.stage.alaban),
            w.hero.do(w.i.callhero, w.day.first),
            w.hero.go(w.stage.castle),
            w.hero.meet(w.stage, w.king),
            w.king.talk(w.hero, w.i.reviveboss),
            w.hero.know(w.i.reviveboss),
            w.king.ask(w.hero, w.i.voyage),
            w.hero.reply(w.king, w.i.voyage),
            w.hero.go(w.i.voyage, "$must"),
            w.hero.go(w.stage.field1),
            w.hero.meet(w.daemon1),
            w.hero.be(w.daemon1, w.i.deadly),
            w.hero.do(w.hero99, "rescue"),
            w.hero.know(w.hero99, w.i.worldsecret),
            w.hero.have(w.hero99, w.i.coop),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

