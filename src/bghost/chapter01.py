# -*- coding: utf-8 -*-
"""Story: chapter 01
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.bghost import config as cnf
THM = cnf.THEMES

# scenes
def sc_horrortalk(w: wd.World):
    h = ryoma = w.ryoma
    takeru, w.akari = w.takeru, w.akari
    return w.scene("恐い話",
            h.be(w.stage.classroom, w.day.kaidan),
            # NOTE: 主人公視点一人称で
            # NOTE: 空き教室に集まっていつものメンバで恐い話をする
            # NOTE: そこから懐かしい小学校時代の思い出と、別の学校に行った彼女のこと
            )

def sc_oldschool(w: wd.World):
    return w.scene("解体になる小学校",
            # NOTE: 通った小学校が解体になると聞く
            # NOTE: 忘れ物を思い出す。取りに行こうぜ
            )

def sc_lostarticle(w: wd.World):
    return w.scene("あの頃の忘れ物",
            # NOTE: 旧校舎に忍び込む。忘れ物を取りに。そこで幽霊を見る
            )

def sc_checkghost(w: wd.World):
    return w.scene("幽霊を探しに",
            # NOTE: 幽霊の確認に戻り、懐かしい転校していった彼女と再会
            )

def sc_clubagain(w: wd.World):
    return w.scene("もう一度同好会を",
            # NOTE: 同好会をやろうと提案。夏休みの間だけ。そして幽霊を探そうと
            )

def sc_findghost(w: wd.World):
    return w.scene("幽霊を見つけた",
            # NOTE: 幽霊を見つける、少年の。本物？
            )

def sc_casehim(w: wd.World):
    return w.scene("幽霊の事情",
            )

def sc_clubwork(w: wd.World):
    return w.scene("同好会の最後の仕事だ",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_horrortalk(w),
                w.ryoma.explain(w.info("小学校が取り壊されると知る")),
            )

def ep_oldschool(w: wd.World):
    return (w.chaptertitle("旧校舎"),
            sc_oldschool(w),
            sc_lostarticle(w),
                w.ryoma.explain(w.info("小学校に忘れ物を取りに行く")),
            )

def ep_boyghost(w: wd.World):
    return (w.chaptertitle("少年の幽霊"),
            sc_clubagain(w),
            sc_findghost(w),
                w.ryoma.explain(w.info("幽霊の少年を見つける")),
            )

def ep_lastwork(w: wd.World):
    return (w.chaptertitle("同好会最後の仕事"),
            sc_casehim(w),
            sc_clubwork(w),
            # NOTE: 小学校が廃校になり、同窓会に集まる仲良しメンバ、そこにイレギュラーな彼女
            # NOTE: 地縛霊という少年を見つける、本物？　少年ホームレス？
                w.ryoma.explain(w.info("同好会で少年を成仏させてやることにした")),
            )


# outline
def story_baseinfo(w: wd.World):
    return [
            ("story-ch1", story(w), w.ryoma, w.miko),
            ]

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.ryoma.explain(w.info("小学校が取り壊されると知る")),
                w.ryoma.explain(w.info("小学校に忘れ物を取りに行く")),
                w.ryoma.explain(w.info("幽霊の少年を見つける")),
                w.ryoma.explain(w.info("同好会で少年を成仏させてやることにした")),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLES["ch01"]),
            ep_intro(w),
            ep_oldschool(w),
            ep_boyghost(w),
            ep_lastwork(w),
            )

def main(): # pragma: no cover
    from src.bghost.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

