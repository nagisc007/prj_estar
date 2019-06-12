# -*- coding: utf-8 -*-
"""Story: chapter 04: The another me
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_disliked(w: wd.World):
    kyoko, shota = w.kyoko, w.shota
    return w.scene("自分を嫌う自分",
            kyoko.look(w.another),
            kyoko.be(w.stage.apart, w.day.proposed),
            kyoko.think("自分が増えてどうするか"),
            )

def sc_univlife(w: wd.World):
    kyoko, shota, matsu = w.kyoko, w.shota, w.matsumoto
    return w.scene("アナザーとの大学生活",
            kyoko.come(w.stage.univ),
            kyoko.meet(matsu),
            )

def sc_rebellion(w: wd.World):
    kyoko, shota, matsu = w.kyoko, w.shota, w.matsumoto
    return w.scene("アナザーたちの反乱",
            kyoko.deal("四人の暮らし"),
            kyoko.deal("みんな出ていった"),
            )

def sc_matsumoto(w: wd.World):
    kyoko, shota, matsu = w.kyoko, w.shota, w.matsumoto
    return w.scene("松本",
            matsu.talk("呼び止められる"),
            kyoko.deal(matsu, "会話"),
            matsu.ask("最近一緒にいる奴いないな"),
            matsu.ask("男じゃなく、女"),
            kyoko.think(matsu, w.i.look_another),
            )

def sc_knownanother(w: wd.World):
    kyoko, shota, matsu, asumi = w.kyoko, w.shota, w.matsumoto, w.asumi
    return w.scene("アナザーと暮らす男",
            kyoko.come(w.stage.ma_apart),
            kyoko.look(asumi),
            matsu.feel("驚き"),
            asumi.talk("自分が見えるの？"),
            kyoko.know(matsu, w.i.look_another),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("四人目のアナザー"),
            sc_disliked(w),
            )

def ep_anotherproblem(w: wd.World):
    return (w.chaptertitle("もう一人は我慢しない"),
            sc_univlife(w),
            sc_rebellion(w),
            )

def ep_moreanother(w: wd.World):
    return (w.chaptertitle("自分以外のアナザー"),
            sc_matsumoto(w),
            sc_knownanother(w),
            )

# outline
def base_info(w: wd.World):
    return ("chapter4", story(w), w.kyoko, w.matsumoto)

def story_outline(w: wd.World):
    return [
            ("chapter4", story(w),
            w.kyoko.think("自分が増えてどうするか"),
            w.kyoko.look(w.another),
            w.kyoko.deal("四人の暮らし"),
            w.kyoko.know(w.matsumoto, w.i.look_another),
            True),
            ]

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            ep_intro(w),
            ep_anotherproblem(w),
            ep_moreanother(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

