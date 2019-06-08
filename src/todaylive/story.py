# -*- coding: utf-8 -*-
"""Story: Today I've lived
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.todaylive import config as cnf
THM = cnf.THEMES


# scenes
def sc_ruinworld(w: wd.World):
    ito, uncle = w.ito, w.uncle
    return w.scene("荒廃した町",
            w.tag.comment("生存放送。名前など重要項目とフレーズ"),
            w.tag.comment("糸の一人称"),
            ito.deal().d("砂嵐のような雑音が絶えずポータブルラジオのスピーカーから流れてくる"),
            ito.think().d("$meはそれを折れそうな細い手で掴んで",
                "頭上に掲げ", "その時を待つ"),
            ito.feel().d("強い風が幾度も抜け", "亡くなった母親のリボン付きの深緑のワンピースの袖口が大きくはためくけれど",
                "じっと堪えてその僅かな時間を待つ"),
            ito.think().d("思えばいつも$meは待ってばかりだった"),
            ito.think().d("この世界になってからバッサリと耳の後ろまでの長さに切ってしまった髪も",
                "以前は背中でちくちくとするまで放っておいた方だった"),
            ito.talk().t("あ……"),
            ito.hear().d("周波数が変化する"),
            ito.think().d("空はずっと灰色と紫の混ざった雲が細くなってもの凄いスピードで流れていくのに",
                "その瞬間だけ",
                "世界を二つに割ったみたいに青空が覗く"),
            ito.hear(w.i.broadcast).d("その刹那",
                "彼の声が流れ出す"),
            w.george.talk().t("ただ今三時。",
                "みなさん", "元気ですか？",
                "$meは今日も生きてます"),
            ito.have(w.portableradio),
            ito.talk().t("わ、$meも", "まだちゃんと生きてます！"),
            ito.hear().d("けれど彼の声はすぐ砂嵐に呑み込まれて",
                "あと十二時間は聴こえない"),
            ito.think().d("$meは脱力したように持ち上げていたラジオを下ろすと",
                "細い鉄の棒が突き出したコンクリ片に座り込み",
                "へたって顔を覆う"),
            ito.think().d("それは毎日三時にだけ流れる",
                "名も知らない誰かの生存報告だった"),
            ito.look("3時"),
            ito.look("sky"),
            ito.look("海の色").d("ずっと瓦礫が広がる先に濃い紫色の波が迫るのを見やり",
                "$meはただ溜息をついて立ち上がる"),
            ito.look(w.stage.ruintown, w.day.voyage),
            ito.look("高台", w.i.suicide.flag()),
            )

def sc_decision(w: wd.World):
    ito, uncle, kito = w.ito, w.uncle, w.kito
    return w.scene("旅立ちの決意",
            ito.talk().t("ただいま"),
            ito.come(w.stage.home).d("十度くらい斜めに入り口が傾いた建物の中に入ると",
                "補修作業中だったカーキ色のエプロン姿の伯父が軽く手を挙げて出迎えてくれた"),
            uncle.talk("あまり外には").t("今日もラジオ入ったの？"),
            ito.behav().d("小さく頷くだけで言葉は返さない"),
            ito.move().d("懐中電灯にもなるというポータブルラジオは元々は伯父の持ち物だったが",
                "電波障害で殆ど使えなくなったからと", "$meにくれたものだ。",
                "赤い毛糸を輪っかにして通し", "首からぶら下げて無くさないようにしている"),
            ito.reply("ラジオがよく入らない"),
            uncle.talk("電波障害").t("一応$meらも他のコミュニティと連絡が取れないかと思って無線飛ばしたりはしてるんだけどね",
                "どういう訳だかあの日以来さっぱりなんだ"),
            ito.ask().t("三時でも？"),
            uncle.talk().t("そのわずか数秒の間に上手く互いに送受信しないといけないから",
                "ちょっと難しいって話。",
                "こんな状態でずっと電源入れておく訳にもいかないし"),
            ito.look().d("病院だった施設の一階は辛うじて残っていたが",
                "ホールやそこから伸びる通路には",
                "怪我をした人や疲れて横になる人で溢れ返っているのが見える"),
            ito.talk().t("炊き出し手伝ってくるね"),
            uncle.talk().t("ああ"),
            ito.look().d("片方のレンズが外れた眼鏡で", "$uncleは笑う。",
                "あの日以来", "$meの周りの大人はみんな笑顔を標準顔にしているように感じる"),
            ito.move().d("途中少し屋根が崩れた廊下があるが",
                "そこを超えると大きなキッチンが現れる。",
                "電気ではなくガスで火を扱うようになっていたから助かったと",
                "給食センターを首になった$kitoが言っていた"),
            kito.talk().t("あら$ito。",
                "今日の放送終わったの？"),
            ito.reply().t("ええ。無事に"),
            ito.look().d("$meの返事に$n_kitoはにっこりとする"),
            ito.look().d("彼女は少し丸くなった背で両手を使って巨大なスチール寸胴の中身をかき混ぜていた"),
            ito.ask().t("カレーですか？"),
            kito.reply().t("色と風味だけね。",
                "もう一月になるけど", "こっから先もこのまま救助隊だの何だの来ないとしたら",
                "本格的に自給自足考えなきゃならないしね"),
            ito.think().d("最近は中身がほとんどないスープ状のものばかりで",
                "備蓄庫は綺麗に空っぽだと聞いている。",
                "誰もが不安なことは分かっていたから",
                "余計に自分がまだここにいることが", "いたたまれない"),
            ito.feel(w.i.hurted.flag()).d("バンドで覆った左の手首が", "時折酷くヒリヒリとした"),
            kito.talk().d("それじゃあじゃがいもの皮むきお願いしようかね"),
            ito.reply().t("分かりました"),
            ito.behav().d("スチールの長机の上の段ボール箱から拳大の芋を取り出すと",
                "ピーラーを動かし始める"),
            ito.think().d("何かをしていれば", "何も考えなくていい"),
            ito.think().d("けれどどうせ剥くなら玉葱の方が良かったと", "目元が痛む$meは苦笑した"),
            ito.think("世界がどうなったか"),
            ito.think("彼に会いたい"),
            ito.do("調べる", "電波のこと"),
            uncle.deal("噂を教える"),
            ito.think("決意"),
            uncle.talk("昔登山をよくしていた"),
            ito.have(w.mybag),
            ito.ask("本当に行っても？"),
            uncle.talk("今の目は信じられる"),
            ito.go(w.stage.tower),
            )

def sc_voyage(w: wd.World):
    ito, uncle = w.ito, w.uncle
    beforeday = w.day.voyage.elapsed(day=-1)
    return w.scene("旅立ちの決意",
            ito.be(w.stage.hill, beforeday),
            ito.look().d("翌日は磁気嵐が酷くて",
                "午後三時に外に出ることを許可してもらえなかった"),
            ito.be().d("$meは一人窓の外を見ながら",
                "それでも約束の三時になるのを待つ。",
                "ひょっとしたらその瞬間だけ空が開くかも知れない。",
                "そうすれば今日もまた彼が生きていることを確かめられる"),
            ito.deal().d("ポータブルラジオはずっと小さな砂嵐を流していた"),
            ito.think().d("もう一月ばかりダイアルを触っていないけれど",
                "ただ死に場所を求めて彷徨い歩いていた$meが",
                "どうやって彼の声をピタリと受信することができたのか不思議だ"),
            ito.think().d("ひょっとするとそれが”生きている”ということの意味だろうか"),
            ito.look().d("亡くなった父親の形見になってしまったロレックスの", "割れた盤面が三時を差していた"),
            ito.think().d("今日は聞けない。", "また十二時間後だ"),
            ito.think().d("それまで彼は生きているだろうか"),
            ito.think().d("名前も知らない",
                "ただ”生きています”という言葉で繋がるだけの",
                "他人"),
            uncle.talk().t("あぁ$ito", "ここだったのか"),
            ito.look().d("$uncleは顔も満足に洗えていないみたいだ。",
                "鼻の頭に機械油を付けていたが", "本人は気づいているのだろうか"),
            ito.ask().t("ラジオ", "入らなかった"),
            uncle.reply().t("だろうね"),
            ito.look().d("何だか両親を失って呆然としていた$meを迎えに来てくれた時からそうだったけれど",
                "全てを分かり切ったような表情で", "$meの父のように声を荒げたりはしない。",
                "ただそんな$uncleが一度だけ思い切り$meを打ったことがあった。",
                "手首を切り開こうとした", "あの雨の酷い日だ"),
            ito.ask().t("$uncle"),
            uncle.reply().t("ん？", "どうかしたかい？"),
            ito.ask().t("$kitoから聞いたんだけど",
                "近くでラジオ放送できそうなところって芝公園にあるタワーくらいだろうって言われて……"),
            ito.look().d("そうか。", "という溜息にも似た頷きだった"),
            uncle.ask().t("他の電波塔は残っていないという話を",
                "探索隊の人たちからは聞いたよ。",
                "昔にもっと高い電波塔も建てたんだけどね", "あの災害で折れちゃったそうだ。",
                "真っ二つにね"),
            ito.talk().t("……やっぱ駄目", "かな"),
            ito.think().d("それは彼の声を聞いた時から何度も口にしようとしてきた決意だった"),
            ito.look().d("$uncleは困ったように後頭部を掻くと",
                "$meを見て", "やはり困ったように苦笑した"),
            uncle.talk().t("$meが一緒に行く", "とは言ってあげられないのが伯父さんの限界だ"),
            )

def sc_towertown(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("鉄塔のある町",
            ito.think("三日歩く", w.i.hurted.deflag()).d("危険なことはしない",
                "無理だと思ったらすぐに帰ってくる。",
                "あとは決して自分で命を絶とうとしないこと"),
            ito.move().d("その三つの約束を$uncleとして",
                "$meはかつて東京と呼ばれていた土地へと向かって旅立った"),
            ito.have().d("背中には$uncleが餞別にとくれた登山用のしっかりとしたカーキ色のリュックを背負い",
                "その上に寝袋が乗っている"),
            ito.deal().d("非常食は何とか五日程度持たせるつもりでいたが",
                "水はもう一本が空になってしまっている"),
            ito.deal().d("生水は煮沸しないで飲まないよう言われたけれど",
                "このままだと構わずに飲んでしまうかも知れない"),
            ito.think().d("最初の日は傾いた駅舎の中で震えながら一晩を過ごした"),
            ito.think().d("少しくらいは楽しいかも知れない",
                "という思いがなかったとは言わないけれど",
                "自分が何も考えていなかったのだと現実がしっかり教えてくれた"),
            ito.think().d("それでも帰る気にならなかったのは",
                "午後と午前の三時に", "彼の生存報告を聞くことが出来たからだ"),
            ito.think().d("今日も彼は生きている"),
            ito.think().d("ただそれだけのことが", "こんなにも疲れた心と手足に力をくれる"),
            ito.look("道中埋まった建物を見た"),
            ito.deal(w.mybag, "非常食"),
            ito.deal("寝袋"),
            ito.be().d("病院を出てから五日目だった"),
            ito.look("多くが沈んだ都市").d("$meの目の前には大量の水とそこから伸びる傾いたビル等の建物が映っていた"),
            ito.go(w.stage.city, w.day.current).d("そこはかつてこの国の一割以上の人間が生活を送っていた場所だったが",
                "$i_disasterと呼ばれた謎の電波障害を発端とする未曾有の大災害により",
                "その多くが失われたと聞いている"),
            ito.look().d("実際に目にするまで半信半疑な気持ちがあったけれど",
                "人の声どころか小鳥の囀りすら響かない",
                "静寂の瓦礫の海を見て",
                "現実だと受け入れるしかなかった"),
            ito.look().d("$meはリュックから地図を取り出してどこにそのタワーがあるのか確認しようとしたけれど",
                "あまりにも地形が違い過ぎて全然参考にならない"),
            ito.think().d("折角ここまでやってきたのに",
                "正直「どうしよう」という感情しか出てこなかった"),
            ito.move().d("それでも歩ける場所を辿りながら",
                "$meは進んだ"),
            ito.ask(w.man1).t("あ……"),
            ito.look().d("横倒しになったビルの壁面を歩いていると",
                "遠くにボートから網を投げている人がいるのが見えた"),
            ito.deal().d("$meはすぐに大声を出して呼びかけたのだけれど",
                "久しぶり過ぎて何だかガラガラの掠れ声にしかならない"),
            ito.talk().t("す、み、ま、せーん！"),
            ito.deal().d("それでも何度か続けているうちに気づいてもらえたようで、"),
            w.man1.talk().t("あんたも生き残りか？"),
            ito.look().d("ボートを近づけて話しかけてくれた"),
            ito.ask().t("甲府から来たんですけど", "赤い電波塔ってどこにありますか？"),
            w.man1.talk().t("へえ", "山梨の方からここまで？",
                "あっちは無事だったんだ"),
            ito.behav().d("それに苦笑して首を横にすると",
                    "男性はバツが悪そうに「すまない」と謝った"),
            ito.deal().d("$meはラジオ放送のことを手短に伝えると",
                    "その男性は頬の無精髭を掻きながら「もっと東だね」と教えてくれた"),
            w.man1.talk().t("一応ここ", "元は多摩川って呼ばれてた川だったんだが",
                    "今じゃこの有様。",
                    "聞いた話じゃ", "東京湾付近は壊滅的な状況で",
                    "おそらく旧東京タワーも無事じゃないんじゃないかなあ。",
                    "$meには分からんけど"),
            ito.talk().t("ありがとうございます"),
            ito.deal().d("お礼を言ってからアーモンドチョコレートをひと粒分けてあげ",
                    "$meは再び歩き出す"),
            ito.meet().d("それからも時々人に遭遇した。",
                    "彼らはそれぞれに優しく教えてくれて",
                    "$meはその度にお礼のチョコレートを分けて感謝した"),
            ito.move().d("チョコの箱の中身がすっからかんになった頃",
                    "$meの目はやっと遠くに目指す赤いタワーの先端を捉えることができた"),
            ito.think().d("あそこまで行けば彼に会える"),
            ito.think().d("ただそれだけのことが",
                    "へとへとになった体を突き動かしてくれた"),
            ito.move().d("押し流された大量の車の屋根を伝ってそのタワーが立っている根本までやってくると",
                    "日焼けした男性が一人",
                    "その入り口の前に立っていて",
                    "$meの存在に気づくと目を細めて怪訝な表情を浮かべた後で、"),
            shima.ask().t("何？"),
            ito.hear().d("素っ気ない呼びかけを$meに投げた"),
            w.man1.talk(shima, "タワーにいる"),
            ito.go(w.stage.tower),
            ito.look("タワー前の状況"),
            ito.look(shima),
            ito.meet(shima),
            ito.ask("放送"),
            ito.deal(shima, w.i.myalive),
            shima.reply("ジョージじゃない"),
            ito.ask(w.george),
            shima.go("鉄塔の中"),
            )

def sc_inthetower(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("鉄塔にて",
            ito.know().d("その男性は$n_shimaと自己紹介してくれた。",
                "この近所でキャンプを張っていて",
                "今からこの鉄塔の上ですることがあるらしい"),
            ito.move("階段を上がる").d("$meは階段を一段一段上がりながら",
                ""),# TODO: here continue
            shima.explain("タワーについて"),
            ito.come(w.stage.broadroom),
            ito.look("放送室の内装"),
            shima.look(ito, w.broadbox),
            w.tag.comment("ジョージは生存者探しの旅に出た"),
            shima.talk(w.i.george_gone),
            ito.know(w.i.george_gone),
            )

def sc_histalk(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("彼の話",
            ito.come(w.stage.barrack, w.day.current),
            ito.look("ボロ小屋"),
            ito.look("ドラム缶風呂"),
            shima.deal("料理"),
            shima.talk(w.i.george_gone),
            shima.talk("自分も助けられたんだ"),
            ito.know(w.i.george_gone),
            ito.behav("泣いた"),
            ito.look(shima, "困ってる風"),
            ito.explain("涙の理由"),
            )

def sc_truth(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("私の真実",
            ito.talk(shima, w.i.suicide),
            ito.talk("災害と両親の死"),
            ito.talk("孤独"),
            ito.talk("生存報告との出逢い"),
            ito.talk("３時は生まれた時間", "両親が死んだ時間"),
            ito.know(w.i.george_gone),
            ito.talk(shima, w.i.suicide.deflag()),
            ito.think(w.george, w.i.myalive),
            ito.deal(shima, w.i.radio, "使い方"),
            )

def sc_myreport(w: wd.World):
    ito, shima = w.ito, w.shima
    return w.scene("私の生存報告",
            ito.be("wake", "夜の三時"),
            ito.go("tower"),
            ito.move("階段"),
            ito.feel("彼は黙ったまま"),
            shima.talk("外で待ってる"),
            ito.come(w.stage.broadroom, w.day.reporting),
            ito.talk(w.i.reporting, w.i.myalive),
            ito.talk(THM["alive"]).d("$meの報告だった"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_ruinworld(w),
            sc_decision(w),
            )

def ep_towerplace(w: wd.World):
    return (w.chaptertitle("鉄塔の立つ場所"),
            sc_voyage(w),
            sc_towertown(w),
            sc_inthetower(w),
            sc_histalk(w),
            )

def ep_hisreport(w: wd.World):
    return (w.chaptertitle("生存報告"),
            sc_truth(w),
            sc_myreport(w),
            )

# test data
def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.ito.think("彼に会いたい"),
                w.ito.hear(w.i.broadcast),
                w.ito.go(w.stage.tower),
                w.ito.know(w.i.george_gone),
                True),
            ]

def episode_outlines(w: wd.World):
    return [
            ("episode1", ep_intro(w),
                w.ito.think("彼に会いたい"),
                w.ito.hear(w.i.broadcast),
                w.ito.do("調べる"),
                w.ito.go(w.stage.tower),
                True),
            ("episode2", ep_towerplace(w),
                w.ito.deal(w.shima, w.i.myalive),
                w.ito.meet(w.shima),
                w.ito.ask(w.george),
                w.shima.talk(w.i.george_gone),
                True),
            ("episode3", ep_hisreport(w),
                w.ito.think(w.george, w.i.myalive),
                w.ito.know(w.i.george_gone),
                w.ito.deal(w.shima, w.i.radio),
                w.ito.talk(w.i.reporting, w.i.myalive),
                True),
            ]

# main
def world():
    w = wd.World("The golden girld")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("生存報告、今日も私は生きてます"),
            ep_intro(w),
            ep_towerplace(w),
            ep_hisreport(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

