# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd


# configs
CHARAS = (
        ("yuko", "浅見夕子", 18, "female", "高校生",
            "me:私:eri:足立さん:tagawa:田川君:fulltagawa:田川昼男:takemura:竹村:granpa:じいちゃん:granma:ばあちゃん:mam:お母さん:bro:正嗣"),
        ("tagawa", "田川昼男", 18, "male", "高校生", "me:俺:yuko:浅見:granpa:祖父さん"),
        ("takemura", "竹村紀行", 56, "male", "数学教師", "me:僕:yuko:浅見:tagawa:田川"),
        ("boys", "男子生徒", 18, "male", "高校生"),
        ("eri", "足立衣里", 18, "female", "高校生", "ME:足立衣里:me:わたし:yuko:あさみん:tagawa:田川"),
        ("granpa", "浅見健三", 78, "male", "農家", "me:ワシ:yuko:夕子"),
        ("granma", "浅見しの", 77, "female", "農家", "me:わたし:yuko:夕ちゃん"),
        ("mam", "浅見晶子", 40, "female", "レジ打ち", "yuko:夕子:me:私"),
        ("bro", "浅見正嗣", 15, "male", "中学生", "me:俺:yuko:姉ちゃん"),
        )

STAGES = (
        ("town", "衣保川町", "地方都市（岐阜県・揖斐川がモデル）の田舎町"),
        ("school", "高校", "県立高校"),
        ("classroom", "教室"),
        ("tanbo", "田んぼ"),
        ("tahouse", "田川家"),
        ("myhouse", "自宅"),
        )

DAYS = (
        ("sunnyday", "天気な日", 4, 15, 2019),
        ("rainyday", "雨の日", 4, 20, 2019),
        ("examday", "試験日", 4, 24, 2019),
        ("gwday", "ゴールデンウィーク", 5, 3, 2019),
        )

ITEMS = (
        ("tractor", "トラクター"),
        ("cycle", "自転車", "夕子が通学に利用する自転車"),
        ("uniform", "学生服"),
        ("futurepaper", "進路予定表"),
        )

INFOS = (
        ("tagawaseat", "田川の席"),
        ("vanish", "田川不在"),
        ("hiyori", "田川日和"),
        ("myhiyori", "自分日和"),
        ("reason", "サボる理由"),
        ("fam_reason", "家族の事情"),
        ("circs", "田川の事情"),
        ("myfuture", "自分の将来"),
        ("countryside", "田舎"),
        )

FLAGS = (
        ("hiyori", "田川日和の謎"),
        ("future", "夕子の将来"),
        ("transfer", "転校生"),
        )

