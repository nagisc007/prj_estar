# -*- coding: utf-8 -*-
"""Story: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.redchain import config as cnf


# episodes
def ep_intro(w: wd.World):
    return [
            w.masuda.know(w.i.case_fire, w.stage.office, w.day.incident),
            w.masuda.think(w.hideko, "何か臭う"),
            w.masuda.deal(w.i.interview),
            w.masuda.hear(w.doc, w.deadbody),
            w.masuda.know(w.i.truth),
            # TODO
            w.masuda.look(cnf.THEMES["chain"]),
            ]


# main
def world():
    w = wd.World("The red-chain")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("紅い繋がり"),
            ep_intro(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

