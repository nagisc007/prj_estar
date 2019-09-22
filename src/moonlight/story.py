# -*- coding: utf-8 -*-
"""Story: moonlight
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.moonlight import config as cnf
THM = cnf.THEMES


# scenes
def sc_darkhome(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("真っ暗な家の中で",
            h.be(w.stage.myhome, w.day.current),
            luna.talk("おかえり"),
            # NOTE: 真っ暗な家に戻ってきて、ハープだけが聞こえる、人物紹介兼ねて
            )

def sc_alwayshelp(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("いつでも助けたい",
            # NOTE: 仕事にでかけるいつもの朝の様子、不安症の夫
            # NOTE: 会社に行く途中でヘルプマークの人を助ける夫
            )

def sc_alonegoout(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("孤独な外出",
            # NOTE: 彼女が公演で不在、一人孤独、LINEで「月が見える？」と
            )

def sc_fight(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("二人の喧嘩",
            # NOTE: 月のこと（自分がいなくても大丈夫な彼女）で口論になり、出ていく
            )

def sc_worldtone(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("音の世界",
            # NOTE: 出張中、彼女の音が聞こえてくる、音の世界を思い出し、帰る
            )

def sc_lookmoon(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("月を見る、月を聞く",
            # NOTE: 真っ暗な部屋、彼女の音だけ、スマホで月の音を、月を二人で聞く
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            # NOTE: 目が見えない女性とその夫の物語
            sc_darkhome(w),
            )

def ep_yourhelp(w: wd.World):
    return (w.chaptertitle("君の助けに"),
            # NOTE: ずっといつでも君を助ける側でありたい男性
            sc_alwayshelp(w),
            sc_alonegoout(w),
            sc_fight(w),
            )

def ep_hearmoonlight(w: wd.World):
    return (w.chaptertitle("月を聞く"),
            # NOTE: 彼女が月を聞くことで見ていたのが理解できた
            sc_worldtone(w),
            sc_lookmoon(w),
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.goro, w.luna),
            ]

def story_outlines(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The girl hearing a moonlight")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("月を聴く彼女"),
            ep_intro(w),
            ep_yourhelp(w),
            ep_hearmoonlight(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

