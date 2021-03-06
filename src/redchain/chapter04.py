# -*- coding: utf-8 -*-
"""Chapter 04: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.redchain import config as cnf
THM = cnf.THEMES


# scenes

# episodes
def ep_lateyears(w: wd.World):
    ma = w.masuda
    scenes = [
            w.scene("結局何も分からず",
                ma.come(w.stage.office).d("早朝の$st_starcafeは半分程度しか席が埋まってなくて",
                    "$heroは周りを気にせずに一人でテーブルに陣取り",
                    "｜特大サイズ《ベンティ》のカップに入ったカプチーノを一口含んだ"),
                ma.deal().d("モバイルＰＣを持ってくるべきだったと後悔したが",
                    "仕方なくシナモンロールを食べながら",
                    "スマートフォンで$n_hidekoの引退事情を知る人物に辿り着けないかと検索を繰り返す"),
                w.tag.comment("ここで一旦情報まとめ"),
                ma.think().d("まだ糸川町の空き家火災の遺体は身元不明のままだと$newspaperのウェブ版には出ていた"),
                ma.think().d("$ln_sugiokaからはあれ以来メールは入っておらず",
                    "ひょっとしたら遺体は$n_hidekoとは別人で",
                    "自分が調べていることの全てが徒労に終わるかも知れないという考えが浮かんだが",
                    "彼女についてこれ以上調べずに帰ってしまっていいのか",
                    "という思いも同時に持っていた"),
                ma.think().d("今まではこの程度でいいやとしか思わなかったのに",
                    "何故だろう。",
                    "これが$n_managerに言われた「$n_hidekoにやられた」というやつだろうか"),
                ma.look().d("確かに", "調べれば調べるほど$n_hidekoというのは不思議な魅力を持った女性だったということが分かってきた"),
                ma.think().d("家庭についての詳しい事情は分からないが",
                    "母子家庭で育った$fn_hidekoは$n_shopownerに声を掛けられたことがきっかけで",
                    "まずはアイドルの道を目指した。",
                    "彼の話では三人でグループを組んだがその中では群を抜いて素質があったらしい"),
                ma.think().d("しかしソロデビューも控えていた最中に$n_managerの事務所に引き抜かれ",
                    "そこで今までとは一転",
                    "女優を目指し始める。",
                    "初主演を務めた$i_movienameでは自力で出産して子供を育てた女性という難しい役どころを演じ切り",
                    "主演女優賞に輝いた"),
                ma.think().d("だが次に声が掛かったテレビドラマ初主演作では視聴率が奮わずに",
                    "以降彼女はテレビから身を引いて映画と舞台に活躍の場を求めることになった"),
                ma.think().d("その後三十まで", "業界では名を知らない人間はいないほどの人気を博すが",
                    "三十歳を機に突如芸能界を引退して表舞台から姿を消してしまう"),
                ma.think().d("その件について当時の事務所社長だった$ln_managerに経緯を尋ねたが",
                    "彼は何故か口を噤んで教えてはくれなかった"),
                ma.deal().d("$heroはそこまでの情報を文章にまとめると",
                    "一旦$ln_tanabeにメールで送信する"),
                ma.look().d("流石にまだ出勤していないのか返事は戻ってこなかったが",
                    "文章として書き下してみたことで$heroの頭の中では芸能界引退までのことはひとまず把握が出来た"),
                ma.think().d("ただそこには記載しなかった噂レベルの情報もあって",
                    "それはどうやら彼女が表舞台から去った事情に関係してそうなのだ"),
                ma.think().d("$n_coworkerのところで会った劇団員の$n_actoressは",
                    "事務所社長の妻が刺された時期と$fn_hidekoが辞めた時期が一致していることから当時色々と憶測が飛び交ったと言っていた"),
                ma.think().d("$n_managerは彼女の引退は自分の所為ではないとだけ言って",
                    "彼女と何があったのかについては濁していたが",
                    "事務所に引き抜いてきた時には自分の家に住まわせていたらしい"),
                ma.think().d("そしてその引き抜かれたことに対して何か恨みを持ってそうだったアイドル時代のマネージャー$n_shopownerは",
                    "彼女の引退にまつわる噂として",
                    "ある大物俳優の子を身籠ったという話を教えてくれた"),
                ma.talk().t("ああ……けどここから先が繋がらないんだ"),
                ma.think().d("ぽろりと飛び出た独り言に",
                    "隣に座っていたスーツ姿の女性が驚いて見ていたが",
                    "$heroは苦笑を返すと空になったカップを手に席を立った"),
                ma.move().d("ゴミ箱に捨てて外に出る"),
                ma.look().d("既に太陽がしっかりと街を照らし",
                        "往来を人や車が行き交っていた"),
                ma.look().d("けれどぷっつりと途絶えてしまった$n_hidekoの繋がりの尻尾をどう見つければいいやら分からず",
                        "$heroは自分の歩き出す方向すら決められないまま",
                        "その場に取り残されたように立ち止まっていた"),
                ma.deal().d("そこに", "メールが届く。",
                        "$neyaからだ"),
                w.miki.talk().d("今日こっちに帰ってきます？"),
                ma.think().d("どう返すべきかと考えて",
                        "$heroはスマホを持ったまま右の指を宙に浮かせた"),
                ma.think().d("まだ", "何も知ってない"),
                ma.think().d("最終で帰る", "とだけ打って返すと",
                        "すぐに「わかりました。がんばって」と簡素な",
                        "けれど彼女なりのエール付きの返事をくれた"),
                ma.deal().d("それから$heroは登録しておいた電話番号からある人物のものを呼び出すと",
                        "発信ボタンを押した。",
                        "少しばかり時間帯が早いだろうか"),
                ma.hear().d("だがスリーコールで相手が出る。",
                        "そこから響いてきたのはよく通る$n_coworkerの声だった"),
                ma.talk(w.tanabe, "調べた情報"),
                ma.hear(w.tanabe, "彼女の本名"),
                ),
            w.scene("秀子の友達",
                ma.come().d("再び同じ小劇場を訪ねるのかと思っていたが",
                    "彼が指定したのはその近所にあるファーストフード店だった"),
                ma.look().d("通勤通学の時間帯は既に終えていて",
                    "店内の席には主婦や定年を迎えたであろう年齢の男女で埋まり",
                    "意外と賑わっていた。その中を赤と黄色の制服を着た前髪の後退した男性が歩いていて",
                    "ぼうっと立つ$heroを見つけると手を挙げた"),
                w.coworker.talk().t("$me。", "分かる？"),
                ma.ask().t("$ln_coworkerさん？"),
                ma.look().d("それは昨日白塗りの顔だった劇団の座長$n_coworkerだった"),
                ma.talk().t("ここで働いているんですか？"),
                w.coworker.talk().t("他にも色々と掛け持ちしてるよ。",
                    "平日だけならそこまでじゃないけど土日入れると百万コースだからね"),
                ma.think().d("彼らの劇団が毎回どの程度の規模の公演をしているのかは分からない。",
                    "ただこの年齢になってもパートを幾つも掛け持ちしないと続けていけない気苦労が",
                    "向けられた笑顔の目元の皺の深さに刻まれているような気がした"),
                ma.do().d("シフトが十時までだというので",
                    "それまで店内で待たせてもらうことにする"),
                ma.look().d("見ていると$ln_coworkerは意外と頼られているようで",
                    "何かにつけ呼ばれてはあちこち行き来して忙しそうに働いていた。",
                    "文句も言わず", "客が残していったゴミを片付けてテーブルを綺麗にし",
                    "日本語が不自由な観光客には片言の英語と身振り手振りでやり取りをする"),
                ma.think().d("自分がいざこんな暮らしに放り込まれたらどうだろう。",
                    "彼と同じように自分より遥かに若い従業員からの指図に耐えられるだろうか。",
                    "ミスしたことに対して舌打ちされ",
                    "それでも気分を悪くせずにちゃんと謝って",
                    "すぐさま客に対して笑顔で応対する"),
                ma.look().d("演技の練習とでも思ってやっているのかと観察していたが",
                    "それはどうやら彼自身の生き様のようだった。",
                    "何故そう感じたのか",
                    "理由はその時間では見つけられなかったけれど",
                    "敢えて言葉にすれば", "無理をしている", "とは見えなかったからだろう"),
                ma.look().d("あと五分ほどで十時",
                    "というタイミングだった"),
                w.shoko.come().d("どこかで見覚えのある女性が近づいてきて",
                    "目の前の席に座った"),
                w.shoko.ask().t("何？",
                    "$meのこと知ってるの？"),
                ma.think().d("淡紫のコートの下に", "不必要に大きく胸元の開いたワンピースのそれが見える。",
                    "濃い青の鍔広の帽子にやけに口紅が目立つ化粧をした彼女の",
                    "その睫毛の多い気怠げな瞳に", "$heroはようやくどこでそれを目にしたのか思い出す"),
                ma.ask().t("ひょっとして", "とんぼ返りの？"),
                ma.look().d("そう言った$heroのことを彼女は睨みつけるように目を細めて見た"),
                w.shoko.reply().t("……ああ", "新幹線の。",
                    "ひょっとして$meのこと聞きつけて？"),
                ma.think().d("思い出してはくれたようだが", "どうも何か勘違いをしている。",
                    "そもそも彼女が誰なのか", "$heroは何も知らないのだ"),
                ma.look().d("そこに仕事を終えた$ln_coworkerがやってくると", "彼女は立ち上がる"),
                w.shoko.talk().t("ねえ$coworker。",
                    "本当に$meなんかで良いの？"),
                w.coworker.talk().t("いいよいいよ。",
                        "$hidekoの代わりなんてあんたくらいしか頼めないからさ"),
                ma.look().d("彼女は$heroには興味がないようで", "背を向けて何やら$ln_coworkerと話し始めたが",
                        "そこに「すみません」と無理やり割って入った"),
                w.coworker.talk().t("ああ、えっと……二人は知り合い？"),
                ma.look().d("互いの顔を見て$ln_coworkerは笑みを浮かべる。",
                        "$heroは何と答えたものかと言葉を探したが", "彼女の方は即答でこう言った"),
                w.shoko.talk().t("どうやら$meのファンみたいなのよ。",
                        "新幹線からのストーカー"),
                ma.look().d("彼女は$heroを見やって肩を竦めたけれど",
                        "真顔になって互いを見合った二人の男性の様子に気づいて、"),
                w.shoko.talk().t("$me", "何か間違ったこと言ったかしら？"),
                ma.look().d("と小首を傾げた"),
                ),
            w.scene("祥子",
                ma.know(w.shoko).d("彼女は$n_shokoという舞台女優なのだと",
                    "$ln_coworkerから教えられた"),
                w.shoko.talk().t("$meはてっきり新幹線で気に入ってネットなんかで調べてストーキングされたんだと思ったわよ"),
                w.coworker.talk().t("それはもう十年も前の話だろう？"),
                ma.look().d("呆れながら$ln_coworkerは$heroの肩を叩いて苦笑する"),
                ma.come().d("折角だからというので近所にある彼女のスナックに向かっているのだが",
                    "通りを逸れてからもう十分は歩いているのにまだ着かない"),
                ma.ask().t("お店ってこの近くなんですよね？"),
                w.shoko.talk().t("あと五分くらいよ"),
                ma.think().d("つい五分ほど前にも同じ台詞を聞いた気がする"),
                ma.ask().t("ところで$ln_shokoさんの方も$n_hidekoとお知り合いなんですか？"),
                ma.think().d("彼女の名を口に出してしまってから",
                    "新幹線の中で$n_shokoが不機嫌になったことを思い出す"),
                w.shoko.ask().t("知り合い……ね"),
                ma.look().d("そう鼻で笑うと軽く首を振って何も言い返さずに",
                    "彼女は先を急いだ"),
                ma.ask().t("あの", "$meまずいこと言っちゃいましたかね？"),
                w.coworker.reply().t("気にすることはないよ。",
                    "$meなんかしょっちゅう機嫌損ねさせてるよ"),
                ma.ask().t("けど$n_hidekoの名前", "あまり良く思ってないみたいですけど"),
                w.coworker.talk().t("知らないの？"),
                ma.look().d("彼がそう言って立ち止まって$heroを見たところで",
                    "$n_shokoが声を掛けた"),
                w.shoko.talk().t("ここの二階よ"),
                ma.look().d("そこは新しいビルとビルの間に挟まれた三坪ほどの面積に建てられた羊羹の切れ端のような",
                    "雑居ビルだった"),
                ),
            w.scene("秀子の旧友",
                w.shoko.talk().t("お酒は出さないからね"),
                ma.look().d("そう言われて「ＣＬＯＳＥＤ」の札の下げられたドアを潜ると",
                    "五、六人が座れるカウンター席だけの小さな飲み屋になっていた。",
                    "店の名前は『スナック$fn_shoko』だ"),
                ma.look().d("慣れた様子で$ln_coworkerは席に座ると隣の席に上着を脱いで鞄と一緒に置く"),
                ma.deal().d("$heroもそれに習ったが",
                    "スマートフォンだけ取り出してテーブルに置いておいた"),
                w.shoko.talk().t("でさ",
                    "その記者さんが今頃彼女のこと調べてどうしようっていうのよ。",
                    "ひょっとしてアレ？",
                    "あ、けど口止めされてるし違うわね"),
                ma.look().d("$n_shokoはコップに三人分のお茶をペットボトルから注いで用意しながら",
                    "一人芝居でもするように自分で質疑を終えようとする"),
                w.coworker.talk().t("最近はほら",
                    "一昔前に流行ったものを掘り起こしてきてひと儲けしようってのが流行ってるだろ。",
                    "$meたちからすりゃ$n_hidekoなんて誰でも知ってる有名人だ。",
                    "けど最近の若い奴らは名前を聞いたことないってのばっかなんじゃないか？"),
                ma.ask().t("え、ええ。",
                    "$myも今回の事件で出てくるまでは全然聞いたことありませんでした"),
                w.shoko.ask().t("事件……"),
                ma.look().d("その言葉に一番先に反応したのは$n_shokoだった。",
                    "彼女の声で$ln_coworkerも$heroに視線を向ける"),
                ma.talk().t("あ、いえ",
                    "つい事件て言うのが口癖で",
                    "今回の特集記事でって言いたかったんですよ"),
                ma.look().d("苦しい弁解だ。",
                    "特に彼女の方はすっかり腕組みをして$heroことを睨みつけている"),
                ma.talk().t("分かりましたよ。",
                    "正直に言います。",
                    "まだ確定した話じゃないので絶対に他言しないで下さいよ"),
                ma.think().d("こういううっかりは絶対にやってはいけない。",
                    "人間だから多少ミスするのは仕方ないが",
                    "情報の管理と保護に関してのミスについて",
                    "かつての指南役だった$ln_sugiokaは口を酸っぱくして何度も注意した。",
                    "何故ならそれは単なるミスではなく",
                    "ブン屋にとって一番大事な信頼を失い兼ねない大きな損失だからだ"),
                ma.look().d("事実",
                    "今目の前の二人の雰囲気が", "先程の”事件”という一言でがらっと変わってしまった"),
                ma.think().d("それでも口が滑ってしまったものは取り返しがつかない。",
                    "$heroは覚悟を決め",
                    "全て打ち明けることにした"),
                ma.talk().t("実は$meが住んでいる町で空き家火災があったんですよ。",
                    "そこで二人のご遺体が発見されたんですが",
                    "現在はまだ身元不明になっています"),
                ma.look().d("$ln_coworkerの方はそれを聞いて「へえ」と声を漏らしたが",
                    "彼女の方はじっと黙ったまま", "その厚塗りになった睫毛の瞳を何度か瞬かせただけだ"),
                ma.talk().t("ある筋からその片方の遺体が元女優の$n_hidekoではないかとの疑いがある",
                    "という情報がもたらされました"),
                w.coworker.ask().t("え？",
                    "それじゃあ$hideko死んじゃったってこと？"),
                ma.look().d("目を大きく開けた$ln_coworkerに対して「情報が確かなら」と頷くと",
                        "$n_shokoの方は急に背を向けてカウンターにもたれ掛かった"),
                w.shoko.talk().t("本当に亡くなったっていうんなら",
                        "こんな風に掘り起こさずにひっそりと本名$n_h_laterという女性が亡くなっただけにしておけばいいじゃない。",
                        "それこそが彼女が本当に望んでいたことでしょう？"),
                ma.hear().d("彼女の口から$n_hidekoの本名が出たことにも驚きがあったが",
                        "それ以上にそのよく通る発声で映画の一場面でも演じているかのように滞りなく出てきた文言に",
                        "耳を奪われた"),
                w.coworker.talk().t("おい$shoko。",
                        "お前まだあのこと根に持ってるのか？"),
                ma.ask().t("あの",
                        "まだ疑いがあるというだけで別に本当に亡くなられたかどうかは分かっていないんですよ。",
                        "それこそ今だってこの国のどこかで買い物にでも出かけているかも知れないし"),
                ma.look().d("慰めにもならないとは分かっていたけれど",
                        "彼女の一言で重くなってしまった空気を少しでも何とかしようとしての言葉だった"),
                ma.think().d("けれど",
                        "こちらを振り返って向けた$n_shokoの目には既に涙が蓄えられていた"),
                ma.ask().t("あの、えっと……"),
                w.shoko.talk().t("あんたさ", "火事で焼き出された人間の顔を見たことはある？"),
                ma.think().d("一体何を問われているのだろう"),
                w.shoko.talk().t("酷い臭いだよ。",
                        "何より肌は赤黒くて強張って歯がよく見えるように剥き出しでね",
                        "辛うじて顔の造形が分かったけど",
                        "目鼻の位置関係とかそんなもので",
                        "ああひょっとしたら$n_hidekoかも知れないなって思うくらい。",
                        "あんな風な最期を迎えるって分かっていたら",
                        "そうなる前に$meなんかは死んでしまいたいよ"),
                ma.ask().t("すみません。",
                        "ひょっとして$ln_shokoさんは遺体確認をされたんですか？"),
                ma.look().d("彼女は暫く$heroを見つめてから",
                        "雫で濡れた睫毛を下げた"),
                ma.ask().t("どうして$ln_shokoさんが？"),
                w.coworker.talk().t("彼女は$n_hidekoの妹の旦那の姉",
                        "つまり義理の妹になるんだよ"),
                ma.talk().t("え……"),
                ma.think().d("どうにかして$n_hidekoの関係者に会えないものかと思っていたが",
                        "まさかこんなところにいるとは思わなかった"),
                ma.ask().t("それじゃあの「とんぼ返り」って",
                        "遺体確認？"),
                w.shoko.reply().t("そうだよ"),
                ma.look().d("ティッシュを出して涙を拭いながら答えた彼女に",
                        "その時の話を聞き出したいという衝動が喉元まで上がってくる。",
                        "けれどそれを無理やり呑み込んで",
                        "当初$ln_coworkerから聞き出そうとしていた質問を投げた"),
                ma.ask().t("芸能界を引退してからの$n_hidekoさんのことについて",
                        "何でもいいんで話してもらえますか"),
                ),
            w.scene("芸能界引退後の秀子の話",
                w.shoko.talk().t("ちょっとだけ", "飲んでもいいかい？"),
                ma.look().d("彼女はそう言って棚からワインを持ち出して椅子に座ると",
                    "それを開けてグラスに注いだ。",
                    "真っ赤な液体が満ち満ちていくが",
                    "零れそうになったところで一度半分くらいまで飲むと",
                    "そこに再び注ぎ足した"),
                w.coworker.talk().t("$meも貰っていいか？"),
                ma.look().d("$ln_coworkerは既に空にしたコップを差し出したが、"),
                w.shoko.talk().t("日本酒じゃないんだよ"),
                ma.look().d("苦笑してそのコップを引っ手繰ると",
                    "代わりに別のワイングラスを用意してそれに半分ほど注いで渡す"),
                w.shoko.talk().t("記者さんも飲む？"),
                ma.reply().t("いえ。$meはまだこれから帰って仕事しなきゃならないんで"),
                w.shoko.talk().t("何だい。",
                    "じゃあこれは仕事じゃないっての？"),
                ma.think().d("言われてから",
                    "どうして自分は今追いかけている$n_hidekoのことを仕事と考えなくなっているのだろう",
                    "と気づいた"),
                ma.talk().t("たぶん",
                    "今はただ単純に知りたいっていう気持ちを満たす為に動いているから",
                    "ですかね"),
                ma.think().d("記者としてはどうなのか知らないが",
                    "それでも今のこの気持ちこそが",
                    "以前$ln_sugiokaに「何かが欠けてる」と言われた部分なのだろうか。",
                    "もしそうなら",
                    "もう少しちゃんと記者という仕事を考え直してみても良いのかも知れない"),
                ma.ask().t("それで",
                    "引退後もお二人は付き合いがあったんですか？"),
                ma.look().d("軽いジャブのような質問だと思ったのだが",
                    "どういう訳か二人は互いの顔を見合わせた後で気まずそうに俯いてしまう"),
                ma.ask().t("別に話し辛かったら話さなくても大丈夫です。",
                    "お二人ともそれぞれ$n_hidekoさんに思うところがあるみたいですし"),
                w.coworker.talk().t("そういう訳じゃないんだ。",
                    "ただその……彼女は突然目の前から消えてしまってね"),
                ma.think().d("$ln_coworkerが語ってくれたのはこんな話だった"),
                ma.know().d("その日",
                    "マスコミ各社ほか", "関係があった芸能事務所に向けて一通のファックスが送られた。",
                    "それは個人的な事情により本日付けを以って芸能界を引退し$n_hidekoという名前を捨てる",
                    "というものだった"),
                ma.know().d("記者たちは慌てて事務所前に駆けつけたが",
                    "それと時を同じくして事務所社長は自宅で強盗に刺された妻の応対で手一杯だった為に事務所は開いておらず",
                    "自宅に慌ててやってきたカメラが捉えたのは",
                    "血だらけになって救急車を待っている$n_managerの姿だった"),
                ma.know().d("そんな衝撃映像も重なり",
                    "世間では様々な憶測が乱れ飛んだ。",
                    "その中には$ln_coworkerが言ったように$n_hidekoが社長を刺し殺したというものも混ざっていた"),
                w.coworker.talk().t("まあそんな騒動もあったから余計に$hidekoは誰にも何も言えなかったんじゃないかな",
                    "って$meなんかは思うんだ"),
                w.shoko.talk().t("違うわよ"),
                ma.think().d("既にグラスを空にした目元の赤い$n_shokoは新しいワインを開けながらも",
                        "「それは違う」と否定する"),
                w.shoko.talk().t("あの人はね",
                        "そんな騒動なんて微塵も堪えるような女性じゃなかったわ。",
                        "だって$meに言ったんだもの。",
                        "この世界でずっと生きていきたい。",
                        "自分が生きていると感じられるのは舞台とカメラの中だけだからって。",
                        "そこまで女優でいる覚悟をした人間がさ",
                        "ちょっとくらい世間で騒がれたからって何よ？",
                        "そんなの逆に人気が出て嬉しいくらいよ。",
                        "それで顔を売るくらいの気概がないと女優なんてやっていけないのよ"),
                ma.think().d("それはずっとその世界で生きてきた彼女の",
                        "偽らざる本音だろう"),
                ma.look().d("黙って聞いていた$ln_coworkerを見やると溜息をついてから",
                        "空になったグラスを置いた"),
                w.coworker.talk().t("そうなんだよな。",
                        "$hidekoがそんな簡単に女優を辞めるとは思えなかったし",
                        "今だってそんなもの信じられないよ。",
                        "どんな理由を持ってきたら自分の一生を女優に捧げるとまで言っていた人間を心変わりさせられるんだ？",
                        "なあ"),
                ma.think().d("言われてみればその通りだった。",
                        "仮に大物俳優との間に隠し子を作ったとしてそれで揉めたとしても",
                        "命を懸けるくらいに演じることを愛していたなら",
                        "どこかで今でも演劇を続けているだろう"),
                ma.think().d("けれど先程の$n_shokoの話が事実だとすると",
                        "あの焼け出された遺体の一つは$n_hidekoであり",
                        "女優を辞めてからの彼女の人生の経緯は誰にも知られないままあの古い木造の空き家の中で",
                        "終わりを迎えたことになる"),
                ma.ask().t("あの", "$n_hidekoさんの妹さんてどこにいらっしゃるんですか？",
                        "今でも$ln_shokoさんの義理の姉になるんですよね？"),
                ma.look().d("けれど彼女は目を閉じて首を振ると",
                        "昨年に病気で亡くなったことを教えてくれた"),
                ma.ask().t("それじゃあ他の親族の方って……"),
                w.shoko.talk().t("だから$meが呼ばれたんだろうさ。",
                        "あの人の母親は彼女の舞台の最中に倒れて病院に運ばれたけれどそのまま亡くなったし",
                        "父親は小さい頃に出て行ったきり梨の礫。",
                        "唯一の肉親だったのは$meの義姉になるあの人の妹だけで",
                        "他に親戚がいるなんて話は聞いたことないわ"),
                ma.ask().t("それじゃあ女優を引退した後の足取りは完全に途絶えているんですね"),
                ma.look().d("二人の顔をそれぞれ見たが",
                        "どちらもその後についての情報は持っていないようだ"),
                w.coworker.talk().t("当時ならマスコミを始めとする多くの人間が彼女の足跡を追いかけていたと思うけど",
                        "あの頃ですら確実と思われる噂なんて何もなかったからな。",
                        "そもそも当時一番信じられていたのが社長の妻を殺して海外逃亡というのを除けば",
                        "どこかでひっそり自殺したんだってものだったから"),
                ma.think().d("二十年前に既に亡くなっていた。",
                        "それが焼け出されて遺体となって発見される"),
                ma.think().d("そんな可能性を思いついたが",
                        "果たして二十年もの間", "空き家の中で亡くなった人間が発見されずにいられるだろうか"),
                w.shoko.ask().t("ところで逆にあんたに訊きたいことがあるんだけどさ"),
                ma.reply().t("何ですか？"),
                w.shoko.ask().t("$n_hidekoの遺体と共に発見されたもう一つの遺体って",
                        "誰なんだい？"),
                ma.ask().t("$ln_shokoさんは確認されたんですか？"),
                ma.look().d("彼女は顔を顰めて首を横に振る"),
                ma.talk().t("実はもう一人の方に関しては何も分かりません。",
                        "$meも知人の記者に教えてもらっただけなんで",
                        "彼が何も言ってこないところを見ると",
                        "警察の方でも捜査が難航しているってことでしょうね"),
                w.shoko.talk().t("そうかい。",
                        "それじゃああの子は一体何なのかしらね。",
                        "$n_hidekoと関係があるのか", "ないのか"),
                ma.look().d("$n_shokoはそう呟いて天井を見上げると",
                        "その頬に涙を数滴流した"),
                ),
            w.scene("手がかりなく",
                ma.go("station").d("その後",
                    "二人から聞いた当時の劇団関係の知人を何人か当たってみたが",
                    "女優時代の彼女の話ばかりで",
                    "引退後の彼女の動向に関する情報は噂レベル以上のものは何も得られなかった"),
                ma.look().d("東京駅の構内は午後三時を過ぎても人の波が途絶える気配はなく",
                    "何とか帰りの新幹線の席を押さえると",
                    "随分と遅くなった昼食の弁当を買ってホームに上がった"),
                ma.feel().d("風が強く抜けていく"),
                ma.think().d("肝心のその後どうやって糸川町のあの空き家に辿り着いたのかという情報が得られないまま東京を去ることに",
                    "自分の無力さを痛感する。",
                    "ただその後悔の気持ちが大事なのだと", "$ln_sugiokaからは教わった。",
                    "後悔するからこそ次に繋がる何かが生まれるのだと"),
                ma.think().d("ホームに入ってきた新幹線を見ながら",
                    "$heroはこのレールの上を$n_hidekoは辿ったのだろうか",
                    "それとも誰かに運ばれたのだろうかと",
                    "そんな想像をして列の最後尾に付いた"),
                ),
            w.scene("町の人々への聞き込み",
                ma.know(w.h_later),
                ma.have(w.h_later, w.i.life),
                ma.come(w.stage.town, w.day.interview3),
                ma.deal(w.i.interview, w.stage.town),
                ma.know(w.doc),
                ),
            ]
    return [w.chaptertitle("晩年のこと"),
            *scenes,
            ]



# main
def story(w: wd.World):
    return ep_lateyears(w)


def main(): # pragma: no cover
    from src.redchain.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

