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
def sc_afraid(w: wd.World):
    kyoko, shota, child, stu, univ = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("怯え",
            kyoko.be(w.stage.living, w.day.volunteer),
            # TODO: 会うことになった、四番目との対峙、怯え
            )

def sc_testperiot(w: wd.World):
    kyoko, shota, child, stu, univ = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("テスト期間",
            kyoko.be(w.stage.library, w.day.report1),
            # TODO: 試験が手に付かない、四番目の影
            )

def sc_meetingdad(w: wd.World):
    kyoko, shota, child, stu, univ = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("父の出迎え",
            kyoko.be(w.stage.station, w.day.dadvisit),
            )

def sc_dadtalk(w: wd.World):
    kyoko, shota, child, stu, univ = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("父の話",
            kyoko.be(w.stage.famires),
            # TODO: 父が部屋を見て、話す、いい人、苦手。IFたち怯える
            )

def sc_dadcomming(w: wd.World):
    kyoko, shota, child, stu, univ = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("父と私たち",
            )

def sc_univlife(w: wd.World):
    kyoko, shota, matsu = w.kyoko, w.shota, w.matsumoto
    return w.scene("三番目との大学生活",
            # TODO: 三番目の意味、夏休みに入る
            kyoko.come(w.stage.univ, w.day.current),
            kyoko.meet(matsu),
            ).omit()

def sc_rebellion(w: wd.World):
    kyoko, shota, matsu = w.kyoko, w.shota, w.matsumoto
    return w.scene("三番目の反乱",
            # TODO: ボランティア日、三番目が邪魔する、翔太郎が救世主
            kyoko.deal("四人の暮らし"),
            kyoko.deal("みんな出ていった"),
            )

def sc_shotarowork(w: wd.World):
    kyoko, shota, child, stu, univ = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
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
    return (w.chaptertitle("混乱する私"),
            sc_afraid(w),
            )

def ep_anotherproblem(w: wd.World):
    return (w.chaptertitle("父親と友だちと私たちと"),
            sc_testperiot(w),
            sc_meetingdad(w),
            sc_dadtalk(w),
            sc_dadcomming(w),
            sc_univlife(w),# NOTE: omit
            sc_rebellion(w),
            )

def ep_moreanother(w: wd.World):
    return (w.chaptertitle("そして彼は消えた"),
            sc_shotarowork(w),
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
    return [w.chaptertitle(cnf.TITLE["chap4"]),
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

