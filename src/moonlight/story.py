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
            h.look("駅前の喧騒をやり過ごして暗がりの住宅街へと戻ってくる"),
            h.look("見上げると三日月。暗い中を歩いて帰ると家に近づいて、ハープの音が聞こえる。彼女と分かる"),
            h.deal("鍵を開けて中に入る。家は真っ暗。そこに音だけが響く"),
            luna.talk("おかえり"),
            # NOTE: 真っ暗な家に戻ってきて、ハープだけが聞こえる、人物紹介兼ねて
            )

def sc_alwayshelp(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("いつでも助けたい",
            h.be(w.stage.myhome, w.day.goout),
            h.deal("朝食の準備をする。彼女は目が見えない。音だけを頼りに生きている"),
            h.deal("それでも時々見えているんじゃないかと疑ってしまう。そういう所作"),
            luna.talk("今日は、遅い？"),
            h.deal("感が鋭い。だからなるべく心配をかけないようにと振る舞う"),
            goro.talk("いってくるよ。なるべく早く帰らせてもらう"),
            # NOTE: 仕事にでかけるいつもの朝の様子、不安症の夫
            h.be(w.stage.onstreet),
            h.deal("外を歩く。駅前。ヘルプマークをつけている女性を見つけ、助ける"),
            h.think("彼女との出会いもこんなきっかけだったことを思い出す"),
            # NOTE: 会社に行く途中でヘルプマークの人を助ける夫
            h.be(w.stage.intrain),
            h.think("吊革を握りながら、彼女が心配"),
            h.hear("耳障りなシャカシャカ音が大きく"),
            h.feel("電車が止まり、停電？　ちかちかっと"),
            h.deal("車内アナウンスで「点検中です。しばらくお待ち下さい」"),
            h.deal("ほどなくして動き出す"),
            )

def sc_alonegoout(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("孤独な外出",
            h.be(w.stage.myhome),
            h.deal("夜遅くに帰宅。家は真っ暗"),
            h.deal("物音がしない。返事もない"),
            h.deal("一人でカップ麺を食べていると彼女が起きてきて"),
            h.deal("明日からの公演に備えて早めに休んだ方がいい。どうした？"),
            luna.talk("あなたには$meの助けが必要ないんだと思って。おやすみなさい"),
            h.think("考え込む"),
            h.deal("翌朝、彼女の楽団のメンバーと挨拶を交わしてお願いする"),
            h.deal("見送る"),
            h.deal("その夜、LINEがくる。月が見える？と"),
            # NOTE: 彼女が公演で不在、一人孤独、LINEで「月が見える？」と
            )

def sc_fight(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("二人の喧嘩",
            h.be(w.stage.myhome, w.day.fight),
            h.deal("ある日のこと、彼女が突然ハープを弾くのをやめてしまった"),
            h.deal("公演で何かあったみたいだが、あまり話さないから分からない"),
            goro.talk("もうちょっと言葉にしてくれないと分からない"),
            h.deal("けれど彼女は「関係ない」とだけ"),
            h.deal("そのうち口論になり"),
            luna.talk("目が見えるあなたには分からないわよ！"),
            h.deal("言ってはいけないことを口にしたんだと、絶望する"),
            h.deal("彼女が出ていく。追えない夫"),
            # NOTE: 月のこと（自分がいなくても大丈夫な彼女）で口論になり、出ていく
            )

def sc_worldtone(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("音の世界",
            h.be(w.stage.myhome),
            h.deal("楽団の知人の家に泊まっていると高橋から連絡がある"),
            h.deal("電話の向こうで楽しげな声"),
            h.think("彼女がどんな気持ちか知らない"),
            h.deal("暗闇の中で過ごす"),
            h.hear("様々な息吹。音"),
            h.think("月なんて見えないだろ、という言葉"),
            h.deal("外に飛び出す"),
            h.deal("タクシーを拾い、向かう"),
            # NOTE: 出張中、彼女の音が聞こえてくる、音の世界を思い出し、帰る
            )

def sc_lookmoon(w: wd.World):
    h = goro = w.goro
    luna = w.luna
    return w.scene("月を見る、月を聞く",
            h.be(w.stage.onstreet),
            h.deal("高橋に連れられ、彼女が待っていた"),
            h.deal("彼に感謝をして、彼女を受け取る"),
            h.deal("彼に少し睨まれた気がした"),
            h.deal("尋ねる。音の世界のこと"),
            h.deal("彼女からスマホで月の音を聞かされる"),
            luna.talk("月だけじゃなくずっと遠くの星もね、音を持っているんだって。誰もが音をもっているの。$meはいつもあなたの音を聞いているのよ？"),
            h.look("見上げる。雲が多くて見えないだろうと言われていたのに雲が千切れた"),
            h.look("月が見える"),
            h.deal("彼女に月を聞かせてと言われる"),
            h.look("月を見る"),
            h.deal("言葉は出ない。でも彼女はその胸に耳を当てて言う"),
            luna.talk("月が、聞こえた"),
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
    return (w.maintitle("月が、聴こえた"),
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