# episodes
def ep_intro(w: wd.World):
    yuko, tagawa, boys, eri, takemura = w.yuko, w.tagawa, w.boys, w.eri, w.takemura
    sunnyday = w.day.sunnyday
    nextday = sunnyday.elapsed(day=1)
    classroom, school, town = w.stage.classroom, w.stage.school, w.stage.town
    reason, hiyori = w.i.reason, w.i.hiyori
    tractor, uniform, futurepaper = w.tractor, w.uniform, w.futurepaper
    sc1 = w.scene("田川のいない日",
            w.tag.comment("夕子の一人称"),
            w.tag.comment("田川はep2まで登場させない"),
            yuko.be(classroom, sunnyday).d("教室の窓側を見やると温かな日差しが入り込んで眩しい"),
            yuko.look("黒板").d("$Sは黒板に書かれた『山月記』というタイトルと",
                "それに続く留め跳ねのしっかりとした箇条書きをノートに書き写しながら",
                "もう一度窓際の彼の席を見やった"),
            yuko.look(w.i.tagawaseat).d("ぽつんと一つだけ空いている"),
            yuko.think(w.tagawa).d("田川昼男は今朝からずっといない。",
                "と言っても彼が不登校という訳ではない。",
                "事実昨日は登校してちゃんと苦手な数学の授業も聞いていた"),
            yuko.think().d("田川がいない"),
            yuko.think().d("けれどそのことに関して気にしているのは",
                "どうやら自分だけだと気づいて",
                "$Sは頬杖を突きながら何だか納得できない気持ちにとりあえず蓋をした"),
            )
    sc2 = w.scene("田川日和",
            w.combine(
                sunnyday.explain("午前の休み時間").d("休み時間になり、"),
                classroom.explain("教室の様子").d("誰もが友達同士で集まってどうでも良い話で適当に盛り上がるのを見ながら、"),
                yuko.think(uniform, w.flag.transfer).d("$Sは未だに馴染めない",
                    "真新しい野暮ったい紺のブレザーの青いタイを弄っていた"),
                ),
            eri.ask(yuko).t("ねえ$yuko。",
                "アレ書いた？"),
            yuko.look(eri).d("後ろを振り返って訊いてきたのは",
                "この数日で急に会話をするようになった足立衣里だ"),
            eri.explain("赤縁の眼鏡が目立つけれど",
                "それよりも今朝はいつも自分で切るという前髪の右の方がカットし過ぎた感がある方が",
                "$Sとしては気になった"),
            yuko.reply(eri).t("アレじゃ分かりません"),
            eri.ask(yuko).t("そういうのは適当に察していかないと",
                "この田舎町じゃ生きてけないよ？"),
            yuko.think(w.i.countryside).d("田舎",
                "という言葉の響きが",
                "どうしようもなく後ろに括った髪の房にぶら下がるようで",
                "それに触れる度に$Sは気分が沈んでしまう"),
            eri.look(futurepaper).t("ソレですよ", "ソレ。",
                "ちゃんと$yukoの机の上にあるじゃない"),
            yuko.have(futurepaper, w.flag.future).d("言われて咄嗟に手で隠した印刷物には",
                "進路予定表と書かれていた"),
            boys.talk(tagawa, "またサボり").t("そういや田川またか？"),
            boys.explain(uniform, "制服の前を全開にした男子").d("前の席に集まっている数人の男子生徒の声だ"),
            boys.look(w.i.tagawaseat).d("彼の席をちらちらと見やりながら口元を同じように歪めて",
                "へへら", "みたいな笑い声を漏らしている"),
            yuko.hear(eri, reason).t("あのさ"),
            yuko.ask(eri).d("何も書いていない夕子の予定表を取り上げて眺めている衣里に",
                "そんな$fulltagawaについてそれとなく訊いてみた"),
            yuko.ask(eri).t("みんな何も言わないの？"),
            eri.reply(yuko, "知らない").t("$yuko知らないんだっけ？"),
            yuko.reply(eri).t("逆にみんなは知ってるの？").omit(),
            yuko.look("$ps", eri).d("足立衣里は目を細めて意味ありげに彼の席を見ると",
                "$Sに視線を戻してからこう言った"),
            eri.talk(w.i.hiyori, w.flag.hiyori).t("田川日和"),
            yuko.ask().t("何それ"),
            eri.reply(yuko).t("やっぱりそうだよね。",
                    "でも思い出してみてよ。",
                    "田川君が今月に入って休んでる日ってさ……ほら", "ね？"),
            yuko.remember(w.i.hiyori).d("曜日", "時間帯",
                    "その他にも何か共通項があったろうか。",
                    "$Sは必死に思い出してみたが彼女が口にした言葉からある可能性に思い至った"),
            yuko.talk().t("ひょっとして", "天候？"),
            eri.reply().t("正解。",
                    "ぜーんぶ天気良かった日でしょ？　だから田川日和なのよ"),
            yuko.ask().t("でも田川君って", "天気が良いから今日学校休みますっていう",
                    "その手の奇人だったっけ？"),
            eri.talk(yuko, reason, "今年は多い", w.deflag.transfer).t("$yukoは転校してきたとこだから知らないかもね。",
                    "小学校の頃からそのあまりのマイペースさに当時の担任が命名したんだよ",
                    "田川日和って"),
            yuko.know(tagawa, reason, "$want").d("その肝心の$fulltagawaは学校をサボってどこに居るのだろう"),
            eri.ask(yuko).t("$tagawaがどこで何してるかって？").omit(),
            yuko.reply(eri).d("こくり", "と頷いた$Sに$eriは男子たちと同じような笑みを口元に浮かべて勿体ぶってから",
                    "こう答えた").omit(),
            eri.reply(yuko).t("それこそ$tagawaに聞けって話じゃない？").omit(),
            yuko.look(sunnyday, "驚くほどの晴天"),
            town.explain("見渡す限り閑散とした町並み"),
            takemura.come(classroom, "授業の鐘"),
            takemura.explain("担任", "定年間際で白髪混じり"),
            )
    sc3 = w.scene("抜け出す夕子",
            nextday.explain("翌日も晴れ").d("翌日も驚くほどの快晴だった"),
            yuko.look(classroom, tagawa, "サボる").d("だから今日も彼はいない。",
                "相変わらずの空席だ"),
            boys.talk("笑う", w.i.hiyori).d("男子は相変わらず田川日和と笑っている"),
            yuko.think("サボる決断").d("でも誰一人として",
                "彼が何をしているのか知っていなかった"),
            yuko.talk(eri, "田川を探す").t("ねえ$eri"),
            eri.reply().t("なに？"),
            yuko.ask(eri).t("$Sも田川日和してもいいかな？"),
            eri.reply(yuko).t("$yukoってそういうキャラなの？！"),
            yuko.look(eri).d("$eriは$Sをまじまじと眼鏡の奥の瞳を大きくして見つめるが",
                "驚いているというよりもどこか楽しげで",
                "腕組みをする動作をしてから教室を見回すと$Sに親指を立てて見せた"),
            eri.reply(yuko).t("代返なら任せろ"),
            yuko.talk(eri).t("大学じゃないから無理でしょ。",
                "けど", "ありがと"),
            yuko.go(school, "抜け出す").d("そう言って$eriに手を振ると",
                "$Sは鞄を持って教室から抜け出した"),
            w.combine(
                school.explain("授業中の学校は静か").d("授業開始のチャイムが鳴り響き",
                "廊下にいた生徒たちがわっと各々の教室に駆け込んでいくが、"),
                yuko.go().d("$Sはそれを尻目に一階の通用口目掛けて思い切り走った"),
                ),
            takemura.talk(yuko).t("おい$yuko。", "何か忘れ物か？"),
            yuko.think().d("階段で$takemura先生に見つかったが、"),
            yuko.reply().t("良い日和なんで！"),
            yuko.go().d("それだけ笑顔で答えると",
                "白髪混じりの眉毛を凹ませた担任を放置して",
                "階段の踊り場に思い切り飛び降りた"),
            )
    return (w.chaptertitle("田川日和"),
            sc1, sc2, sc3)

