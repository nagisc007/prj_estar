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
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("望んだはずの空虚",
            h.be(w.stage.apart, w.day.empty),
            h.look("一人きりのアパート"),
            h.think("何かが違うと感じている"),
            h.look("でも翌日も次の日も誰もいなかった。一人だった"),
            )

def sc_circlemeeting(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    kunugi, sayama, saito, matsu = w.kunugi, w.sayama, w.saito, w.matsumoto
    return w.scene("サークルのミーティングにて",
            h.be(w.stage.classroom, w.day.meeting),
            h.look("サークルの会合。週末にまた清掃活動"),
            saito.ask("大丈夫？", "最近あまりメールも返ってこないし"),
            h.deal("面倒な彼女みたいなことになっている$saito"),
            h.look("$matsumotoがじっと$meを見ていた"),
            matsu.ask("なあ"),
            h.deal("解散になったところで", "$matsumotoから声を掛けられる"),
            matsu.talk("ちょっと訊きたいことがあってさ"),
            h.deal("彼が見せてくれたのはまだ小さい頃の$shotaの写真だった"),
            )

def sc_meetmatsu(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    matsu, asumi = w.matsumoto, w.asumi
    return w.scene("松本と出会う",
            h.be(w.stage.ma_apart),
            h.come("彼のアパートにやってくる。木造の旧い二階建て。その一階に彼女と暮らしていると聞いた"),
            h.look("大学からは少し遠くて", "三十分はかかる"),
            kyoko.talk("お邪魔します"),
            h.look("見ると綺麗に片付いていたが", "誰もいない"),
            matsu.talk("$asumi", "連れてきたぞ"),
            h.look("何も見えない。聞こえない"),
            matsu.talk("適当に座ってくれ。", "今お茶いれてもらうから"),
            h.look("けれど彼は自分で台所に立ち",
                "ペットボトルからお茶を注いでいる"),
            h.deal("お茶を出してくれた彼は",
                "明らかに$meとの間にもう一人いる空間を挟んで座る"),
            matsu.ask("……やっぱ$kyokoにも見えないのか"),
            kyoko.talk("どういうこと？"),
            matsu.talk("いや気にしないでくれ。", "説明しても理解してもらえない"),
            h.think("その諦めの瞳を知っている"),
            kyoko.ask("ひょっとして$matsumotoさんて", "$i_IF",
                "つまり$i_imagefriendが見えるんですか？"),
            h.look("明らかに表情が変わっていた"),
            h.explain("彼から簡単な説明を受ける"),
            kyoko.talk("えっと", "見えないんですけど初めまして。", "$n_kyokoです。",
                "$matsumotoさんとは同じサークルに入ってます"),
            h.deal("誰もいない空間に対して$meは頭を下げた"),
            matsu.talk("驚かないんだな"),
            h.explain("自分も経験者だということを話した"),
            matsu.talk("$meは気にしないことにした。",
                "それにこいつと一緒にいると楽しいんだ。",
                "$meの知らない音楽とか色々教えてくれるし",
                "何よりいい女だし"),
            h.look("そんな風に言える彼が羨ましい"),
            kyoko.ask("それで$shotaの写真なんだけど", "あれはいつ頃なの？"),
            h.deal("それは$meがまだ$i_IFを持っていない", "$childが生まれる前のことだった"),
            matsu.talk("$asumiがさ", "見かけたっていうからちょっと気になってな"),
            h.think("$meが彼に連れられてラブホテルに行った日だった"),
            matsu.talk("小学校の同窓会に呼ばれた時にさ", "知ったんだ。",
                "$shotaが実は亡くなってたって"),
            h.deal("そのことについて詳しく聞いた"),
            h.deal("当時の彼の実家を教えてもらう"),
            )

def sc_hismanshion(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    dad = w.sho_dad
    return w.scene("彼の家",
            h.come(w.stage.hishome, w.day.meeting, shota),
            h.look("彼の家は聞いていたそのままだった"),
            h.deal("インタフォンを押す"),
            h.look("現れたのは髪が真っ白になった父親らしき男性だった"),
            h.deal("応接間に案内される"),
            h.hear("死因は脳腫瘍だった"),
            )

def sc_hisvanish(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    dad = w.sho_dad
    return w.scene("彼はもういない",
            h.look("彼の部屋を見た"),
            h.look("当時のまま残されているという"),
            h.look("小さな彼の写真はマッシュルームカットだ"),
            h.look("そこに彼の絵日記を見つけた"),
            h.think("思い出した。",
                "それは$meが小さな家出をして泣いていた時だった"),
            h.think("彼が助けてくれる。", "結婚してくれると約束したのだ"),
            dad.talk("$fn_kyokoさんに謝っておいてくれと言われたんだが",
                "当時探してもそんな名前の同級生はいなかったものでね"),
            kyoko.talk("ありがとうございます"),
            )

def sc_alone(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("今日子ひとり",
            # TODO: 彼とか好きじゃなく、ただ自分の理解者が欲しかっただけだった
            )

def sc_goodbyeanothers(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("さよならわたし",
            h.hear("$childたちの笑い声が聞こえた気がした"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("誰もいない"),
            # NOTE: 翔太郎までいなくなり、完全に孤独になった今日子
            sc_anyones(w),
            )

def ep_matsumoto(w: wd.World):
    return (w.chaptertitle("松本とIF"),
            sc_circlemeeting(w),
            sc_meetmatsu(w),
            )

def ep_truth(w: wd.World):
    return (w.chaptertitle("真実と真相"),
            sc_hismanshion(w),
            sc_hisvanish(w),
                w.kyoko.deal("vanish", w.shota),
            sc_alone(w),
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
            ]

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            ep_intro(w),
            ep_matsumoto(w),
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

