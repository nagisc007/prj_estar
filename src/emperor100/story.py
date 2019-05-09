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
    h, lion, milea, garneth = w.hero, w.lion, w.milea, w.garneth
    scenes = [
            w.scene("父の帰還",
                w.tag.comment("ここで簡単な世界観説明"),
                h.be(w.stage.castle, w.day.returnemp),
                h.look(w.stage.balcony, "父の帰還"),
                h.talk(milea, "父の功績"),
                milea.talk(h, "次の皇帝"),
                h.look(milea, w.i.pregnancy.flag()),
                h.be(w.i.throne, "次期皇帝"),
                h.be("皇帝の息子"),
                ),
            w.scene("継承の不安",
                h.go(w.stage.hall, "父を出迎え"),
                lion.come("here"),
                lion.talk(h, "孫の無事を確認"),
                lion.feel(w.i.badcondition.flag()),
                h.ask(w.i.peace_nego),
                lion.reply("上々"),
                garneth.come(),
                h.look(garneth, w.i.pope),
                h.think(w.i.pope, "マルダ教の最高司祭"),
                garneth.ask(lion, "ちょっと用件が"),
                h.look(lion, garneth, "行ってしまう"),
                ),
            w.scene("父の死去",
                lion.be("dead"),
                garneth.talk(h, lion, w.i.badcondition.deflag()),
                h.think(w.i.lion_dead),
                garneth.talk(h, w.i.enthrone),
                h.know(w.i.throne),
                ),
            ]
    return [w.chaptertitle("皇帝の死"),
            *scenes,
            ]


def ep_preparation(w: wd.World):
    h, milea, garneth = w.hero, w.milea, w.garneth
    scenes = [
            h.be(w.stage.castle, w.day.dead),
            garneth.talk(h, w.i.throne),
            h.be(w.i.throne, "$must"),
            h.know(w.i.lion_dead),
            h.talk(garneth, w.i.throne),
            h.be(w.i.throne, w.i.emperor100),
            h.remember(w.i.murder_mam),
            h.talk(milea, w.i.emperor_bug),
            h.know(w.i.milea_mind),
            # TODO
            h.know(w.i.childbirth, w.i.pregnancy.deflag()),
            ]
    return [w.chaptertitle("儀式の準備"),
            *scenes,
            ]


def ep_ceremony(w: wd.World):
    h, milea, garneth, child = w.hero, w.milea, w.garneth, w.child
    scenes = [
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
    return [w.chaptertitle("百代目のバグ"),
            *scenes,
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

