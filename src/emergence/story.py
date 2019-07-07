# -*- coding: utf-8 -*-
"""Story: The red emergence
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.emergence import config as cnf
THM = cnf.THEMES


# scenes
def sc_redmoon(w: wd.World):
    miyako = w.miyako
    return w.scene("赤い月",
            miyako.look(w.info("赤い月"),"赤い月を見ていた"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_redmoon(w),
            w.miyako.think(w.aya, w.info("見てない")),
                w.miyako.look(w.aya, w.i.herstatus),
                w.miyako.think(w.aya, w.i.herrefusal),
            )

def ep_chrysalis(w: wd.World):
    return (w.chaptertitle("蛹の少女たち"),
            w.miyako.come(w.stage.ayaroom, w.day.discover1),
            w.miyako.look(w.aya, w.sanagi),
                w.miyako.look(w.kirimura, w.i.hercause),
            )

def ep_reasons(w: wd.World):
    return (w.chaptertitle("彼女たちの理由"),
                w.miyako.know(w.i.aya_mind),
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.miyako, w.aya),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.miyako.look(w.aya, w.i.herstatus),
                w.miyako.think(w.aya, w.i.herrefusal),
                w.miyako.look(w.kirimura, w.i.hercause),
                w.miyako.know(w.i.aya_mind),
                True),
            ]

# main
def world():
    w = wd.World("The red emergence")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("くれなゐの羽化"),
            ep_intro(w),
            ep_chrysalis(w),
            ep_reasons(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

