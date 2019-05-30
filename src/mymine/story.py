# -*- coding: utf-8 -*-
"""Story: I am my mine
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.mymine import config as cnf
from src.mymine import chapter01 as chap1
from src.mymine import chapter02 as chap2
from src.mymine import chapter03 as chap3
from src.mymine import chapter04 as chap4
from src.mymine import chapter05 as chap5
THM = cnf.THEMES


# episodes
# main
def world():
    w = wd.World("I am my mine")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("わたしとワタシと私"),
            chap1.story(w),
            chap2.story(w),
            chap3.story(w),
            chap4.story(w),
            chap5.story(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

