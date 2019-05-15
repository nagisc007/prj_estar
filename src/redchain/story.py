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
    ma = w.masuda
    scenes = [
            w.scene("取材",
                ma.know(w.i.case_fire, w.stage.office, w.day.incident),
                ma.think(w.hideko, "何か臭う"),
                ma.deal(w.i.interview, w.stage.thesite),
                ma.hear("関係者"),
                ma.know(w.deadbody, w.hideko),
                ),
            ]
    return [
            w.chaptertitle("焼死体二つ"),
            *scenes,
            ]


def ep_idolyears(w: wd.World):
    ma = w.masuda
    scenes = [
            w.scene("元プロデューサー",
                ma.know(w.h_idol),
                ma.look(w.h_idol, w.i.life),
                ma.come(w.stage.idoloffice, w.day.interview2),
                ma.deal(w.i.interview, "当時を知る人"),
                ma.know(w.i.retire_business),
                ),
            ]
    return [w.chaptertitle("アイドル時代"),
            *scenes,
            ]


def ep_actoryears(w: wd.World):
    # NOTE: 女優時代の方が知名度があるのでこちらを先に調査
    ma = w.masuda
    scenes = [
            w.scene("同業者",
                ma.know(w.h_actor),
                ma.look(w.h_actor, w.i.life),
                ma.deal(w.i.interview, w.stage.theater, w.day.interview1),
                ma.deal(w.i.interview, "業界人"),
                ma.know(w.hideko, w.h_idol),
                ),
            ]
    return [w.chaptertitle("女優時代"),
            *scenes,
            ]


def ep_lateyears(w: wd.World):
    ma = w.masuda
    scenes = [
            w.scene("町の人々への聞き込み",
                ma.know(w.h_later),
                ma.have(w.h_later, w.i.life),
                ma.come(w.stage.town, w.day.interview3),
                ma.deal(w.i.interview, w.stage.town),
                ma.know(w.doc),
                ),
            ]
    return [w.chaptertitle("晩年のこと"),
            *scenes,
            ]


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
            # TODO
                ma.look(cnf.THEMES["chain"]),
                ),
            ]
    return [w.chaptertitle("彼女の真実"),
            *scenes,
            ]


# main
def world():
    w = wd.World("The red-chain")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("紅い繋がり"),
            ep_intro(w),
            ep_idolyears(w),
            ep_actoryears(w),
            ep_lateyears(w),
            ep_truth(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

