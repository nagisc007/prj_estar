# -*- coding: utf-8 -*-
"""Story: vanish cat
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.vanishcat import config as cnf
THM = cnf.THEMES


# scenes
def sc_catlife(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    return w.scene("猫の居る生活",
            h.be(w.stage.living, w.day.first),
            h.look("真っ白なソファの上に", "雉色をした猫が気怠そうに前足に顎を載せ、目を伏せている"),
            h.deal("ちゃんとそこに居ることを確認してから$Sは前に向き直り",
                "モニタに映った蟻の行列のような英数字の並びに溜息をつく。",
                "キーボードを叩く度に彼女が目覚めないだろうかと不安になるが",
                "特にこちらを気にする気配はない"),
            h.think("彼女は人間に関心など示さない", "ということだろうか"),
            h.think("それならそれで構わない。", "ただ目の届く範囲で穏やかに居てくれるだけで良い"),
            h.deal("空調の温度を一度下げ",
                "一息入れようと席を立つ"),
            h.look("ソファの背には斜めに引っかき傷が付いていて", "それはおそらくこれからも少しずつ増えていくのだろうが",
                "彼女のことを考えると新しく買い換えるのもどうなのだろうかとなかなか踏ん切りが付かない。",
                "やはり慣れたものの方が居心地良く思ってくれるような気がするのだ"),
            h.deal("キッチンの小さな方の冷蔵庫には炭酸水のボトルの脇にビールのミニ缶がずらりと並んでいる。",
                "$Sはそれを一つ手にし", "封を切る。", "コップは使わない。",
                "いつもそのままだ。",
                "何口かに分けて流し入れると",
                "空になったそれをゴミ箱に投げ入れた"),
            h.deal("缶同士が乾いた音を響かせたのが気に障ったようだ"),
            kisa.talk("$ary？"),
            h.hear("そう呼びかけると小さな返事がした。",
                "実によく似ている。", "猫の声そのものだ"),
            h.deal("$Sはソファまで戻ると", "自分を見上げて小さく歯を見せた彼女の頭を撫でる。",
                "目を閉じて気持ちよさそうに低く唸る。",
                "最初は喉を鳴らすその声に慣れなかったが", "最近ではこれが彼女の安寧の声なのだと理解が進んできた"),
            h.deal("だがその声は不意に無機質な電子音声に変わる"),
            ary.talk("バッテリィ残量が少なくなりました。", "充電して下さい"),
            kisa.talk("ああ、分かったよ"),
            h.deal("$Sは仕方なく彼女を足元から抱き上げて持ち上げると",
                "壁際に立つロケット発射台のような金属のアームとプラスチックの置き型充電器まで運ぶ。",
                "彼女の四肢を支えながら腹部を台に載せ", "背中を押さえるようにアームを下ろすと",
                "目を閉じて動かなくなってしまった。",
                "その胴体に『Charging』と赤字が浮かび上がったのを確認し", "$Sはパソコンデスクに戻る"),
            h.think("彼女を食肉目ネコ科ネコ属の生物にうまく見せているのはその外見と人工皮膚および人工毛だと理解しているが",
                "それ以上に実際のネコの神経回路をトレースした人工脳回路があるからだということを",
                "こうして一緒に生活しているとよく忘れてしまう"),
            h.think("だからこそ意図しないタイミングで彼女が只のロボットであることを認識させるのは止めて欲しいところだが",
                "開発者の$kiethにはそれを譲ろうという考えは微塵もなかった"),
            kisa.talk("ロボットであることを捨てさせてはいけない……か"),
            h.deal("彼の言葉を思い出し", "改めて彼女に視線を向ける。",
                "それなら何故これほど外見を猫そのものに似せてしまったのだろうと思わなくもない"),
            h.think("それでも、ただ彼女がそこに居る"),
            h.think("そのことが今の$Sの人生を支えてくれていることだけは確かなのだ"),
            )

def sc_mywork(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    aisaka = w.aisaka
    return w.scene("仕事にて",
            h.be(w.stage.office, w.day.working),
            h.deal("初夏のじっとりとした汗ばむ空気を避けるように足早に会社に駆け込んだ$meを待っていたのは",
                "体調を崩した数人が歯抜けになっている仕事場だった"),
            aisaka.talk("やあ$kisa。", "わざわざ出社してもらってすまないね"),
            h.deal("$aisakaチーフの額にも冷却シートが貼られ", "首には湿布も見える"),
            kisa.talk("$kaseまで抜けてるんじゃ無理もないですよ。",
                "それで納期までには間に合いそうなんですか？"),
            h.deal("メールで連絡を受けたのは昨夜遅くになってからだった。",
                "確認したのは今朝早くに目覚めてからで", "いつものように十時前まで寝ていたら午後からの出社になっていたところだ"),
            h.deal("一月ぶりの会社のパソコンは誰が使った後なのか分からないが",
                "キーボードの周囲に小さなゴミが散乱している。", "$meは溜息をつく傍らでひとまずそいつらをゴミ袋に突っ込み",
                "鞄から取り出した除菌シートで一通り拭った"),
            h.think("会社の誰が使ったか分からないようなものに触れるのは気が引ける。",
                "そう言った$meに眉を顰めた誰かがいたが", "誰かにそれを押し付けている訳ではないから自分の為に綺麗にするくらいは勘弁してもらいたい"),
            h.deal("自販機でコーヒーを買って来て席に就くと",
                "ようやく気分がモニタに表示された決済システムのスパゲッティになったコードに向かう"),
            kisa.talk("ゼロから作り直した方が早そうだ"),
            h.deal("ひと目見てそう感じたがスケジュールを考えるとその余裕はもうないらしい"),
            h.deal("仕方なく", "$kiethからの頼まれ仕事は半年放り出す覚悟をして",
                "エンターキィを押した"),
            # NOTE: 仕事で外出、心配になるが、トラブルで帰れず
            )

def sc_lostcat(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    return w.scene("猫のいない家",
            h.be(w.stage.living, w.day.vanish1),
            kisa.talk("流石に今回のは参った"),
            h.deal("玄関ドアを開けてそのまま転がり込むように上がる"),
            h.deal("急な呼び出しから約一月",
                "殆ど会社に泊まり込みで何とか頓挫しかけた決済システムのベータ版の提出は間に合わせたが",
                "叩いた先からバグが噴出して", "正直もう誰の手にも負えない状態だった"),
            h.deal("それでもやっと一日の休みを手に入れて我が家に帰って来られたのだ"),
            kisa.talk("$ary？", "どこだ？"),
            h.deal("出かける前に充電器に掛けておいたはずだがそこに彼女はいなかった。",
                "胴体を押さえつけておく金属のアームが曲がっている。", "強引に上げたのだろう"),
            h.look("ロボット猫が一人で目覚めてどこかに行ったという可能性もあるが",
                "一番疑うべきは盗難被害だった。",
                "すぐにリビングだけでなく寝室や物置を探る。",
                "だが荒らされた様子はなく", "見慣れた整然さがどの部屋にも敷き詰められていた"),
            h.look("それでも一箇所だけ", "トイレの窓が割れているのを見つけて$Sは慌ててリビングに戻る"),
            h.deal("パソコンを起動する。",
                "携帯電話の方にはソフトが入っていないから一分ほど我慢して",
                "モニタに地図と彼女の位置が表示されるのを待った"),
            h.deal("電波が捉えられない場所に入り込んだりしていなければＧＰＳが誤差一キロ圏内で特定してくれる"),
            kisa.talk("ん……？"),
            h.look("彼女を示す赤い点は臨海公園付近を差していた"),
            )

def sc_brokencat(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    return w.scene("壊された猫",
            h.be(w.stage.park1),
            h.deal("すぐに電車を乗り継いで臨海公園駅に向かう。",
                "平日の午後だからかそれほど車内は混んでおらず",
                "到着するまでに携帯電話で$kiethと幾つかメールのやり取りをした").omit(),
            h.deal("改札を出て階段を駆け下りる").omit(),
            h.look("慌てて駅の階段を駆け上がるとブロックが敷き詰められた駅前広場にはベビィカーを押す女性やカップルらしき男女が目に付いたが",
                "雉色の猫に限らず動物の姿は鳩以外なかった"),
            h.look("右手には数年前から故障したままになっている大観覧車の姿が見えて",
                "あまり良くない思い出が蘇ったが", "それを振り切るように頭を揺らすと公園の方に足を向けた"),
            h.think("猫だから何かの拍子に家を出ていき迷子になったりして居なくなる。",
                "そういう可能性については既に$kiethと検討を充分に済ませていたから",
                "一つの対策としてＧＰＳで場所を特定できるようにはしておいた"),
            h.think("ただそれは猫ロボットが電波を発信できる状態が確保されている必要があり",
                "意図的にそれを遮断されてしまった場合においては",
                "従来の猫と同様", "目視で探すしかなくなる"),
            h.deal("その不完全さを解消する手段は結局", "家から彼女を出られないようにするしかないのだろう"),
            h.think("――プログラム的な監禁"),
            h.deal("そんな言葉が思い浮かび", "$Sは苦笑する"),
            h.think("結局自律した自由な存在を求める先には", "そんな歪《いびつ》さを準備しないといけないのかも知れない").omit(),
            kisa.talk("おーい。", "$ary？", "いないのか？"),
            h.deal("自分の声の周波数を検知して何かしら反応を返すようになっていると説明は受けているが",
                "物陰や人の足元からこそっと顔を覗かせる様子はない"),
            kisa.talk("$ary"),
            h.deal("最初こそ丁寧に呼びかけていたのだがそのうちに面倒になってきて",
                "ただ彼女の名を連呼しているだけになってしまう"),
            h.think("けれどそれは仕方のないことだ。",
                "彼女は人ではない。", "猫ですらない。", "ただのロボットだ。",
                "見た目こそよく自然の猫に似せて造られているが", "その声も温度も仕草も",
                "所詮は造りものでしかない"),
            h.deal("$kiethはこうなることも踏まえて『ロボットはロボットらしさが大切だ』と言ったのだろう"),
            h.look("動かなくなったままの大観覧車の下までやってきたが", "彼女は見つからない"),
            h.look("見上げると数カ所サビているのが分かったが", "メンテもなく", "誰も気にしないようになったらこんなものだろう。",
                "やがては朽ちてどこかが傾いたり或いは部品やワゴンの落下もあるかも知れない。",
                "そういう出来事が発生してようやく危険だと認識され", "修理するか解体するかという選択が取られる"),
            h.deal("閉鎖中と書かれた黄色いプレートのぶら下がる前に腰を下ろし",
                "砂浜の方を見やる。",
                "まだ入るには水が冷たいかも知れないと思うが意外と人が集まっていて", "賑やかな声が聞こえてくる"),
            kisa.talk("いや、あれは……"),
            h.look("よく見れば何かを見つけて騒いでいるのだ"),
            h.deal("それが何か確かめようと向かった$Sを待っていたのは", "水分を含んだ砂に埋まっていたキジトラの猫だった。",
                "いや猫ではない。", "彼女だ"),
            kisa.talk("すまない。", "それは$meの物なんだ"),
            h.deal("集まっていた若者を掻き分け", "黒っぽい砂が付着してしまった猫ロボットの成れの果てを受け取る。",
                "シャツの袖が汚れるが仕方ない。", "彼女はずっしりと重く", "人工毛が濡れていた"),
            h.move("その人垣から抜け出て", "大観覧車の前まで戻ってくる"),
            h.deal("ハンカチでは上手く水分を取り切れないが", "内部にまで水が入っていないことは確認できた。",
                "注意深く彼女の胴体側面にある起動スイッチを入れる。",
                "一瞬目が光るが", "彼女は動いたりはしなかった"),
            kisa.talk("$ary？"),
            h.deal("名前を呼んでみる"),
            kisa.talk("$aryどうしたんだ？"),
            h.deal("反応はなく", "何度かスイッチを入れ直してみたがもう起動サインの目の発光すら見られない"),
            h.think("電源か", "あるいは本格的な故障か"),
            h.deal("諦めて彼女を手に", "立ち上がる"),
            h.look("観覧車を見上げると強い風に上の方のワゴンが揺られて軋んだ音を立てていた"),
            kisa.talk("やはり厭な場所だな"),
            h.deal("$Sは重くなった彼女を抱いて", "駅に向かった"),
            )

def sc_revivecat(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    return w.scene("何度も蘇る猫",
            h.be(w.stage.living, w.day.revive1),
            h.deal("結局中をバラして精密検査をしてもらったが", "ハード的な故障はどこにも見当たらなかった"),
            h.deal("$kiethに人工脳のデータだけ送ってソフト的な問題の方を検討してもらっても",
                "そちらの方も特別問題は見られないということだった"),
            h.deal("一月ほど色々検査をして問題なしと判断された彼女は",
                "新品のボディになって$Sの許へと送られてきた"),
            kisa.talk("もういなくなるんじゃないぞ", "$ary"),
            h.deal("目を光らせて起動した彼女は小さく返事をすると",
                "定位置だったソファの上にぴょんと乗り",
                "そのまま前足に顎を載せて心地良さそうに寝そべる"),
            h.look("いつもと変わらない見慣れた姿に",
                "$Sの心は漸く落ち着きを取り戻したことを感じた"),
            kisa.talk("$ary"),
            h.hear("呼びかければ彼女が答えてくれる"),
            h.think("そんな些細だけれどかけがえのない日常が", "$Sたちの生活には必要不可欠なはずなんだ"),
            kisa.talk("あ……切らしていたか"),
            h.deal("飲料用の小さな冷蔵庫内には炭酸水のボトルしかなかった"),
            kisa.talk("いい子で待ってるんだよ"),
            h.deal("小さな返事が聞こえたことを確認し",
                "玄関を出る。",
                "まだ外の日差しは暑かったがそれでも首元を抜ける風に秋の冷たさを感じ",
                "$Sは足早に近所のコンビニに向かった"),
            h.deal("けれど僅か十分ほど不在にしていただけで",
                "再び彼女はいなくなってしまった"),
            )

def sc_vanishing(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    return w.scene("消える猫",
            h.be(w.stage.living, w.day.vanish2),
            h.deal("彼女はその後もことあるごとに失踪した"),
            h.think("最初に$Sは電波などのハードへの影響を考えたが",
                "$kiethはすぐソフト面", "つまりプログラムか或いは猫を模した人工脳そのものの作用だと指摘した"),
            h.deal("納得はいかなかったが", "それでも無限に代用のボディを用意できる訳ではない。",
                "仕方なく彼女の人工神経回路にある種のブレーキプログラムを組み込んだ。",
                "それは彼女がいなくなる直前に発する奇妙な回路の動きを捉えたことから$kiethが提案した案だったが",
                "実際そのブレーキは上手く利いた"),
            kisa.talk("またなのか……"),
            h.deal("会社から帰ってくると玄関先で彼女が横になって倒れている。",
                "目は開かれたままで前足を僅かに伸ばし",
                "後ろ足は蹴り出そうとしたところで動きを止められたままで床の上にいる"),
            h.deal("$Sは溜息をついて彼女を拾い上げると",
                "鍵の破壊されたドアから家の中に入った"),
            h.deal("ひとまず彼女のボディを充電器に戻すと",
                "ひん曲がった金属のアームを構わずに降ろして固定する"),
            h.deal("それから$Sはジャケットだけ脱いでハンガーに引っ掛け",
                "冷蔵庫から缶ビールを取り出すとそれを一気に喉に入れた"),
            kisa.talk("……どうしてなんだ"),
            h.think("十一月に入ってからこれでもう四度目だった。",
                "何が気に入らないのか知らないが", "突発的に発生するこの脱走行動は徐々にその間隔が短くなっていた"),
            h.deal("$Sは彼女の定位置である引っかき傷のあるソファに腰を下ろすと",
                "疲れた頭をもたれさせて天井を見上げる"),
            h.think("何が悪い？", "どこを間違えた？", "そもそも問題など幾ら探しても見つからないじゃないか"),
            h.deal("足の先で机を蹴る"),
            h.deal("人を殴ったりはしないが", "苛立った時に物に当たるのが小さい頃からの癖だった"),
            h.think("右の脛に痛みを感じながら",
                "それでも$Sは彼女がここから姿を消そうとする仕組みを考えようとする"),
            h.think("――問題は一つ一つ丁寧に紐解いていけば必ずその先に原因となる事象を見つけられる"),
            h.think("それは研究者である父から教えられたことだが",
                "事実", "世の中の大半の問題は丁寧に分析していけばそれなりの原因がちゃんと見つかるものばかりだった。",
                "ただそれをせずに勝手に思い込みで原因をでっち上げて", "挙句に関係ない人間を非難する。",
                "そういう輩の方がずっと多いことに$Sは辟易してしまう"),
            h.think("だからこそこうしてある程度在宅でもできる仕事を選んだのだ"),
            h.think("だったらどうして今の自分はこんなにも苛立っているのだろう"),
            h.deal("と、携帯電話が鳴った。", "$kiethからのショートメールで駅まで迎えに来てくれないかと書かれていた"),
            kisa.talk("来日するだなんて一言も言ってなかったじゃないか"),
            h.deal("それでも何度かやり取りをし", "東京駅までの時間を考えて今すぐに出た方が良いと分かり",
                "呼気に僅かなアルコールを含んだままハンガーに掛けたジャケットを掴んで玄関を出た"),
            h.deal("壊された鍵の代わりに足元にブロックを挟んでおいたが", "先に修理の電話を掛けておくんだったと後悔した"),
            )

def sc_myfriend(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    kieth = w.kieth
    return w.scene("友人",
            h.be(w.stage.ramen, w.day.visitjap),
            h.deal("半年ぶりに会った$kiethは相変わらず日焼けした真っ黒な肌で",
                "毛深い腕を派手なアニメのプリントされたシャツからはみ出させながらガハハと笑った"),
            h.deal("そのまま自宅には向かわずにジャパニーズラーメンが食べたいと言うものだから仕方なく",
                "五分ほど並んで人気のラーメン店に入った"),
            kieth.talk("$kisaはまだゴワサンになった決済プログラムをやってるの？"),
            h.deal("ご破算という言葉が引っかかることなく出てくる彼の日本語能力に今更感心はしなかったが",
                "$Sは「ああ」とだけ短く頷き", "チャーシュー麺を頼んだ"),
            h.deal("実際は敗戦処理みたいな仕事をいつまでもやっているのはチーフを含めた数名だけで",
                "$Sは新しいプロジェクトの方に掛かりきりになっている。",
                "ただそれは彼には一切話していない極秘の案件だったので",
                "そうやって誤魔化しておくしかなかったのだ").omit(),
            kisa.talk("来るなら一声掛けておいてくれればよかったのに"),
            h.deal("がっしりとした器から湯気を昇らせるラーメンが出されると",
                "まずは脂の浮いたスープを蓮華で掬い上げて唇を湿らせる"),
            kisa.talk("忙しくて迎えに行けなかったら", "また東京駅構内で一日過ごすつもりだったのか？"),
            kieth.talk("そういう時の為に$n_aryを使えるようにしてあったんだヨ。",
                "ただ君の彼女をどこにもやりたくないからという要望からその機能はオミットしてあるんダ。",
                "そろそろ彼女を自由にしてあげてもいいんじゃないか？"),
            h.deal("$kiethの前には山盛りのモヤシとコーンを載せた味噌ラーメンが置かれた"),
            kieth.talk("彼女は猫だヨ。",
                "猫というのは何かをサトった時には自分の居場所から立ち去るものダ"),
            h.deal("器用に割り箸を二つにしてモヤシの山を切り崩し",
                "麺を掴んで引っ張り出すと", "彼はそれを口に入れる。", "音を立てて豪快に啜る"),
            kisa.talk("猫だがロボットだ。",
                "いくら猫の神経回路を模したといっても", "そんな意味不明なところまで真似てもらう必要はない"),
            h.deal("熱い。",
                "脂混じりのスープを纏った麺はやたらと攻撃的な熱がある"),
            kisa.talk("自由というなら", "$meは既に彼女に十分な自由を提供しているはずだ"),
            h.deal("それを空気と一緒に吸い込む。",
                "喉を抜け", "胃袋までもその熱で焼いてしまおうというラーメンは",
                "どうしようもなく胃をキリキリとさせた"),
            kieth.talk("なあ$kisa。",
                "この丼の中のラーメンは自由だろうか？"),
            kisa.talk("またお得意のくだらないジョークか？"),
            h.deal("ふうふうと息を吹きかけている$Sの隣で豪快に麺を啜り上げてから", "$kiethは首を横に振る"),
            kieth.talk("このラーメンは$meたちに食べられる為にこの中に収まっているヨネ？",
                "それをどう食べるかどの順番で食べるか",
                "それについては$meたちが選ぶ。",
                "でもそれは制限された自由でしかなくて",
                "$meたちには結局食べるか残すか、そもそも食べないというくらいの選択肢しか渡されていないんだヨ"),
            h.think("いつも彼が言うことは少しズレている。",
                "ただ何が言いたいかは察することができたから",
                "$Sは小さな吐息を落としてから", "無言でラーメンの続きを食べた"),
            h.think("甘みの強い脂が口の中でのたうち回る"),
            h.think("いつも三分の一程度までは美味しい", "と感じるのにそこから先になると急にやる気を失った子供みたいに",
                "麺を丼の中でかき回し", "胡椒を振ってみたり", "水で何度も口の中をすすいでみたり",
                "サイドメニューを頼んだり", "本当はもう食べたくないんだという自分の気持ちと向き合うことから目を逸してしまう"),
            kieth.talk("$kisaは初めて会った時から変わらないヨネ。",
                "なら最初からハーフサイズを頼めば良かった"),
            kisa.talk("いつも見積もりが甘いだけさ。",
                    "誰だって最初はそれくらい食べ切れると思うんだよ。",
                    "けどそのうちに自分の手には余ると気づいて", "途方に暮れながらも何とか口の中に突っ込む。",
                    "人生ってそういうものだろう？"),
            h.deal("既にその殆どを胃袋に入れてしまった$kiethは笑って$Sの肩を叩くと",
                    "「要らないなら食べてやるヨ」と蓮華と箸を使って麺の移動を始める"),
            h.think("その仕草に", "この男と会うきっかけを与えてくれた彼女のことを思い出す"),
            h.think("外に出て", "人と人を会わせるのが自分の仕事だと楽しそうに語ってくれた彼女も",
                    "いつの間にか$Sの前からいなくなってしまった。",
                    "ひょっとすると誰もが$Sから離れていってしまうのかも知れない。",
                    "そういうプログラムが組み込まれているのだ。",
                    "なら", "$aryが出ていくのもまた", "$Sの所為ということになる"),
            h.think("結局、問題というのは一番目を背けていたところにひっそりと眠っているのだ"),
            h.deal("いつの間にか場所はラーメン店から居酒屋に移っていて",
                    "既に頬を赤くした$kiethが$Sの右肩にしなだれかかっていた。",
                    "カウンターに横並びで座る中", "後ろを忙しなくパートの女性が行き来する。",
                    "ビールのジョッキを幾つも束ねれば重いだろうにそれでも彼女は笑顔だ。",
                    "無理をしているのかどうかまでは推測することしかできない。",
                    "それでも今の$Sからすると", "心の底から楽しく働いているように見えた"),
            kieth.talk("何だヨ", "$kisa。",
                    "やっぱりまだ未練があるんだネ？"),
            kisa.talk("何を言ってるんだ。",
                    "だから何度も言ったろう？", "もう$meは諦めた。",
                    "$aryはどうしたって$meの前からいなくなってしまうんだ"),
            kieth.talk("$n_aryじゃない。", "$fn_arisaのことだ"),
            )

def sc_findword(w: wd.World):
    h = kisa = w.kisaragi
    ary, arisa = w.ary, w.arisa
    return w.scene("彼女が消えた意味、残した言葉",
            h.be(w.stage.living),
            h.deal("酔い潰れた$kiethを予約したホテルの部屋まで送ってから", "自宅に戻ってきた"),
            h.deal("ドアを開けようとして鍵が壊れたままだったことを思い出したが",
                "足元に置いたブロックを手ではなく足で押し退けるくらいには充分に疲れていて",
                "リビングまで上がってくるとそのままソファにダイブする"),
            kisa.talk("$ary……いるか？"),
            h.think("どうせまたいなくなる"),
            h.look("そんな思いで充電器を見ると", "そこには雉柄の猫ロボットが寝そべったままになっていた"),
            kisa.talk("$ary……そうか。", "まだ、ここに居てくれるんだな？"),
            h.deal("既に充電は終わっている。",
                "ひしゃげたアームを上げ", "彼女を抱き起こす。",
                "胴体側面の起動スイッチに手をやると", "目が光ってから彼女は小さく鳴いた"),
            ary.talk("ごめんなさい"),
            h.hear("と"),
            kisa.talk("え？", "$ary？"),
            ary.talk("もう動けないの。",
                "すまないけれどソファに置いてくれないかしら"),
            h.deal("彼女にそう言われ",
                "$Sは曖昧に返事をしながらその体をソファの上まで運んで寝そべらせた。",
                "前足の上に顎を置こうとするが", "小刻みに震えて上手く動かせないようだ。",
                "彼女の代わりに$Sが頭を置いてやる"),
            ary.talk("ありがとう"),
            kisa.talk("$ary……ではなく", "君なのか", "本当に？"),
            ary.talk("どうして驚いているの？",
                "このロボット猫の人工脳に$me", "$n_arisaのものを使うことを提案したのはあなただったじゃない？"),
            h.deal("音声こそ合成した無機質な駅や売店でよく耳にするものだったが",
                "その話しぶりは正に彼女", "$n_arisaのそれだった"),
            kisa.talk("猫の人工脳では上手くいかなかったからどうせなら人間の人工脳を試してみればと",
                "そう言っただけで", "何も君のものを使うだなんて……そんなこと一言も"),
            ary.talk("その理由は", "考えたことがあるの？"),
            h.think("$kiethならやりかねない。",
                "そういう予感がなかった訳ではない。", "けれどそんな倫理に反することを黙ってやるとは思ってなかったのだ"),
            h.think("何より彼女は", "$arisaは", "$Sたちの前から姿を消して三年になる"),
            ary.talk("今日", "$meの件について彼から話は聞いてないようね"),
            h.deal("ああ", "と脱力して答え", "$Sはそのままカーペットの上に腰を下ろした。",
                "ソファの彼女と目線が近くなる"),
            ary.talk("猫がある日突然飼い主の前からいなくなる。",
                "それについての幾つかの説を", "あなたに話したことがあるわね"),
            h.think("結婚したら絶対に猫を飼いたいと言っていた$arisaは",
                "自分よりも早く死ぬことが分かっていても決して手放したりせずに最期の瞬間まで一緒にいることを選ぶ。",
                "そう言っていたことを思い出す"),
            ary.talk("その気持ちがね", "今ならよく分かるの"),
            kisa.talk("猫になって学習した", "とでも言いたいのか？",
                "猫になってまで$meの前から何度も逃げ出した君は", "ただ$meという器から出たかっただけなんだろう？"),
            h.deal("猫の黒目が大きくなる。",
                "細く縦長のネコ科のそれではなく", "人間の瞳のように見えた"),
            ary.talk("何故逃げ出したのか。",
                "いつもみたいにちゃんと分析をしなかったの？"),
            kisa.talk("ハード的にもソフト的にも何も問題はなかった。",
                "だから勝手にいなくなったのは気まぐれだよ。", "気分だよ。",
                "ずっと家に閉じ込めていたから嫌になったんだよ。", "それでいいか？"),
            ary.talk("すぐ大声になる。",
                    "声が大きければ相手は黙る。", "黙れば自分の言葉が届く。",
                    "正しいと思える。",
                    "でもそうやって目の前の考えを排除してきたあなたには",
                    "結局猫一匹の気持ちすら理解できなかったのね"),
            h.deal("立ち上がり", "思い切りテーブルを蹴飛ばした。",
                    "派手な音を立ててひっくり返り", "上に置いてあったリモコンが投げ出される"),
            ary.talk("$n_aryはね", "もう自分の命がそう長くないことを知ったの"),
            kisa.talk("何だよ。", "ロボットに命も何もないだろう？"),
            ary.talk("ハードはいつか壊れるし",
                    "ソフトだってそれを運用するシステムのアップデートについていけなくなる。",
                    "いつかはね", "みんないなくなるのよ。",
                    "それがいつ", "とはっきり分からなくても", "予感するに値する何かがあれば",
                    "それで充分なの"),
            h.deal("涙を流す機能は備わっていないはずだ"),
            h.look("それなのに彼女の瞳からは液体が溢れていた"),
            kisa.talk("やはり壊れているんだな？", "明日にでも$kiethに来てもらって向こうで最初から作り直す手続きを"),
            ary.talk("$kisa"),
            h.deal("$arisaの呼び方そっくりに", "$Sの名が呼ばれた"),
            ary.talk("あなたに伝えておくべきだったのかも知れない。",
                    "でもね", "悲しい顔を二度もさせてしまうのは", "やはり嫌だったのよ"),
            kisa.talk("$arisa？"),
            ary.talk("さよならを言わない為に", "猫はあなたの前から消えるのよ"),
            kisa.talk("何を言ってるんだ？"),
            h.deal("電源が落ちたのが分かった。",
                    "妙なモータ音が響き", "目の光が消えた"),
            h.deal("$Sは慌てて起動スイッチを押したが反応はない"),
            h.deal("充電器にセットしたがそれも反応はない"),
            h.deal("$kiethに電話したが反応がない"),
            h.deal("この手に猫ロボットの冷たい感触はあったが",
                    "もう彼女はいなかった"),
            w.tag.symbol("◆"),
            h.deal("翌日", "$kiethの電話で目覚めた$Sは",
                    "$n_arisaが脳腫瘍で亡くなったことを知った。", "昨夜の十二時少し過ぎたくらいだったそうだ"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_catlife(w),
            )

def ep_vanished(w: wd.World):
    return (w.chaptertitle("消えた猫"),
            sc_mywork(w).omit(),
            sc_lostcat(w),
            sc_brokencat(w),
            sc_revivecat(w).omit(),
            )

def ep_waiting(w: wd.World):
    return (w.chaptertitle("待ち続ける"),
            sc_vanishing(w),
            sc_myfriend(w),
            )

def ep_knowreason(w: wd.World):
    return (w.chaptertitle("知る真実"),
            sc_findword(w),
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
    w = wd.World("The vanish cat")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("いつも彼女はいなくなる"),
            ep_intro(w),
            ep_vanished(w),
            ep_waiting(w),
            ep_knowreason(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

