# -*- coding: utf-8 -*-
"""Story: The blue ghost
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
THM = cnf.THEMES


# scenes

# episodes
# chapters
def ch1(w: wd.World):
    return (w.chaptertitle("序章"),
            # NOTE: 小学校が廃校になり、同窓会に集まる仲良しメンバ、そこにイレギュラーな彼女
            # NOTE: 地縛霊という少年を見つける、本物？　少年ホームレス？
            )

def ch2(w: wd.World):
    return (w.chaptertitle("序盤"),
            # NOTE: ゴーストを成仏させることになる、それが元同好会の最後の成果
            )

def ch3(w: wd.World):
    return (w.chaptertitle("中盤"),
            # NOTE: それぞれがバラバラになる、ゴーストが嘘と発覚
            )

def ch4(w: wd.World):
    return (w.chaptertitle("終盤"),
            # NOTE: 本物のゴーストを見つけてしまう、彼女を成仏させるために苦労する
            )

def ch5(w: wd.World):
    return (w.chaptertitle("エピローグ"),
            # NOTE: 彼女との別離、大人になること
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ]

def story_outlines(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The blue ghost")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("青春ゴースト"),
            ch1(w),
            ch2(w),
            ch3(w),
            ch4(w),
            ch5(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

