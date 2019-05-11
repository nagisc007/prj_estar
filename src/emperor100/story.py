# -*- coding: utf-8 -*-
"""Story: the emperor 100
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.emperor100 import config as cnf


# episodes
def ep_intro(w: wd.World):
    h, lion, milea, garneth = w.hero, w.lion, w.milea, w.garneth
    scenes = [
            w.scene("父の帰還",
                w.tag.comment("ここで簡単な世界観説明"),
                h.be(w.child, "wakeup").d("小さな指先が頬を幾度も撫でる"),
                milea.talk().t("あなた大丈夫？",
                    "酷くうなされていたようだけれど"),
                h.look().d("天蓋で陰の出来たベッドの上で目覚めると",
                    "愛しい$mileaの長い睫毛に彩られた星のような瞳が$heroを心配そうに見やっていた。",
                    "彼女の長い金髪が外からの風で靡くが",
                    "その裾野からまだ五歳になったばかりの息子が必死に小さな手を彼の顔へと伸ばしていた"),
                w.child.talk().t("だいじょーぶ？"),
                h.talk().t("ああ$child。",
                    "父は近衛兵長にも一度勝ったことがあるくらい強いんだぞ"),
                milea.talk().t("あなたそれ", "全然自慢になりませんよ。",
                    "兵長さん来年で還暦でしょう？"),
                h.look().d("薄ピンクの唇が花びらのような曲線で笑ったが",
                    "息子にはまだ理解が難しい冗談だったようだ。",
                    "彼女が$hero似だという",
                    "その栗色のはっきりとした瞳をきょろきょろさせながら",
                    "二人だけで笑っていることに少しむくれて不細工になった"),
                h.be(w.stage.castle, w.day.returnemp),
                h.hear().d("そこにドアがノックされる。",
                    "叩き方が強く",
                    "すぐに近衛兵の$albertだと分かった"),
                w.albert.talk().t("殿下！",
                    "お父上……陛下がお帰りになられたようです！"),
                h.reply().t("わかった。",
                    "準備をして出向くと大臣たちに申しておけ",
                    "$albert"),
                w.albert.reply().t("は、はい！"),
                h.hear().d("すぐに慌ただしい足音が遠ざかっていく"),
                w.child.talk().t("おじいちゃん？"),
                milea.talk().t("ええそうよ。",
                    "遠征から帰ってこられたの"),
                h.go().d("$heroはベッドから体を起こすと",
                    "薄手のローブだけを引っ掛けてバルコニィへと出る"),
                h.look(w.stage.balcony, "父の帰還").d("既に城門前にはかき集められた兵士たちがずらりと並び",
                    "砂埃で煙る遠方から黒い影の隊列が近づいてくるのを",
                    "騒々しく待ち構えている様子が覗き見えた"),
                h.talk(milea, "父の功績").t("あの様子だと今回の$st_randoleとの和平交渉が上手くいったのだろうな"),
                milea.ask().t("これで暫くの間",
                    "戦に怯えなくても良くなりますね"),
                h.look().d("三年の戦火を鎮火に向かわせたのは$emp_titleと呼ばれている$st_kingdom皇帝$lionの",
                    "皇品と称えられる人格の成せる業だった"),
                h.talk().t("父上のことだ。",
                    "そこは抜かりなく事を運ばれたことだろう"),
                milea.talk(h, "次の皇帝").t("せめてあなたが皇帝になるまでは",
                    "何事もない世であって欲しいわ"),
                h.look(milea, w.child).d("妻の$mileaはそう言いながら我が子の金髪を撫でたが",
                    "まだ何も知らない息子はきょとんとしたまま二人の大人を見つめ返していた"),
                h.be(w.i.throne, "次期皇帝"),
                h.be("皇帝の息子"),
                ),
            w.scene("継承の不安",
                h.go(w.stage.hall, "父を出迎え"),
                lion.come("here"),
                lion.talk(h, "孫の無事を確認"),
                lion.feel(w.i.badcondition.flag()),
                h.ask(w.i.peace_nego),
                lion.reply("上々"),
                garneth.come(),
                h.look(garneth, w.i.pope),
                h.think(w.i.pope, "マルダ教の最高司祭"),
                garneth.ask(lion, "ちょっと用件が"),
                h.look(lion, garneth, "行ってしまう"),
                ),
            w.scene("父の死去",
                h.hear().d("だがそれから一月も経たない内のことだった"),
                w.albert.do().d("まだ月が天高くて真っ赤に輝く夜半",
                    "激しくドアが叩きつけられ", "$heroは目覚めた"),
                w.albert.talk().t("た、大変です！"),
                h.reply().t("それはそうだろう。",
                    "だが夜中に騒ぎ立てるほどの何かなのか？"),
                w.albert.talk().t("陛下が亡くなられました！"),
                h.think().d("$albertの言葉に一瞬まだ夢の中にいるのかと勘違いする"),
                h.talk().t("陛下とは我が父$lionのことか？"),
                w.albert.talk().t("そうでございます。",
                    "$st_kingdom第九十九代皇帝陛下のことでございます！"),
                w.child.talk().t("なあに？"),
                milea.talk().t("大丈夫よ。",
                    "寝てなさい"),
                h.look().d("騒動で目を覚ました息子を$mileaが脇に抱いているが",
                    "彼女は$heroに心配そうな視線を投げかけながらも",
                    "小さく頷いた"),
                h.talk().t("確認してくる"),
                h.go().d("ただそれだけ言ってローブを羽織ると",
                    "鍵を開けて部屋の外に出た"),
                h.look().d("$albertは装備もなく剣も持たずに下は膝丈のパンツ姿のまま",
                    "目に涙を溜めて$heroを待っていた"),
                h.ask().t("何があった？"),
                h.look().d("そう尋ねたが$albertはただ首を横にするばかりで",
                    "口を開けば、"),
                w.albert.talk().t("$garneth聖下が殿下を呼んで来いと",
                    "ただそれだけ$meに言われて……"),
                h.reply().t("分かったから",
                    "もうその涙を仕舞え。",
                    "して",
                    "父上はどこだ？"),
                lion.be("dead"),
                garneth.talk(h, lion, w.i.badcondition.deflag()),
                h.think(w.i.lion_dead.flag()),
                garneth.talk(h, w.i.enthrone),
                h.know(w.i.throne),
                ),
            ]
    return [w.chaptertitle("皇帝の死"),
            *scenes,
            ]


def ep_preparation(w: wd.World):
    h, milea, garneth = w.hero, w.milea, w.garneth
    scenes = [
            w.scene("父の死、皇帝の死",
                h.be(w.stage.castle, w.day.dead),
                garneth.talk(h, w.i.throne),
                h.be(w.i.throne, "$must"),
                h.know(w.i.lion_dead),
                h.talk(garneth, w.i.throne),
                garneth.talk(h, "日程や心得"),
                h.remember(w.i.emperor_bug.flag()),
                garneth.go("出ていく"),
                h.think("今後のこと"),
                ),
            w.scene("継承のこと",
                h.be(w.stage.hisroom),
                h.be(w.i.throne, w.i.emperor100),
                h.remember(w.i.lion_word),
                h.talk("彼女を呼んでくれ"),
                ),
            w.scene("母殺しの疑惑",
                h.remember(w.i.murder_mam),
                h.talk(milea, w.i.emperor_bug),
                milea.ask(h, "あなた私を殺すと？"),
                h.reply("自信がない"),
                milea.talk(h, "あなたを信じています"),
                milea.talk(w.child, "この子もいるし"),
                h.think(w.i.lion_word),
                h.know(w.i.milea_mind),
                h.look(w.child),
                ),
            w.scene("そして儀式を迎える",
                h.do("wake", w.day.ceremony),
                h.look(w.i.moon),
                h.think(w.i.moon, "凶事の象徴"),
                ),
            ]
    return [w.chaptertitle("儀式の準備"),
            *scenes,
            ]


def ep_ceremony(w: wd.World):
    h, milea, garneth, child = w.hero, w.milea, w.garneth, w.child
    scenes = [
            w.scene("儀式前",
                h.be(w.stage.hisroom, w.day.ceremony),
                h.think("whether", w.i.throne),
                milea.come("here"),
                h.ask(milea, "即位が恐ろしい"),
                milea.behav(h, "抱きしめる"),
                milea.talk(h, "本当は強い人よ"),
                h.talk(milea, "最愛の者を殺してもか？"),
                milea.talk(h, "それが神の示される運命なら受け入れます"),
                h.be(w.i.ceremony, "時間が迫る"),
                h.do(w.i.his_mind),
                ),
            w.scene("儀式",
                w.hero.do(w.i.enthrone),
                h.be("戴冠"),
                garneth.talk(h, "第百代皇帝"),
                w.people.talk("祝福"),
                garneth.talk(h, w.i.emp_ceremony),
                h.go(garneth, "二人だけで", w.stage.cathedral),
                ),
            w.scene("秘密の地下室へ",
                h.go(w.stage.cathedral),
                garneth.talk("王家代々継承時のみ入ることを許可されている"),
                h.look("秘密の部屋"),
                h.go("秘密の通路"),
                h.think("見た記憶がある"),
                ),
            w.scene("人格の継承",
                h.look(w.stage.lab),
                garneth.talk(h, "継承を始める"),
                h.do("薬を打たれる"),
                h.talk("何を"),
                garneth.talk("皇帝の人格を継承する"),
                h.ask("そのような魔術を？"),
                garneth.talk("太古のヒトの技術です"),
                garneth.talk("代々技術者の家系だった"),
                garneth.talk("人格の継承"),
                w.hero.be(w.i.portchara, "強制的に"),
                ),
            w.scene("最愛殺し",
                h.be(w.stage.hisroom),
                garneth.ask(h, "お目覚めですか？"),
                h.ask(garneth, "儂は皇帝か？"),
                garneth.reply("yes"),
                garneth.deal(h, w.tsword),
                h.go(milea, "彼女の居室"),
                milea.ask("お目覚めですね？"),
                h.deal("殺害"),
                w.hero.do(w.milea, "殺害", w.i.emperor_bug.deflag()),
                ),
            w.scene("呪いの継承",
                h.know(garneth, w.i.lion_dead.deflag()),
                h.look(child),
                h.talk(child, "お前もいずれ最愛の者を殺す"),
                ),
            ]
    return [w.chaptertitle("百代目のバグ"),
            *scenes,
            ]


# main
def world():
    w = wd.World("100 characters")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("皇帝百代の呪（バグ）"),
            ep_intro(w),
            ep_preparation(w),
            ep_ceremony(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

