# -*- coding: utf-8 -*-
"""Story: The blue ghost
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
from src.bghost import chapter01 as ch01
from src.bghost import chapter02 as ch02
from src.bghost import chapter03 as ch03
from src.bghost import chapter04 as ch04
from src.bghost import chapter05 as ch05
THM = cnf.THEMES


# outline
def story_baseinfos(w: wd.World):
    return [
            ] + ch01.story_baseinfo(w) \
                + ch02.story_baseinfo(w) \
                + ch03.story_baseinfo(w) \
                + ch04.story_baseinfo(w) \
                + ch05.story_baseinfo(w)

def story_outlines(w: wd.World):
    return [
            ] + ch01.story_outline(w) \
                + ch02.story_outline(w) \
                + ch03.story_outline(w) \
                + ch04.story_outline(w) \
                + ch05.story_outline(w)

# main
def world():
    w = wd.World("The blue ghost")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("青春ゴースト"),
            ch01.story(w),
            ch02.story(w),
            ch03.story(w),
            ch04.story(w),
            ch05.story(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

