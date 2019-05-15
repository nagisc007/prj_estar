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
            w.scene("車内にて親の愚痴",
                ma.be(w.stage.car, w.day.incident),
                ma.hear(w.mam, "祖父母の墓参り"),
                ma.look("緊急車両"),
                ma.look("消防車等を見送る"),
                ma.have("上司からのメール"),
                ),
            w.scene("現場取材",
                ma.come(w.stage.thesite),
                ma.look(w.takamori, "知人", "学校の先輩"),
                ma.know(w.i.case_fire, w.stage.office),
                ma.think(w.hideko, "何か臭う"),
                ma.deal(w.i.interview, w.stage.thesite),
                ma.hear("関係者", w.takamori),
                w.takamori.talk(ma, "空き家だったが"),
                ma.hear("人がいたらしい"),
                ma.hear("消防士が無理だと"),
                ),
            w.scene("会社風景",
                ma.come(w.stage.office, w.day.nextday),
                ma.talk(w.tanabe),
                ma.talk("昨日の火災事件"),
                w.tanabe.reply("遺体が二つ出てきたそうだ"),
                ma.go("取材に出かける"),
                ),
            w.scene("出てきた遺体が二つ",
                ma.come(w.stage.policestation),
                ma.hear("警察発表"),
                ma.ask(w.sugioka, w.deadbody),
                w.sugioka.talk(w.hideko),
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
            w.scene("漫画喫茶で",
                ma.look("アイドル時代の資料を持っている人とやり取り"),
                ),
            w.scene("元プロデューサー",
                ma.know(w.h_idol),
                ma.look(w.h_idol, w.i.life),
                ma.come(w.stage.idoloffice, w.day.interview2),
                ma.deal(w.i.interview, "当時を知る人"),
                w.manager.talk(w.h_idol),
                w.manager.talk("辞めてからも付き合いがあった"),
                w.manager.talk("事情があって芸能界引退"),
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
            w.scene("彼女の関係者",
                ma.be(w.stage.office),
                ma.deal("関係者を探す電話"),
                ma.ask(w.hideko),
                ma.go(w.stage.tokyo),
                ),
            w.scene("東京へ",
                ma.be(w.stage.train),
                ma.look("webで彼女の情報", w.hideko),
                w.tag.comment("ここで女優時代の基本的情報"),
                ma.know(w.movie),
                ),
            w.scene("同業者の行方",
                ma.come(w.stage.idoloffice),
                ma.hear("元マネージャの行方"),
                ),
            w.scene("同業者の現在",
                ma.know(w.h_actor),
                ma.look(w.h_actor, w.i.life),
                ma.deal(w.i.interview, w.stage.theater, w.day.interview1),
                ma.deal(w.i.interview, "業界人"),
                ma.meet(w.actoress),
                w.actoress.talk(w.h_actor),
                w.actoress.talk("アイドル時代に声かけた"),
                ma.know(w.hideko, w.h_idol),
                ),
            ]
    return [w.chaptertitle("女優時代"),
            *scenes,
            ]


def ep_lateyears(w: wd.World):
    ma = w.masuda
    scenes = [
            w.scene("結局何も分からず",
                ma.come(w.stage.office),
                w.tag.comment("ここで一旦情報まとめ"),
                ma.talk(w.tanabe, "調べた情報"),
                ma.hear(w.tanabe, "彼女の本名"),
                ),
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

