# -*- coding: utf-8 -*-
"""Story: chapter 05: The another me
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_anyones(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("望んだはずの空虚",
            kyoko.be(w.stage.apart, w.day.empty),
            kyoko.think("何かが違う"),
            kyoko.look("not", shota),
            kyoko.know(w.i.another_truth),
            kyoko.look(w.his_phone),
            )

def sc_hismanshion(w: wd.World):
    kyoko, shota, dad = w.kyoko, w.shota, w.sho_dad
    return w.scene("彼の家",
            kyoko.come(w.stage.hishome),
            kyoko.meet(dad),
            kyoko.deal("調査", shota),
            )

def sc_hisvanish(w: wd.World):
    kyoko, shota, dad = w.kyoko, w.shota, w.sho_dad
    return w.scene("彼はもういない",
            kyoko.deal("vanish", w.shota),
            kyoko.talk(dad, "彼について"),
            dad.explain(w.i.shota_truth),
            )

def sc_hischildhood(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("彼の子供時代のこと",
            )

def sc_alone(w: wd.World):
    return w.scene("今日子ひとり",
            # TODO: 彼とか好きじゃなく、ただ自分の理解者が欲しかっただけだった
            )

def sc_knowntruth(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("知らされた真実",
            kyoko.know(w.i.shota_truth),
            )

def sc_goodbyeanothers(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("さよならアナザー",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("誰もいない"),
            sc_anyones(w),
            )

def ep_hishome(w: wd.World):
    return (w.chaptertitle("彼の実家"),
            sc_hismanshion(w),
            sc_hisvanish(w),
            )

def ep_truth(w: wd.World):
    return (w.chaptertitle("真実と真相"),
            sc_hischildhood(w),
            sc_knowntruth(w),
            )

def ep_epilogue(w: wd.World):
    return (w.chaptertitle("エピローグ"),
            sc_goodbyeanothers(w),
            )

# outline
def base_info(w: wd.World):
    return ("chapter5", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return [
            ("chapter5", story(w),
            w.kyoko.know(w.i.another_truth),
            w.kyoko.look("not", w.shota),
            w.kyoko.deal("調査", w.shota),
            w.kyoko.know(w.i.shota_truth),
            True),
            ]

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            ep_intro(w),
            ep_hishome(w),
            ep_truth(w),
            ep_epilogue(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

