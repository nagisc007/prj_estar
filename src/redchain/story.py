# -*- coding: utf-8 -*-
"""Story: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.redchain import config as cnf
from src.redchain import chapter01 as chap1
from src.redchain import chapter02 as chap2
from src.redchain import chapter03 as chap3
from src.redchain import chapter04 as chap4
from src.redchain import chapter05 as chap5
from src.redchain import chapter06 as chap6
THM = cnf.THEMES


# main
def world():
    w = wd.World("The red-chain")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("紅い繋がり"),
            chap1.story(w),
            chap2.story(w),
            chap3.story(w),
            chap4.story(w),
            chap5.story(w),
            chap6.story(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

