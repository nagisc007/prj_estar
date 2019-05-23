# -*- coding: utf-8 -*-
"""Chapter 05: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.redchain import config as cnf
THM = cnf.THEMES


# scenes

# episodes
def ep_truth(w: wd.World):
    ma = w.masuda
    scenes = [
            w.scene("検死結果",
                ma.come(w.stage.medicals, w.day.interview3),
                ma.know(w.doc),
                ma.meet(w.doc),
                ma.talk(w.doc, w.i.doc_secret),
                ma.hear(w.doc, w.deadbody),
                ma.know(w.anotherbody, w.benio),
                ma.know(w.i.truth),
                ),
            w.scene("火災現場にて",
                ma.come(w.stage.thesite),
                ma.look("再度調査"),
                ma.meet(w.sugioka),
                ),
            w.scene("杉岡と",
                ma.come(w.stage.bar),
                ma.talk(w.sugioka, w.hideko),
                w.sugioka.talk("彼女の男の話"),
                ),
            w.scene("役場の対応",
                ma.come(w.stage.townoffice),
                ma.meet(w.hino),
                ma.hear(w.hino, w.i.deal_deads),
                ),
            w.scene("遺体の果て",
                ma.come(w.stage.temple),
                ma.meet(w.priest),
                ma.hear(w.priest, w.i.deal_deads),
                ma.think(cnf.THEMES["chain"]),
                ),
            ]
    return [w.chaptertitle("彼女の真実"),
            *scenes,
            ]

# main
def story(w: wd.World):
    return ep_truth(w)


def main(): # pragma: no cover
    from src.redchain.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

