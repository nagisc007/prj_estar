# -*- coding: utf-8 -*-
"""Story: chapter 03: The another me
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_proposed(w: wd.World):
    kyoko, shota, child, stu = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko
    return w.scene("彼のプロポーズから",
            kyoko.be(w.stage.living, w.day.proposed),
            kyoko.look("楽しそうな$childたちの笑い声に",
                "$meはゆっくりと目を開く"),
            kyoko.think("また布団の上で飛び跳ねたり",
                "好き勝手に押入れから物を引っ張り出してばらまいたりしているのだろう"),
            kyoko.look("そんな思いでぼんやりとした視界の中に何人かのシルエットを捕まえる。",
                "小さなのは$childだ。", "まだ十歳だった頃の$meの$i_IF", "$i_imagefriend。",
                "他にもう一人壁を背もたれに本を読んでいる",
                "$studentは十五歳の自分。", "彼女もまた$i_IFだった"),
            kyoko.talk("あれ？"),
            kyoko.look("$meは三人目の存在を確認して",
                "慌てて上半身を起こす"),
            shota.talk("あ", "起きた？"),
            kyoko.look("そう言って笑顔を見せたのは",
                "もう一人の$meではなく",
                "あいつ", "$n_shotaだった"),
            kyoko.ask("どうして家にあなたが入っているの？"),
            shota.talk("覚えてない？",
                "急に$kyokoが倒れたからここまでみんなで運んできたんだよ？",
                "ねえ"),
            child.talk("うん！"),
            kyoko.look("$childも$studentも一様に頷いている"),
            kyoko.deal(shota, w.i.proposed, w.stage.apart, w.day.proposed),
            shota.deal(w.i.proposed),
            kyoko.think(w.i.proposed),
            # TODO: 約束の内容＝プロポーズ
            )

def sc_strangeteam(w: wd.World):
    return w.scene("幸子と松本と",
            # TODO: サークルにて、翔太郎のこと悩み、松本と一緒になる、松本に彼女いると知る
            )

def sc_workhard(w: wd.World):
    return w.scene("職場でのハラスメントと",
            # TODO: ベテランさんが休んで、いつもより近い、精神的ストレス、逃げ出す、翔太郎が助ける
            )

def sc_withshota(w: wd.World):
    return w.scene("二人の帰路",
            # TODO: 二人での帰り道、翔太郎との思い出の欠片、別れ際にキスされる額
            )

def sc_birthanother(w: wd.World):
    kyoko, shota, child, stu = w.kyoko, w.shota, w.child_kyoko, w.student_kyoko
    return w.scene("三人目の誕生",
            # TODO: 動揺、翌朝、三人目が誕生している、生まれた瞬間のこと
            kyoko.come(w.stage.living),
            kyoko.deal(w.i.meeting),
            kyoko.come(w.stage.living),
            kyoko.look(w.another),
            kyoko.be(w.i.birth_another),
            )

def sc_withanother(w: wd.World):
    return w.scene("大学にいる彼女",
            # TODO: 大学にもついてくる三人目、翔太郎との再会
            )

def sc_shotaro(w: wd.World):
    return w.scene("翔太郎の記憶",
            # TODO: 翔太郎の話、彼のこと、実家のこと、親からの連絡
            )

def sc_mydad(w: wd.World):
    return w.scene("私の父親",
            # TODO: 父親を待つ駅前、再会
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("プロポーズ"),
            sc_proposed(w),
            )

def ep_meeting(w: wd.World):
    return (w.chaptertitle("翔太郎のこと"),
            sc_strangeteam(w),
            sc_workhard(w),
            sc_withshota(w),
            )

def ep_4thanother(w: wd.World):
    return (w.chaptertitle("四番目の今日子"),
            sc_birthanother(w),
            sc_shotaro(w),
            sc_mydad(w),
            )

# outline
def base_info(w: wd.World):
    return ("chapter3", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return [
            ("chapter3", story(w),
            w.kyoko.think(w.i.proposed),
            w.kyoko.deal(w.i.proposed, w.shota),
            w.kyoko.deal(w.i.meeting),
            w.kyoko.be(w.i.birth_another),
            True),
            ]

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            ep_intro(w),
            ep_meeting(w),
            ep_4thanother(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

