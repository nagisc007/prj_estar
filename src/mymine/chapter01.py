# -*- coding: utf-8 -*-
"""Story: chapter 01: I am my mine
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.mymine import config as cnf
THM = cnf.THEMES


# scenes
def sc_campuslife(w: wd.World):
    k = w.kyoko
    return w.scene("大学生活",
            k.be(w.stage.univ, w.day.current),
            )

def sc_mytable(w: wd.World):
    k = w.kyoko
    return w.scene("わたしたちの食卓",
            k.look(w.another),
            k.think("他人と付き合えない"),
            k.look("３つある茶碗"),
            )

def sc_friendA(w: wd.World):
    k = w.kyoko
    return w.scene("友人A",
            k.think(THM["problem"]),
            k.go(w.circle, "逃げ出す"),
            )

def sc_meetboy(w: wd.World):
    k = w.kyoko
    return w.scene("彼と出会った",
            k.meet(w.shota),
            )

# episodes
def ep_intro(w: wd.World):
    k = w.kyoko
    return (w.chaptertitle("ワタシが見える"),
            sc_campuslife(w),
            sc_mytable(w),
            )

def ep_mylife(w: wd.World):
    return (w.chaptertitle("わたしの日常"),
            sc_friendA(w),
            )

def ep_unknownboy(w: wd.World):
    return (w.chaptertitle("知らない男の子"),
            sc_meetboy(w),
            )

# test data
def base_info(w: wd.World):
    return ("chapter1", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return ("chapter1", story(w),
            w.kyoko.think("他人と付き合えない"),
            w.kyoko.look(w.another),
            w.kyoko.go(w.circle, "逃げ出す"),
            w.kyoko.meet(w.shota),
            True)

# main
def story(w: wd.World):
    return [w.maintitle("わたしとワタシ"),
            ep_intro(w),
            ep_mylife(w),
            ep_unknownboy(w),
            ]


def main(): # pragma: no cover
    from src.mymine.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

