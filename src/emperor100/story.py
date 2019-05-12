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
    h, milea, garneth, runolf, marf = w.hero, w.milea, w.garneth, w.runolf, w.marf
    scenes = [
            w.scene("父の死、皇帝の死",
                h.go(w.stage.office).d("日が明けて間もなく",
                    "$heroは身支度も程々に執務室へと急いでいた"),
                h.be(w.stage.castle, w.day.dead),
                h.look().d("部屋に入ると既にそこには教皇$garnethほか",
                    "宰相", "近衛兵長", "王国軍最高司令官など",
                    "国政の中枢を司るひと握りの者が集まっていた"),
                garneth.talk(h, w.i.throne).t("随分と悠長なお出ましですな殿下……",
                    "それとも陛下とお呼びした方が宜しいですかな？"),
                h.look().d("白蛇を思わせる頭髪と眉毛を全て排除したその出で立ちは教皇にだけ許された聖装らしいが",
                    "$heroからすると不気味を全身に装備しているようにしか見えない"),
                runolf.talk().t("このような時に悪趣味な冗談は止してくれまいか",
                    "$garneth聖下"),
                h.look().d("目元がすっかり白くなった眉毛で覆われた近衛兵長が窘めたが",
                    "当の$garnethはぎょろりとした目を細めて笑みを返しただけだ"),
                h.ask().t("まだどこにも情報は漏れていないのだな？"),
                h.think().d("臣下たちの啀み合いに付き合っていられる心の余裕はなかった。",
                    "皇帝の死",
                    "という事実は国の一大事であると共に",
                    "この$st_kingdomでは一刻も早く次なる皇帝へと継承の儀式を行う必要があったのだ"),
                h.be(w.i.throne, "$must"),
                h.know(w.i.lion_dead),
                marf.reply().t("はい", "大丈夫でございます"),
                h.look().d("険しい表情で答えたのは宰相$marfだった"),
                marf.talk().t("ここにおられる方々に加えて",
                    "陛下の世話係だった数名の女官たちだけです。",
                    "その者たちには他言せぬよう固く言いつけてあります"),
                h.reply().t("分かった。",
                    "だがしかし",
                    "$meにはまだ父が亡くなったことが信じられないのだ。",
                    "あれだけ勇猛で鳴らした父上が",
                    "胸の病を患っていたなどとどうして信じられようか"),
                h.look().d("会食中に突然血を吐いて倒れた",
                    "と$garnethから報告を受けた。",
                    "食事を運び入れた女官たちを除けば",
                    "部屋には二人切りだったと聞いているが",
                    "その教皇は半眼で頷きながら身振りを交えてこう答えた"),
                garneth.talk().t("$godの名において真実しか口にしておりませぬが",
                    "$meの言葉は信用に値せぬとお考えですか？",
                    "事実陛下は$meの目の前で倒れられた。",
                    "すぐに女官を呼び確認させたところ",
                    "口から血を吐き出されており",
                    "王医が駆けつけた時には既に絶命されていた"),
                h.look().d("今朝から何度もそう聞かされていた。",
                    "$hero以外の者は一様に互いの表情を伺ったが",
                    "ここでの真偽の追求を申し出る者はいなかった"),
                garneth.talk().t("それよりも一日と時間を置いては皇帝の御心を定着させることが出来なくなります。",
                    "そうすれば我が国で脈々と受け継がれてきた皇位が途絶えてしまうのですよ？",
                    "そちらの大事のこと",
                    "まさかお忘れではありませぬな？"),
                h.look().d("$garnethの大きな目玉が$heroを捉える"),
                h.talk(garneth, w.i.throne).t("分かっている。",
                        "だが本当に$meで良いのだろうか。",
                        "初代赤獅子帝と比類するとまで云われた父上の後",
                        "それも第百代目という節目だ。",
                        "その器があるとは$meはとても思えない"),
                h.think().d("それは何度も近衛兵長や$albert",
                        "妻$mileaの前で吐露してきた本心だった"),
                garneth.talk().t("だからこその継承の儀なのですよ。",
                        "代々受け継がれてきた皇帝の御心をご自身の内に宿すのです。",
                        "そうすることで我が$st_kingdomは絶対の安寧を手に入れてきたのですから"),
                h.look().d("物心付いた頃から周りの者には言われてきた。",
                        "やがて百代目皇帝となる御方だ。",
                        "皇帝の魂を宿す器になる。",
                        "特別な神の子なのだと"),
                h.think().d("けれど$heroは今でも時々夢に見るのだ。",
                        "誰も見たことがない",
                        "教皇と皇帝のみが知るというその儀式の場で",
                        "彼の母が殺された場面を"),
                garneth.talk(h, "日程や心得").t("……日暮れまでには儀式が終わりますが",
                        "殿下",
                        "ちゃんと聞いておられましたか？"),
                h.reply().t("ああ", "すまない。",
                        "少し目眩がしてな"),
                runolf.talk().t("お父上を亡くされたばかりなのだ。",
                        "ご心労もありましょう"),
                h.look().d("いつも$runolfには助けられてきた。",
                        "片目を瞑って見せると",
                        "儀式まで自室で休むように提案する"),
                h.reply().t("そうだな。",
                        "何かあればすぐに部屋に誰か寄越してくれ"),
                marf.talk().t("御意に"),
                h.look().d("宰相が頭を下げたのを見て",
                        "$heroは席を立つ。",
                        "$garnethは口元に薄っすら笑みを浮かべて視線を送っていたが",
                        "その気持ち悪さから早く逃れるようにと",
                        "部屋を出た"),
                h.remember(w.i.emperor_bug.flag()),
                garneth.go("出ていく"),
                h.think("今後のこと"),
                w.albert.talk().t("殿下……"),
                h.look().d("通路では装備を整えた$albertが不安そうに$heroの顔を見たが、"),
                h.reply().t("部屋に戻る"),
                h.look().d("皇太子がそう言ったことを受け",
                        "一礼すると",
                        "先頭を切って歩き出した"),
                ),
            w.scene("継承のこと",
                h.be(w.stage.hisroom).d("部屋に戻ると$mileaを呼ぶように女官に言いつけ",
                    "そのままベッドに倒れ込んだ"),
                h.think().d("仰向きになって見上げた天蓋の一部が",
                    "黒く汚れている。",
                    "まだ自分が何者で将来国というものを背負って立つことなど知らない",
                    "幼子の頃に父を困らせてやろうと投げつけたインクの染みが",
                    "未だに取り替えられないまま残ってしまっているのだ"),
                h.think().d("人は死ぬとどこに行くのか"),
                h.think().d("そんな話を何度か臣下の者と話したことがある。",
                    "多くは土に帰るとか星になるとか",
                    "どこかの学者が言いそうなことで彼を納得させようとしたが",
                    "教皇である$garnethだけは異なっていた"),
                h.remember().d("彼は人が死ぬというのは外側の器だけが壊れ",
                    "中身である精神はまた別の世界へと旅立ち",
                    "そこに住み着くのだと教えてくれた"),
                h.think().d("完全に精神が離れてしまうまでの時間が約三日であり",
                    "それを過ぎるまでに別の器に移すことで人は永遠を手に入れることが出来る。",
                    "その為の儀式が御心継承の儀ということらしい"),
                h.think().d("$mileaは宗教家の考えることは肌に合わないと言っていたが",
                    "事実",
                    "儀式を終えて皇帝となった父の言動は",
                    "それまでの優しいものとは様変わりしてしまったことを覚えている"),
                h.talk().t("$meもあのようになるのだろうか"),
                h.think().d("そして",
                    "儀式の日に母が亡くなったように",
                    "皇帝の御心の呪が",
                    "再び大切な伴侶の命を奪ってしまうのだろうか"),
                h.be(w.i.throne, w.i.emperor100),
                h.remember(w.i.lion_word),
                h.talk("彼女を呼んでくれ"),
                ),
            w.scene("母殺しの疑惑",
                h.remember(w.i.murder_mam),
                h.talk(milea, w.i.emperor_bug),
                milea.talk().t("入ります"),
                milea.come().d("そう彼女が告げてドアが開けられる"),
                h.look().d("そこに",
                    "いつもカワセミの親子のようにぴったりとくっついている息子の姿はなかった"),
                milea.talk().t("大切なお話をされると聞きましたので"),
                h.talk().t("ありがとう。",
                    "さあ",
                    "傍に来て座っておくれ"),
                milea.talk().t("はい"),
                h.look().d("はっきりと返事をしたその表情には",
                    "妻としてのものよりも",
                    "次の皇帝を支える者としての覚悟が見て取れた"),
                h.talk().t("これから$meが話すことは",
                    "誰にも話したことのない",
                    "$meがずっと心の中に閉じ込めていた秘密だ。",
                    "おそらく誰に話しても妄想だと馬鹿にされるだろうが",
                    "それでも信じて聞いてくれるか？"),
                milea.reply().t("$meがあなたを信じなかったことがありますか？"),
                h.look().d("彼女が笑みを見せて安心させてくれたことに感謝しつつ",
                    "$heroはいつも見る夢の話を彼女に聞かせた"),
                h.think().d("それは父親である皇帝$lionが継承の儀式を行っている場面を",
                    "まだ五歳だった当時の$heroがこっそりと覗き見しているのだ。",
                    "父は不思議な金属製の棺桶に入り",
                    "$garnethが呪いをしながらそこに不思議な糸を取り付けていく。",
                    "糸の先にはタコの吸盤のようなものが付いており",
                    "それを次々と半裸になった父の体に貼り付けていく"),
                h.think().d("父は何も言わずに眠っていて$garnethが一人で喋っているのだが",
                    "それが何と言っているのかは決して思い出せない。",
                    "不思議に光る金属の棺桶のすぐ傍に置かれた巨大な何かの塊を",
                    "ただただ恐ろしいと感じながらも目を離すことが出来ないでいるのだ"),
                h.think().d("全ての糸を付け終えると",
                    "$garnethは初代皇帝の御心が受け継がれると宣言し",
                    "その巨大な箱に手を触れる。",
                    "するとたちまちに部屋全体が小さな震動を始め",
                    "棺桶だけでなく",
                    "父の体までもが発光する"),
                h.think().d("それがどれくらいの時間続くだろう"),
                h.think().d("気づくと部屋は暗がりになり",
                    "棺桶から父が起き上がる"),
                h.look().d("目覚めた父は$garnethから宝剣を貰うと",
                    "やはり傍に寝かされていた母の首を撥ねるのだ"),
                h.talk().t("……$meはいつもそこで目を覚ます。",
                    "お前も何度か聞いたことがあるだろう",
                    "$meが叫んで目覚めるのを"),
                milea.reply().t("はい"),
                h.look().d("彼女は小さく頷くと",
                    "$heroが再び話し始めるのを待った"),
                h.talk().t("実は代々皇帝になる者だけに伝えられる呪というものがある。",
                        "そのことを$meは父から先の和平交渉に出かけられる前に聞かされてな"),
                milea.ask().t("呪",
                        "とは？"),
                h.talk().t("父は運命のように逃れられぬものの名前だと仰られていた"),
                h.look().d("その言葉に$mileaの表情が益々険しくなったが",
                        "構わずに続けた"),
                h.talk().t("初代赤獅子帝がその手で最愛の妻を殺してしまったという逸話は",
                        "お前も知っているだろう"),
                milea.reply().t("え、ええ"),
                h.talk().t("皇帝となった者はその初代と同じ行為をしてしまう",
                        "というのがその呪らしい"),
                milea.ask(h, "あなた私を殺すと？").t("つまりそれは",
                        "あなたが$meを殺すということですか？"),
                h.look().d("声に出さずに頷くと",
                        "彼女は悲しげに目を伏せてそのまま黙り込んでしまった"),
                h.reply("自信がない").t("この話を父から聞かされ",
                        "$meは自分がいつも見ていた夢が",
                        "本当は夢じゃなかったのだと確信したんだよ。",
                        "そうだ。",
                        "$meもきっとお前を手に掛けてしまう"),
                milea.talk(h, "あなたを信じています").t("あなたは本当はお強い人です。",
                        "その呪とやらに負けませんよ"),
                h.think().d("そう信じたい",
                        "と口にすることすら出来ず",
                        "$heroは力なく笑みを作っただけだ"),
                milea.talk(w.child, "この子もいるし").t("それにほら",
                        "我が子もいますし",
                        "これから国を治めようというあなたがそんなに弱気でどうします"),
                h.think(w.i.lion_word),
                h.ask().t("ではもしそれでも$meがお前に剣を向けたとしたら",
                        "その時はどうすれば良いのだ？"),
                milea.reply().t("運命ならば",
                        "$meはあなたの妻としてこの身を捧げましょう"),
                h.know(w.i.milea_mind).d("彼女のその瞳には恐れも怯えもない",
                        "真の人間の強さという光が宿っているように感じた"),
                h.talk().t("$meがお前であったならなあ"),
                milea.reply().t("$meは馬に乗れませんから"),
                h.look().d("そう言って笑った彼女を見て",
                        "不安な気持ちを押し殺すように$heroは思い切り笑い声を上げた"),
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
                h.be(w.stage.hisroom, w.day.ceremony).d("正午に皇帝崩御の報告を済ませると",
                    "午後からは慌ただしく継承の儀の準備が進められた"),
                h.think().d("中身のない父の棺桶を前に今までの感謝と労い",
                    "それから皇位を正しく継承する旨の報告を済ませた$heroは",
                    "日が山の稜線に掛かるまでに戴冠した"),
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
                h.be("戴冠").d("形式上ではこれで第百代皇帝と名乗っても良かったが",
                    "この$st_kingdomでは正式な皇位は未だに前皇帝の体に残っているとされていた"),
                h.look().d("大小百の宝石で彩られた重々しい冠を頭から持ち上げると",
                    "拍手をしながら$garnethが部屋に入ってくる"),
                garneth.talk(h, "第百代皇帝").t("これはこれは百代陛下。",
                    "いや",
                    "まだ陛下ではありませんでしたな"),
                h.talk().t("呼称などどちらでも良い。",
                    "それよりも$meに",
                    "というよりも",
                    "この器に用があるのだろう？"),
                h.look().d("そう言うと$garnethは右目を少し下げてから口の中だけで笑い",
                    "$heroに向かって手を出す"),
                garneth.talk().t("では皇位継承の為",
                    "これより聖櫃の間へと向かいましょう"),
                h.think().d("聖櫃とは初代皇帝の遺体を収めた聖なる棺桶のことだ。",
                    "それは聖堂の地下深くに埋められ",
                    "皇帝と教皇以外の者はそこに立ち入ることすら禁じられていた"),
                w.people.talk("祝福"),
                garneth.talk(h, w.i.emp_ceremony),
                h.go(garneth, "二人だけで", w.stage.cathedral).d("$heroは大きなフードの付いた漆黒のローブの背に付いて",
                    "部屋を出た"),
                h.think().d("聖堂へと続く回廊を抜け",
                    "これから教皇だけが知るというその間に向かうことを思うと",
                    "儀式の為にと身につけた黄金の皇衣がその一歩一歩で更に重くなっていくように感じられた"),
                ),
            w.scene("秘密の地下室へ",
                h.go(w.stage.cathedral).d("拝堂と呼ばれる表の聖堂の裏手に抜けると",
                    "大理石に赤い染料で模様が刻まれた柱が何本も立っている路が",
                    "その小さな建物に向かっていた"),
                h.look().d("自分の居室とそう大差ないと思える大理石の立方体の上",
                    "屋根は玉葱のような黄金で形作られ",
                    "その芯に一本だけ細い尖塔が飛び出ている"),
                garneth.talk().t("本堂の方にはあまり来られたことがないですかな"),
                h.reply().t("父から近づくことを固く禁じられていたのでな"),
                h.think().d("$garnethが知らないはずはないのだが",
                    "こういった物言いをして相手の様子を見る癖があるのだ。",
                    "それを快く思わない者は多いが",
                    "教皇という権威に口出し出来る人間は皇帝以外には存在しなかった"),
                garneth.talk("王家代々継承時のみ入ることを許可されている").t("こちらです"),
                h.look().d("そう言って取っ手のないドアに触れる"),
                h.look().d("扉は音もなく右側に滑っていくと",
                    "そこに薄暗い口を開けた。",
                    "口の中は通路ではなく",
                    "下へと続く階段になっている"),
                garneth.talk().t("どうされました？",
                    "行きましょうぞ"),
                h.think().d("気圧された",
                    "という訳ではないが",
                    "その不可思議な扉がどうこうというのではなく",
                    "先の見えない地下階段から言い知れぬ警告の風を感じたのだ"),
                h.go().d("それでも降りない訳にはいかない"),
                h.talk().t("分かっている"),
                h.go().d("短く答えると",
                    "彼に続いて石段に足を踏み出した"),
                h.look("秘密の部屋"),
                h.go("秘密の通路").d("階段は何度か曲がりながら果てしなく地下へと降りていて",
                    "けれどその薄暗い通路や天井",
                    "苔で湿った壁",
                    "足元を真っ黒な虫や蜥蜴が抜けていく様を",
                    "初めて見るとは感じなかった"),
                h.think("見た記憶がある").d("そう。",
                    "これはいつも夢で見るあの光景へと続く",
                    "悪夢の階段なのだ"),
                ),
            w.scene("人格の継承",
                h.look(w.stage.lab).d("小さな部屋に入った"),
                h.look().d("そこは儀式の間の前にある控室のようで",
                    "誰が使っていたのかよく分からない木製の机と椅子がある。",
                    "他にも棚や大きな縦に長い壺が置かれ",
                    "儀式の間へと繋がる扉は金属の格子になっていた"),
                garneth.talk().t("一説ではここは重罪人を閉じ込めておく為の地下牢だった",
                    "とも云われておりますな。",
                    "この$st_kingdonが興るまでには様々な血腥い歴史があったと聞きます。",
                    "おそらくはそういった者たちを葬る為に用いられたのでしょう"),
                h.look().d("$garnethは錆びついた鉄錠を開けながら",
                    "御伽噺でも聞かせるかのように淡々と語る"),
                h.think().d("国には表に出せない歴史もある"),
                h.think().d("まだ理解出来ない頃にそう語ってくれたのは",
                    "亡くなった母だった"),
                h.think().d("人は誰かが自分より上に立つことを酷く恐れ", "嫌う生き物で",
                    "だからこそ神の代理人である教皇がただ一人の治世者として皇帝を認めるのだと。",
                    "つまり皇帝もまた",
                    "人々の代表者でしかない"),
                h.think().d("その言葉は今でも日々$heroの頭の中で",
                    "事あるごとに思い返すようにしている大切なものだった"),
                garneth.talk(h, "継承を始める").t("それでは儀式を始めましょう"),
                h.go().d("背筋が寒くなるような音をさせ鉄格子が開くと",
                    "$garnethは慣れた様子で部屋の中央へと進む"),
                h.look().d("そこはいつも夢で見たあの金属の棺桶が置かれ",
                    "その周囲から百足の足のように太い糸が何本も後ろに置かれた巨大な箱へと伸びていた"),
                h.talk().t("これは何なのだ？"),
                garneth.talk().t("継承の箱",
                    "と呼んでおります。",
                    "正式なものはお話してもご理解願えないでしょう。",
                    "神々の技術で造られたものだ",
                    "と云われておりますな"),
                h.go().d("近づいてその銀色の箱に触れる"),
                h.feel().d("ひやりとしたその感覚は刃の先を首筋に当てられたそれによく似ている",
                    "と思った"),
                garneth.talk().t("こちらに入って横になられて下さい"),
                h.reply().t("あ、ああ"),
                h.go().d("戸惑いがちにその金属の棺桶に足を入れる。",
                    "中は真っ黒な分厚い布のようなものが詰まっていて",
                    "腰を沈めるとそこから動けなくなった"),
                garneth.talk().t("少し痛みますが",
                    "これも儀式の一環です故"),
                h.do("薬を打たれる").d("そう言って$garnethは何かの先を首筋に当てる"),
                h.talk("何を").t("何だ……"),
                h.feel().d("感じたのは小さく抓られたような痛みだ。",
                    "それに続いて視界がぼやけ始める"),
                h.talk().t("おい！", "$garneth！",
                    "これが儀式だというのか？！"),
                h.think().d("ぼやけてきたのは視界だけではない。",
                    "自分の発した言葉も形を成さなくなり始め",
                    "やがては思考もまとまらなくなってしまった"),
                h.hear().d("$garnethが何やら喋っていたが",
                        "それを聞き取ることすらままらない"),
                h.feel().d("そこにあったのはただ暗闇と",
                        "雨粒が葉から滴り落ちるような一定のリズムだった"),
                h.feel().d("死",
                        "という連想と",
                        "ただ最愛の妻と我が子の笑顔だけが瞼に浮かび",
                        "それを思うだけで心の中に涙が満ちた"),
                garneth.talk().t("……これが初代皇帝陛下の",
                        "永遠の御意志なのです"),
                h.think().d("それは随分と遠くで聴こえていた"),
                garneth.talk("皇帝の人格を継承する").t("……人はやがて死ぬ。",
                        "けれどその中身さえ移すことができれば",
                        "それは永遠に生き延びることと同じ"),
                h.think().d("神話の時代。",
                        "神々は自らの中身を次々と移し替えて長寿を得たのだと云う。",
                        "もし本当にそのような技術が存在したとすれば",
                        "移し替えられた方の中身は",
                        "一体どこに行ってしまうのだろうか"),
                h.think().d("そんなことを考えていた意識も徐々に霧散する煙のように薄まっていき",
                        "やがて完全に闇に溶けた"),
                h.ask("そのような魔術を？"),
                garneth.talk("太古のヒトの技術です"),
                garneth.talk("代々技術者の家系だった"),
                garneth.talk("人格の継承"),
                w.hero.be(w.i.portchara, "強制的に"),
                ),
            w.scene("最愛殺し",
                h.be(w.stage.hisroom),
                h.hear().d("最初に気づいたのは彼女の声だった"),
                h.look().d("目を開けるとベッドに横たえられた最愛の女性が",
                    "目を見開いたまま必死に叫んでいる"),
                h.look().d("だが$meには何も聞こえない。",
                    "何も届かない"),
                h.feel().d("ただ右腕が重いことだけを意識していて",
                    "その手に握られている何かが容赦なく振り下ろされた"),
                h.look().d("その女性の胸元に突き立てられた黄金の剣には",
                    "金銀や光る石の装飾に混ざって",
                    "黒にも似た赤いものが飛び散っていた"),
                h.do().d("汚してしまったな",
                    "という誰かの声が響くと",
                    "手渡された布でその液体を拭い去る"),
                garneth.ask(h, "お目覚めですか？").t("お目覚めですか？"),
                h.look().d("そう言った者はニヤリとして被っていた漆黒のフードを取り去った"),
                h.ask(garneth, "儂は皇帝か？").t("$mineは皇帝か？"),
                garneth.reply("yes").t("その通りでございます"),
                h.hear().d("その男の答えに満足すると",
                    "元通りになった剣を鞘に収めて彼に渡した"),
                garneth.deal(h, w.tsword),
                h.go(milea, "彼女の居室"),
                milea.ask("お目覚めですね？"),
                h.deal("殺害"),
                w.hero.do(w.milea, "殺害", w.i.emperor_bug.deflag()),
                ),
            w.scene("呪いの継承",
                h.ask().t("ところで$garnethよ"),
                garneth.talk().t("はい陛下。",
                    "何でございましょうか"),
                h.ask().t("$mineは何度目の継承をしたのだ？"),
                h.know(garneth, w.i.lion_dead.deflag()),
                garneth.reply().t("百になります"),
                h.ask().t("つまり百の最愛を$mineは自ら葬ったのだな？"),
                garneth.talk().t("そうしないとお目覚めになられませんので……必要悪",
                    "というものでしょう"),
                h.look().d("感情のない", "蛇の目玉のようにもそれは見えた"),
                h.look(child).d("だがその男の遥か後ろ",
                    "もう一つの目がこちらを覗き見している"),
                h.talk(child, "お前もいずれ最愛の者を殺す").t("お前もいずれは同じ過ちを犯すだろう。",
                    "それが百代の平和の為の",
                    "皇帝だけが知る｜悲しみ《バグ》だ"),
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

