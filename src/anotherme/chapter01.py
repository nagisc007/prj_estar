# -*- coding: utf-8 -*-
"""Story: chapter 01: The another me.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_campuslife(w: wd.World):
    kyoko = w.kyoko
    return w.scene("大学生活",
            kyoko.be(w.stage.univ, w.day.current),
            )

def sc_mytable(w: wd.World):
    kyoko = w.kyoko
    return w.scene("わたしたちの食卓",
            kyoko.be(w.another, "一緒に暮らす"),
            kyoko.deal("面倒見る", w.another),
            kyoko.look(w.another),
            kyoko.deal("生活する", w.another),
            kyoko.think("他人と付き合えない"),
            kyoko.look("３つある茶碗"),
            )

def sc_friendA(w: wd.World):
    kyoko, sayama, matsu = w.kyoko, w.sayama, w.matsumoto
    return w.scene("友人A",
            kyoko.deal(sayama, "電話"),
            sayama.talk(w.i.circle),
            kyoko.think(THM["problem"]),
            kyoko.feel(w.another, "邪魔"),
            kyoko.think(w.i.vanish_another),
            kyoko.go("彼女たちのいない場所"),
            )

def sc_circleact(w: wd.World):
    kyoko, sayama, matsu = w.kyoko, w.sayama, w.matsumoto
    return w.scene("サークル活動",
            kyoko.go(w.i.circle, "逃げ出す"),
            kyoko.go(w.another, "家に帰る"),
            )

def sc_strangeday(w: wd.World):
    kyoko, shota, sayama = w.kyoko, w.shota, w.sayama
    return w.scene("奇妙な日",
            kyoko.come(w.stage.univ),
            kyoko.deal("授業"),
            kyoko.hear(w.i.stalker.flag()),
            kyoko.look(shota, "知らない男子"),
            )

def sc_parttimer(w: wd.World):
    kyoko, arase, minori = w.kyoko, w.arase, w.minori
    return w.scene("パートのお時間",
            kyoko.go(w.i.partwork),
            kyoko.go(w.stage.office),
            kyoko.deal("データ入力の仕事"),
            kyoko.deal(w.i.relation, "$must"),
            kyoko.think("人間関係の問題"),
            )

def sc_meetboy(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("彼と出会った",
            kyoko.come(w.stage.apart),
            kyoko.look(shota, "不審者", w.i.stalker.deflag()),
            kyoko.meet(w.shota),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("ワタシが見える"),
            sc_campuslife(w),
            sc_mytable(w),
            )

def ep_mylife(w: wd.World):
    return (w.chaptertitle("わたしの日常"),
            sc_friendA(w),
            sc_circleact(w),
            )

def ep_unknownboy(w: wd.World):
    return (w.chaptertitle("知らない男の子"),
            sc_strangeday(w),
            sc_parttimer(w),
            sc_meetboy(w),
            )

# test data
def base_info(w: wd.World):
    return ("chapter1", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return [
            ("chapter1", story(w),
                w.kyoko.think("他人と付き合えない"),
                w.kyoko.look(w.another),
                w.kyoko.go(w.i.circle, "逃げ出す"),
                w.kyoko.meet(w.shota),
            True),
            ("chapter1-avant", ep_intro(w),
                w.kyoko.deal("面倒見る", w.another),
                w.kyoko.be(w.another, "一緒に暮らす"),
                w.kyoko.deal("生活する", w.another),
                w.kyoko.look(w.another),
                True),
            ("chapter1-A", ep_mylife(w),
                w.kyoko.think(w.i.vanish_another),
                w.kyoko.feel(w.another, "邪魔"),
                w.kyoko.go("彼女たちのいない場所"),
                w.kyoko.go("家に帰る", w.another),
                True),
            ("chapter1-B", ep_unknownboy(w),
                w.kyoko.deal(w.i.relation, "$must"),
                w.kyoko.think("人間関係の問題"),
                w.kyoko.go(w.i.partwork),
                w.kyoko.meet(w.shota),
                True),
            ]

# main
def story(w: wd.World):
    return [w.maintitle("わたしとワタシ"),
            ep_intro(w),
            ep_mylife(w),
            ep_unknownboy(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

