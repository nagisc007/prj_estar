# -*- coding: utf-8 -*-
"""Story: lv1 yusha.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.lv1yusha import config as cnf


# episodes
def ep_intro(w: wd.World):
    outfield = w.stage.field1.insided("町の外")
    scenes = (
            w.scene("父の背中",
                w.tag.comment("なるべく説明文じゃなく世界観説明"),
                w.hero.do("襲われた", w.i.monster, outfield, w.day.childhood),
                w.hero.look(w.monster1),
                w.hero.look(w.father, "背中"),
                w.father.do("beat", w.monster1),
                w.hero.do("助けられた", w.father),
                ),
            w.scene("剣の修行",
                w.day.first.explain("歳月が過ぎた"),
                w.hero.do("剣の練習", w.bazem, w.stage.church, w.day.first),
                w.hero.be("十六に成長"),
                w.hero.explain("体格も大きく"),
                w.hero.look(w.bazem, "白髪混じり", "微動だにせず隙きがない"),
                w.hero.do(w.bazem, "やられる"),
                w.tag.comment("最近の魔物事情"),
                w.bazem.talk(w.hero, w.i.monster, w.flag.increasing),
                w.bazem.talk(w.hero, w.i.dadlost),
                w.hero.know(w.i.dadlost),
                w.hero.talk(w.bazem, w.i.becomeyusha),
                w.hero.go(w.i.voyage),
                w.hero.be(w.i.becomeyusha),
                ),
            w.scene("欠けた家族",
                w.tag.comment("ここで少しだけ家族の現状"),
                w.hero.go(w.stage.myhome, "朝食"),
                w.hero.talk(w.mother, "剣の修行"),
                w.mother.explain("髪が長い", "最近目が見えづらい"),
                w.hero.talk(w.mother, "普通の仕事をしてくれても"),
                w.hero.think(w.mother, w.i.becomeyusha),
                w.hero.talk(w.mother, w.i.dadlost),
                w.hero.talk(w.mother, w.i.callhero),
                ),
            w.scene("呼び出し",
                w.tag.comment("ヴェルンは黒幕側だがそれを感じさせない"),
                w.vern.come(w.stage.myhome),
                w.vern.talk(w.hero, w.i.callhero),
                w.hero.deal(w.i.callhero),
                w.hero.talk(w.mother, "no warry"),
                w.hero.go(w.stage.castle),
                ),
            )
    return [w.chaptertitle("旅立ちまでの序章"),
            *scenes,
            ]


def ep_heros_sun(w: wd.World):
    scenes = (
            w.scene("英雄の子",
                ),
            w.scene("知らされる事実",
                ),
            w.scene("勇者誕生",
                ),
            )
    return [w.chaptertitle("英雄の息子"),
            w.hero.go(w.stage.castle, "$must"),
            w.hero.go(w.stage.myhome),
            w.hero.deal(w.i.callhero),
            w.hero.meet(w.stage.castle, w.king, w.day.first),
            w.king.talk(w.hero, w.deflag.increasing),
            w.king.talk(w.hero, w.i.reviveboss),
            w.hero.know(w.i.reviveboss),
            w.king.ask(w.hero, w.i.voyage),
            w.hero.reply(w.king, w.i.voyage),
            w.hero.go(w.i.voyage, "$must"),
            w.hero.deal(w.king, w.i.bustered),
            ]


def ep_allies(w: wd.World):
    scenes = (
            w.scene("秘書官の助言",
                ),
            w.scene("酒場にて",
                ),
            w.scene("助けられる英雄",
                ),
            w.scene("仲間"),
            )
    return [w.chaptertitle("初めての仲間"),
            w.hero.deal(w.i.gatherally),
            w.hero.know(w.marc, w.i.gatherally),
            w.hero.go(w.stage.bar, w.day.first),
            w.hero.meet(w.diana, w.kult, w.maririn),
            w.hero.talk(w.diana, w.i.voyage),
            w.hero.have(w.diana, w.i.coop),
            ]


def ep_destruction(w: wd.World):
    scenes = (
            w.scene("街の外",
                ),
            w.scene("最強の魔物",
                ),
            w.scene("圧倒的虐殺",
                ),
            )
    return [w.chaptertitle("全滅"),
            w.hero.know(w.diana, w.stage.tower1),
            w.hero.go(w.stage.tower1, "$must"),
            w.hero.go(w.stage.field1, w.day.first),
            w.hero.go("walk", w.stage.tower1),
            w.hero.meet(w.daemon1),
            w.hero.be(w.daemon1, w.i.deadly),
            w.hero.be(w.i.massacre),
            ]


def ep_anotherhero(w: wd.World):
    scenes = (
            w.scene("もう一人の英雄",
                ),
            w.scene("世界改変",
                ),
            w.scene("レベル１",
                ),
            )
    return [w.chaptertitle("もう一人の勇者"),
            w.hero.do("生き延びる"),
            w.hero.be(w.i.massacre),
            w.hero.go("runaway"),
            w.hero.be(w.stage.field1, w.day.first),
            w.hero.think("死を覚悟"),
            w.hero.do(w.hero99, "rescue"),
            w.hero.know(w.hero99, w.i.worldsecret),
            w.hero.have(w.hero99, w.i.coop),
            ]


# main
def world():
    w = wd.World("lv1 yusha project")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w


def story(w: wd.World):
    return (w.maintitle("レベル１勇者の旅立ち"),
            ep_intro(w),
            ep_heros_sun(w),
            ep_allies(w),
            ep_destruction(w),
            ep_anotherhero(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

