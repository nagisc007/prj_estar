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
            f.be("tv見ていた", w.stage.home).d("折角の休日だというのに",
                "先月買い替えたばかりの６５型の４Ｋテレビの中ではいつの時代の芸能人か知らないが",
                "お値打ち価格だと言って金の腕輪やネックレスを売り捌こうと必死の笑顔を作っていた"),
            f.talk().t("おい$fn_hiroko",
                "お茶はまだか？"),
            f.think().d("来客の応対に出たまま一向に戻ってこない妻に苛立った声を上げたが",
                "玄関の方ではまだぼそぼそとした話し声が響いているのが分かった"),
            f.move().d("$Hは仕方なくソファから立ち上がり", "自分でキッチンへと向かう"),
            f.think().d("結婚して十八年", "一人娘は来年の春に高校卒業を迎える。",
                "そんな自分は世間的にはまだ幸福な部類に入るのだろうが",
                "$H自身はそんなものを感じたことは一度としてなかった"),
            hiroko.deal("応対", w.believer),
            f.move().d("冷蔵庫から麦茶を詰めたペットボトルを取り出し",
                "棚から出した適当なグラスに注ぐ。",
                "沢山飲みたいからと大きめのものを取ったが",
                "なみなみと注がれた濃い黄金色の液体は手にずっしりと重い"),
            f.ask().t("ん？"),
            f.look().d("振り返ると", "そこには妻の$fn_hirokoが立ってじっと$Hのことを見ていた"),
            f.ask("何だったんだ？"),
            hiroko.reply("宗教").t("宗教の勧誘ですよ"),
            f.look().d("濃いグレィのパンツスーツに身を包んだ$fn_hirokoは彼女がそのまま勧誘員だと言っても通用するくらい",
                "陰鬱な表情で溜息混じりにふたつ折りのパンフレットを差し出す"),
            f.look().d("表紙にはインドにでも転がってそうな目の細い仏像の写真が掲載されていたが",
                "”運命を変える”とか”幸福は手に入れるものではなく気づくもの”といったお決まりのフレーズがちらついたので",
                "すぐにゴミ箱に投げ入れてしまった"),
            f.talk(w.i.nogod.flag()),
            f.ask(kana).t("ところで$fn_kanaはどうした？", "昼飯にも顔を出さなかったが",
                "アレはまた仮病か？"),
            hiroko.talk().t("知りませんよ。",
                "そんなに心配なら$fukuoが見てくればいいでしょう？"),
            f.look().d("凝固した血のような口紅のそれがパクパクと開く。",
                "眉間に寄った皺は張り付いた汚れのように落ちなくなっているのか", "と思えてしまう"),
            hiroko.talk().t("$meはこれから塾の夏期講習の打ち合わせなんですよ。",
                "その後には$i_wifecircleもあるし……",
                "今日の夕飯は一人で食べて下さいね。",
                "それでなくてもさっきの人に時間を取られて忙しいのよ"),
            f.talk().d("お前がいつも相手に付き合って長話をするからじゃないか"),
            f.think().d("と言いたくなるのを堪えて首を振ると",
                "$Hはそのままリビングへと戻っていく。",
                "二階に上がれば部屋にいる娘に会うことも可能だろうが",
                "それよりはくだらないテレビ番組を流しながら午睡に浸る方を選んだ"),
            f.deal(hiroko, "口論", w.i.coupleproblem.flag()),
            )

