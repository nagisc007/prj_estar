# -*- coding: utf-8 -*-
"""Story: The red emergence
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.emergence import config as cnf
THM = cnf.THEMES


# scenes
def sc_redmoon(w: wd.World):
    miyako, aya = w.miyako, w.aya
    return w.scene("赤い月",
            miyako.be(w.stage.myroom),
            miyako.look("赤い月を見ていた"),
            aya.talk("ブラッドムーンて言うんだ", "皆既月食"),
            miyako.deal("その言葉を最後に返信がなくなった"),
            )

def sc_hermother(w: wd.World):
    miyako, kikyo = w.miyako, w.kikyo
    return w.scene("彼女の母",
            miyako.go(w.stage.ayahome, w.day.vanishnext),
            kikyo.talk("ごめんなさい。", "あの子部屋から出てこなくて"),
            miyako.reply("わかりました"),
            miyako.think("彼女の母はちょっと変わった人で苦手だった"),
            miyako.look("知らない女性が入れ替わりに入って行った"),
            miyako.think("けれど翌日も次の日もずっと",
                "$ayaとは連絡がつかないままだった"),
                w.miyako.look(w.aya, w.i.herstatus),
                w.miyako.think(w.aya, w.i.herrefusal),
            )

def sc_boringday(w: wd.World):
    miyako, kiri = w.miyako, w.kirimura
    return w.scene("退屈な日々",
            miyako.be(w.stage.classroom, w.day.valentain),
            miyako.hear("先生の言葉がどんどんすりぬけていく"),
            miyako.think("あれからずっと$ayaと連絡が取れない。",
                "家にも入れてもらえない。",
                "ただＬＩＮＥの既読だけが細い糸のような繋がりだった"),
            # TODO: ayaの学校での状況、いじめ、孤立がち
            miyako.remember("そういえば$ayaが美術部だったことを思い出す"),
            )

def sc_strangeman(w: wd.World):
    miyako, kiri = w.miyako, w.kirimura
    return w.scene("妙な先生",
            miyako.come(w.stage.artroom),
            miyako.look("先生の絵を見た"),
            miyako.look("あまりの迫力に気圧された"),
            # TODO: ayaの執念、悲しみ、そんなものが表現された
            kiri.talk("たった一人の部員がいなくなってしまってな"),
            miyako.ask("$ayaのことですか？"),
            kiri.ask("友だちなのか？"),
            miyako.think("友だち", "なんだろうか"),
            )

def sc_transformed(w: wd.World):
    miyako, kiri, kikyo = w.miyako, w.kirimura, w.kikyo
    return w.scene("彼女の変身",
            miyako.go(w.stage.ayahome),
            kiri.ask("すみません。", "$ln_kirimuraですが"),
            miyako.look("不在のようだった"),
            kiri.talk("開くぞ……"),
            miyako.look("初めて入った$ayaの家の中",
                "妙な置物や絵が飾られていて不気味だ"),
            miyako.move("階段を上がる"),
            w.miyako.come(w.stage.ayaroom, w.day.discover1),
            miyako.move("返事がない。",
                "先生がドアを開けた"),
            miyako.look("そこはカーテンが閉め切られて真っ暗な中",
                "不自然なほどの埃が舞い上がってうっすら霧掛かっているようにも見えた"),
            miyako.talk("$aya？"),
            miyako.look("先生が電気をつける。",
                "浮かび上がったそれに思わず口を押さえた"),
            # TODO: 蛹描写
            miyako.deal("それは$ayaからのＬＩＮＥだった"),
            miyako.look("$hermessage1"),
            w.miyako.look(w.aya, w.sanagi),
                w.miyako.look(w.kirimura, w.i.hercause),
                w.miyako.think(w.i.rescue_aya),
                w.miyako.meet(w.aya),
                w.miyako.know(w.i.ijime),
                w.miyako.go(w.kikyo),
            miyako.hear("先生が救急車を呼びつける声を聞きながら",
                "$meはその巨大な繭から伸びた一本の赤い糸を見つけた"),
            miyako.talk("糸？"),
            )

def sc_othergirls(w: wd.World):
    miyako, kiri = w.miyako, w.kirimura
    return w.scene("蛹の少女たち",
            miyako.think("その後",
                "学校で不登校だった生徒が一斉に調べられ",
                "この学校だけで五名の生徒が繭化しているのが発見された"),
            miyako.come(w.stage.artroom),
            miyako.ask("あの", "先生？"),
            kiri.talk("これ見てみろ"),
            miyako.look("そこにあったのは先日まで$ayaが描いていたキャンバスだった"),
            miyako.look("今はそこに赤く咲いた少女たちが描かれていた"),
            kiri.talk("妙だと思って剥がしたらこれが出てきた"),
            miyako.ask("あの", "実は"),
            miyako.think("$meはずっと参加を促されていたＬＩＮＥグループの話をした"),
            kiri.talk("ちょっと預からせてくれないか？"),
            )

def sc_catchmyheart(w: wd.World):
    miyako = w.miyako
    mam, dad, sis = w.mam, w.dad, w.sister
    return w.scene("囚われる心",
            miyako.be(w.stage.myhome),
            # TODO: 家族の食卓、野木さんの母がおかしい、宗教？
            )

def sc_crazy(w: wd.World):
    miyako = w.miyako
    return w.scene("狂った女",
            # TODO: 壊れている野木、桔梗の話
            )

def sc_rebirth(w: wd.World):
    miyako, kikyo = w.miyako, w.kikyo
    return w.scene("生まれ変わる",
            )

def sc_mymind(w: wd.World):
    miyako, kikyo, kiri, aya = w.miyako, w.kikyo, w.kirimura, w.aya
    return w.scene("私も蛹に",
                w.miyako.know(w.i.aya_mind),
                w.miyako.meet(w.kikyo),
                w.miyako.look(w.aya_letter),
                w.aya.do(w.i.rebirth),
            miyako.look(aya, "真っ赤になって生まれでた彼女の姿だった"),
            miyako.talk("ごめん。", "$me何も分かってなかった"),
            kiri.talk("$ln_miyako！"),
            miyako.look("先生が引っ張り出してくれる"),
            miyako.talk("先生！", "$ayaが！"),
            miyako.look("赤に溶けていく。",
                "そこから一斉に真っ赤な蝶が飛び立った"),
            kiri.talk("こいつだ"),
            miyako.look("先生が見せてくれたのは小さくて真っ白な蜘蛛だった"),
            kiri.talk("$spider。",
                "人の悲しみを喰らう妖魔だ"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_redmoon(w),
            )

def ep_chrysalis(w: wd.World):
    return (w.chaptertitle("蛹の少女たち"),
            sc_hermother(w),
            sc_boringday(w),
            sc_strangeman(w),
            sc_transformed(w),
            )

def ep_reasons(w: wd.World):
    return (w.chaptertitle("彼女たちの理由"),
            sc_othergirls(w),
            sc_catchmyheart(w),
            sc_crazy(w),
            sc_rebirth(w),
            sc_mymind(w),
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.miyako, w.aya),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.miyako.look(w.aya, w.i.herstatus),
                w.miyako.think(w.aya, w.i.herrefusal),
                w.miyako.look(w.kirimura, w.i.hercause),
                w.miyako.know(w.i.aya_mind),
                True),
            ("ep1", ep_chrysalis(w),
                w.miyako.think(w.i.rescue_aya),
                w.miyako.meet(w.aya),
                w.miyako.know(w.i.ijime),
                w.miyako.go(w.kikyo),
                True),
            ("ep2", ep_reasons(w),
                w.miyako.know(w.i.aya_mind),
                w.miyako.meet(w.kikyo),
                w.miyako.look(w.aya_letter),
                w.aya.do(w.i.rebirth),
                True),
            ]

# main
def world():
    w = wd.World("The red emergence")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("くれなゐの羽化"),
            ep_intro(w),
            ep_chrysalis(w),
            ep_reasons(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

