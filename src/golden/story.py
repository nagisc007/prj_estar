# -*- coding: utf-8 -*-
"""Story: the golden girl
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.golden import config as cnf
THM = cnf.THEMES


# scenes
def sc_religious(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    return w.scene("謎の宗教家",
            # NOTE: 地域提示
            w.tag.comment("宗教と夫婦間関係の提示。あと娘の病弱と不登校"),
            f.be("tv見ていた", w.stage.home),
            hiroko.deal("応対", w.believer),
            f.ask("何だった？"),
            hiroko.reply("宗教"),
            f.talk(w.i.nogod.flag()),
            f.ask(kana),
            f.deal(hiroko, "口論", w.i.coupleproblem.flag()),
            )

def sc_golden(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    return w.scene("黄金になる娘",
            w.tag.comment("娘の不登校、黄金発症"),
            # NOTE: 黄金化のきっかけ
            f.think("いつまでも起きない娘"),
            f.talk(hiroko, w.i.truancy),
            hiroko.look(w.stage.kanaroom),
            hiroko.talk(f, "娘が"),
            f.go(w.stage.kanaroom),
            kana.be(w.i.goldsyndrome, w.stage.home, w.day.current),
            f.deal("guard", kana),
            f.come(w.stage.kanaroom),
            f.look(kana, "黄金化"),
            kana.talk("きれい"),
            f.talk(hiroko),
            )

def sc_strangesick(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    return w.scene("奇妙な病",
            f.go(w.stage.hospital),
            kana.deal("診察"),
            w.medic1.feel("驚き"),
            w.medic1.talk("大きな病院で診てもらった方が"),
            f.look("看護師が触れた", w.i.infection.flag()),
            f.go(w.stage.univhospital),
            w.medic2.talk("専門の機関を紹介"),
            )

def sc_goldsyndrome(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("黄金化症候群",
            f.go(w.stage.labo),
            doc.talk(f, "黄金化症候群"),
            f.know("不治の病"),
            doc.talk("莫大な研究費"),
            doc.talk("国の助成金が少ない"),
            f.know(THM["money"]),
            )

def sc_doctor(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("博士の来訪",
            f.deal(w.fund),
            hiroko.talk("娘の細胞を売るべき"),
            doc.come(w.stage.home),
            doc.deal(w.i.heal),
            doc.talk("我々に任せて下さい"),
            f.know("看護師の感染", w.i.infection.deflag()),
            f.deal("研究所に預ける決断"),
            f.look(hiroko, "渋っているよう"),
            f.deal(kana, "預ける", w.stage.labo),
            kana.deal("奪われる", w.kanacell),
            )

def sc_kanacondition(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("娘の状態",
            f.go(w.stage.labo),
            f.meet(kana),
            kana.ask("母のこと"),
            f.reply("用があって", w.i.wifetrouble.flag()),
            f.hear(doc, "容態"),
            f.be("娘の状態が安定していると聞いて安心して帰る"),
            )

def sc_wifecondition(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("妻の苦悩",
            f.go(w.stage.home),
            f.talk(hiroko, kana, "状態"),
            f.look(hiroko, "疲れ"),
            hiroko.talk(f, w.i.wifetrouble.deflag()),
            f.know(hiroko, "病気のことは母親が悪い"),
            hiroko.deal("辞めたい", w.i.wifecircle),
            f.talk("辞めればいい"),
            hiroko.talk("何も分かってない"),
            )

def sc_robbed(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("奪われる細胞",
            f.be("穏やかな日々"),
            hiroko.talk("娘のこと", "今後のこと"),
            f.think(hiroko, "気が滅入っている"),
            f.deal(hiroko, "旅行にでも"),
            hiroko.talk("一人になりたいわ"),
            f.come(w.stage.home, w.day.case1),
            f.know("tv", "研究所に強盗"),
            f.deal(doc, "大丈夫か確認"),
            )

def sc_famous(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("有名になる娘",
            f.look("tv", "取り上げられる"),
            f.think(kana, "guard"),
            f.go(w.stage.labo),
            f.ask(doc, "どういうつもりだ"),
            doc.reply("研究費用を集める為"),
            doc.explain(f, w.i.gatherfund, THM["money"]),
            doc.ask(f, "命を守る為なんですよ？"),
            f.think("承諾するしかない"),
            f.look("研究所内を案内される記者たち"),
            f.look(w.suzuno, "案内している女性"),
            # NOTE: suzuno外見描写
            )

def sc_neverstop(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("止まない悲劇",
            kana.deal(w.kanacell, "奪われる"),
            f.know("強奪"),
            w.tag.comment("本当は横流ししている"),
            f.come(w.stage.labo),
            f.look(kana),
            kana.be("ボロボロの皮膚"),
            kana.talk("痛いよ"),
            f.go(doc),
            )

def sc_takehome(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("引き取る",
            f.come(doc, w.stage.docroom),
            f.deal("娘を引き取る"),
            doc.talk(f, "娘を殺すのか？"),
            f.talk(doc, "あんたには任せられない"),
            f.be(kana, w.stage.home, "匿う"),
            f.come(w.kana, w.stage.home, "連れ帰る", w.day.takehome),
            hiroko.talk("反対だった"),
            hiroko.talk("どうして連れ帰ったの？"),
            f.talk(hiroko, "娘を殺したい親がいるか？"),
            f.look(hiroko, "不機嫌"),
            f.look("毎日見張り"),
            f.be("睡眠不足"),
            kana.deal("奪われる", w.kanacell),
            )

def sc_spreading(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("広まる病",
            w.tag.comment("ある程度分裂を終えると採取した黄金細胞はがん細胞になる"),
            kana.deal("誘拐される"),
            f.do("拘束銃で確保"),
            f.deal("防犯と戦闘整備"),
            )

def sc_limitpoint(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("限界点",
            f.look("tv", w.i.docnews),
            f.look("博士たち逮捕"),
            f.know("博士たちが横流ししていた"),
            f.talk(hiroko, w.i.docnews),
            hiroko.talk(f, "もう限界"),
            hiroko.be(w.i.neurosis),
            f.hear("物音"),
            hiroko.talk(f, w.i.killkana),
            f.deal("stop", hiroko),
            f.think("どうすべきか"),
            f.look(kana),
            )

def sc_puzzled(w: wd.World):
    f, hiroko, kana, suzuno = w.fukuo, w.hiroko, w.kana, w.suzuno
    return w.scene("迷い",
            f.be("資金不足"),
            f.look("食べるものも満足に食べられない"),
            f.look(w.stage.hirokoroom, hiroko),
            f.look(hiroko, "衰弱"),
            hiroko.talk(f, "自分たちだけじゃ無理"),
            suzuno.come(w.stage.home),
            suzuno.talk("自分が助ける"),
            hiroko.deal(suzuno, "信じない"),
            suzuno.explain(f, w.i.injustice),
            f.think(suzuno, "信じてみる"),
            suzuno.deal("米国の機関を紹介する"),
            f.talk("保留"),
            f.talk("金はどうする？"),
            hiroko.talk(w.kanacell, "資金集めに使う"),
            f.talk("それには反対だ"),
            hiroko.talk(f, "あなたはいつも娘が一番なの？"),
            f.think(hiroko, THM["relation"]),
            hiroko.think(w.i.killkana),
            f.do("stop", hiroko),
            f.deal(hiroko, w.i.golden),
            )

def sc_hirokoburst(w: wd.World):
    f, hiroko, kana, suzuno = w.fukuo, w.hiroko, w.kana, w.suzuno
    return w.scene("妻の暴走",
            f.look("香奈恵がいない"),
            f.know(hiroko, "研究機関に明け渡す"),
            f.deal(kana, "取り返す"),
            suzuno.deal("謝罪"),
            suzuno.behav("泣く"),
            f.behav(suzuno, "慰める"),
            f.hear("物音"),
            f.go(w.stage.kanaroom),
            f.deal(hiroko, "stop"),
            hiroko.talk("この子が全部悪いの"),
            f.talk("お前はずっとそう思ってたのか！"),
            hiroko.talk("本音", w.i.coupleproblem.deflag()),
            )

def sc_kanamind(w: wd.World):
    f, hiroko, kana, suzuno = w.fukuo, w.hiroko, w.kana, w.suzuno
    return w.scene("娘の気持ち",
            f.know(THM["means"]),
            w.tag.comment("香奈恵が本当に望んでいたことを提示"),
            kana.talk("ごめんなさい"),
            hiroko.behav("泣く"),
            hiroko.be("黄金化"),
            f.think("病じゃない"),
            f.think("神の存在を感じる", w.i.nogod.deflag()),
            )

def sc_godbirth(w: wd.World):
    f, hiroko, kana, suzuno = w.fukuo, w.hiroko, w.kana, w.suzuno
    return w.scene("そして神が生まれた",
            f.deal("案内", w.stage.home, w.day.goddess),
            f.deal(kana, w.i.god),
            )

# episodes
def ep_intro(w: wd.World):
    return [w.chaptertitle("黄金の娘"),
            sc_religious(w),
            sc_golden(w),
            sc_strangesick(w),
            sc_goldsyndrome(w),
            sc_doctor(w),
            ]

def ep_unfortune(w: wd.World):
    return [w.chaptertitle("不幸の始まり"),
            sc_kanacondition(w),
            sc_wifecondition(w),
            sc_robbed(w),
            sc_famous(w),
            sc_neverstop(w),
            sc_takehome(w),
            sc_spreading(w),
            sc_limitpoint(w),
            ]

def ep_decision(w: wd.World):
    return [w.chaptertitle("決断の時"),
            sc_puzzled(w),
            sc_hirokoburst(w),
            sc_kanamind(w),
            sc_godbirth(w),
            ]


# main
def world():
    w = wd.World("The golden girld")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("不幸の黄金少女"),
            ep_intro(w),
            ep_unfortune(w),
            ep_decision(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

