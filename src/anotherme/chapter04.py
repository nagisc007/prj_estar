# -*- coding: utf-8 -*-
"""Story: chapter 04: The another me
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_dadtalk(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("父の話",
            # TODO: 父が部屋を見て、話す、いい人、苦手。IFたち怯える
            )

def sc_univlife(w: wd.World):
    kyoko, shota, matsu = w.kyoko, w.shota, w.matsumoto
    return w.scene("三番目との大学生活",
            # TODO: 三番目の意味、夏休みに入る
            kyoko.come(w.stage.univ, w.day.current),
            kyoko.meet(matsu),
            )

def sc_rebellion(w: wd.World):
    kyoko, shota, matsu = w.kyoko, w.shota, w.matsumoto
    return w.scene("三番目の反乱",
            # TODO: ボランティア日、三番目が邪魔する、翔太郎が救世主
            kyoko.deal("四人の暮らし"),
            kyoko.deal("みんな出ていった"),
            )

def sc_shotarowork(w: wd.World):
    return w.scene("翔太郎と一緒",
            # TODO: 翔太郎とカフェ（伏線）、
            )

def sc_promisedate(w: wd.World):
    return w.scene("デートの約束",
            )

def sc_sapporo(w: wd.World):
    return w.scene("札幌",
            )

def sc_hotel(w: wd.World):
    return w.scene("ホテルで",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("父と私"),
            sc_dadtalk(w),
            )

def ep_anotherproblem(w: wd.World):
    return (w.chaptertitle("三番目の反乱"),
            sc_univlife(w),
            sc_rebellion(w),
            sc_shotarowork(w),
            )

def ep_moreanother(w: wd.World):
    return (w.chaptertitle("そして彼は消えた"),
            sc_promisedate(w),
            sc_sapporo(w),
            sc_hotel(w),
            )

# outline
def base_info(w: wd.World):
    return ("chapter4", story(w), w.kyoko, w.matsumoto)

def story_outline(w: wd.World):
    return [
            ]

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            ep_intro(w),
            ep_anotherproblem(w),
            ep_moreanother(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

