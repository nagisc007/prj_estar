# -*- coding: utf-8 -*-
"""Story: The night festa
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.festa import config as cnf
THM = cnf.THEMES


# scenes
def sc_nightfesta(w: wd.World):
    h = hikawa = w.hikawa
    sudo, takao = w.sudo, w.takao
    return w.scene("夜祭り",
            w.tag.comment("夢美の視点の三人称。最後に彼女は向こう側にいってしまうので"),
            h.feel("甘いシロップの匂いに鉄板の上で焼けるソースのそれが混ざり合って",
                "$n_hikawaはいつもふらつきを覚えてそれに気づく"),
            hikawa.talk("あ、ごめんなさい"),
            sudo.talk("大丈夫？　石畳がところどころ浮いてるから気をつけないとね"),
            h.deal("紺の浴衣姿の$n_sudoが野球部らしい丸刈りの頭で手を伸ばす。それを取って立ち上がると改めて周囲を見渡した"),
            h.look("夏の一日だけ行われる夜祭り。神社の境内に沢山の夜店が並び、人が溢れる。誰もが浴衣だ。同級生も多く、制服姿のままで着ている人は上級生だろうか。誰もがそれぞれの恋を探してキラキラとした表情をしている"),
            takao.talk("お、今年も来たね。どうだい、彼氏と食べていく？"),
            h.deal("そう声を掛けたのはかき氷マシンを手動で必死に回している$n_takaoだ。近所で小さい頃からよく遊んでもらっていた"),
            hikawa.talk("彼氏とかじゃないですよ"),
            sudo.talk("あ、どうも。須藤といいます。いつもマネージャーでお世話してもらってます"),
            takao.talk("おお野球部員か。後輩よ。最近どうだ？　$meらの頃は弱かったが最近は県大会いいとこまでいけるか？"),
            sudo.talk("全然ですよ"),
            hikawa.talk("あの……いいですか"),
            h.deal("彼女はいつも決まってストロベリーを注文する。何でも王道を選んでしまうのだ。冒険できないのがたまに悲しいと友だちには漏らしていた"),
            sudo.talk("それじゃあ$meも"),
            takao.talk("よし、二つだな。特別サービスしてやるよ"),
            h.deal("二人ともが山盛りになったかき氷を手に、少し離れたところにあるベンチに向かった"),
            h.deal("けどそこは既に満席で、二人して苦笑すると、手に持ったまま食べながら歩く"),
            h.move("長い階段の途中で休み、ちょっと食べ損ねた分をどうしようか迷っていたら、$sudoが「いいよ」ともらってくれた"),
            h.feel("冷えているはずなのに温かい。そんな気持ちをどう伝えればいいだろう"),
            h.look("不意に提灯が消え", "寒風が抜ける"),
            )

def sc_mydream(w: wd.World):
    h = hikawa = w.hikawa
    return w.scene("いつもの夢",
            h.look("目覚めるとじっとりと首筋が濡れていた。触るとひやりとする"),
            h.deal("時計を確認するとまだ三時半だ"),
            h.look("カーテンを引いて外を見る。遠くで奇妙な獣の声が響いていた"),
            # TODO: 簡単な彼女の現状の気持ち紹介（既婚者。隣に須藤の寝顔）
            )

def sc_schoollife(w: wd.World):
    h = hikawa = w.hikawa
    kiri = w.kirimura
    return w.scene("私の人生",
            h.move("職員室に入ってくると", "$kirimura先生と目が合った"),
            hikawa.talk("どうも"),
            kiri.talk("……"),
            h.look("無言で頭を下げると", "袖の汚れた白衣を羽織って出ていってしまう"),
            h.think("気持ち悪い", "と$meでなくとも思っている。",
                "それなのに意外と彼を慕う生徒がいるのは驚きだ"),
            h.deal("スマートフォンを見ると夫から連絡が入っていた。"),
            # NOTE: 何か二人の現在の関係性を見せるメッセージ
            h.think("こうして$meはいつも不安になる"),
            h.think("もしあの日に戻れるなら", "失敗してしまった選択をやり直すことができるだろうか"),
            # TODO: 学校での私生活、職員室で霧村と
            )

def sc_ghostdream(w: wd.World):
    h = hikawa = w.hikawa
    sudo, takao = w.sudo, w.takao
    return w.scene("幽霊の夢",
            h.look("首元の冷気に驚いて目を覚ますと",
                ""),
            # TODO: また夜祭り、そこで繰り返しの悲劇、やり直したい何か
            )

def sc_snowfesta(w: wd.World):
    h = hikawa = w.hikawa
    return w.scene("雪の夜祭り",
            # TODO: 夜祭りの中で季節だけが推移していく、それは彼女の生命力
            )

def sc_truth(w: wd.World):
    h = hikawa = w.hikawa
    return w.scene("真実",
            # TODO: 廃墟神社に行くと、そこで桜が咲いている、だがそれが妖魔。燃やしてしまう
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("夜祭り"),
            sc_nightfesta(w),
            sc_mydream(w),
            # NOTE: 普通の夜祭の様子、主人公、その後悔
            )

def ep_tragedy(w: wd.World):
    return (w.chaptertitle("繰り返す悲劇"),
            sc_schoollife(w),
            # NOTE: 主人公現在（高校教師）、疲れている、気づく男
            )

def ep_hermind(w: wd.World):
    return (w.chaptertitle("祭りの跡"),
            sc_ghostdream(w),
            sc_snowfesta(w),
            sc_truth(w),
            # NOTE: 真実暴露、主人公の選ぶ「現在」
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ]

def story_outlines(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The night festa")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("夜祭り"),
            ep_intro(w),
            ep_tragedy(w),
            ep_hermind(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

