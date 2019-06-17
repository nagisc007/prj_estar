# -*- coding: utf-8 -*-
"""Story: chapter 01: The another me.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherme import config as cnf
THM = cnf.THEMES


# scenes
def sc_campuslife(w: wd.World):
    kyoko = w.kyoko
    return w.scene("大学生活",
            kyoko.be(w.stage.univ, w.day.current),
            kyoko.feel().d("半分ほど開けられた教室の窓から入り込んできた風に$meの左頬がそっと撫でられ",
                "意識を黒板の教育と心理学などと書かれた文字に向かわせる"),
            kyoko.look().d("机の上に出した分厚い教育心理学概論の教科書は開いていたページが流れてしまっていて",
                "ずっと同じ調子の先生の声に瞼を閉じられないように注意しながらどこのことを言っているのか探す"),
            kyoko.look().d("スマートフォンに表示されている時刻は四時を回っている"),
            kyoko.look().d("前の席に座って肩を寄せてこそこそ話している同期生は",
                "大学の前に新しく出来たラーメン屋に行くかどうしようかそれなら同じサークルの$ln_matsumotoを誘いたいけれど彼って彼女持ちっぽい",
                "みたいな会話をして",
                "チョークを手にした先生の視線を何度か奪っていた"),
            kyoko.think().d("そんな風に誰かのことを気にせず生きていけたら",
                "$meはきっと",
                "もっと孤独になれたのだろう"),
            )

def sc_backhome(w: wd.World):
    kyoko, child, student = w.kyoko, w.child_kyoko, w.student_kyoko
    return w.scene("帰宅",
            kyoko.move().d("自転車で路地を駆け抜ける"),
            kyoko.think().d("段差で少し跳ねて",
                "前の籠に入れた買い物袋の中の生卵のことが気になったけれど",
                "この前のように落とした訳じゃないから大丈夫だろうと思うことにした"),
            kyoko.look().d("見上げた空は雲が多くて",
                "それでも最近はこの時間もまだまだ明るい"),
            kyoko.look().d("路地の街灯はぼんやりとした光を放ち始め",
                "帰宅途中の学生や会社員をそれとなく照らしている"),
            kyoko.think().d("この辺りは学生が暮らすアパートが多いけれど",
                "明かりの付いた住宅から漂ってくるのは家庭の夕食の香りだった"),
            kyoko.hear().d("子供たちのはしゃぐ声に", "母親の声が重なる"),
            kyoko.think().d("ちょっと苛立ったやり取りのようだったけれど",
                "それでもどこかごく普通の家庭のそれに思えて",
                "$meは腰を上げペダルを漕ぐ足に力を入れた"),
            kyoko.feel().d("ここ最近は六月とは思えないくらい暑くなる日が増えたけれど",
                "このくらいの時間帯になればしっとりと空気が落ち着いて",
                "幾分心地良い。",
                "風を切って走るこの時間が",
                "$meを色々なものから自由にしてくれるような気がして", "好きだった"),
            kyoko.look().d("交差点で左に曲がり",
                "ブロック塀を少し行くと二階建てのアパートが見えてくる"),
            kyoko.move().d("自転車を駐輪場に止めて籠から買い物袋を取り出すと",
                "鍵を掛けてから鉄製の階段をたんたんと登って自宅に向かう"),
            kyoko.look().d("まだ明かりの付いていない部屋が殆どで",
                "$meの二〇五号室まで暗がりを歩いていく。",
                "お隣は今は空いていると聞いているから",
                "できればこのまま残り三年間を何事もなく過ごせるように",
                "そのままでいて欲しいと思っている"),
            kyoko.deal().d("鍵を差し込んで",
                "ドアを開ける"),
            kyoko.deal().d("スイッチに手をやり明かりが灯ると",
                "そこには待ち構えてましたとばかりに赤い水玉のワンピースを着た女の子が",
                "満面の笑みで「おかえり」と$meを出迎えた"),
            )

def sc_mytable(w: wd.World):
    kyoko, child, student = w.kyoko, w.child_kyoko, w.student_kyoko
    return w.scene("わたしとワタシたち",
            kyoko.be(w.another, "一緒に暮らす"),
            child.talk().t("ねぇ"),
            kyoko.talk().t("すぐご飯にするから待って"),
            kyoko.look().d("彼女は$meのジーンズにまとわりついて",
                "買い物袋からあれやこれやと取り出すのに邪魔になって仕方ない"),
            kyoko.deal().d("それでも冷蔵庫を開けて割れていなかった生卵を仕舞うのを手伝ってくれたり",
                "「はい」と袋の中から豆腐やネギ", "魚肉ソーセージを取っては渡してくれる。",
                "彼女にとってはそれはとても大切な仕事なのだ。",
                "お手伝いではないことを", "$meはよく知っている"),
            kyoko.move().d("冷蔵庫を閉じると", "袋を畳んでリビングへと移動する"),
            kyoko.look().d("六畳間には小さな白いテーブルと二段に積み上げた衣装ボックス",
                "それに布団が三組", "畳んで隅に置いてある"),
            kyoko.look().d("その積み上がった布団にもたれかかりながら膝を抱えて$meを見る",
                "グレィのパーカーを着た少女がいた"),
            student.talk().t("またサークル顔出さなかったんだ"),
            kyoko.reply().t("いいのよ。",
                "出たところでみんなお菓子食べて喋ってるだけだから"),
            kyoko.look().d("唇を少し尖らせて黙り込むと",
                "彼女は足元に積み上がっていた文庫小説を手に取って開いた。",
                "口を開けば文句か小言で", "それ以外は常に本を読んでいる"),
            kyoko.look().d("その反対側では十歳の少女がスカートの裾がほつれてしまっている人形を手に",
                "一人でままごとをしていた"),
            kyoko.look().d("彼女たちの名前は$n_kyoko。",
                "そして$meの名前も$n_kyokoだった"),
            kyoko.deal("面倒見る", w.another).d("$meは彼女たちに分からないように小さく溜息を落として",
                "上着をハンガーに掛ける。",
                "今日は味噌汁と玉子焼き", "半分残っている大根は千切りにしてサラダにでもしよう"),
            kyoko.move().d("キッチンに立ち", "蛍光灯を点ける。",
                "リビングからは時折十歳の$fn_child_kyokoの声が聴こえたが",
                "何も構わずに包丁を取り出して", "味噌汁に入れる人参と大根を刻み始めた。",
                "分量は約三人前だ"),
            kyoko.look(w.another),
            kyoko.deal("生活する", w.another),
            kyoko.think("他人と付き合えない"),
            kyoko.look("３つある茶碗"),
            )

def sc_morning(w: wd.World):
    kyoko, child, student = w.kyoko, w.child_kyoko, w.student_kyoko
    return w.scene("朝の日常",
            kyoko.be(w.stage.living),
            kyoko.deal().d("昨夜作った味噌汁の残りを温めながら",
                "炊き上がったご飯の半分をおにぎりにする。",
                "ゴムで思い切り上げた前髪が引っ張られて僅かな痛みを感じたけれど",
                "気怠い意識を目覚めさせるにはちょうど良い"),
            kyoko.look().d("左を見ればまだ敷かれたままの布団の上に$fn_child_kyokoは大の字で眠っていて",
                "それをもう一人の$fn_student_kyokoが壁を背に座って本を読みながら時折睨みつけている"),
            kyoko.think().d("それでも最近喧嘩にならなくなっただけマシかな", "と思う"),
            kyoko.deal().d("三つのおにぎりの中にはそれぞれ",
                "岩のり", "鮭フレーク", "梅干し", "を入れる。",
                "別に彼女たちは学校に一緒に来る訳じゃないけれど",
                "三人分作らないと$meの空腹は満たされない"),
            kyoko.talk().t("もうそろそろ起きてくれないと困るんだけど"),
            kyoko.deal().d("温まった味噌汁をお椀三つに分けながらそう声を掛けると",
                "仕方ない", "といった動作で$fn_student_kyokoが$fn_child_kyokoの丸出しになったお腹を擦る。",
                "小さな呻きと共に伸びをすると",
                "むくっと上半身を起こして「おはよ」と寝ぼけ顔で言った"),
            kyoko.deal().d("$meはテーブルの上に味噌汁とご飯を三人分置いて",
                "一人でいつものワンピースに着替えている$fn_child_kyokoを横目に",
                "足元の目覚まし時計の時刻を確認する"),
            kyoko.look().d("七時五十八分。",
                "準備して出掛けて何とか一時限目の講義には間に合うだろう"),
            kyoko.talk().t("いただきます"),
            kyoko.hear().d("$meが手を合わせたのを見て彼女たちも同じようにそれぞれの声で「いただきます」と言った"),
            kyoko.think().d("別に結婚している訳でもなく",
                "兄弟がいる訳でもない"),
            kyoko.think().d("けれど$meにとってはこれが日常だった"),
            kyoko.think().d("それは十年前に$n_child_kyokoが生まれて以降ずっと",
                "紛れもない$meの日常なのだ"),
            )

def sc_gotouniv(w: wd.World):
    kyoko, sayama = w.kyoko, w.sayama
    return w.scene("大学に向かう",
            kyoko.move().d("自転車で朝の路地を駆け抜ける"),
            kyoko.feel().d("大学までの十分程度の行程が",
                "$meの心をほんの少しだけ解き放ってくれる"),
            kyoko.think().d("でもそれは",
                "天気が良い時に限るというのは",
                "$meだけに限定した話じゃないだろう"),
            kyoko.talk().t("何でなのよ……"),
            kyoko.deal().d("急に振り出した雨は$meの肩まで伸びた髪をしっかりと濡らして雫を大量に滴らせる。",
                "駐輪場は屋根付きで心底良かったと思うけれど",
                "正直一度帰って着替えてきたい気分だ"),
            kyoko.move().d("$meは鞄からハンドタオルを出して", "何とか髪の上辺の水分と冷たくなったシャツの肩なんかを拭うが",
                "とてもそれで何とかなるような濡れ方ではなかった"),
            w.tag.comment("ここで松本が出ている。後にそれと分かるよう、多少の彼の描写"),
            kyoko.look().d("他の生徒も同様に文句を言いながら自転車で入ってきたけれど",
                "中にはどこかで拾ったんじゃないかと思うような骨の折れたビニール傘で何とか一時しのぎをしたように見える男性もいた"),
            kyoko.look().d("彼は$meを一瞬だけ見たが", "すぐにそのまま講義棟の方へと駆けて行ってしまった"),
            kyoko.deal().d("$meは籠から鞄を引っ張り出して一度天を見上げる。",
                "雨は少し弱まったけれど", "もうちょっとだけ濡れる覚悟が必要かも知れない"),
            kyoko.move().d("心の中で「よし」と合図して駆け出そうとしたところで",
                "声を掛けられた"),
            kyoko.look().d("赤と白の市松模様をした傘を持った友人が",
                "小さく手を挙げてこちらに近づいてくる"),
            sayama.talk().t("入ってく？"),
            kyoko.reply().t("助かります"),
            kyoko.behav().d("三十度の深いお辞儀をしてから顔を上げ",
                "互いの顔を見合わせると気の置けない笑顔になる"),
            kyoko.move().d("$meは$n_sayamaの傘の下をおすそ分けしてもらうと",
                "彼女が話し出した昨夜のドラマの話に適当に相槌を打ちながら歩き出した"),
            )

def sc_friendA(w: wd.World):
    kyoko, sayama, matsu, taka = w.kyoko, w.sayama, w.matsumoto, w.takamura
    return w.scene("友人A",
            kyoko.be(w.stage.lechall).d("階段教室になった講堂では既に社会心理学概論の授業が始まっていたが",
                "$meたちより後からバラバラとやってくる生徒が開始五分を過ぎても沢山目に付いた"),
            kyoko.think().d("最近はノートを広げるよりもパソコンやスマートフォンにメモを取ったりするという人が増えているみたいだけど",
                "$meはガラケーだし", "左隣に座る$fn_sayamaも$meと同じようにノート派だ。",
                "ただ彼女の場合はノートの隅に花びらを書き込んでいて",
                "それがあまりにも丁寧に漫画の背景みたいに線が沢山あって",
                "思わず見惚れてしまった"),
            sayama.talk().t("これでも昔は漫画家を目指したものよ"),
            kyoko.look().d("彼女はそう得意げに口の端を上げる"),
            sayama.ask().t("あ、そうそう。",
                "$i_cir_nameに新しい人入ったんだけど聞いてる？"),
            kyoko.reply().t("え？　知らない"),
            kyoko.think().d("正式名称『$i_circle』だけれどそれを略して先輩たちは$i_cir_nameと呼んでいる。",
                "$meはＬＩＮＥをやっていないのでこういった情報がすぐに回ってこないけれど",
                "$meと$fn_sayamaも去年の秋に人数が足りないからどうしてもと誘われたから入ったくらいで",
                "人が増えることは結構稀だった"),
            kyoko.deal(sayama, "電話"),
            sayama.talk(w.i.circle),
            sayama.talk().t("えっとね……"),
            kyoko.look().d("彼女はバッグからピンクの水玉柄のスマホケースに包まれたそれを取り出すと",
                "右の真ん中の指三本を使って器用に画面を操作する。",
                "それは使い慣れない$meからすれば魔法そのものに映るが",
                "驚いている間にもモニタには写真付きで$n_matsumotoという男性が現れた"),
            kyoko.talk().t("あ……"),
            sayama.ask().t("何？",
                "ひょっとして好み？"),
            kyoko.look().d("短く切り揃えられた髪に他人を値踏みするような奥二重の目",
                "何よりも顎髭が中央部だけ濃いところが",
                "見間違えようがない"),
            sayama.ask().t("でもなんか彼女持ちだって言ってたから残念だね"),
            kyoko.talk().t("好みじゃないし", "そういうんじゃないけど……"),
            kyoko.think().d("さっき駐輪場で$meを一瞬睨んでいった人だった"),
            kyoko.ask().t("その人ってさ",
                "$meの顔とかも知ってるの？"),
            kyoko.look().d("質問の意味が分からなかったのか彼女は顔を顰めたが",
                "「どうだろ」と答えただけでスマートフォンで別の操作を始めてしまう。",
                "ＬＩＮＥでも届いたのだろうか"),
            kyoko.hear().d("前の大きなホワイトボードには『イマジナリーフレンド』と乱暴な字で書かれ",
                "手に持った資料を何度か見ながら", "白髪混じりの男性講師は話を続けた"),
            taka.talk().t("君らも耳にしたことはあるだろう。",
                "$i_imagefriendとは空想上の友達のことだ。",
                "小さい頃に子供が何もない場所を指差して”誰かいる”と言うのは",
                "何も幽霊やそういった超常的な存在を見つけたからではなく",
                "自分が生み出した架空の友達を見ているからだ", "とも云われている"),
            kyoko.look().d("隣で$fn_sayamaはスマートフォンを見てほくそ笑んでいたけれど",
                "$meの関心は講師の口から紡ぎ出される見に覚えのある事柄に向けられていた"),
            taka.talk().t("一部の研究では幼少期には誰もがこの$i_IFを持っており",
                "成長には欠かせない存在だという提言もなされている。",
                "ただ一方でこの$i_IFは多くは二歳から三歳までに消えてしまい",
                "その多くは記憶からも消えてしまう"),
            kyoko.think().d("$i_IFと呼ばれる存在を",
                    "$meは高校時代に相談に乗ってもらった理科教師から教わった"),
            taka.talk().t("だが稀に大人になっても", "あるいは成長してからこの$i_IFを生み出してしまう人間がいる。",
                    "彼らは精神的なストレスから逃避を図る為に$i_IFを生み出すが",
                    "時にこの$i_IFに依存しすぎて彼らの存在なしには生きていけない",
                    "といった精神状態を構築することもあるそうだ"),
            kyoko.look().d("他にも集中して聞いている生徒がいるかと思って自分より下に座っている人たちを覗いてみたが",
                    "午前一番始めの授業だけあって誰もが眠そうにしていた。",
                    "ただその中で一人",
                    "一番隅の席で背筋をぴんと張って真っ直ぐに講師を見ている大柄の男性がいた"),
            taka.talk().t("大人になってからの$i_IFというのはよく幻視や幻覚",
                    "解離性同一性障害のようなものと勘違いされることもあるが",
                    "これについては同一のものではないという研究結果がある"),
            kyoko.think().d("その男性はおそらく$n_matsumotoだと思ったけれど",
                    "$fn_sayamaから呼びかけられて$meの意識からは抜け出してしまった"),
            kyoko.ask().t("何？"),
            sayama.talk().t("それで$kyokoはサークルどうする？"),
            kyoko.look().d("彼女はＬＩＮＥの画面を見せながら週末の奉仕活動への参加の可否を$meに求めてくる"),
            kyoko.deal().d("$meは最初から今回は断ろうと思っていたが",
                    "彼のあの目を思い出してしまったからだろうか",
                    "参加することにしておいてもらった"),
            sayama.talk().t("そっか。",
                    "$kyokoが行くなら$meも参加する"),
            kyoko.talk().t("$sayamaって", "そういうところがあるよね"),
            sayama.talk().t("いい性格してるって言われる"),
            kyoko.think().d("少しくらい小言を口にしても笑ってくれるところは",
                    "確かに付き合い易いし",
                    "何より他人とは一定の距離感を置いていたい$meからすると",
                    "必要以上にこちら側に介入してこない彼女は",
                    "一番安心できる友達かも知れない"),
            kyoko.hear().d("いつの間にか講師の説明は$i_IFから別の話題へと移り",
                    "どうやって心理学調査というのは行われるべきかという方法論の解説が息継ぎの難しそうなタイミングで行われていた"),
            kyoko.think(THM["problem"]),
            kyoko.feel(w.another, "邪魔"),
            kyoko.think(w.i.vanish_another),
            kyoko.go("彼女たちのいない場所"),
            )

def sc_circleact(w: wd.World):
    kyoko, sayama, matsu, kunugi = w.kyoko, w.sayama, w.matsumoto, w.kunugi
    return w.scene("サークル活動",
            kyoko.move().d("この日はしっかり六時限目まで入っていて",
                "最後のドイツ語の講義を終えた後でぼんやりとした眠気と共に教室を出た"),
            kyoko.look().d("まだ日は高くて",
                "午前中に降り続いていた雨がすっかり上がった為か",
                "いつもより空が綺麗な気がする。",
                "それでも体はすっかり気だるくて",
                "二十歳を超えた自分から体力というものが日に日に失われていっているような心地になってしまう"),
            kyoko.look().d("鞄から携帯電話を取り出して時刻だけ確認し",
                "参加すると返事した手前", "今日のサークルの会合には顔を出すべきなんだろうな",
                "という諦めにも似た気持ちを思い出した"),
            kyoko.move().d("講義棟から外に出るとずっと続く並木道の下を生徒が疎らに歩いている"),
            kyoko.look().d("暫く行くとベンチの前に座る$sayamaと$ln_kunugi先輩の姿を見つけ",
                "$meは小走りになって彼女たちの前に向かう。",
                "先輩の方は今日も相変わらず上下とも黒のぴったりした服を着ていて",
                "特に立って腰に手を当てているそのパンツのラインがモデルのようだ"),
            sayama.talk().t("$kyoko。", "今日は３０２だって"),
            kunugi.talk().t("聞いたよ。",
                "あんたの方から参加するって言ってくれたんだって？"),
            kyoko.look().d("先輩は$meの肩に手を掛けて嬉しそうに身を乗り出す。",
                "しっかりと化粧された整った顔の長い睫毛の強い瞳にじっと見られると",
                "女性の$meでも何だか照れてしまうけれど",
                "入会当初から何かと気に入られていた。",
                "特に何かをした", "という訳ではないのだけれど",
                "集会の時には何かと声を掛けてくれる"),
            kyoko.talk().t("ちょうどその日", "用事がなかったもので"),
            kyoko.think().d("そう答えた$meを見て先輩の後ろで$sayamaが笑いを堪えているように",
                "確かに最初は行く気はなかったのだ"),
            kyoko.talk().t("あの"),
            sayama.talk().t("そういえばもうすぐ彼も来る予定なんだけど"),
            kyoko.look().d("$sayamaの視線が右肩を超えたずっと後ろに向けられ",
                "それから「あ」という声で$meもそちらを振り返った"),
            kyoko.look().d("$n_matsumotoだ"),
            kyoko.look().d("首のところから黒い紐が伸びたカーキ色のパーカー姿で",
                "のっそりと会釈をしてぼそり", "低い声で挨拶をした"),
            matsu.talk().t("$ln_matsumotoです。", "よろしく"),
            sayama.talk().t("$meは$ln_sayamaでこっちの彼女が$n_kyoko"),
            kyoko.talk().t("なんで$meだけフルネームなの？"),
            kyoko.look().d("けれど彼女は「いいからいいから」と$meと$ln_matsumotoを向き合わせる。",
                "彼とは頭一つ分以上差があるからどうしたって顔を見上げることになるのだけれど",
                "特に彼に照れた様子はなく",
                "それどころかやはり$meに対して何か気に入らないことがあるのか",
                "一瞬睨むような表情になってから",
                "すっと視線を逸して先輩を見た"),
            matsu.talk().t("$kunugi。$me", "今日はちょっと用事あるんで決まったこと後でＬＩＮＥしといてもらえますか"),
            kunugi.talk().t("入部そうそうサボるとはなかなか良い根性じゃないか", "ln_$matsumoto"),
            kyoko.look().d("$ln_kunugi先輩は構わずに$ln_matsumotoの肩に手を回して舐めるようにその顎を見上げる"),
            matsu.talk().t("いや勘弁して下さいよ。",
                "今日は彼女のライブの手伝いしないといけないんすから"),
            kunugi.talk().t("$ln_matsumotoの彼女って軽音部？"),
            matsu.talk().t("大学じゃないすよ。", "普通にバンド組んで歌ってます"),
            kyoko.look().d("へえ", "と声を漏らしたのは$sayamaだった。",
                    "先輩はどんな彼女なのかの質問を始めて",
                    "彼は困った様子で何とか逃れようとする"),
            kyoko.think().d("その姿を見ながら「彼女がいる」と堂々と口にできる$n_matsumotoという人間が",
                    "少しだけ羨ましく感じた"),
            kyoko.go(w.i.circle, "逃げ出す"),
            kyoko.go(w.another, "家に帰る"),
            )

def sc_strangeday(w: wd.World):
    kyoko, shota, sayama = w.kyoko, w.shota, w.sayama
    return w.scene("奇妙な日",
            kyoko.come(w.stage.univ).d("次の日も一時限目から授業を入れていて",
                "それでもこの日はいつもより早く出掛けられたこともあって",
                "十五分も前に教室に入ることができた"),
            kyoko.deal("全部で八十ほど席が並ぶ中", "$meはいつも後ろの窓際を確保する。",
                "窓際が空いていなかったら廊下側。",
                "真ん中や前の方は落ち着かない。",
                "誰かに見られているかも知れない", "という感覚が強くなるからだ"),
            kyoko.think().d("あの子たちがいない",
                "見えない空間というのは",
                "普通に考えれば$meにとってとても落ち着ける空間のはずだった。",
                "けれど現実はびくびくと怯えて",
                "つい周囲の人の視線を確認してしまう"),
            kyoko.look().d("開始時刻が近づくにつれ",
                "教室にも人が増えていくけれど",
                "$meを視界に入れて何か表情が変わるような人間はいない"),
            kyoko.think().d("気にしすぎている",
                "ということは理解していた"),
            kyoko.think().d("それがまた新しい自分を生み出すかも知れないということも",
                "中学の頃から診てもらっている$ln_miura先生に注意されていた"),
            kyoko.think().d("常に一緒にいる訳ではない$fn_child_kyokoも$fn_student_kyokoも",
                "本当に$meの$i_imagefriendなのだろうか。",
                "未だに一度として", "クリニックの病室に彼女たちが現れたことはなかった"),
            kyoko.look().d("気を抜くと",
                "授業が始まっていた"),
            kyoko.look().d("眼鏡を掛けた女性講師が教育と子供の成長について",
                "やたらとカタカナ語を交えて話している"),
            kyoko.hear().d("けれど$meの二つ前に座った女子二人組はそんな内容とは全く関係のない雑談を",
                "こそこそと",
                "それでも何とか聞き取れる程度の大きさで行っていた"),
            kyoko.look().d("先生はそれについていちいち気にしたりはしないようだが",
                "美人な同級生の誰々がストーカーされて大変だとか",
                "$meにもその先生にも一切関係なさそうな話題で",
                "それでも時折笑い声を漏らすものだから集中して講義を聞いていられないな",
                "という思いが湧き上がった"),
            kyoko.deal("授業"),
            kyoko.hear(w.i.stalker.flag()),
            kyoko.think().d("彼女たちは大学に何をしに来ているのだろうか"),
            kyoko.think().d("ということは思わないけれど",
                "何も文句を言わずに大学の授業料から月々の仕送りから出してくれた新しい父親のことを考えると",
                "$meは心の中で小さな溜息を吐き出すしかなくなる"),
            kyoko.look().d("視野から彼女たちの姿を消したい",
                "という思いで廊下側に視線を向けると",
                "窓から教室を覗き込む一人の男性がいることに気づいた"),
            kyoko.look(shota, "知らない男子").d("$ln_matsumotoとは全く違うタイプで",
                "髪の色を染めているのか", "濃い栗色のように見える。",
                "前髪多めで首裏の辺りが刈り上げになっているので",
                "マッシュルームという印象を抱いたが",
                "くりっとした人形のような大きな瞳は一瞬だけ$meに投げかけられ",
                "彼は楽しそうに唇を結んだ"),
            )

def sc_lunchtime(w: wd.World):
    kyoko = w.kyoko
    return w.scene("ランチタイム",
            kyoko.think().d("教室を覗いていた彼は誰を探していたのだろう"),
            kyoko.be("ベンチ").d("鞄から出したアルミホイルに包んだおにぎりを頬張りながら",
                "$meは図書館で借りた本を開いていた"),
            kyoko.look().d("晴れた日はベンチでなく芝生の上の木陰に場所取りをして",
                "一人の時間を満喫する。",
                "吹き抜ける風がちょうど心地よくて",
                "日本一の面積を誇るこの大学のキャンパスには緑も多く植えられている"),
            kyoko.look().d("フリスビーを持ち出して遊んでいる男女の集団や",
                "バドミントンをしている女性陣",
                "彼女の膝枕で横になっている男性がいたりと",
                "それぞれ思い思いの時を過ごしている"),
            kyoko.think().d("そんな誰かと一緒の時間を少しだけ羨ましいと思うこともあるけれど",
                "見えないはずの誰かをつい見てしまうんじゃないか",
                "それを気味悪がられてまたあの目を向けられてしまうんじゃないか",
                "と怯えながら息をすることは",
                "今の$meにはまだまだ難しいことだった"),
            kyoko.look().d("だからこうして", "本を読む"),
            kyoko.look().d("本の中には沢山の友人がいて",
                "そんな彼らは決して$meを裏切るようなことはないから"),
            kyoko.think().d("彼らはいつだって",
                "$meの目の前には現れない。",
                "勝手に喋らないし",
                "物を奪ったりもしない"),
            kyoko.think().d("ご飯を食べることだって", "彼らには必要ないのだ"),
            )

def sc_parttimer(w: wd.World):
    kyoko, arase, minori = w.kyoko, w.arase, w.minori
    return w.scene("パートのお時間",
            kyoko.go(w.i.partwork).d("この日は大学の授業を終えると",
                "その足で電車でニ駅先まで移動する"),
            kyoko.move().d("中央駅にほど近い繁華街は大学にはない人の賑わいで",
                "それだけで目眩がしてしまいそうになるのだけれど",
                "大事な生活の糧を得る為には少しくらいの我慢が必要だった"),
            kyoko.move().d("株式会社$st_officeは雑居ビルの三階にオフィスを構えている"),
            kyoko.move().d("路地に入り",
                "五分ほど歩くと五階建てのビルが見えてきて",
                "その一階のコンビニに人が忙しなく出入りしているのが分かる。",
                "$meはその隣の階段を無心で上がっていく"),
            kyoko.look().d("三階まで登るとドアの前に『株式会社$st_office』と書かれていて",
                "慎重にドアノブを回して押し開けた"),
            kyoko.go(w.stage.office),
            kyoko.talk().t("こんにちは……"),
            kyoko.look().d("うつむき加減でぼそりとした声の挨拶をする$meに",
                "奥の窓席に座ってパソコンで作業中だった$n_minoriだけが小さく手を挙げてくれる"),
            kyoko.deal().d("会釈をしてから入り口脇のタイムカードに時刻を記録して",
                "右手側の机の一つに席を取る。",
                "荷物を足元に置いてから", "マウスを動かして切り替わった画面でＩＤとパスワードを打ち込んだ"),
            arase.talk().t("おっはよ", "$kyoko"),
            kyoko.reply().t("あ、はい。", "おはようございます"),
            kyoko.look().d("急に肩を叩いて声を掛けてきたのが", "室長と呼ばれている現場監督の$n_araseだ。",
                "堀の深い顔に跳ね返った癖の強い髪から強烈な甘い匂いをさせている。",
                "ストライプ柄のスーツがお気に入りで", "今日はネイビーブルーのそれにオレンジのタイを合わせていた"),
            arase.talk().t("どう？",
                "大学は順調？"),
            kyoko.talk().t("ええ。", "あの、今日の分の打ち込み資料はそれですか？"),
            kyoko.look().d("$ln_araseが手に持っているファイルが$meの本日の担当分だと分かっていたけれど",
                "確認の為に敢えて尋ねる"),
            arase.talk().t("そうそう。",
                "あと出来れば", "もうひとセット頼みたいんだけど今日時間ある？"),
            kyoko.look().d("最近はいつもこうだ。",
                "$meが仕事に慣れてきたこともあるのだろうけど",
                "他のパートの人の分まで作業を回そうとするのだ"),
            kyoko.talk().t("今日は", "ちょっと"),
            kyoko.deal().d("だから用事がある風を臭わせて", "何とか滞在時間の延長を防ぐ"),
            arase.talk().t("そうだよね。",
                "$kyoko真面目な学生だもんね。",
                "勉強で忙しいよね"),
            kyoko.look().d("$ln_araseは資料ファイルを机に置くと",
                "ぶつぶつと言いながら自分の席に戻って行く。",
                "それを$minoriが眼鏡の目で咎めるように見ていたが", "彼は気づいていないようだった"),
            kyoko.look().d("$meの視線に気づいた$minoriは右の掌をひらひらとやってさっさと仕事するように促すが",
                "その表情は$meと同じように苦笑を浮かべていた"),
            kyoko.deal("データ入力の仕事").d("画面に視線を戻すと",
                "作業用ファイルを開いて集計シートの番号を確認する。",
                "続いてエクセルのシートをコピーして画面いっぱいに広げると",
                "資料の数字を見ながら該当する項目に打ち込んでいく"),
            kyoko.think().d("単純なアンケートのデータ集計作業だった"),
            kyoko.look().d("社員は$ln_araseと$minoriだけで",
                    "他に常時作業をしている派遣の人が数名と",
                    "残りは$meみたいなパートタイムの人間ばかりだ"),
            kyoko.look().d("基本的に私語もほとんどなく",
                    "黙々と数字を打ち込んで三時間経過すれば",
                    "作業が途中でも終わることができる"),
            kyoko.think().d("時給も悪くないし", "文句を言われることもない"),
            kyoko.think().d("ただ", "$ln_arase室長がやたらと絡んでくることと",
                    "$minoriに気に入られないと仕事がしづらい", "というだけだ"),
            kyoko.look().d("前髪を右の眉毛の端あたりできっちりピンで留めているその几帳面さは",
                    "少しだけ$meの母親を思い出させる。",
                    "何事もきっちりと決められたようにこなしていないと駄目な人で",
                    "それを自分だけでなく相手にも求めてしまう。",
                    "結果", "周囲の人間は疲れ果てて彼女からは離れていってしまう"),
            kyoko.think().d("$meの最初の父親も", "そうだった"),
            kyoko.look().d("画面にはただ数字が並ぶ。",
                    "その意味するところなんか考えなくても",
                    "とにかく空白を埋めていくだけで誰かの役には立つのだろう"),
            kyoko.look().d("それでも",
                    "と少し気になって資料のタイトルを見やると『家族の会話について』と書かれていた"),
            kyoko.deal(w.i.relation, "$must"),
            kyoko.think("人間関係の問題"),
            )

def sc_meetboy(w: wd.World):
    kyoko, shota, child = w.kyoko, w.shota, w.child_kyoko
    return w.scene("彼と出会った",
            kyoko.go().d("仕事を終えて外に出た時には",
                "すっかり夜の街に様変わりしていた"),
            kyoko.look().d("会社帰りのサラリーマンの集団や", "既に酔っ払っている人の大きな声が路上に響く"),
            kyoko.look().d("通りにはタクシーが並び",
                "綺麗に着飾った女の人と男性がその一台に乗り込んでいく"),
            kyoko.think().d("$meも将来", "あの中の誰かになるのだろうか"),
            kyoko.move().d("そんなことを考えながら駅へと急いだ"),
            kyoko.look().d("電車で大学まで戻り",
                "自転車を取りに行って夜道の家路を帰る"),
            kyoko.feel().d("日中の青空の下を駆けるのも心地良かったが",
                "こうして夜風を切るのも悪くない"),
            kyoko.think().d("それでもアパートが近づくと胃袋の下の方が重くなり始め",
                "彼女たちの存在が自分の中で膨らみ始める。",
                "別に何か危害を加えるということはないのだけれど",
                "彼女たちを目にすることで否応なく",
                "自身のトラウマを思い出してしまう"),
            kyoko.look().d("電信柱に取り付けられた外灯が",
                "嘲るように明滅した"),
            kyoko.move().d("そこから左に曲がり",
                "アパートの駐輪場へと滑り込む"),
            kyoko.think().d("普通$i_IF", "つまり$i_imagefriendを持つというのはその人物にとっての精神安定剤のようなものらしいが",
                "$ln_miura先生にも指摘されたように",
                "$meのように常にアパートにいて一緒に暮らしている他人のように振る舞うというのは珍しいそうだ。",
                "通常何か精神的なストレスを抱えた時", "不意に現れたり",
                "相談相手として振る舞ったりする。",
                "ごっこ遊びの延長としての$i_imagefriendというのが患者によく見られる症状だと",
                "別の先生からも説明された"),
            kyoko.think().d("そんなことを言われても実際問題",
                "$meの$i_IFたちは",
                "$ln_child_kyokoと$ln_student_kyokoは",
                "$meにとっての同居人でしかなかった"),
            kyoko.look().d("自転車を降りて階段を登ろうとしたところで",
                "そこに座り込んでいる見慣れない男性に気づいた"),
            kyoko.look().d("その彼は隣に座った$ln_child_kyokoと一緒に", "綾取りをして遊んでいる"),
            kyoko.think().d("え……"),
            kyoko.feel().d("その違和感は", "最初は分からなかった"),
            kyoko.ask().t("あの"),
            kyoko.think().d("けれどじわじわと足元から這い上がってきて",
                "それが首筋まで到達すると同時に",
                "その正体である彼が$meを見て", "人懐こい笑顔になった"),
            shota.talk().t("$ln_kyoko……$fn_kyokoさん", "でいいかな？"),
            kyoko.hear().d("その声は甲高く", "少年のそれのように聞こえる"),
            kyoko.talk().t("そうだけど"),
            kyoko.remember().d("と答えてから思い出した。",
                "教室を覗いていた彼だ"),
            child.talk().t("おかえり"),
            kyoko.hear().d("十歳の$meが言う"),
            kyoko.look().d("その$childの手の上から指を差し込んで器用に紐を受け取ると",
                "$meに向けて真っ直ぐ三本になった川を見せながら",
                "彼も同じようにこう言った"),
            shota.talk().t("おかえり……$kyokoさん"),
            kyoko.come(w.stage.apart),
            kyoko.look(shota, "不審者", w.i.stalker.deflag()),
            kyoko.meet(w.shota),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("ワタシが見える"),
            sc_campuslife(w),
            sc_backhome(w),
            sc_mytable(w),
            )

def ep_mylife(w: wd.World):
    return (w.chaptertitle("わたしの日常"),
            sc_morning(w),
            sc_gotouniv(w),
            sc_friendA(w),
            sc_circleact(w),
            )

def ep_unknownboy(w: wd.World):
    return (w.chaptertitle("知らない男の子"),
            sc_strangeday(w),
            sc_lunchtime(w),
            sc_parttimer(w),
            sc_meetboy(w),
            )

# test data
def base_info(w: wd.World):
    return ("chapter1", story(w), w.kyoko, w.shota)

def story_outline(w: wd.World):
    return [
            ("chapter1", story(w),
                w.kyoko.think("他人と付き合えない"),
                w.kyoko.look(w.another),
                w.kyoko.go(w.i.circle, "逃げ出す"),
                w.kyoko.meet(w.shota),
            True),
            ("chapter1-avant", ep_intro(w),
                w.kyoko.deal("面倒見る", w.another),
                w.kyoko.be(w.another, "一緒に暮らす"),
                w.kyoko.deal("生活する", w.another),
                w.kyoko.look(w.another),
                True),
            ("chapter1-A", ep_mylife(w),
                w.kyoko.think(w.i.vanish_another),
                w.kyoko.feel(w.another, "邪魔"),
                w.kyoko.go("彼女たちのいない場所"),
                w.kyoko.go("家に帰る", w.another),
                True),
            ("chapter1-B", ep_unknownboy(w),
                w.kyoko.deal(w.i.relation, "$must"),
                w.kyoko.think("人間関係の問題"),
                w.kyoko.go(w.i.partwork),
                w.kyoko.meet(w.shota),
                True),
            ]

# main
def story(w: wd.World):
    return [w.maintitle("わたしとワタシ"),
            ep_intro(w),
            ep_mylife(w),
            ep_unknownboy(w),
            ]


def main(): # pragma: no cover
    from src.anotherme.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

