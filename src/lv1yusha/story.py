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
def ep_intro(w: wd.World):
    outfield = w.stage.field1.insided("町の外")
    return [w.chaptertitle("旅立ちまでの序章"),
            w.tag.comment("なるべく説明文じゃなく世界観説明"),
            w.hero.do("襲われた", w.i.monster, outfield, w.day.childhood),
            w.hero.do("助けられた", w.father),
            w.day.first.explain("歳月が過ぎた"),
            w.hero.do("剣の練習", w.bazem, w.stage.church, w.day.first),
            w.bazem.talk(w.hero, w.i.monster),
            w.bazem.talk(w.hero, w.i.dadlost),
            w.hero.know(w.i.dadlost),
            w.hero.go(w.i.voyage),
            w.hero.be(w.i.becomeyusha),
            w.hero.go(w.stage.myhome, "朝食"),
            w.hero.talk(w.mother, w.i.dadlost),
            w.hero.talk(w.mother, w.i.callhero),
            w.hero.do(w.i.callhero, w.day.first),
            w.hero.go(w.stage.castle),
            ]


def ep_heros_sun(w: wd.World):
    return [w.chaptertitle("英雄の息子"),
            w.hero.go(w.stage.castle, "$must"),
            w.hero.go(w.stage.myhome),
            w.hero.deal(w.i.callhero),
            w.hero.meet(w.stage.castle, w.king, w.day.first),
            w.king.talk(w.hero, w.i.reviveboss),
            w.hero.know(w.i.reviveboss),
            w.king.ask(w.hero, w.i.voyage),
            w.hero.reply(w.king, w.i.voyage),
            w.hero.go(w.i.voyage, "$must"),
            w.hero.deal(w.king, w.i.bustered),
            ]


def ep_allies(w: wd.World):
    return [w.chaptertitle("初めての仲間"),
            w.hero.deal(w.i.gatherally),
            w.hero.know(w.marc, w.i.gatherally),
            w.hero.go(w.stage.bar, w.day.first),
            w.hero.meet(w.diana, w.kult, w.maririn),
            w.hero.talk(w.diana, w.i.voyage),
            w.hero.have(w.diana, w.i.coop),
            ]


def ep_destruction(w: wd.World):
    return [w.chaptertitle("全滅"),
            w.hero.know(w.diana, w.stage.tower1),
            w.hero.go(w.stage.tower1, "$must"),
            w.hero.go(w.stage.field1, w.day.first),
            w.hero.go("walk", w.stage.tower1),
            w.hero.meet(w.daemon1),
            w.hero.be(w.daemon1, w.i.deadly),
            w.hero.be(w.i.massacre),
            ]


def ep_anotherhero(w: wd.World):
    return [w.chaptertitle("もう一人の勇者"),
            w.hero.do("生き延びる"),
            w.hero.be(w.i.massacre),
            w.hero.go("runaway"),
            w.hero.be(w.stage.field1, w.day.first),
            w.hero.think("死を覚悟"),
            w.hero.do(w.hero99, "rescue"),
            w.hero.know(w.hero99, w.i.worldsecret),
            w.hero.have(w.hero99, w.i.coop),
            ]


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
            ep_intro(w),
            ep_heros_sun(w),
            ep_allies(w),
            ep_destruction(w),
            ep_anotherhero(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

