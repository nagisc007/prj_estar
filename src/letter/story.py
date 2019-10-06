# -*- coding: utf-8 -*-
"""Story: the letter
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.letter import config as cnf
THM = cnf.THEMES


# scenes
def sc_warmingdays(w: wd.World):
    h = hiroki = w.hiroki
    yoko = w.yoko
    return w.scene("温かい日々",
            h.be(w.stage.wooddeck, w.day.warming),
            h.deal("家の庭で二人でバーベキューしながらはしゃぐ$S"),
            h.deal(w.info("子どもの話").flag(),
                "お酒を飲み、将来の家族像を語る"),
            h.deal("妹に手紙を書いている$n_yoko。だが筆を落としてしまう。何度も拾えない"),
            yoko.talk("え……"),
            # NOTE: 夫婦の幸せな日々の情景、その中にシミが落ちる
            # NOTE: 手紙好きなこと
            )

def sc_sickrepot(w: wd.World):
    h = hiroki = w.hiroki
    yoko = w.yoko
    doc = w.doctor
    return w.scene("病気のこと",
            h.be(w.stage.consulroom, w.day.consul1),
            h.deal("医師から検査結果などを聞かされる"),
            h.know("筋力が落ちて最終的に命が亡くなってしまうと聞かされる"),
            h.deal("ALSの説明。現在では胃ろうや呼吸器補助などの技術が進み",
                "進行が遅ければ十年以上生きることができると希望を伝える"),
            h.deal("平均すると二年から五年で亡くなることも"),
            doc.talk("お二人でよく話し合ってみて下さい"),
            # NOTE: 症状と余命など
            )

def sc_confab(w: wd.World):
    return w.scene("上司に相談",
            # NOTE: 博樹の会社で相談する中で解決の糸口を見つける
            )

def sc_modelingwork(w: wd.World):
    h = hiroki = w.hiroki
    yoko = w.yoko
    return w.scene("モデリング",
            h.be(w.stage.myoffice, w.day.model1),
            h.deal("腕や指の造形の仔細をセンサーで取得し、まずＣＧモデルを作る"),
            h.deal("それとは別に彼女の腕の動きをトレース"),
            h.deal("彼女の直筆を解析しデータ化、ＡＩ学習させる"),
            h.deal("そういう日々を重ねる中でも彼女の病状は進展していった"),
            # NOTE: 彼女の腕や書き方のモデルを作る
            )

def sc_herdead(w: wd.World):
    h = hiroki = w.hiroki
    yoko = w.yoko
    sis = w.sister
    return w.scene("彼女の死",
            h.be(w.stage.ceremonyhall, w.day.dead),
            h.deal("彼女は発症から三年で亡くなった。その間に準備は終わった"),
            h.deal(w.info("子どもの話").deflag(),
                "人工授精によって妹のお腹には彼女の子がいる"),
            # NOTE: 事故のような突然の死、ただし備えは全部終えた
            )

def sc_birthmychild(w: wd.World):
    h = hiroki = w.hiroki
    yoko = w.yoko
    sis = w.sister
    return w.scene("私の子",
            h.be(w.stage.hospital, w.day.birth),
            h.deal("代理母により出産"),
            h.deal("息子に最初の手紙が届く"),
            h.deal("それを読み上げる$S"),
            h.deal("手紙には母がもうこの世にいないこと、あなたを直接抱いてあげられないこと、その代わりに沢山の記念日の手紙を用意してもらったこと――"),
            # NOTE: 出産、そして成長
            )

def sc_mothersletter(w: wd.World):
    h = hiroshi = w.hiroshi
    helper = w.helper
    return w.scene("母の手紙",
            h.be(w.stage.labo, w.day.future),
            h.deal("手紙が高額になった未来"),
            h.deal("助手に紙を購入してもらってきた$S"),
            helper.talk("どうしてわざわざ？"),
            hiroshi.talk("母さんがね、手紙が好きだったんだ"),
            h.deal("新しくなったモデル。それが手紙を書き出す"),
            hiroshi.talk("今日が誕生日でね。だから書いてもらっている"),
            h.deal("毎年いろいろな言葉や教訓をもらったことを話す"),
            h.deal("書き上がった手紙には「そろそろ彼女かお嫁さんがいるかしら」と書かれていて、それを見た彼女は頬を染めていた"),
            h.deal("そして$Sは返事を書く。彼もまた手紙を書くようになっていた"),
            h.deal("母さん。ありがとう。から始まる手紙"),
            # NOTE: 機械処理にてその年齢や誕生日や都度の手書きの手紙が届けられた
            # NOTE: 息子は技師になる。そして高価になってしまって手紙を書き、お墓に入れた
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_warmingdays(w),
                w.hiroki.explain(w.info("彼女の病気が発覚する")),
            )

def ep_hersick(w: wd.World):
    return (w.chaptertitle("彼女の病気"),
            sc_sickrepot(w),
            sc_confab(w),
                w.hiroki.explain(w.info("彼女の死んでも手紙を書くという夢を開発")),
            )

def ep_modeling(w: wd.World):
    return (w.chaptertitle("彼女をモデルに"),
            sc_modelingwork(w),
            sc_herdead(w),
                w.hiroki.explain(w.info("彼女が死ぬ")),
            )

def ep_herletter(w: wd.World):
    return (w.chaptertitle("彼女からの手紙"),
            sc_birthmychild(w),
            sc_mothersletter(w),
                w.hiroki.explain(w.info("彼女の手書きの手紙を子に見せる")),
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.hiroki, w.yoko),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.hiroki.explain(w.info("彼女の病気が発覚する")),
                w.hiroki.explain(w.info("彼女の死んでも手紙を書くという夢を開発")),
                w.hiroki.explain(w.info("彼女が死ぬ")),
                w.hiroki.explain(w.info("彼女の手書きの手紙を子に見せる")),
                True),
            ]

# main
def world():
    w = wd.World("The letter")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("彼女はそれでも手紙を書きたかった"),
            ep_intro(w),
            ep_hersick(w),
            ep_modeling(w),
            ep_herletter(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

