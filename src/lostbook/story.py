# -*- coding: utf-8 -*-
"""Story: Lost her book
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.lostbook import config as cnf
THM = cnf.THEMES


# scenes
def sc_myfavorite(w: wd.World):
    return w.scene("本が好きだ",
            w.nao.be(w.stage.town, w.day.current),
            )

def sc_knownews(w: wd.World):
    return w.scene("本屋潰れるって",
            w.nao.know(w.i.vanishshop),
            )

def sc_herbook(w: wd.World):
    return w.scene("彼女の同人誌",
            w.nao.think("全ての本を集める"),
            w.nao.deal("本を集める"),
            )

def sc_holdshop(w: wd.World):
    return w.scene("店を閉める",
            )

def sc_getlastbook(w: wd.World):
    return w.scene("最後の作品",
            w.nao.go(w.saya, "彼女に会う"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("本屋が無くなる町"),
            sc_myfavorite(w),
            sc_knownews(w),
                w.nao.think("彼女の本を全部そろえたい"),
                w.nao.think("人生を救われた"),
                w.nao.go(w.stage.bookshop),
                w.nao.know(w.i.vanishshop),
            )

def ep_buyout(w: wd.World):
    return (w.chaptertitle("買い占めなきゃ"),
            sc_herbook(w),
                w.nao.deal("店が潰れるまでに収集しなきゃ"),
                w.nao.know(w.i.vanishshop),
                w.nao.deal("本を買い集める"),
                w.nao.know("金が足りない"),
            )

def ep_working(w: wd.World):
    return (w.chaptertitle("働く日々"),
                w.nao.deal("働く"),
                w.nao.deal("金を貯める"),
                w.nao.look("バイト探し"),
                w.nao.know("閉店が早まる"),
            )

def ep_closedshop(w: wd.World):
    return (w.chaptertitle("閉店する"),
            sc_holdshop(w),
                w.nao.think("彼女に会いたい"),
                w.nao.know("全ては集められない"),
                w.nao.deal(w.akiko, "頼む"),
                w.nao.know(w.i.her_addr),
            )

def ep_lastbook(w: wd.World):
    return (w.chaptertitle("最後の本"),
            sc_getlastbook(w),
                w.nao.go(w.saya),
                w.nao.know(w.i.her_addr),
                w.nao.meet(w.saya),
                w.nao.know(w.i.her_mind),
            )


def ep_remainheart(w: wd.World):
    return (w.chaptertitle("消えても残るもの"),
                w.nao.know(w.i.her_reason),
                w.nao.meet(w.saya),
                w.nao.ask(w.i.her_reason),
                w.nao.deal("想いを伝えた"),
            )

# test data
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.nao, w.saya),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.nao.think("全ての本を集める"),
                w.nao.know(w.i.vanishshop),
                w.nao.deal("本を集める"),
                w.nao.go(w.saya, "彼女に会う"),
                True),
            ("ep0", ep_intro(w),
                w.nao.think("彼女の本を全部そろえたい"),
                w.nao.think("人生を救われた"),
                w.nao.go(w.stage.bookshop),
                w.nao.know(w.i.vanishshop),
                True),
            ("ep1", ep_buyout(w),
                w.nao.deal("店が潰れるまでに収集しなきゃ"),
                w.nao.know(w.i.vanishshop),
                w.nao.deal("本を買い集める"),
                w.nao.know("金が足りない"),
                True),
            ("ep2", ep_working(w),
                w.nao.deal("働く"),
                w.nao.deal("金を貯める"),
                w.nao.look("バイト探し"),
                w.nao.know("閉店が早まる"),
                True),
            ("ep3", ep_closedshop(w),
                w.nao.think("彼女に会いたい"),
                w.nao.know("全ては集められない"),
                w.nao.deal(w.akiko, "頼む"),
                w.nao.know(w.i.her_addr),
                True),
            ("ep4", ep_lastbook(w),
                w.nao.go(w.saya),
                w.nao.know(w.i.her_addr),
                w.nao.meet(w.saya),
                w.nao.know(w.i.her_mind),
                True),
            ("ep5", ep_remainheart(w),
                w.nao.know(w.i.her_reason),
                w.nao.meet(w.saya),
                w.nao.ask(w.i.her_reason),
                w.nao.deal("想いを伝えた"),
                True),
            ]

# main
def world():
    w = wd.World("Lost her book")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("彼女の本が、消えます"),
            ep_intro(w),
            ep_buyout(w),
            ep_working(w),
            ep_closedshop(w),
            ep_lastbook(w),
            ep_remainheart(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

