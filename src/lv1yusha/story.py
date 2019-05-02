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
                w.bazem.talk(w.hero, w.flag.strangerogue),
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
            w.scene("城へ向かう",
                w.hero.go(w.stage.castle, "$must"),
                w.hero.go(w.stage.myhome),
                w.hero.look(w.stage.town),
                w.stage.town.explain("人々の賑わい"),
                w.hero.meet(w.gandof),
                w.gandof.talk(w.hero, w.father),
                w.hero.look("sky", "怪しい雲"),
                w.hero.remember(w.day.dadvoyage),
                w.hero.go("hurry", w.stage.castle),
                ),
            w.scene("城内へ",
                w.hero.look(w.stage.castle, "gate"),
                w.gatekeeper1.ask(w.hero, "用事"),
                w.hero.reply(w.gatekeeper1, w.i.callhero),
                w.hero.deal(w.i.callhero),
                w.gatekeeper1.talk(w.hero, w.i.herosun),
                w.hero.go(w.stage.castle.insided("城内通路")),
                ),
            w.scene("城内の様子",
                w.hero.go(w.stage.castle.insided("ホール")),
                w.hero.look("物珍しい"),
                w.hero.look(w.vern),
                w.vern.talk(w.hero, "案内"),
                w.vern.ask(w.hero, "大事な話"),
                w.vern.ask(w.hero, w.brokens),
                w.hero.reply(w.vern),
                w.hero.have(w.brokens),
                w.vern.talk(w.hero, w.stage.castle.insided("謁見の間")),
                ),
            w.scene("英雄の子",
                w.hero.meet(w.stage.castle.insided("謁見の間"), w.king, w.day.first),
                w.king.talk(w.hero, w.i.herosun),
                w.king.talk(w.hero, w.father),
                w.cornel.talk(w.king),
                w.cornel.talk(w.vern),
                w.vern.talk(w.i.worldinfo),
                w.hero.know(w.i.worldinfo, "$not"),
                w.vern.talk(w.i.dadlost),
                ),
            w.scene("知らされる事実",
                w.king.talk(w.hero, w.deflag.increasing),
                w.king.talk(w.hero, w.i.reviveboss),
                w.hero.know(w.i.reviveboss),
                w.king.ask(w.hero, w.i.case_caravan),
                w.hero.know("$not"),
                w.vern.talk(w.hero, w.i.case_caravan),
                w.hero.ask(w.i.monster),
                w.vern.reply(w.hero, w.i.reviveboss),
                w.hero.talk(w.father, w.i.dadlost),
                ),
            w.scene("勇者誕生",
                w.king.ask(w.hero, w.i.voyage),
                w.king.talk(w.hero, w.i.dadlost),
                w.king.talk(w.hero, w.father),
                w.hero.reply(w.king, w.i.voyage),
                w.hero.go(w.i.voyage, "$must"),
                w.hero.deal(w.king, w.i.bustered),
                w.king.talk("勇者誕生"),
                ),
            )
    return [w.chaptertitle("英雄の息子"),
            *scenes,
            ]


def ep_allies(w: wd.World):
    scenes = (
            w.scene("絡まれる英雄",
                w.hero.go(w.stage.castle.insided("城の外")),
                w.hero.meet(w.marc, w.deflag.strangerogue),
                w.marc.explain("ならず者風"),
                w.marc.ask(w.hero, w.i.herosun),
                w.hero.ask(w.marc, w.father),
                w.marc.do(w.hero, "斬りかかる"),
                w.hero.be("何もできない"),
                w.marc.talk(w.hero, w.i.level),
                w.marc.talk(w.hero, w.i.gatherally),
                w.hero.know(w.marc, w.i.gatherally),
                w.marc.talk(w.stage.bar, w.i.gatherally),
                w.marc.go("out"),
                w.hero.deal(w.i.gatherally),
                ),
            w.scene("酒場にて",
                w.hero.go(w.stage.bar, w.day.first),
                w.stage.bar.explain("薄暗い", "煙草やアルコール臭が漂う"),
                w.hero.look("酒場の人間たち"),
                w.barmaster.ask(w.hero),
                w.hero.reply(w.i.gatherally),
                w.barmaster.talk(w.hero, "無理だな"),
                ),
            w.scene("絡まれる英雄その２",
                w.diana.talk(w.hero),
                w.diana.explain("長身", "酔っぱらい"),
                w.diana.talk(w.hero, w.i.herosun),
                w.hero.talk(w.diana, w.i.herosun),
                w.hero.ask(w.diana, w.i.ally),
                w.diana.talk("laugh"),
                w.diana.talk(w.hero, w.i.level),
                w.hero.talk(w.i.becomeyusha),
                w.diana.ask(w.i.battle, w.hero),
                w.hero.reply("yes"),
                ),
            w.scene("仲間を賭けた戦い",
                w.barmaster.talk("外でやれ"),
                w.hero.go(w.stage.bar.insided("店の外")),
                w.hero.ask(w.diana, w.i.ally),
                w.diana.reply(w.hero, "yes"),
                w.hero.be("動けない"),
                w.diana.do(w.hero, "圧倒"),
                w.diana.talk(w.hero, w.i.level),
                w.hero.think("隙きができる"),
                w.hero.look(w.diana, "つまずく"),
                w.hero.do("attack"),
                w.diana.ask(w.hero, "罠"),
                w.diana.be(w.hero, "win"),
                w.hero.ask("もう一度"),
                w.kult.come("そこまで"),
                ),
            w.scene("仲間"),
                w.maririn.come(),
                w.maririn.ask(w.diana, "なんでそんなこと？"),
                w.diana.reply(w.maririn, "こいつの覚悟を知りたかった"),
                w.maririn.talk("なら充分じゃん"),
                w.maririn.talk(w.hero, w.i.diana_reason),
                w.hero.know(w.i.diana_reason, w.father),
                w.hero.meet(w.diana, w.kult, w.maririn),
                w.hero.talk(w.diana, w.i.voyage),
                w.diana.reply(w.hero, "yes"),
                w.diana.talk("introduce"),
                w.maririn.talk("introduce"),
                w.kult.talk("introduce"),
                w.hero.have(w.diana, w.i.coop),
            )
    return [w.chaptertitle("初めての仲間"),
            *scenes,
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

