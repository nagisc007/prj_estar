# -*- coding: utf-8 -*-
"""Story: chapter 05: The another me
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_anyones(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("望んだはずの空虚",
            h.be(w.stage.apart, w.day.empty),
            h.think("あれから散々駅前や大学のキャンパスを探し回ったが",
                "どこにも$n_shotaの姿は見つけられなかった"),
            h.move("疲れた足取りで自宅アパートの鉄階段を登る頃には既に日も高くなっていて",
                "ひょっとしたらそんな$meを見て彼が「朝帰りだ」なんて冗談めかした笑い声を掛けてくるかなと思ったけれど",
                "全然そんなことはなく",
                "ただ$meの足音だけが響いて消えていく"),
            h.deal("玄関の鍵を開け", "一瞬覚悟してから", "ドアノブを捻った"),
            h.look("日差しが奥のリビングを照らしていたけれど",
                "誰もいない部屋のむわっと温められた空気が漏れ出してきただけで",
                "そこには$childの騒ぎ声も", "壁に背をつけて本を読む$studentの姿もなかった"),
            h.deal("もしかしたら。",
                "そんな思いで冷蔵庫を開けてみた。",
                "でも中身は昨日のままで", "何も変わっていない。",
                "飲みかけのペットボトル", "ラップを掛けた残りの焼き秋刀魚",
                "タッパに入った和物", "個包装になったチョコレートが幾つかと",
                "調味料たち"),
            h.move("部屋に戻り", "疲れた体をそのまま畳んである布団の上に投げ出す"),
            h.feel("何日も干していない湿気を含んだそれが$meを受け止めてくれたけれど",
                "その背中に飛び乗ってくる$childはいない"),
            h.think("何か疲れてるんじゃない？", "と訊いてくる$studentはいない"),
            h.look("バカにして文句ばかり言う$univすらいない"),
            h.think("$meは一人だ"),
            h.think("違う。", "独りだ"),
            h.look("仰向けになって天井を見上げる"),
            h.look("部屋の大きさは変わっていないのに", "こんなにも広かったんだと思って",
                "首筋が涼しくなった"),
            h.behav("だから$meは横になって赤ん坊のようにぎゅっと丸まり",
                "意識を閉じる。",
                "眠ってしまえば", "何もかも気にせずに済む。",
                "心や体がいっぱいだと感じた時",
                "$meはいつもこうしていた"),
            h.think("でも最近は全然こんなことする必要なかったな"),
            h.behav("そのことに気づいたからか", "閉じたままなのにその目元が濡れてしまった"),
            h.look("でも翌日も次の日も誰もいなかった。",
                "$meは一人で", "四人分の食器を並べて朝食を食べた"),
            )

def sc_circlemeeting(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    kunugi, sayama, saito, matsu = w.kunugi, w.sayama, w.saito, w.matsumoto
    return w.scene("サークルのミーティングにて",
            h.be(w.stage.famires, w.day.meeting),
            h.feel("じっとりと汗を掻きながらファミレスに入る"),
            sayama.talk("$kyoko", "こっち！"),
            h.look("既に奥の四人席には$sayamaと$saitoが座っていて",
                "$meは店員に断ってそっちに歩いていく。",
                "入り口を振り返ると$matsumotoと$kunugiが何やら話しながら入ってきたところだった"),
            saito.talk("久しぶり"),
            h.deal("そう言って$saitoはわざわざ自分の隣を開けて$meを誘導する。",
                "一瞬迷ったけれど", "他にも続けて入ってくる先輩たちの姿を見て",
                "仕方なく奥から詰めて座ることにした"),
            sayama.talk("$ln_saitoさんが最近返事ないからって気にしてたんだけどさ",
                "$kyokoひょっとして実家に帰ったりしてたの？"),
            kyoko.talk("ううん。", "バイトが忙しかっただけ"),
            h.deal("$sayamaは少しだけ事情を知っている。",
                "$meと母親の仲が良くないことや", "友だち付き合いが得意ではないことなんかを"),
            h.look("ほんとに？", "という彼女の視線に微笑を返してから",
                "$meは手を挙げて現れた$kunugiに頭を下げる"),
            kunugi.talk("これ教室でミーティングしてたら軽く逝ける温度だね。",
                "文明の利器さまさまだ"),
            h.deal("先輩たちも珍しく全員揃い",
                "四人席を三つも占拠して店内に賑やかな一画を作ってしまう。",
                "それでも他のサークルほど騒ぐ人もいないので",
                "演劇部も掛け持ちしている$kunugiの声が大きいのが少し迷惑な程度だった"),
            h.deal("全員の注文が揃うと",
                "ささやかな乾杯の音頭と共に$kunugiのハッピーバースディが歌われる。",
                "誕生日そのものは一週間ほど前なのだが全員揃うのが今日しかなかった為だ"),
            kunugi.talk("みんな", "ありがとう。",
                "プレゼントはまた個別に受け付けることにして",
                "明後日の清掃ボランティアなんだけど",
                "それを最後に$meはしばらくサークルに顔出さないことにしたから"),
            kyoko.ask("何でですか？"),
            h.deal("きっと誰もがそう感じただろうに",
                "声を上げたのは$meだけだった"),
            kunugi.talk("$kyoko", "ありがとうね。",
                "将来のことも考えて", "ちょっと本気で演劇に打ち込もうと思って。",
                "九月にある劇団のオーディション", "受かりたい"),
            h.look("先輩たちはみんな知っていたのか",
                "黙ってそれを聞いている"),
            h.look("$saitoは当然として$sayamaも$meも勿論聞いてなくて",
                "$matsumotoを見ると考え込んだ様子で先輩と$meを見ていた"),
            kunugi.talk("そういう事情もあって",
                "部の今後のことを", "二年たち中心に話し合ってもらいたいなって思ってる。",
                "どうだろうか"),
            h.look("四年生たちの視線は$sayamaや$matsumotoではなく$meに集まり",
                "$saitoがいつの間にか$meの右腕をぎゅっと掴んでいた"),
            h.think("$meはすぐには答えられず",
                "代わりに$sayamaが、"),
            sayama.talk("$meたちで考えておきます"),
            h.think("珍しく真剣な顔で答えた"),
            h.deal("$kunugiの「じゃあ食べよっか」の声で場の空気は元に戻ったように見えたが",
                    "$meの心の中は波立ったまま落ち着く様子もなく",
                    "目の前にしたチキンドリアは熱くて",
                    "なんでこんなもの頼んでしまったのだろうという後悔を抱えたまま",
                    "いつまでもスプーンを口には運べないでいた"),
            )

def sc_meetmatsu(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    sayama, saito = w.sayama, w.saito
    matsu, asumi = w.matsumoto, w.asumi
    return w.scene("松本と出会う",
            matsu.ask("なあ"),
            h.deal("ミーティングが解散になったところで$matsumotoから声を掛けられた"),
            h.think("$meの頭はすっかりこの後$sayamaと$saitoの三人で今後の話をすることに向いていたのに",
                "彼の重苦しい声に「何？」と振り向かずにはいられなかった"),
            matsu.talk("ちょっと", "訊きたいことがあってさ"),
            h.deal("そう言って彼が見せてくれたのはまだ小さい頃の$shotaが写った写真だった。",
                "画像ではなく", "つるんとした照り返しのある写真。",
                "少し古いものみたいで", "端の白いところが一部黄色くなっていた"),
            kyoko.talk("えっと……"),
            h.look("見た瞬間に心は決まっていたけれど",
                "言葉を上手く選べずに視線を前にいた$sayamaと$saitoに向ける"),
            sayama.talk("あ、じゃあ$meは$saitoと二人でデートしとくから",
                "$kyokoは$ln_matsumotoとデートしなよ"),
            h.deal("冗談のつもりなんだろうけれど",
                "突然デートなんて言われて$saitoは慌てていた。",
                "けれど$sayamaは強引に彼女の腕を取ると",
                "そのまま連れて行ってしまう"),
            saito.talk("$kyokoあとでちゃんと連絡するから！"),
            h.look("その姿は連行されていく容疑者みたいな有様だったけれど",
                "$meは手を振って見送ると",
                "改めて$matsumotoに向き直る"),
            kyoko.talk("その写真のこと", "教えて欲しい"),
            w.tag.br(),
            h.be(w.stage.ma_apart),
            h.come("$n_matsumotoのアパートは大学から少し遠くて",
                "二人とも自転車で縦に並んで走りながら三十分ほど",
                "黙ったままペダルを踏み続けた"),
            matsu.talk("すまないな。", "わざわざ来てもらって"),
            h.deal("そう言って謝りながら彼は自転車を駐輪場に停める。",
                "$meもその隣に停めさせてもらいながら建物を見たが",
                "$meの暮らすアパートよりも十年ほど余分に古そうな木造二階建てだった"),
            kyoko.talk("確か$matsumotoさんて彼女と同棲してるんですよね？"),
            matsu.talk("そうだけど", "気にしなくても大丈夫だ"),
            h.think("気になるという話をしようと思ったけれどそう言われてしまっては覚悟を決めないといけない"),
            h.deal("彼が一階の一番端の部屋のドアを開けるのに続いて",
                "$meも中に入った"),
            kyoko.talk("お邪魔します"),
            h.look("六畳間と聞いていたけれど",
                "キッチンの部分が狭いからか$meのアパートよりも小さく見えた。",
                "それでも水回りまで含めて割と綺麗に片付いていて",
                "彼女が綺麗にしてくれているのだろうな",
                "と想像できた"),
            matsu.talk("$asumi", "言った通り連れてきた"),
            h.look("彼はそう言って部屋に入ったが",
                "そこには$meが想像していた彼女がいなかっただけでなく",
                "何も", "誰の姿も見えなかった"),
            matsu.talk("ああ", "そうだろ？"),
            h.look("けれど彼はそう答えて何もない空間に笑顔を向けると",
                "$meに座るように促した"),
            kyoko.talk("あの……"),
            matsu.talk("適当に座ってて。",
                    "今$asumiにお茶いれてもらうから"),
            kyoko.ask("$asumiさん？"),
            h.deal("要領を得ないままとりあえず小さなテーブルの前に腰を下ろすと",
                    "黒のタンクトップ姿の逞しい彼を見上げる"),
            matsu.ask("普通のお茶でいいよな？"),
            kyoko.talk("え、ええ"),
            h.look("そう尋ねた彼は何故か自分で台所に向かい",
                "冷蔵庫の中に入っていたペットボトルを出してお茶を注いでいる。",
                "ただし並べたコップは三つだ"),
            h.look("$meはそのまま彼がそれをどうするのか見ていたが",
                    "二つを右手で", "残る一つを左手で掴むと",
                    "そのままこっちにやってきてテーブルに置いた"),
            h.deal("彼は普段は見せないにこやかさで腰を下ろしたが",
                "明らかに$meとの間にもう一人いる", "という体なのだ。",
                "事実", "テーブルの上にもその誰もいないが誰かがいるらしい場所に",
                "残り一つのコップが置かれていた"),
            matsu.talk("えっと", "自己紹介はしてもらったか？"),
            kyoko.talk("あの……$matsumotoさん"),
            h.look("$meは気まずさをそのまま表情に出して",
                    "彼に見えないことを訴える"),
            matsu.ask("そうか……やっぱ$kyokoにも見えないのか"),
            h.deal("彼は溜息をつくと",
                    "一口お茶を飲んでから",
                    "彼の同棲しているという彼女", "$n_asumiについて話してくれた"),
            matsu.talk("$kyokoは小さい頃に", "その",
                    "想像上の友だちというのを見たことがあるか？"),
            h.deal("どうやらその$n_asumiという女性は",
                    "彼が大学に入ってから現れた想像上の恋人らしい。",
                    "$meのようにもう一人の自分という訳ではなく",
                    "完全な他人だ"),
            kyoko.ask("つまり$matsumotoさんて", "$i_IF",
                "$i_imagefriendが見えるんですか？"),
            h.look("$meがそう尋ねると明らかに彼の表情が変わった"),
            matsu.talk("やっぱり$kyokoも見えるんだな？"),
            h.deal("彼は中腰になるとその手を伸ばして$meの両肩に載せる"),
            matsu.talk("$kyokoにもちゃんといるんだな？",
                    "誰にも見えない友だちや恋人が"),
            h.look("その瞳の真っ直ぐさは少しだけ$shotaを思い起こさせた"),
            h.deal("$meは$matsumotoから簡単な彼女の紹介を聞いて",
                    "彼女がいるであろう空間に向き直る"),
            kyoko.talk("えっと", "見えないんですけど初めまして。", "$n_kyokoです。",
                "$matsumotoさんとは同じサークルに入ってます"),
            h.deal("$n_asumiがいるつもりで",
                    "誰もいない空間に対して頭を下げた"),
            matsu.talk("$asumiも宜しくって。",
                    "それにちゃんと理解してくれると思ってたとも"),
            h.deal("$meは見えない彼女にもう一度頭を下げる"),
            matsu.talk("実は$asumiの奴", "最初から$kyokoは大丈夫って言ってたんだよ。",
                    "まさか同じ仲間だとは思わなかったけど",
                    "今も誰か連れてるのか？"),
            kyoko.talk("今はいない。", "$meにはこの部屋にいるのは自分と$matsumotoさんしか見えてないよ"),
            h.deal("そっか", "と彼は頷いて", "腰を下ろす"),
            kyoko.ask("それで$shotaの写真のことなんだけど"),
            h.think("彼が$i_IFを持っていたことにも驚いたけれど",
                    "今日ここに来たのは何もその彼女に自己紹介をする為じゃない。",
                    "それを思い出して", "$meは再び彼が出した$shotaの写真に視線を注いだ"),
            matsu.talk("$meと$shotaはさ", "小学校の同級生だったんだ"),
            h.deal("そう言って彼は小さかった頃の$shotaのことを少し語ってくれた"),
            matsu.talk("$meは小学校に入る前からデカくてさ",
                    "逆に$shotaのやつはチビでよく他の男子にいじめられてて",
                    "最初のきっかけはよく覚えてないんだが",
                    "どういう訳か自然と一緒にいてあいつを守ってやるようになったんだ"),
            h.think("彼が話してくれた小さい頃の$shotaは",
                    "$meの前に現れた彼から感じた雰囲気と全然違ってなくて",
                    "きっとそのまま大きくなったような人だったのだろうと分かり",
                    "それが少し嬉しかった"),
            matsu.talk("そんな縁もあってよく一緒に遊んだりしてたんだけど",
                    "$meが小五の時に引っ越してからは連絡も特にしなかったから",
                    "ずっと忘れてたんだよ。",
                    "それがさこの前$asumiに言われて",
                    "その……$kyokoと$shotaがホテル街を歩いてたって"),
            kyoko.ask("何で$asumiさんがそんなことを？"),
            h.think("$meが彼に連れられてラブホテルに行った日のことだ。",
                    "あの時近くに$matsumotoがいたのだろうか"),
            matsu.talk("$asumiがバンドやっててさ", "$meもたまにスタジオに行ったりするんだけど",
                    "ちょうど見かけて", "そうじゃないかなって"),
            kyoko.talk("別に何もしてないから"),
            h.look("言ってしまってから", "自分で認めたようなものだと気づいて思わず目を閉じる"),
            matsu.talk("別に$meは$kyokoが誰と付き合おうと気にしないが",
                    "$shotaのことはちょっと見逃せなくてな"),
            h.look("その声の調子の真面目さに「何？」と無言で視線を送ると",
                    "彼がずっと感じていた違和感の正体が明らかになった"),
            matsu.talk("前に小学校の同窓会に呼ばれた時にさ", "知ったんだよ。",
                "$shotaが実は亡くなってたって"),
            )

def sc_hismanshion(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    dad = w.sho_dad
    return w.scene("彼の家",
            h.come(w.stage.hishome, w.day.meeting, shota),
            h.come("$matsumotoに聞いた$n_shotaの実家は",
                "$meが彼から聞かされた印象のままの真っ白な二階建てだった"),
            h.look("大きな木造の塀に囲まれていて",
                "格子状になった開き戸と車用だろう", "大きなシャッターが降ろされた門があり",
                "$meは恐る恐る『$ln_shota』とだけ書かれた表札の下のインタフォンを押した"),
            h.deal("一分ほどだろうか。",
                "応答があって男性の声がすると",
                "$meはたどたどしさをどうにもできないまま",
                "何とか$shotaの知り合いで", "彼が亡くなったことを知ってやってきたことを告げた"),
            dad.talk("分かりました。",
                "ちょっと待ってて下さい"),
            h.look("そう言われて緊張が取れないまま待っていると",
                "ほどなくして戸が開けられた。",
                "現れたのは髪が真っ白になった彼の父親らしき男性だった"),
            dad.talk("さあ", "どうぞ"),
            kyoko.talk("突然すみません。", "お邪魔します"),
            h.look("その男性の優しく目元が緩むと", "やはり$shotaの面影を感じさせた"),
            h.move("$meは彼について中に入る。",
                "五十メートルほどの前庭があり",
                "植木や花で玄関に向かう石畳以外は鬱蒼としていた"),
            w.tag.br(),
            h.deal("通されたのは応接間だった"),
            h.look("中庭に面していて",
                "本棚やゴルフのトロフィーなんかが飾られたガラス棚がある。",
                "革製のソファは見た目ほど硬くはなくて",
                "座ると$meの下半身が軽く沈んでそこに吸い付いたみたいになった"),
            h.look("棚にはトロフィー以外にも小さなクマのぬいぐるみや",
                "古い家族写真がある。", "黄色い帽子を被った小さな彼と父親",
                "少し離れて母親が一緒に写っている。",
                "保育園か幼稚園の遠足だろうか。",
                "幸せそうに笑っている彼が少し羨ましい"),
            dad.talk("珈琲が良かったかな？"),
            kyoko.talk("あ、いえ。", "お構いなく"),
            h.look("ポロシャツ姿の彼は小さなお盆に持ってきたお茶の入ったコップを$meの前に置いた。",
                "立ち姿はすっと背筋が伸びていてスタイルが良く",
                "大きくなったら$shotaもこんな風になっていたのだろうかと想像してしまう。",
                "ただ父親の方が彼よりも背が高く骨格もがっちりしているので",
                "ひょっとしたら$shotaは母親似なのかも知れない"),
            dad.talk("$kyokoだったかな"),
            kyoko.talk("はい"),
            h.look("ガラステーブルを挟んで対面に座ると",
                "彼は$meの顔を確かめるようにじっと見つめた"),
            kyoko.talk("あの？"),
            dad.talk("いや", "女の方が訪ねてこられたのは初めてなのでね。",
                "その", "$shotaとは小学校で？"),
            kyoko.talk("その……"),
            h.think("適当を言って誤魔化すことも可能だったけれど",
                "$meは正直に打ち明けることを選んだ。",
                "それがどんなにおかしなことだと笑われても",
                "$meにとっての$shotaはあの時間の中にしかいないから"),
            dad.talk("……そうですか"),
            h.look("$meが大きくなった彼と会って話したり",
                    "結婚の約束をしていたと言われたりしたと語ると",
                    "彼は大きく溜息をついてから",
                    "考え込むようにテーブルを見つめた"),
            kyoko.talk("$meにもそれが本当のことだったのかどうか",
                    "よく分かりません。",
                    "ただ", "$meには記憶が思い出せない頃があって",
                    "もしその時に彼と本当に結婚の約束をしていたんだとしたら",
                    "何かそういう不思議な縁みたいなものが", "会わせてくれたのかなって"),
            dad.talk("ちょっとだけ待って下さい"),
            h.look("そう言って彼は立ち上がると",
                    "$meを部屋に残して出て行ってしまう"),
            h.think("やはり不快にさせたのだろうか", "と思ったが",
                    "暫くすると彼はその手にアルバムを持って戻ってきた"),
            dad.talk("見て下さい"),
            h.look("$meはそこに彼の幼少期の愛らしい姿が写り込んでいるものと思って目を向けたが",
                    "開かれたページにあった写真はどれも病室のそれだった"),
            kyoko.ask("これは？"),
            dad.talk("$shotaが亡くなる一週間から半年ほど前までのものです。",
                    "あの子は脳腫瘍でこの世を去りました。",
                    "今月の十日が", "あの子の命日です"),
            h.hear("それは$meが$shotaに連れられてホテルに行ったあの日だった"),
            )

def sc_hisvanish(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    dad = w.sho_dad
    return w.scene("彼はもういない",
            h.deal("二階の一室のドアを",
                "彼の父親が開けてくれている。",
                "鍵が掛けられていて",
                "それでもドアの前にひらがなの『しょうたろう』プレートが掛かったままで",
                "それが全然埃塗れになっていないことが",
                "彼の中ではまだ$shotaが生きているだろうことを思わせた"),
            dad.talk("気が済むまで見てやって下さい。",
                "$meは一階の方にいますから。",
                "何かあれば声を掛けて下さい"),
            kyoko.talk("ありがとうございます"),
            h.look("$meは頭を下げ",
                "彼が階段を降りていくのを見送ると",
                "ドアを開けて彼の部屋に入った"),
            h.look("当時のまま残されていると聞いたけれど",
                "本当に小さな子が眠るサイズの小さなベッドとその脇の壁の一画を占拠する大きな本棚",
                "液晶の薄型テレビに", "その下には当時流行ったゲーム機が繋がっている"),
            h.look("木目のある机の上に広げられているのは学校の宿題だろうか。",
                "ノートは閉じられていて", "さんすうやこくごと書かれた教科書がその隣に置いてあった"),
            h.look("鉛筆と布の筆箱", "小さな鉛筆削りもあって",
                "振り返れば今も小学生の彼がここにいるのが見えるんじゃないかと思ってベッドの方を見たが",
                "当然誰もいなかった"),
            h.look("本棚の一画だけ父親が手を入れたのか",
                "小さな本立てによって区切られていて",
                "そこに遺影としてなのか",
                "小さな彼の写真が飾られていた。",
                "細い毛が金色に輝いて見えるマッシュルームカットの彼が",
                "笑顔で飛び上がっているところだ"),
            h.look("その写真のすぐ下の段に",
                "大判のスケッチブックが立てかけてある。",
                "引き抜いて中を見ると彼の絵日記だった"),
            h.look("ひらがなと", "習いたての漢字がいくつか混ざっている。",
                "流石に自分の名前は難しかったのかその殆どをひらがなで書いてあったが",
                "太郎だけは何とかがんばって漢字にしてあった。",
                "でも郎の字がうまく書けずに", "途中で何度かひらがなに戻っていたけれど"),
            h.look("その中に", "砂場が好きだったと書かれていた"),
            h.look("砂場らしき四角の中に",
                "お城ではないもっと先の尖った細い塔のようなものが描かれている。",
                "他のページの砂場にも", "同じものがあった。",
                "そう。", "これはきっとタワーだ。",
                "東京タワーなのか札幌のテレビ塔なのか",
                "それともエッフェル塔のつもりなのか分からないが",
                "砂で作ろうとしたタワーだ"),
            child.talk("それ", "なに？"),
            h.look("まだ五歳の$meが尋ねる"),
            shota.talk("タワーだよ。",
                "とってもたかいところまで見えて",
                "いいきぶんになれるんだ"),
            h.look("同じくらいの年齢の$shotaが",
                "笑顔で答える"),
            h.look("一瞬$i_IFなのだろうかと思ったが",
                    "周囲の景色が一変していて",
                    "$meの気持ちがその頃に戻っているのだと思った"),
            h.think("ああ", "これはあの日だ。",
                "$meが初めて小さな家出をして",
                "公園で独り", "泣いていた日のことだ"),
            shota.talk("どうして", "ないてるの？"),
            child.talk("だって", "おかあさんが", "はしが",
                    "ちゃんともてない子は", "いらないって", "おこるから"),
            h.think("今なら最初の父親との離婚協議で気が立っていたから",
                    "いつもなら「ちゃんと持ちなさい」で済んだものがつい「要らない」と強い言葉になってしまったと",
                    "それなりに理解もできるけれど",
                    "当時の母親だけが自分の生命線みたいな人生だった$meにとって",
                    "その言葉はとても重いものだった"),
            shota.talk("それじゃあ", "$meんちの子になる？",
                    "$meははしもてないけど", "おこらないし"),
            child.talk("いいの？"),
            h.think("そんな風に自分に対して言ってくれたのは", "彼が初めてだった"),
            shota.talk("じゃあ", "けっこんしよ？"),
            child.talk("けっこん？"),
            shota.talk("いっしょにくらすことだよ。",
                    "けっこんして", "おかしをいっしょにたべよう"),
            child.talk("うん！"),
            h.think("そうだった。",
                    "たぶん$meも$shotaもその意味なんて分からないまま約束をして",
                    "けれどそのまま二度と会うこともなく",
                    "$meの方はその約束のことをすっかり忘れてしまっていた"),
            h.look("風が頬を撫でて", "$meは気がついた"),
            dad.talk("いや、その……すまない"),
            h.look("見ると入り口のドアが開いて", "$shotaの父親が立っていた"),
            dad.talk("いつまでも君が降りてこないから", "その", "少し心配になって"),
            kyoko.talk("あの、$meの方こそ……すみません"),
            h.look("咄嗟に謝りの言葉を選んだけれど",
                    "自分が泣いていることに気づいて",
                    "$meは慌てて目元を拭った"),
            dad.talk("ありがとう"),
            h.look("そう言われて意味が分からずに彼を見ると",
                    "頭を深々と下げてもう一度「ありがとう」と言われた"),
            h.look("その頭が上がった父親の目元は濡れていて",
                    "けれどその目線は$meではない場所に向かっている。",
                    "振り返るとベッドの上で小さな$shotaが寝転がって大の字になっていて",
                    "どうやら父親にもその姿が見えているようだった"),
            h.deal("$meは小さく頭を下げるとそっと部屋から出て",
                    "彼が押し殺して泣くのを聞かないようにと",
                    "足早に一階に降りた"),
            )

def sc_alone(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    return w.scene("今日子ひとり",
            h.think("帰りの電車に乗りながら",
                "ぼんやりと$shotaのことについて",
                "あるいは彼の家族のことについて", "考えていた"),
            h.look("夏休みだからか", "車内には小学生や普段着姿の中高生らしき人たちが多い。",
                "大半はスマートフォンを触っていて", "あるいはゲーム機で遊んでいて",
                "互いを見ていない"),
            h.look("それは何も子供たちばかりではなく",
                "$meたちのような大人だって同じだ。",
                "ただ$meのようにその小さなパーソナルコンピュータを持っていない人間だけが",
                "この空間にいる沢山の人間のことを見つめていた"),
            h.think("どうして$shotaは$meの前に現れたのだろう"),
            h.think("彼は幽霊だったのだろうか。",
                "それとも彼もまた$meにとっての$i_IFだったのだろうか"),
            h.think("来月始めの診察の時に$ln_miura先生に訊いてみるつもりだけれど",
                "それまでずっと$childたちが戻ってこないなら",
                "先生は何と言うだろう。",
                "見えなくなったことで治ったと思われるのだろうか"),
            h.look("考え込んでいたからか",
                "$meの前にやってきてじっと顔を見ている男の子に気づかなかった"),
            kyoko.ask("何？"),
            h.look("けれど男の子は$meではなくその隣の空席を見つめて笑うと",
                "走って行ってしまった"),
            h.look("座りたかったのかな。",
                "そう思って右側を見たら", "$childがいて笑いかけた気がした"),
            h.look("でもそれは本当に気がしただけで",
                "何も見えない。", "ちゃんと空席で",
                "「すみませんね」とお婆さんがやってきて", "埋めてしまった"),
            h.think("$meは紛れもなく独りだ"),
            h.think("もう$childたちは現れない"),
            h.think("今やっとそれが実感に変わって",
                "どうしようもなく涙が溢れた"),
            )

def sc_goodbyeanothers(w: wd.World):
    h = kyoko = w.kyoko
    shota, child, stu, univ = w.shota, w.child_kyoko, w.student_kyoko, w.univ_kyoko
    miura = w.miura
    return w.scene("さよならわたし",
            miura.talk("それじゃあ",
                "一月ほどの間", "ずっと彼女たち$i_IFの姿は見えていない訳だね？"),
            h.look("診察室には向日葵の絵が飾られていて",
                "$meはそれを眺めながら$ln_miura先生の質問に答えていく"),
            miura.talk("$kyokoが見たという別の$i_IFだけれど",
                "彼が現れてから何か大きな変化はありましたか？"),
            kyoko.talk("よく分かりません。",
                "$me自身はそう変わっていないようにも思いますが",
                "先生から見て何か違いがありますか？"),
            h.think("自分の変化なんて", "そう簡単に自覚できるのなら",
                "$meはもっと上手く生きられている気がする。",
                "大学も", "サークルも", "仕事も",
                "家族のことも", "何もかもが大きな変化なんてない。",
                "ただ$kunugiのように$me以外の変化はあったり",
                "$saitoみたいに新しい人間関係が生まれたりはしたけれど",
                "それが$me自身に大きな影響を与えたとも思えない"),
            miura.talk("特別な違いは感じませんが",
                "そうですね"),
            h.look("先生はうっすら伸びた顎髭を撫でてから",
                "眼鏡の目を$meに向けていつにない優しい笑みを見せてこう続けた"),
            miura.talk("部屋に入ってくる時に", "$meの目を見てから挨拶をしていました。",
                "以前は決して$meの目を見ませんでしたから", "変化といえば変化でしょうか"),
            h.think("そうなのだろうか。",
                "自分では意識したことがなかった。",
                "もしそれが誰かの影響だとすれば",
                "いつも真っ直ぐに$meを見つめてくれた子犬のような目の彼の所為かも知れない"),
            miura.talk("それでは次は三ヶ月後で良いですかね"),
            kyoko.talk("はい。", "次も宜しくお願いします"),
            h.look("そう答えて頭を軽く下げた$meを",
                "何故か先生は驚いた顔で見ていた"),
            w.tag.br(),
            h.look("クリニックを出ると",
                "うろこ状になった雲が青い空に綺麗に並んでいた"),
            h.move("人通りの少ない路地を", "駅に向かって歩き出す"),
            h.think("スニーカーの足音は自分にだけ響いて",
                "それはたぶん普通のことなのだろうけれど",
                "この一月ばかり", "ふとした瞬間に訪れる「わたし」という感覚に戸惑っていた"),
            h.think("きっと誰もが生まれながらにして持っていて",
                "それは「ワタシ」でも「私」でもなく「わたし」なのだけれど",
                "いつからかそれが「私」だったり「僕」だったり或いはもっと他の",
                "その場限りの自分になる"),
            h.think("わたしだけれど", "その場専用のワタシになる"),
            h.think("きっとそんな器用さでみんなは迷うこともなく生きている"),
            h.think("でも時々$meのような",
                "上手くその場の自分を繕えなくて",
                "どうしていいのか分からないまま", "他人と距離を離すことで何とかやりくりしなければいけないような",
                "そんな人もいる"),
            h.think("$meにとって$childや$studentの存在は",
                "わたしやワタシを上手く扱えない$meという人間を助ける為の",
                "世界からの贈り物みたいなものだったのかも知れない"),
            h.look("大通りに出ると",
                    "急に車の音や人の声がよく響いてきて",
                    "$meは一瞬自分の存在を見失いそうに感じたが",
                    "立ち止まり", "ゆっくりと空を見上げてから呼吸を整え",
                    "今一度視線を戻すと",
                    "鼓動も気持ちも落ち着きを取り戻していた"),
            h.move("駅を目指して歩いていく"),
            h.look("すれ違う人", "追い抜いていく人",
                    "コンビニに入っていく人",
                    "タクシーを呼び止めている人",
                    "待ち合わせをしているカップル",
                    "ベビィカーを押している母親",
                    "ハンカチで額を拭うスーツの男性",
                    "台車を押して走っていく運送会社の人",
                    "そして$meの目の前で立ち止まったシャツの少年"),
            h.look("振り返った彼は少しだけ$shotaに似ている気がしたが",
                    "$meの脇を素通りしていく"),
            h.look("振り返ると小学生たちの待ち合わせの群れに彼が合流していて",
                    "楽しそうな笑い声を上げていた"),
            h.move("$meは彼らに背を向けて", "歩いていく"),
            child.think("$meで、"),
            stu.think("$meで、"),
            h.think("$meらしく"),
            w.tag.symbol("（了）"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("誰もいない"),
            # NOTE: 翔太郎までいなくなり、完全に孤独になった今日子
            sc_anyones(w),
            )

def ep_matsumoto(w: wd.World):
    return (w.chaptertitle("松本とIF"),
            sc_circlemeeting(w),
            sc_meetmatsu(w),
            )

def ep_truth(w: wd.World):
    return (w.chaptertitle("真実と真相"),
            sc_hismanshion(w),
            sc_hisvanish(w),
                w.kyoko.deal("vanish", w.shota),
            sc_alone(w),
            )

def ep_epilogue(w: wd.World):
    return (w.chaptertitle("エピローグ"),
            sc_goodbyeanothers(w),
            )

# outline
def base_info(w: wd.World):
    return ("chapter5", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return [
            ]

# main
def story(w: wd.World):
    return [w.chaptertitle("わたしとワタシ"),
            ep_intro(w),
            ep_matsumoto(w),
            ep_truth(w),
            ep_epilogue(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

