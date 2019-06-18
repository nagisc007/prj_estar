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
            )

def ep_buyout(w: wd.World):
    return (w.chaptertitle("買い占めなきゃ"),
            sc_herbook(w),
            )

def ep_working(w: wd.World):
    return (w.chaptertitle("働く日々"),
            )

def ep_closedshop(w: wd.World):
    return (w.chaptertitle("閉店する"),
            sc_holdshop(w),
            )

def ep_lastbook(w: wd.World):
    return (w.chaptertitle("最後の本"),
            sc_getlastbook(w),
            )


def ep_remainheart(w: wd.World):
    return (w.chaptertitle("消えても残るもの"),
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