def ep_tagawa(w: wd.World):
    yuko, tagawa, granpa = w.yuko, w.tagawa, w.granpa
    nextday = w.day.sunnyday.elapsed(day=1)
    tanbo, town = w.stage.tanbo, w.stage.town
    reason, fam_reason, myfuture = w.i.reason, w.i.fam_reason, w.i.myfuture
    cycle, tractor = w.cycle, w.tractor
    sc1 = w.scene("田川の居場所",
            yuko.go(cycle, town).d("自転車の前籠に鞄を投げ込んで漕ぎ出す。",
                "校門を出たところで校舎の方を見ると",
                "見渡す限りが山に囲まれた場所なのだと実感できた"),
            town.explain("田畑が多い", "のどか").d("通りには車が渋滞しているようなこともなく",
                "すれ違う車も小型のものや軽トラックが多い。",
                "トラクターがぶるぶるとエンジン音をさせて道路を走っていることだって珍しくないのだ"),
            yuko.look(tagawa, "どこにいるか"),
            yuko.know(tagawa, reason, "$want"),
            yuko.look(granpa, tractor).d("ほら", "今だって前方をゆるゆる走っている真っ赤なトラクターが……"),
            yuko.look(granpa).t("あれ？"),
            granpa.explain("目元がぼさぼさの毛で覆われ背中が曲がる").d("よく見れば特徴的な赤い野球帽は私の祖父だ"),
            granpa.ask(yuko, "もう学校終わったのか").t("もう学校終わったのか？"),
            yuko.ask(granpa, tagawa, "見なかったか").t("そうじゃないんだけど",
                "説明が難しいからいいや。",
                "それより$granpa。", "$tagawa見なかった？",
                "こう", "スポーツ刈りみたいな感じで丸顔の男の子なんだけど"),
            yuko.think().d("自分で説明してみて", "この辺りならどこにでもいそうな見た目をしているな",
                "と改めて感じた。",
                "唯一違う点といえば", "あの真っ直ぐ他人を見抜く鋭い瞳だろうか"),
            granpa.reply(yuko, tagawa, tanbo).t("田川んとこの坊主だろ？"),
            yuko.ask(granpa, tagawa, "知ってるの？").t("知ってるの！？"),
            granpa.talk("田川は小さい頃からの喧嘩仲間").t("小学校の頃からの喧嘩仲間だよ。",
                "あいつとは昔っから反りが合わなくてなあ……どうにも顔見る度に口論になっちまう。",
                "それでもこの辺一帯を収める大地主様だろ？",
                "口出ししたら親父にゲンコツされてなあ"),
            yuko.look().d("またいつものように思い出話が始まりそうだったので",
                "$Sはそれを遮って尋ねる"),
            yuko.hear(granpa, tagawa, "居場所").t("で",
                "どこで見たの？"),
            )
    sc2 = w.scene("田川の秘密",
            w.combine(
                yuko.go(tanbo, tagawa).d("自転車を漕ぐ足が筋肉痛になりそうだなと思いつつ、"),
                yuko.look(tanbo).d("何とか坂道を登り終えるとその先にやっと目的の田んぼが広がっていた。",
                "それも一枚や二枚程度じゃなく、見渡す限り一面が田んぼ用に区画整理されていた。"),
                ),
            tanbo.explain("土が耕された広大な区画"),
            w.combine(
                nextday.explain("日が高くなる").d("ここまで一時間程度は掛かっただろうか。",
                "もう充分に日が高く、"),
                yuko.feel().d("$Sの首筋を幾筋も汗が流れ落ちて",
                    "下着がじっとりとしていた"),
                ),
            yuko.talk().t("いた……"),
            yuko.look(tagawa, tanbo).d("けれどここまで来たことは全然無駄じゃなかった。",
                "カーキ色の庇が付いたトラクターの上",
                "見慣れたスポーツ刈りがランニングシャツ姿で乗り込んで操作している"),
            tractor.explain("真っ赤なボディは既に泥まみれ"),
            tagawa.explain("頭に手ぬぐいをまきつけ、野良作業着"),
            yuko.talk(tagawa).t("おーい"),
            yuko.think().d("ずっと見つけたら何て言おうか考えていたのに",
                "ここまで来るので疲れてそれどころじゃなくなってしまった。",
                "それで出た言葉はなんて平凡な呼びかけなのだろうと思ったけれど、"),
            tagawa.reply(yuko).t("なに？"),
            yuko.feel().d("案外うまくいったんじゃないかと",
                "内心ではほっとした"),
            yuko.ask(tagawa, reason).t("何？　じゃないです。",
                "何で$tagawaはこんなとこでトラクター動かしてるの？"),
            yuko.feel().d("ちゃんと聴こえたのだろうか",
                "と不安になるくらい大きなエンジン音で",
                "自転車を置いて近くまで畦を歩いて寄ってみたけれど",
                "$tagawaは表情一つ変えずに何かの作業を続けていた"),
            yuko.ask(tagawa).t("ねーえー？"),
            tagawa.reply(yuko, "終わるまで待ってくれ").t("わりぃ。",
                "これ終わるまで待ってくれ"),
            yuko.reply(tagawa).t("いいけどー"),
            yuko.be("待つ").d("とは答えたものの",
                "まだまだ$tagawaが作業している田んぼは草が生え放題の箇所ばかりだった"),
            yuko.look(tagawa, "普段見せない顔").d("$Sは足を折り畳んでしゃがみ込み",
                "頬に手を当ててしばらく彼が器用に大きな機械を動かすのを見守った。",
                "庇で陰になった$tagawaの表情は",
                "普段学校で見せない充実した笑みを作っていて",
                "何が面白いのか分からないけれど",
                "何だかちょっとだけ羨ましい気持ちが生まれた"),
            )
    sc3 = w.scene("田川日和",
            tagawa.do("農作業終わる", nextday).d("結局彼が作業に一区切り付けてトラクターを下りてきたのは",
                "お昼のサイレンが鳴り響いたすぐ後のことだった"),
            yuko.talk(tagawa).t("はいこれ"),
            yuko.have(tagawa, "ジュース").d("と",
                "ひんやり汗をかいたサイダーの缶を彼に差し出す"),
            tagawa.reply(yuko, "ありがとう").t("サンキューな"),
            yuko.feel(tagawa, w.X()).d("そう言って彼は受け取るなりプシュリと良い音をさせて開封し",
                "喉がひりつくのも構わずに一気にそれを流し込む"),
            yuko.look(tagawa, "噎せる").d("だから思い切り噎せて危うく中身を$Sにぶちまけそうになったが",
                "寸でのところで何とか留まり",
                "それからじっと互いを見やって",
                "どちらともなく笑い出した"),
            yuko.do("drink").d("$Sも自分用に買ったオレンジジュースを開けて一口飲むと",
                "それを見て彼は笑いながらこう言った"),
            tagawa.talk(yuko).t("$Sもオレンジの方が良かった"),
            yuko.reply(tagawa).t("え？　そうなの？",
                "ごめんなさい。",
                "けどもう飲んじゃったし"),
            tagawa.talk(yuko).t("いいよ。",
                "炭酸そこまで苦手って訳じゃないし"),
            yuko.look(tagawa).d("それでも$tagawaは何度か飲んでは苦しそうに噎せていた"),
            yuko.ask(tagawa).t("あのさ"),
            tagawa.reply(yuko).t("なんで$yukoまで学校サボったの？"),
            yuko.feel().d("気になったから",
                "とは言えなかった"),
            yuko.ask(tagawa, reason).t("田川日和"),
            tagawa.look(yuko).t("あぁ"),
            yuko.feel().d("彼はそうつまらなさそうに返すと",
                "$Sを見て",
                "それから目の前に広がる何枚もの田んぼへと視線を投げやった"),
            tagawa.reply(yuko, reason, w.deflag.hiyori).t("ここ全部さ",
                "$granpaの田んぼなんだよ"),
            yuko.ask().t("それをなんで$tagawaが耕してるの？"),
            tagawa.talk(yuko, reason, "農業を継ぐ").t("聞いてないんだな"),
            yuko.feel().d("何のことだろう。",
                "$Sは小さく頷いて彼の言葉を待った").omit(),
            tagawa.talk(yuko, reason).t("$Sは将来農家になる。",
                "なんてったって江戸時代からずっと続く農家の",
                "一人息子だからな").omit(),
            yuko.look(tagawa).d("そう言って彼は恥ずかしそうに笑ったけれど",
                "どこか誇らしげに$Sには見えた").omit(),
            yuko.look().d("サイダーを飲み干して缶を草むらに置くと",
                "彼は立ち上がり",
                "またトラクターに乗り込もうとする"),
            yuko.ask().t("まだやるの？").omit(),
            tagawa.reply(yuko, "将来農家やりたい").t("今日中にあと三枚はやりたい。",
                "だってさ",
                "こんなに良い日和なんだぜ。",
                "正に田川日和ってやつだよ").omit(),
            yuko.reply().t("うん……そうかもね").omit(),
            yuko.think().d("$tagawaがあまりにも良い顔でそう言うものだから",
                    "学校をサボったことについての言い訳を聞こうと思ったのに",
                    "何も言えなくなってしまった").omit(),
            tagawa.talk(yuko, "家族の事情", fam_reason).t("実はさ",
                    "$granpaまた先週から入院してんだ。",
                    "$Sががんばらないと田植えが終わらないんだわ"),
            yuko.ask(tagawa).t("え？"),
            yuko.know(tagawa, reason).d("知らなかった。",
                    "クラスの誰もそんなことは言っていなかったし",
                    "担任だって一言も教えてくれなかった"),
            tagawa.ask(yuko, myfuture).t("なあ$yuko"),
            yuko.look().d("彼はトラクターの運転席に乗り込むと$Sを見てこんなことを尋ねた"),
            tagawa.ask(yuko).t("$yukoには将来の夢ってあるのか？"),
            yuko.talk(tagawa, myfuture, "$not").d("将来も夢も",
                    "実は今一番耳にしたくない言葉だった"),
            )
    return (w.chaptertitle("学校外の田川"),
            sc1, sc2, sc3)