def sc_golden(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    return w.scene("黄金になる娘",
            w.tag.comment("娘の不登校、黄金発症"),
            f.talk(hiroko, w.i.truancy),
            hiroko.look(w.stage.kanaroom),
            hiroko.talk(f, "娘が"),
            # NOTE: 黄金化のきっかけ
            f.be().d("その日の晩御飯は近所のコンビニで何か買ってくることにした"),
            f.think("いつまでも起きない娘").d("娘は何がいいだろうか考えようとしたが",
                "普段から声を掛けてもあまり反応がないような父娘関係だ。",
                "自分が考えたものを喜ばないだろう"),
            f.go(w.stage.kanaroom).d("階段を登り終えると",
                "すぐ左手に見える花形のプレートが掛かったドアの前に立つ。",
                "ノックは三度", "それもゆっくり叩くと決めていた"),
            f.ask().t("$fn_kana", "起きてるか？",
                "晩御飯を買って来ようと思うんだが", "何かリクエストはあるか？"),
            f.hear().d("返事はないだろう"),
            f.think().d("そう思っていたがか細い娘の声がドア越しに響いたことに気づいた"),
            f.ask().t("ん？　何か欲しいものがあるのか？"),
            f.hear().d("再び返答のようなものがあったのだが",
                "いかんせんドアが邪魔だ"),
            f.ask().t("入るぞ？", "いいか？"),
            f.go().d("それに対して断るような声でなかった為",
                "$Hはドアを開けた。",
                "鍵は掛かっておらず", "そのままするりと押すことができた"),
            f.ask().t("$fn_kana？"),
            kana.be(w.i.goldsyndrome, w.stage.home, w.day.current),
            f.look().d("いつものようにカーテンが締め切られているのが分かったが",
                "何故か真昼のような部屋の明るさだった。",
                "まるで投光機でも焚いているかのような眩しさに",
                "$Hは思わず自分の顔の前に腕を出す"),
            f.think().d("一体何の悪戯なのだ"),
            f.look().d("指の隙間からその光源に視線を向けてみると",
                "有精卵にライトを当てた時のように中でシルエットが動いていた。",
                "それはよく見れば人の形をしていて",
                "ベッドの上で体を起こす自分の娘のようだと思い至ると",
                "その発光は不意に収まった"),
            f.ask().t("$fn_kana？"),
            f.look().d("小学生の頃と変わらない", "花柄がプリントされた黄色のパジャマ姿の小柄な娘が",
                "微笑みながら自分の右掌を広げて天井へと向けている"),
            f.ask().t("$fn_kana……？"),
            kana.talk().t("きれい……"),
            f.look().d("その手の甲が天井の電灯を反射し",
                "$Hの視界を再び奪った"),
            f.look().d("それでもと目を凝らして見やると",
                "娘の皮膚は金粉をまぶされたかの如くに光り輝いていた"),
            f.ask().t("$fn_kana……何だそれは"),
            f.look().d("けれどそれには答えず",
                "$fn_kanaはにっこりとしたまま$Hへとその右の手の甲を向ける"),
            f.deal("guard", kana),
            f.come(w.stage.kanaroom),
            f.look(kana, "黄金化"),
            kana.talk("きれい").t("ねえ$dad。", "$me",
                    "こんなに綺麗なものになれるんだね"),
            f.talk(hiroko),
            f.think().d("それはこの十数年の内で初めて目にする",
                    "娘の嬉しそうな表情だった"),
            )

def sc_strangesick(w: wd.World):
    f, hiroko, kana = w.fukuo, w.hiroko, w.kana
    return w.scene("奇妙な病",
            f.go(w.stage.hospital).d("その日の内に市民病院に向かい",
                "娘の変色してしまった右手を診てもらった"),
            kana.deal("診察"),
            w.medic1.feel("驚き").t("これは……"),
            f.deal().d("だが救急の先生も",
                "呼び出した皮膚科の先生も",
                "その初めて目にする奇妙な現象に口を閉ざし",
                "自分たちの手には負えないからと大学病院への紹介状を書いて",
                "病室から追い出してしまった"),
            w.medic1.talk("大きな病院で診てもらった方が"),
            f.look("看護師が触れた", w.i.infection.flag()),
            f.go(w.stage.univhospital).d("その翌日",
                "仕事を休んで隣の大きな市内にある大学病院に向かったが",
                "朝から予約をしたのに結局診てもらえたのは昼を過ぎてしまってからだった"),
            f.deal().d("皮膚癌の専門医だと紹介されたが",
                "彼も初めて見る症状にその日から数日を掛けて精密検査を行った"),
            f.deal().d("その間", "仕事を無理には休めないという妻に代わり",
                "$Hが有給を消化して何とか毎日病室へと通った"),
            f.look().d("娘は何故か集中治療室の個室に移され",
                "世話をする看護師たちは手袋と完全防護の滅菌服を着て作業を行い",
                "$Hはただ服や下着などを彼女らに手渡すことしか許可されなかった"),
            w.medic2.talk("専門の機関を紹介"),
            f.deal().d("それでもちょうど十日が経ち",
                "やっと$fn_kanaを診察した専門医の男性から容態の説明を受ける機会を得られた"),
            f.ask().t("あの",
                "それで娘は一体何が悪いんですか？"),
            f.look().d("けれどそう尋ねた$Hに彼は首を横に振って答えると",
                "一枚の名刺と茶封筒を手渡しながらこう言った"),
            w.medic2.talk().t("$me共の手には負えません。",
                "紹介状を書いたのでこちらの研究機関を訪ねて下さい"),
            )

def sc_goldsyndrome(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("黄金化症候群",
            f.go(w.stage.labo).d("名刺に書かれていた$st_laboは神戸にあった"),
            f.deal().d("移動には公共交通機関は絶対に使わないで下さい",
                "と注意され",
                "慣れない運転で高速道路を一昼夜掛けて走り抜け",
                "研究所の駐車場に滑り込んだ時には約束の十時を大幅に過ぎてしまっていた"),
            f.talk().t("すみません。",
                "普段あまり長時間運転をしないもので"),
            f.look().d("受付でそう謝罪しながら約束をしていた$ln_fukuoだと名乗ると",
                "話が通っていたようで",
                "すぐに内線で担当者が呼び出された"),
            f.deal().d("自分で娘を連れて部屋まで行くと言ったのだが",
                "何故かその場でスタッフが来るまで待機させられ",
                "手袋にしっかりと全身を覆う長袖のワンピースを着込んで疲れた様子の娘と共に",
                "十五分ほどだろうか",
                "ソファに座ってじっと待っていた"),
            f.meet(w.stage.labo, doc).d("エレベータを降りて現れたのは",
                "医者や研究者というよりも",
                "取引先企業の重役といった雰囲気の",
                "仕立ての良いスーツを着た男だった"),
            doc.talk().t("どうも初めまして。",
                "$n_docと言います。",
                "こちらの所長を務めておりますが",
                "うちの研究プロジェクトのリーダーもやっております"),
            f.look().d("差し出された手を握ると",
                "彼は軽くそれに左手も重ねてから「宜しくお願いします」と言葉を付け加えた"),
            doc.talk().t("まずはお嬢さんをうちのスタッフが預かります。",
                "おそらくここまで来るのに症状が進んでいる可能性もあるので",
                "今から緊急に検査を行いますが",
                "宜しいですね？"),
            f.reply().t("ええ、はい"),
            f.think().d("その手際の良さに圧倒されながら",
                "現れたマスクに手袋といった完全防備のスタッフたちによって担架に乗せられた娘が運ばれるのを見送ると、"),
            doc.talk().t("ではあちらで詳しいお話をしましょう"),
            f.go().d("$Hは$ln_docについてエレベータに向かった"),
            f.deal(kana, "預ける", w.stage.labo),
            doc.talk(f, "黄金化症候群"),
            f.know("不治の病"),
            doc.talk("莫大な研究費"),
            doc.talk("国の助成金が少ない"),
            f.know(THM["money"]),
            )

def sc_doctor(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("博士の説明",
            f.go(w.stage.docroom).d("五階に上がると",
                "そのまま突き当たりの部屋へと案内された"),
            doc.talk().t("研究室は別にあるんですがね",
                "ここが外の景色も見えて気に入っているんですよ"),
            f.look().d("ドアを入ったところはパーテーションで仕切られていたが",
                "そこを抜けると全面ガラス張りの見通しの良い明るい部屋が広がった。",
                "ベランダもあり", "そこに立てば潮風も感じられそうだ"),
            doc.talk().t("適当に掛けて下さい。",
                "そうだ。",
                "何か飲まれますか？"),
            f.look().d("そう言って彼は冷蔵庫を開ける。",
                "$Hはソファに腰を下ろしながら$ln_docがビールの缶を取り出したのを見て",
                "苛立ちを抑えながら自分は要らないと告げた"),
            f.ask().t("あの、すみませんが",
                "$meはお酒を飲みにここまで来た訳じゃないんです"),
            doc.reply().t("分かっていますよ。",
                "これは冗談です。",
                "少しお疲れのようだから気分を緩めてもらおうと思いましてね"),
            f.look().d("苦笑するとそれを冷蔵庫に戻してソーダ水のペットボトルを二つ取ると",
                "$ln_docは$Hの対面に座ってその一本を前に置いた"),
            doc.talk().t("大学病院からは既に検査データを貰っていますが",
                "こちらでより専門性の高い精密検査を行わせていただきます"),
            f.talk().t("また検査ですか"),
            f.think().d("今までの医者たちも散々検査しておいて「他のところで」と何度も先送りにされ",
                "いい加減頭に来ていたが",
                "$Hの小さな溜息を見て$ln_docは首を横に振った"),
            f.ask().t("何だというんだ？"),
            doc.talk().t("ある程度予測はついています。",
                "ただ世界でも類を見ない症例なので慎重に慎重を重ねているのです"),
            f.look().d("ペットボトルの蓋を捻ると", "プシュ",
                "と小気味よい音が響く。",
                "それを一口飲んで$ln_docは眉を寄せる"),
            doc.ask().t("進行性骨化性線維異形成症",
                "という言葉を耳にしたことはありますか？"),
            f.think().d("突然の専門用語だった。",
                "病気の名前だということは理解したが",
                "いくら医療機器の開発に携わっているとはいえ",
                "その方面に明るい訳ではない"),
            f.reply().t("いえ。全然分かりません。",
                "それが娘の病名なのですか？"),
            doc.talk().t("これはかつて”石化”と呼ばれていたものですが",
                "現在では遺伝子異状によるものであり",
                "筋繊維などが骨へと変わるものだということが分かっています"),
            f.think().d("話された意味こそ何とか理解できたが",
                "それが娘の症状だと言われると違和感があった。",
                "そもそも$fn_kanaの右手のあの状態はとても骨になったとは言えない"),
            f.ask().t("それじゃあ娘はこのまま全身が骨になってしまうというんですか？"),
            f.look().d("けれどその問いかけに首を振り", "彼は$Hの目をじっと見据えてこう唇を動かした"),
            doc.talk().t("彼女の場合は骨ではありません。",
                "金です。", "黄金になるんですよ"),
            f.deal(w.fund),
            hiroko.talk("娘の細胞を売るべき"),
            doc.come(w.stage.home),
            doc.deal(w.i.heal),
            doc.talk("我々に任せて下さい"),
            f.know("看護師の感染", w.i.infection.deflag()),
            f.deal("研究所に預ける決断"),
            f.look(hiroko, "渋っているよう"),
            kana.deal("奪われる", w.kanacell),
            )

def sc_kanacondition(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    return w.scene("娘の状態",
            f.go(w.stage.labo).d("自宅から神戸までとなると流石に毎日通う",
                "という訳にはいかなかった"),
            f.think().d("おまけに妻は夏期講習の準備だ何だと忙しいらしく",
                "大半は$Hが一人で向かうことになった"),
            f.go().d("そのお陰という訳ではないが",
                "道や運転にも慣れ",
                "スムーズに研究所の駐車場に車を停められるようになった"),
            f.go().d("娘の着替えなどを入れた大きな紙袋を持って車を下りると",
                "玄関へと向かう"),
            f.talk().t("こんにちは。", "$Hです"),
            f.deal().d("受付でゲスト用のＩＤカードを貰い", "エレベータで三階に上がる"),
            f.talk().t("調子はどうだ？"),
            f.meet(kana).d("娘の部屋は完全な個室で",
                "入室するには手袋にマスク、滅菌エプロンが必須だったが",
                "それでも面会謝絶という訳ではなく",
                "今までの待遇に比べると恵まれているように感じられた"),
            f.look().d("ベッドに横になる$fn_kanaは少し腫れぼったい目をこちらに向けると",
                "まだ黄金化していない左手を挙げて僅かに微笑む"),
            kana.ask("母のこと").t("$dadだけ？"),
            f.reply("用があって", w.i.wifetrouble.flag()).t("ああそうだ。",
                "あいつは塾の仕事がどうしても抜けられないんだと言っていたよ。",
                "それよりまだ毎日検査ばかりなのか？"),
            f.deal().d("血圧や体温の計測をしていたスタッフが苦笑して$Hを見たが",
                "娘と目線を合わせて笑うと軽く会釈して部屋を出て行った"),
            kana.talk().t("検査というより観察されているみたいって",
                "$suzunoとも話してたの"),
            f.ask().t("$fn_suzunoさん？", "今出て行った人？"),
            kana.talk().t("うん。",
                "博士の助手の中で", "$meに一番優しい人"),
            f.reply().t("そうか"),
            f.think().d("ここに来てから娘の表情が柔らかくなった",
                "と感じる。",
                "それともただ単に",
                "今まで$Hがあまり娘と話す時間を持とうとしなかっただけだろうか"),
            f.ask().t("それで治りそうなのか？"),
            f.think().d("所長の$ln_docからは娘は特殊な症状であり",
                "まずは治療法云々ではなく類似する症例との比較から進行を緩和する方法を模索すること",
                "それと同時に国や団体からの資金援助を受ける為に精密な検査結果とそれをまとめた提出書類の作成が必要であり",
                "最終的には現在遺伝子治療の最先端であるｉＰＳ細胞を使った治験を行えるよう働きかけなければならないと",
                "早口で説明を受けた"),
            kana.reply().t("刺激を与えちゃいけないんだって"),
            f.ask().t("転んで打ったりとか", "ぶつけたりとか",
                "そういうことか？"),
            f.look().d("娘は力なく頷くと",
                "留められたバンドを外してその右手を覆う分厚い手袋を取った"),
            f.talk().d("あぁ……"),
            f.look().d("窓からの明かりを強く反射する黄金の皮膚は",
                "$Hが最初に部屋で見た時よりもずっとその範囲が広がっていた。",
                "今では手首から前腕の中程までが光り輝いている"),
            kana.talk().t("もう指が動かなくなったの"),
            f.look().d("その黄金細工のようになった右の五本の指を見せながら",
                    "娘は笑おうとしていた"),
            f.hear(doc, "容態"),
            f.be("娘の状態が安定していると聞いて安心して帰る"),
            )

def sc_wifecondition(w: wd.World):
    f, hiroko, kana, doc = w.fukuo, w.hiroko, w.kana, w.doc
    afterhospitalize = w.day.hospitalize.elapsed(day=10)
    return w.scene("妻の苦悩",
            f.go(w.stage.home, afterhospitalize).d("一晩を研究所内の仮眠室で過ごし",
                "翌朝には自宅に向けて出発する。",
                "着いた頃には既に今日の大半が終わっていて",
                "鍵の掛かった玄関を開けて自室に戻ると",
                "明日の仕事の準備もままならないまま",
                "ベッドに倒れ込む"),
            hiroko.talk().t("あなた？",
                "ねえあなた……？"),
            f.look().d("目覚めると$fn_hirokoが心配そうに顔を覗き込んでいた。",
                "七月半ばに入ったのに薄手とはいえスーツを着込む彼女に呆れつつも目覚めると",
                "手短に容態を告げる"),
            hiroko.talk().t("それよりもご飯にしましょう。",
                "ちゃんと食べた方がいいわ"),
            f.reply().t("ああ", "そうだな"),
            f.think().d("そう答えた自分の声が随分と痩せているように感じた"),
            f.think().d("この一月ばかり病院や研究所", "それと会社と家の往復以外は殆ど眠ってばかりいる。",
                "けれどいくら目を閉じて休んでみたところで",
                "現実という疲労はどこにも消えてくれない"),
            f.deal().d("だから食事を終えると",
                "また出かけるという妻を呼び止め",
                "つい口走ってしまった"),
            f.talk().t("お前は$fn_kanaのことを何とも思わないのか？"),
            hiroko.reply().t("ずっと思ってましたよ……あなたと違って"),
            f.look().d("洗面台に向かって口紅を直す妻の瞳は",
                "鏡越しに$Hへと向けられる"),
            hiroko.talk().t("$fn_kanaを産んでから一体何年間ずっと思っていたか",
                "あなたには分からないでしょうね。",
                "そもそも$meが塾で働くことになったのだって",
                "元はといえばあなたがどうしても現場の仕事がしたいと再就職なさったからでしょう？",
                "そういうこと全部忘れて今だけ父親らしい面をしたところで",
                "これまでの十八年間がチャラになるとでも？"),
            f.talk().t("なら仕事を辞めればいいだろ？",
                "やりたくないことを無理して続けなくていい。",
                "それは$meが君と結婚する時にも言ったはずだ"),
            f.talk(hiroko, kana, "状態"),
            f.think().d("苛立ちの言葉を上手く呑み込むことができなかった"),
            f.look(hiroko, "疲れ").d("化粧を直し終えた$fn_hirokoが振り返ると",
                "ＣＡＤによってミリ単位まで綺麗に整形された図案のような顔を向け",
                "怒りも苛立ちも捨て去った声でぽつり", "と言った"),
            hiroko.talk(f, w.i.wifetrouble.deflag()).t("じゃあ行ってきます"),
            f.look().d("その背を見送りながら",
                "これは妻の意趣返しだろうかとぼんやり考えていた。",
                "中学の頃に不登校になった娘を「どうしよう」と相談してきた時に",
                "自分も同じように会社や仕事を口実に背を向けてしまったことに対しての",
                "言葉よりもずっと重い何かの塊なのだろう"),
            f.know(hiroko, "病気のことは母親が悪い"),
            hiroko.deal("辞めたい", w.i.wifecircle),
            f.talk("辞めればいい"),
            hiroko.talk("何も分かってない"),
            )

def sc_robbed(w: wd.World): # NOTE: 分量的にカット
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
            ).omit()

def sc_famous(w: wd.World):
    f, hiroko, kana, doc, suzuno = w.fukuo, w.hiroko, w.kana, w.doc, w.suzuno
    return w.scene("有名になる娘",
            f.be().d("八月もいつの間にか終わりを迎えようとしていた"),
            f.look("tv", "取り上げられる").d("その日は珍しく家でゆっくりとテレビを見て過ごすことが出来たのだが",
                "朝のワイドショーの特集の中で",
                "『黄金になる少女』として娘のことが取り上げられているのを目にした"),
            f.think().d("名前や顔こそ隠されていたが",
                "その施設は明らかに$st_laboであり",
                "インタビューを受けていたのは所長である$n_docだった"),
            f.talk().t("どういうことなんだ？"),
            f.deal().d("慌てて電話をしたが",
                "急用で出かけていると言われて",
                "$Hの応対にはスタッフの$n_suzunoが当たってくれた"),
            f.ask().t("今テレビでやっているのを見たんですけど",
                "あれじゃまるで面白半分の娯楽番組じゃないですか"),
            suzuno.reply().t("$meもそう思うんですけど",
                "こうやって認知度を上げてそれを後押しに何とか研究費用を獲得しようと博士も必死なようで"),
            f.talk().t("お金が掛かるのは何度も言われて分かっていますよ。",
                "けどね",
                "娘はパンダじゃない。",
                "それに娘にマイクを向けたあの女性",
                "マスクも何もしていなかったじゃないか。",
                "一体あんたのところの管理体制はどうなってるんです？"),
            f.think().d("思わず声が荒くなる。",
                "それでも病気の進行が緩くなっていると言われて気分が落ち着いていたところにこんなものを見せられたのだ。",
                "誰だって血圧が上がる"),
            f.think(kana, "guard"),
            f.look().d("時刻を確認するとまだ昼には早い。",
                "今から出れば夕方までには着くだろう"),
            f.talk().t("とにかく",
                "今からそっちに行きます"),
            suzuno.reply().t("あ、あの", "$ln_fukuoさん"),
            f.deal().d("電話を切り",
                "おちゃらけた笑い声が響くテレビも消した"),
            f.think().d("今日も仕事だという妻に何か言っておくべきかと思ったが",
                "メモを残すことも面倒になり",
                "結局そのまま台所のシンクに飲みかけのジンジャーエールを置いて",
                "出掛けた"),
            f.go(w.stage.labo),
            f.ask(doc, "どういうつもりだ"),
            doc.reply("研究費用を集める為"),
            doc.explain(f, w.i.gatherfund, THM["money"]),
            doc.ask(f, "命を守る為なんですよ？"),
            f.think("承諾するしかない"),
            f.look("研究所内を案内される記者たち"),
            f.look(w.suzuno, "案内している女性"),
            # NOTE: suzuno外見描写
            hiroko.be(w.i.neurosis),
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
            ]

def ep_unfortune(w: wd.World):
    return [w.chaptertitle("不幸の始まり"),
            sc_doctor(w),
            sc_kanacondition(w),
            sc_wifecondition(w),
            sc_robbed(w),
            sc_famous(w),
            sc_neverstop(w),
            sc_takehome(w),
            ]

def ep_decision(w: wd.World):
    return [w.chaptertitle("決断の時"),
            sc_spreading(w),
            sc_limitpoint(w),
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
    return (w.maintitle("幸福の黄金少女"),
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

