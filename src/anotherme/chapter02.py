# -*- coding: utf-8 -*-
"""Story: chapter 02: The another me
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_visited(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("訪問者",
            # TODO: 翔太郎の説明、見える説明、プロポーズ
            shota.come(w.stage.apart, w.day.encounter),
            kyoko.deal(shota, w.i.proposed),
            )

def sc_canlook(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("見える人",
            # TODO: いつの間にか帰っている。わたし会議まで
            shota.look(w.another),
            kyoko.think(shota, "知りたい"),
            )

def sc_mymeeting(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("わたし会議",
            # TODO: 三人で翔太郎について。意見の相違、結論出ない
            )

def sc_notfound(w: wd.World):
    return w.scene("彼は見つからない",
            )

def sc_hisvisit(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("彼の再訪",
            # TODO: 本気のプロポーズ、三番目誕生
            )

def sc_birthnew(w: wd.World):
    return w.scene("三番目の今日子",
            )

def sc_livewith(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("同棲",
            kyoko.deal("一緒に暮らす"),
            )

def sc_hispropose(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("プロポーズ",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("ワタシが見える人"),
            sc_visited(w),
            sc_canlook(w),
            )

def ep_rebellion(w: wd.World):
    return (w.chaptertitle("ワタシの反乱"),
            sc_mymeeting(w),
            sc_notfound(w),
            sc_hisvisit(w),
            sc_birthnew(w),
            )

def ep_confess(w: wd.World):
    return (w.chaptertitle("彼の告白"),
            sc_livewith(w),
            sc_hispropose(w),
            )

# outline
def base_info(w: wd.World):
    return ("chapter2", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return [
            ("chapter2", story(w),
            w.kyoko.think(w.shota, "知りたい"),
            w.shota.look(w.another),
            w.kyoko.deal("一緒に暮らす"),
            w.kyoko.deal(w.shota, w.i.proposed),
            True),
            ]

# main
def story(w: wd.World):
    return [w.maintitle("わたしと彼"),
            ep_intro(w),
            ep_rebellion(w),
            ep_confess(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