def ep_future(w: wd.World):
    yuko, tagawa, takemura, eri = w.yuko, w.tagawa, w.takemura, w.eri
    classroom, myhouse, school, tanbo = w.stage.classroom, w.stage.myhouse, w.stage.school, w.stage.tanbo
    rainyday, examday = w.day.rainyday, w.day.examday
    myfuture, reason, hiyori, myhiyori = w.i.myfuture, w.i.reason, w.i.hiyori, w.i.myhiyori
    cycle, futurepaper = w.cycle, w.futurepaper
    sc1 = w.scene("夕子の将来",
            yuko.be(myhouse, rainyday).d("翌日は雨だった"),
            yuko.remember(classroom).d("土曜日は午前中だけで授業は終わりだったが",
                "そこにはちゃんと$tagawaの姿もあり",
                "普通に周りの男子と楽しそうに喋っていて",
                "授業中に$takemuraから叱られていた"),
            yuko.look("myroom").d("母方の祖父の実家に急遽作られた$Sの部屋は",
                "畳敷きの和室で",
                "腐っていたものを全て真新しくしたらしく",
                "藺草の香りが寝ている間も$Sを襲ってくる"),
            yuko.think(myfuture).d("ベッドのない生活になって",
                "父親が戸籍から外れて",
                "通学が電車から自転車に変わってしまって。",
                "それなのに$Sは何も変わらずにいる"),
            yuko.hear(tagawa, reason).d("夏頃にはもうどこの大学に行くのか決めないといけない。",
                "そんな風に前の学校では言われていたのに",
                "担任の$takemuraからは",
                "色々と家庭の事情もあるだろうから何だったら今回の調査票は白紙でも良い",
                "なんて言われてしまった"),
            yuko.think(myfuture, "$must").d("$Sはまだ自分がやりたいことも",
                "進みたい道も", "とりあえずの未来も",
                "全然分からない。",
                "それでも何も決めない訳にはいかない").omit(),
            yuko.think(myfuture, "$not").d("寝転がる。",
                "天井を見上げても未来なんて見えないからと畳にキスしてみても",
                "誰も答えを教えてくれない"),
            yuko.do("sleep").d("それでも雨音を聞いている内に眠気がやってきて",
                "$Sは午睡に落ちていった"),
            )
    sc2 = w.scene("試験の日",
            yuko.go(school, examday).d("週明けの月曜には先生から小テストをやると宣告されていた"),
            tagawa.be(classroom, examday, "$not").d("にも関わらず",
                "今日も田川日和だ。", "彼は教室にいない"),
            yuko.ask(eri, tagawa,"いない").t("ねえ$eri。",
                "$tagawa欠席だけど良いの？",
                "学校卒業できなくなるんじゃないの？"),
            yuko.remember().d("$Sが転校してくるまでもかなり欠席していると聞いていた"),
            eri.reply(yuko, hiyori).t("別に中退になっても良いってことじゃないの"),
            yuko.reply(eri).t("え？", "だってそれじゃあ中卒だよ？"),
            eri.ask(yuko).t("$yukoはさ",
                "どうしてそこまで$tagawaのこと気にするの？",
                "この前も訊いたけど", "ほんとに好きじゃないんだよね？"),
            yuko.think().d("これは恋愛感情", "じゃない。",
                "その確信だけはあった。",
                "でも平気で学校を休んでトラクターを乗り回す$tagawaのことも",
                "それに慣れ切った周囲の生徒たちのことも",
                "気になってどうしようもなかった"),
            yuko.talk(eri, "馬鹿じゃないの").t("なんで誰も疑問じゃないの？"),
            eri.do("surprise").t("急にどうしたの$yuko"),
            yuko.look(eri).d("体を半分捻って後ろを向いていた$eriはあまりに驚いたのか",
                "背中を伸ばした拍子に捻ったらしく",
                "低い唸り声を上げながら前を向いて机に突っ伏した"),
            yuko.talk(eri).t("大丈夫……？"),
            eri.reply(yuko).t("……人生で二番目に痛いよ"),
            yuko.talk().t("ごめん……"),
            yuko.think().d("そう謝ったものの",
                "大きな声になった憤りは全然収まってなくて",
                "結局その後に始まった古典の小テストでは",
                "全然マスが埋められないまま試験時間が終わってしまった"),
            examday.explain("試験が終わる"),
            )
    sc3 = w.scene("学業と仕事",
            tagawa.come(school, "$not"),
            yuko.go(tanbo, cycle).d("試験が終わったその足で",
                "$Sは$tagawaの田んぼに向かった"),
            yuko.look(tagawa, tanbo).t("やっぱり居た"),
            yuko.look(tagawa).d("彼は相変わらず一人でトラクターを動かして",
                "まだ準備が済んでいない田んぼの土起こしをしている"),
            yuko.talk(tagawa).t("ねえ$tagawa？"),
            yuko.look(tagawa, "no recognize").d("なるべく大きな声で呼びかけてみたが聴こえていないのか", "トラクターが止まることはない。",
                "それでも構わずに$Sは続ける"),
            yuko.ask(tagawa, "試験をサボったことを咎める").t("なんで？",
                "今日試験だって知ってたでしょ？",
                "どうしてまたサボってこんなことしてるの？"),
            tagawa.reply(yuko, hiyori).t("田川日和だろ？"),
            yuko.talk(tagawa, "将来").t("何でも田川日和って言えば許されるなんて思ってちゃ駄目だよ。",
                "自分の好き勝手してたらそのうちに愛想尽かされて捨てられちゃうかもなんだから！"),
            tagawa.do(w.tractor, "stop").d("彼はエンジンを止めると一度だけきつく睨むように見ると、"),
            tagawa.talk(yuko, "将来に試験が大事か").t("たかが小テスト休んだくらいで誰も死なないだろ？",
                "そもそも何で$yukoは$Sにそんな鬱陶しいんだよ"),
            yuko.reply().d("鬱陶しい。",
                "それは$Sの母親が元父親から言われた言葉だった"),
            yuko.talk(tagawa).t("わ", "$Sは$tagawaの将来が心配だから言ってあげてるだけで",
                "そんな風に言うならもういいよ"),
            yuko.go().d("何だか背中の方が痛くなって",
                "自転車の方に戻ろうとする"),
            tagawa.talk(yuko).t("$yuko"),
            tagawa.do(w.tractor, "rideout").d("振り返ると",
                "彼がようやくトラクターを下りたところだった"),
            tagawa.ask(yuko).t("$yukoにはさ",
                "自分の日和はないのか？"),
            yuko.reply(tagawa, "大事と思う").t("何よそれ"),
            tagawa.talk(yuko, "大事と思わない"),
            tagawa.talk(yuko, "日和の方が大事だ").t("$Sには田川日和がある。",
                "お前にだって何か日和があるはずだろ。",
                "それが分かれば",
                "小テストなんて大した問題じゃないって分かる"),
            tagawa.ask(yuko, myhiyori),
            yuko.reply(tagawa, "$not").t("そんなの分かる訳ないじゃん！",
                "$Sには学校をサボったり小テストを休んだりするのに充分な理由なんて",
                "どこにもないよ！"),
            tagawa.talk(yuko, "$not").t("そういうことじゃねえんだけど……"),
            yuko.look(tagawa).d("小さく首を振ると",
                "$tagawaは再びトラクターに戻っていった。",
                "それからはいくら見つめてみても",
                "彼は何一つ言葉を返してくれなくなった"),
            )
    sc4 = w.scene("自室にて",
            yuko.be(myhouse, examday.elapsed(hour=20)).d("自宅に戻った$Sは",
                "進路調査票を前にして",
                "訳の分からない涙を流す"),
            yuko.think(myfuture).t("自分日和って何よ"),
            yuko.think().d("$tagawaに言われた言葉の意味が分からなくてというのじゃなく",
                "彼にそんな風に言われたことが",
                "無性に腹立たしかった"),
            yuko.talk("わかんない").t("分かんないよそんなの……"),
            yuko.have(futurepaper, "お嫁さんを消す").d("進路に書いた”幸せな家庭を築く”という小学生の夢みたいな文言を",
                "$Sは紙が千切れるまで必死に消しゴムで擦った"),
            )
    return (w.chaptertitle("自分の将来"),
            sc1, sc2, sc3)

