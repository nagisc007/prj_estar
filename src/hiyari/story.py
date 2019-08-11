# -*- coding: utf-8 -*-
"""Story: The cold town
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.hiyari import config as cnf
THM = cnf.THEMES


# scenes
def sc_main(w: wd.World):
    h = hikari = w.hikari
    regna = w.regna
    return w.scene("main",
            h.be(w.stage.town, w.day.current),
            h.look("白く曇った溜息だけが",
                "凍ったアスファルトの上に落ちていた。",
                "その音すら聴こえそうな静けさの中を$Sは一人", "歩いている"),
            hikari.ask("誰か", "いませんか？"),
            h.be("か細い声だけが、どこまでも響く"),
            h.look("通りに沿って並ぶ家々は全て氷で造られているかのようで",
                "その上を$Sの声が遠くまで滑っていく。",
            "彼女は赤い毛糸で編まれた手袋で覆われた手を摺り合わせ",
            "その冷たさから逃れようとした"),
            h.look("見上げれば今にも雪の降り出しそうな空で",
                "動きのない灰色が隙間なくそこを埋めている。",
                "まだ指先が動かなくなるほどではないけれど",
                "このままだと凍え死んでしまうかも知れない","そんな心地が去来した"),
            h.think("それにしてもどうしてこんな場所で一人なのだろう。",
            "彼女は何も覚えていなかった"),
            h.move("広い交差点までやってきて漸く何かを見つける。",
            "道路の真ん中で少女が横たわっている。",
            "それも氷の少女だ"),
            h.feel("とくん、と心臓が鳴る"),
            h.look("近づいてよく見ると",
                "彼女は$Sに似ていた"),
            h.look("耳が隠れる程度の髪で前髪が少し長い。",
                "真っ直ぐな眉毛よりも長くて", "自信のない目元が少し隠されている。",
                "小柄で猫背。", "それが寝ていてもよく分かる。",
                "おまけにいつも着ている足首までが隠れる丈の長いワンピースは",
                "彼女そのものと言ってしまってもいいくらいだ"),
            regna.ask("悪戯って思った？"),
            h.look("声のした方を見ると",
                "積み木の山のように車が折り重なった上で",
                "両脚をゆらゆらさせる少年が笑っていた"),
            hikari.ask("あなたは、誰？"),
            regna.reply("$n_regna"),
            h.think("ふわりとした金髪を揺らし", "小柄な彼は見つめる。",
                "それは名前なのか苗字なのか", "$Sには判断がつかない"),
            hikari.ask("この町の人？"),
            regna.reply("違うよ"),
            hikari.ask("ここで何をしているの？"),
            regna.reply("君を待っていたんだ"),
            h.hear("――遊ぼうよ$S"),
            h.look("そう言って彼は飛び降りた"),
            h.look("驚いている彼女に笑みを向け", "それから背を見せて突然", "逃げていく"),
            hikari.talk("ちょっと待ってよ"),
            h.think("かけっこには自信があったが",
                "彼はまるで氷の上を滑るように進んでゆく"),
            h.move("何度も転びながらやっと彼に追いついけたのは",
                "どこかの学校のグラウンドだった"),
            hikari.talk("待って",
                "お願い……"),
            h.think("あれ？"),
            h.think("いつもならもっと息が切れていてもいい筈なのに、何かおかしい"),
            regna.ask("どうしたんだい$hikari？"),
            hikari.ask("ねえ。あなた、どうして私の名前を知っていたの？"),
            regna.talk("え、あ、それは"),
            hikari.ask("あの場所から逃げようとしたのは何故？"),
            h.deal("$regnaは口を閉じてしまう"),
            hikari.ask("ひょっとしてあの少女は私？"),
            h.look("彼はすっと視線を逸らす"),
            hikari.talk("そうなのね？"),
            h.look("答えない。",
                    "決して彼女を見ようとしない視線はそのまま泳ぎ続け", "ガラス細工のような街を映していた"),
            hikari.talk("答えて"),
            regna.talk("嫌だ"),
            hikari.talk("知っているんでしょう。お願い、教えて"),
            regna.talk("別に知らなくてもいいじゃないか。二人でこの町に住もうよ。$meは……$hikariを連れて行きたくはないんだ"),
            h.look("$regnaの瞳は何故か、青く澄んだ空のような透明さを湛えていた。",
                    "じっと見ているとそこからすっと一滴の雫が", "流れ落ちる"),
            regna.talk("分かったよ"),
            h.deal("彼は諦めたようにそう言うと",
                    "一つ一つ丁寧に彼女に話してくれた"),
            h.explain("$Sは本当は既に交通事故で死んでいて",
                    "彼はその魂を天国へと届ける天使だということ。",
                    "でも彼はそれが嫌で",
                    "時間を氷の世界に閉じ込めてしまったということを",
                    "流れ落ちる涙を拭いながら", "$Sに語った"),
            hikari.talk("じゃあ、私が天国に行かないでいる間、この町は？"),
            regna.talk("凍ったままだ"),
            hikari.talk("$meのお母さんやお父さんも？"),
            regna.talk("$meと$hikari以外はみんな"),
            hikari.talk("それなら$me",
                    "天国へ行く"),
            regna.talk("$hikari？"),
            hikari.talk("だってみんな冷たいままじゃ", "可哀相でしょ"),
            h.deal("$Sは笑顔を作ってみる。",
                    "それが彼に上手く伝わるかどうかは分からなかったが",
                    "それでも彼女の決意は足元の凍った土を", "少しだけ溶かした"),
            regna.talk("どうしても？"),
            hikari.talk("うん。", "だってね", "ほら"),
            h.deal("そう言って彼女は手袋を両方とも脱ぐと",
                    "両手で彼の頬を包んだ"),
            hikari.talk("$meの手はこんなにもひんやりとしているでしょう？",
                    "$me以外のみんなは", "ちゃんと温かいはずだから"),
            h.deal("けれど彼は嫌嫌をするように首を振ると", "彼女の手を自分の手で覆いながらこう返した"),
            regna.talk("$hikariの手は", "温かいよ。",
                    "凍えて亡くなった小鳥を", "土に埋めてくれたあの時のように", "温かいままだよ"),
            hikari.talk("それでも……ね？"),
            h.deal("わかった"),
            h.look("彼は涙を浮かべながら、それでもこくりと頷いて",
                    "手袋を拾う。",
                    "それを$Sの手に被せると、"),
            regna.talk("行こう"),
            h.deal("涙で光る瞳を向けてから", "その手を引いて飛び上がる"),
            h.deal("ふわり", "と浮かび上がった$Sの体は光の帯に包まれると",
                    "彼と共にどんどん空へ上がっていく。",
                    "曇が覆っていた天は割れ", "彼らを受け入れる光の階段を伸ばした"),
            h.deal("彼女の魂は彼に連れられて天へと昇っていく"),
            h.look("光の階段が消えてしまうと",
                    "空には青が満ち", "ゆっくりと凍った町に光が降り注ぎ始めた"),
            h.explain("町の鼓動が", "蘇る"),
            h.hear("――季節はずれの雪だね"),
            h.look("気づいた誰かが言った"),
            h.look("町には綿雪が降ってくる。",
                    "けれどそこに一枚のの温もりを持った羽根が混ざっていたことは、誰も気づかない"),
            h.hear("遠くで救急車のサイレンが鳴り始めた。",
                    "雪は雨に変わり", "小さな虹がうっすらと", "空に描かれた"),
            )

# episodes
def ep_main(w: wd.World):
    return (w.chaptertitle("main"),
            sc_main(w),
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
    w = wd.World("The cold town")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("凍った町の少女"),
            ep_main(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