def ep_myhiyori(w: wd.World):
    yuko, tagawa, eri, granpa, mam = w.yuko, w.tagawa, w.eri, w.granpa, w.mam
    gwday = w.day.gwday
    tahouse, myhouse = w.stage.tahouse, w.stage.myhouse
    myhiyori, myfuture = w.i.myhiyori, w.i.myfuture
    futurepaper = w.futurepaper
    scenes = [
            w.scene("答えは見えない",
            yuko.be(myhouse, gwday).d("結局白紙の進路調査票を提出して",
                "元号が変わってしまったゴールデンウィークに突入した"),
            gwday.explain("どこにも出かけないGW"),
            yuko.be(myhouse).d("当然$Sはどこに出かける予定もなく",
                "クラスで唯一友だちのようなものになれた$eriとも別に遊びに行くなんて話は出ず",
                "ただ寝転がってＴＶの中で芸能人が楽しげに令和と話すのを見ているだけだ"),
            yuko.think().d("将来なんて考えても考えなくても",
                "こんな風に日常は続いていく").omit(),
            yuko.think().d("ひょっとしたら私日和ってこういう退屈さの延長なのだろうか"),
            yuko.think().d("だとしたら",
                "私日和なんてずっとやって来なくて良い"),
            myhouse.explain("参考書が並ぶ本棚", "布団をかけたベランダ").d("本棚にはまるで大学に行けと急かされているような参考書の列。",
                "ベランダの先には布団が干されていて",
                "母親は足元に転がっていた漫画本を綺麗に束ねて部屋の隅に置いて出ていくと",
                "少しは掃除したら", "とだけ言った").omit(),
            yuko.think(mam).d("離婚したことに対してはごめんとかこれから宜しくとか",
                "そんなしんみりした言葉もなく",
                "ただ住む場所が名古屋よりも随分と北の方になることへの謝罪だけがあった").omit(),
            mam.talk(yuko).t("$yukoご飯"),
            yuko.reply(mam).t("はーい"),
            ),
            w.scene("浅見家の食卓",
            yuko.hear(mam, "ご飯よ"),
            yuko.go(myhouse, "食堂").d("滑り台のような急角度の階段を下りていくと",
                "開け放たれた襖の間から既に食卓に集まっている家族の姿が見えた"),
            yuko.look("family").d("$granpaと$granma",
                "それに$mamと弟の$bro。",
                "変わらない家族の顔。",
                "弟は来年高校生だが$Sよりも頭二つ分ほどでかい。",
                "バスケができればどこでも良いという飄々とした性格が",
                "$Sは少し羨ましかった"),
            yuko.talk().t("いただきます……"),
            yuko.look().d("ご飯が山盛りにされている"),
            yuko.think().d("祖父の家に来て一番変わったことは",
                "ご飯と野菜が大量に食卓に並ぶようになったことだ"),
            yuko.think().d("$granpaはまだ現役で稲作農家だし",
                "家の裏側には広大な畑が年中通して何かしら植えられている。",
                "何か欲しければスーパーに",
                "ではなく",
                "畑に行って収穫をすればいい"),
            yuko.think(mam).d("そんな暮らしが母は少しだけ楽しそうだ"),
            mam.explain("白髪混じりの髪", "ぼさぼさ頭", "染みが多い").d("ただそれでも",
                "知らない間に髪に白いものは増えたし",
                "何よりあんなに毎朝きっちりと整えていた髪が",
                "今日はどこにも出かけないからか",
                "ボサボサのものをヘアピンで右側に束ねていた"),
            granpa.ask(yuko).t("そういえば$yuko",
                "お前田川んちの坊主と付き合ってるってほんとか？"),
            yuko.deal("食事").d("その祖父の言葉に$Sは思わず口に入れたほうれん草の胡麻和えを吐き出すところだった"),
            yuko.reply(granpa).t("な",
                "何なのよそれ。",
                "誰がそんなこと言ってたの？"),
            granpa.talk().t("誰って……"),
            yuko.look(granpa).d("そう口籠ると$granpaは目線を$granmaの方に移す。",
                "その目線を$granmaが今度は$mamに移し",
                "最後には$mamが$Sを見た"),
            yuko.ask(mam).t("何なのよ"),
            mam.talk(yuko).t("$yukoが田んぼでデートしてたってみんな言ってたわよ？"),
            yuko.reply(mam).t("違うわよ。",
                "あれは$tagawaが学校サボってたから注意しに行っただけ。",
                "別に恋とかそんなんじゃないし"),
            w.bro.talk().t("そういうの世話焼き女房って言うらしい"),
            yuko.look().d("ぼそっと低音で弟がそんなことを言う。",
                "$Sは咄嗟に睨みつけたが平気な顔をして$broはご飯のお替りをした"),
            yuko.ask(granpa, "仕事のこと").t("だって$tagawaさ",
                "学校やテストなんて別にどうだっていいって言うんだよ？",
                "天気が良いからサボりましたとか",
                "そんなの社会に出たら通用しないよ"),
            granpa.reply("そんなもん考えなかった").t("それなら$Sも通用してないんやろうね"),
            yuko.reply(granpa).t("え？"),
            granpa.talk(yuko).t("よく田川と二人で学校抜け出しては山に入って駆け回ってたからな。",
                "$Sらが小さかった頃は食べるもんが畑か山か川だった。",
                "けど畑のもん勝手に取ったら祖父さんらにゲンコツされるし",
                "結局山ん中が$Sらの戦場だったな"),
            yuko.look(w.granma).d("じいさん。そう言って$granmaはほっぺを抓ると",
                    "$Sに向かって笑い掛けた"),
            w.granma.talk(yuko).t("学校に行くことも大事。",
                    "でも田んぼの準備は今しかできんからねえ。",
                    "ほら",
                    "田川さんとこまた入院されてるでしょ。",
                    "息子さんが手伝ってくれるようになって随分助かってるって言ってたわよ。",
                    "それが悪いこととは$Sには言えないわ"),
            yuko.reply(w.granma).t("けど"),
            mam.talk(yuko).t("しなきゃならないことばかりだと",
                    "相手が疲れちゃうのかもね。",
                    "ねえ$yuko",
                    "あなたのしたいことって何なんだろうね"),
            yuko.look().d("少しだけ寂しそうに笑って$mamは$Sを見た"),
            yuko.think(myfuture).d("$Sのしたいこと"),
            yuko.look(myfuture, "$want").d("結局それがいつまで経っても見つけられない"),
            ),
            w.scene("告白と自分日和",
            yuko.go(tahouse, gwday.elapsed(day=1)).d("長かったゴールデンウィークも明日で終わる"),
            tahouse.explain("大きな古い木造平屋"),
            yuko.go("田川の部屋").d("$Sは$granmaから教えてもらった$tagawaの実家に一人でやってきた。",
                "当然何の連絡もしていない"),
            yuko.look(tahouse).d("驚くほどの晴天で",
                "実に田川日和だ。",
                "彼がいない可能性の方がずっと高かった"),
            yuko.go().d("それでも",
                "とインタフォンらしきボタンを押す。",
                "ジィィ", "と油蝉の鳴き声みたいな音がして",
                "しばらくすると$tagawaが顔を出した"),
            tagawa.ask(yuko, "何の用？").t("何？"),
            yuko.talk(tagawa).t("なんで田んぼに出てないのよ"),
            tagawa.reply(yuko).t("今日はこれから$granpaの見舞い"),
            yuko.reply(tagawa).t("あ", "ごめん……"),
            yuko.look(tagawa).d("$tagawaは別にいいよ",
                "と呟いてから「で？」と$Sを訝しげに見た"),
            yuko.ask(tagawa, "この前の話", myhiyori).t("この前のこと"),
            tagawa.reply(yuko).t("この前？"),
            yuko.ask(tagawa, myhiyori).t("自分日和"),
            tagawa.talk(yuko, "自分の日和を持てよ").t("ああ。",
                "なんか妙なこと言って悪かった。",
                "その", "$yukoも色々あるんだよな"),
            yuko.talk(tagawa, myhiyori, "自分の考え").t("そうじゃない。",
                "そんなことじゃないの"),
            tagawa.reply(yuko).t("そんなことってな。",
                "$Sなんかうちの両親が離婚したらものすっごく困るぞ"),
            yuko.look(tagawa).d("$tagawaが突然あまりにも真面目な顔をして言うものだから",
                "$Sは何だかおかしくなって吹き出してしまう"),
            tagawa.ask().t("んだよ"),
            yuko.talk(tagawa, "告白").t("あのさ",
                "$tagawaって付き合っている人とか", "いるの？"),
            tagawa.reply().t("はあ？",
                "なんだよそれ"),
            yuko.ask().t("いいから。",
                "いるいない", "どっち？"),
            tagawa.reply().t("い", "いねえよ"),
            yuko.ask().t("それじゃあ十年後って何してる？"),
            yuko.look(tagawa).d("またかよ。",
                "そんな顔をして$Sを見たが",
                "じっと考え込むと$tagawaは小さく溜息を零してから",
                "こう答えてくれた"),
            tagawa.reply(yuko).t("農家。",
                "$Sはずっと小さい頃から$granpaみたいな米や野菜作りがしたいんだよ"),
            yuko.reply().t("うん。",
                "やっぱりそうだよね"),
            yuko.look(tagawa).d("彼は相変わらず分からないといった表情だが",
                "$Sには充分な答えだった"),
            yuko.talk().t("これ"),
            yuko.have(tagawa, futurepaper).d("と彼に見せたのは",
                    "先生が余分にくれた進路調査票だった。",
                    "そこには『幸せな家庭』と書かれている"),
            futurepaper.be("十年後に結婚日和がみたい"),
            tagawa.talk(yuko, "馬鹿なのか？").t("これが$yuko日和か？"),
            yuko.ask(tagawa).t("馬鹿にしないの？"),
            tagawa.reply(yuko).t("$Sには良い日和に見えるけどな"),
            yuko.look(tagawa).d("そう言って$tagawaは親指を立てて見せると、"),
            tagawa.talk().t("ちょっと待ってろ"),
            yuko.look().d("何故か突然家の中に引っ込んでしまう"),
            yuko.talk().t("何なのよ……"),
            yuko.do("wait", tagawa).d("ニ、三分だろうか",
                    "玄関で待ち呆けていると戻ってきた$tagawaの手には彼の足のような立派な太さの大根が握られていた。",
                    "ただ長さが売り場に出ているものの半分程度だ"),
            yuko.ask().t("何？"),
            tagawa.reply().t("田川日和"),
            yuko.ask().t("え？"),
            tagawa.talk().t("$Sが今年植えた春大根だよ。",
                    "もうこんなになったんだけど",
                    "まだ売り場には出せないってさ"),
            yuko.look().d("見れば分かる。",
                    "けど出来損ないかも知れなくても$Sにはそれがとても美味しそうに思えた"),
            yuko.reply(tagawa, "十年あったら何でもできるかもよ"),
            tagawa.look(yuko, "笑顔").t("あと十年もすればもっと立派なのじゃんじゃん作れるようになるさ。",
                    "そん時までには上手く大根炊けるようになっといてくれると助かる"),
            yuko.think().d("彼は$Sを見て照れ臭そうにそう笑ったが、"),
            yuko.ask().t("ねえ。",
                    "なんで$Sが料理下手なの知ってるの？"),
            tagawa.reply().t("えっと……うちの$granpaが"),
            yuko.talk().t("あぁ……もうこれだから田舎は！"),
            yuko.look(tagawa).d("思い切り拳を握り締めた$Sを見て",
                    "$tagawaは大きな声で笑った"),
            yuko.look(myhiyori).d("その笑顔はまるで太陽そのもので",
                    "これが本当の田川日和なんだと",
                    "クラスのみんなが彼を愛する気持ちが今更に理解できた気がした"),
            yuko.think().d("十年後どころか五年後だって自分がどうなっているかなんて分からない。",
                    "けど", "今見つけた自分日和を大切にした先にこんな風に笑える未来があるのかな",
                    "なんて思えるようになっただけ",
                    "平成に置き去りにされた自分からは成長できたのかも知れなかった"),
            futurepaper.be("看護師と書かれている", w.deflag.future),
            w.tag.symbol("（了）"),
            ),
            ]
    return (w.chaptertitle("自分日和"),
            *scenes)


# main
def world():
    w = wd.World("project hiyori")
    w.set_db(CHARAS, STAGES, DAYS, ITEMS, INFOS, FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("田川日和と恋の雨"),
            ep_intro(w),
            ep_tagawa(w),
            ep_future(w),
            ep_myhiyori(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

