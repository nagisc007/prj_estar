# -*- coding: utf-8 -*-
"""Story: Lost her book
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.lostbook import config as cnf
THM = cnf.THEMES


# scenes
def sc_myfavorite(w: wd.World):
    nao, saya, akiko = w.nao, w.saya, w.akiko
    return w.scene("本が好きだ",
            nao.behav().d("本を開く"),
            nao.think().d("ただそれだけの行為が",
                "こんなにも$meの心を震わせる"),
            nao.be("bed").d("俯せになったまま右手を伸ばして枕元のスタンドライトの角度を変える。",
                "薄暗闇の中に煌々とした読書空間を作り出して",
                "開いた本は勿論",
                "最近見つけた個人的な掘り出し物の一冊だ"),
            nao.look().d("サイズはＢ５より少し大きい程度。",
                "淡い花柄が印刷された厚紙をカバーにして綴じられたおよそ百ページほどの同人誌で",
                "タイトルは$i_booktitle1だった"),
            w.nao.be(w.stage.town, w.day.current),
            nao.explain().d("主人公の$n_anzuは真夜中になると寄宿学校の宿舎を抜け出し",
                "使われていなかった旧校舎の図書室を訪れる。",
                "実は夜な夜なそこでは本の霊たちのお茶会が開かれていたのだ"),
            nao.look().d("作者名は小さな字で『$fn_saya』と", "本の右下のところにあった"),
            nao.think().d("おそらく”さや”と呼ぶのだろう。", "それとも”さよ”だろうか"),
            nao.think().d("手触りの良い紙にしっとりとした文章がすぐさま物語の世界に誘ってくれる。",
                "それは退屈という$meの日常をあっという間に忘却してくれ",
                "物語の主人公$fn_anzuと一緒に夢のような体験をさせてくれるのだ"),
            nao.think().d("何の娯楽もないこの町で",
                "本の中でのささやかな出会いが$meにとっての唯一の楽しみと言っても良かった"),
            nao.think().d("今夜読み終えたら",
                "なけなしの小遣いを持ってまた明日",
                "続きを買いに行こう。",
                "あと一週間ほどで夏休みになる。",
                "今よりもっと本に没頭できる時間が増えるから出来れば今出ている全ての彼女の本を揃えて",
                "一日中その世界に浸っていたい"),
            nao.think().d("本棚に並ぶものには途中までしか揃っていないものが多かったけれど",
                "この作者の本だけは何としても全巻揃えたい。",
                "そう思わせる手触りがあった"),
            nao.look().d("綴られた文字が",
                "$meの中に物語を刻んでいく"),
            nao.feel().d("その感覚のあまりの心地よさに",
                "いつまでも彼女の文章の海に浸かっていたい気分だった"),
                w.nao.think("彼女の本を全部そろえたい"),
                w.nao.think("人生を救われた"),
                w.nao.go(w.stage.bookshop),
                w.nao.know(w.i.vanishshop),
            )

def sc_knownews(w: wd.World):
    nao, dad, mam = w.nao, w.dad, w.mam
    return w.scene("本屋潰れるって",
            nao.be(w.stage.dyning, w.day.known),
            nao.behav().d("ぼんやりとした頭のままで箸を持って手を合わせる"),
            nao.look().d("高校の夏服指定の白シャツすら暑いからとＴシャツ姿のままで食卓に就いていたが",
                "手に取ったご飯茶碗は温かいを通り越して火傷しそうな熱を伝えてくれた",
                "大皿には昨夜の残りの野菜だらけの回鍋肉が半分ほど乗っていて",
                "それを適当に箸で摘んでは納豆の掛けられたご飯の上へと移し",
                "そのまま勢いよく口に掻き入れる"),
            mam.ask("夏休みのこと").t("で",
                "$naoは結局大学どうするの？"),
            nao.think().d("いつもみたいに食べ方についての母親の注意だろうと思ったのに",
                "そんな話を持ち出され", "途端に気が重くなる"),
            mam.talk().t("またそんな顔して。",
                "受験まで半年ないんだからいい加減にどうするか決めてくれないと",
                "お金のこともあるし",
                "お母さんたちだって困るのよ？"),
            nao.think().d("そうでなくても溜息がちで口うるさい母親が",
                "最近苦手だった"),
            mam.talk().t("あなたもちょっとは言ってやって下さい"),
            nao.look().d("$meが何も答えずに黙り込むと",
                "その矛先は最上段まできっちりシャツのボタンを留めて",
                "精密部品でも操作しているような箸使いで胡瓜の漬物を摘んでいる父へと向けられる"),
            dad.talk("本屋潰れる").t("小学校の前の$st_bookshop。",
                "閉店することになったそうだ"),
            nao.ask().t("え……それ", "ほんと？"),
            nao.look().d("箸を持ち替え",
                "眼鏡の右側のツルの下側を指で掻きながら「そうだ」と父は答える"),
            dad.talk().t("あそこのおばさんは$meが小学生の頃からずっと店番をしてたからいつまでもそのままな気がしていたが",
                "息子さん夫婦と一緒に暮らすことにしたんだとか"),
            nao.talk().t("誰かに店を譲るとかじゃなくて",
                "本屋さんそのものが閉まっちゃうってこと？"),
            nao.think().d("もしそうなら一大事だ。",
                "何故ならこの町には本屋が一軒しかない"),
            mam.talk().t("あらそうなの？",
                "コンビニじゃあ$poetbookなんて置いてくれないのよね。",
                "やっぱり購読申し込みするしかないかしら"),
            nao.look().d("既にご飯茶碗を空にした母親は",
                "立ち上がってキッチンの流し台に片付いたお椀から運びながら溜息をつく"),
            nao.think().d("意図的に話を逸してくれたのだろうか"),
            nao.look().d("そんな思いで父親を見たが",
                "味噌汁を持ち上げて啜るその目元は何も語らないように平静のままで",
                "小さくずりずりと音を立てて口にワカメを滑り込ませた"),
            nao.think().d("本屋が消える"),
            nao.think().d("その事実は$meにとって大学進学について頭を悩ませるよりもずっと大きな問題として",
                "朝から脳裏に横たわってしまった"),
            w.nao.know(w.i.vanishshop),
            )

def sc_checkclosed(w: wd.World):
    nao, akiko = w.nao, w.akiko
    return w.scene("潰れるんですか！？",
            nao.move().d("その日の高校からの帰り道",
                "一度も腰を降ろさずに立ち漕ぎのままメインストリートを走りぬけ",
                "$meは$st_bookshopまで急いだ"),
            nao.look().d("小学校の緑色の背の高いフェンスを右手に歩道を進むと",
                "交差点を渡ってすぐの模型店の左隣に",
                "小豆色のビニールの庇が出た二階建てが見えてくる。",
                "そこに白で書かれた『$st_bookshop』は輪郭がぼやけて書の字がよく分からなくなってしまっているけれど",
                "前の棚に並んでこちらを見る女性誌の濃いメイクの女性や旅行雑誌のハワイやグアムの文字は見慣れたままで",
                "どこにも”閉店します”なんて書かれていない"),
            nao.deal().d("横断歩道を渡ってすぐにサドルから飛び降りると", "慌てて店前に横付けしてスタンドを立てる"),
            nao.go().d("前籠に入れた鞄を引っこ抜くと",
                "ドアを開けてすぐ右手のカウンターに声を掛けた"),
            nao.ask().t("おばちゃん店閉めるってほんとなの！？"),
            akiko.talk().t("あら$naoどうしたの？"),
            nao.look().d("高くなったカウンターの上には今週発売の週刊少年誌が三冊残っていた。",
                "その後ろで椅子に座りながら銀縁眼鏡を掛けたさらさらの銀髪をした女性が",
                "この店の主である$n_akikoさんだ"),
            nao.talk().t("どうしたじゃないよ。",
                "聞いたんだけど", "ここを閉めるってことは",
                "この町からおばちゃんの大好きな本が消えちゃうってことじゃないの？"),
            nao.look().d("そう言ってカウンターに身を乗り出した$meを",
                "$akikoは眼鏡の奥の優しい瞳をゆっくり閉じて一つ頷いてから",
                "手にしていた文庫本を置いた"),
            akiko.talk().t("うちが無くなったくらいで本は消えないよ。",
                "町民会館の図書室にだって", "$naoの通う学校の図書室にだって本は沢山ある。",
                "それに今はネットでいくらでも手軽に取り寄せられるんだろう？"),
            nao.talk().t("けどそれじゃ……"),
            nao.think().d("彼女の本はどこで手に入れれば良いんだろう"),
            nao.behav().d("それを口に出すことができずに俯いた$meに",
                "$akikoは小さく笑う"),
            akiko.talk().t("$ln_sayaさんの本のことでしょ",
                "$naoが本当に心配してるのは"),
            nao.look().d("$akikoは視線を店の奥",
                "地元の人の自費出版本や同人誌を置いているコーナーに向けた"),
            nao.think().d("その一画に平積みにされた同人誌の中に", "$n_sayaの本も混ざっている。",
                "$meの手元にはまだ二巻までしか揃っていなかったが",
                "そこには五巻まで並べてある"),
            nao.ask().t("いつまで店", "やってるんですか？"),
            akiko.talk().t("心配しなくてもすぐに畳んだりはしないよ。",
                "それでも今年中が期限かねえ"),
            nao.think().d("残り五ヶ月ちょっと。",
                "それだけあれば残りの本は揃えられるだろうけれど",
                "その後", "彼女が続きを出すとすればそれはどこに置かれるだろう"),
            nao.think().d("もう会えないかも知れない"),
            nao.think().d("という思いは",
                "この町から本屋が失われてしまうということ以上に$meにとっては問題なのだと",
                "初めて理解した"),
            akiko.talk("閉店のこと"),
            nao.look("残りの本"),
            )

def sc_lazyschool(w: wd.World):
    nao, anzu, teacher = w.nao, w.anzu, w.teacher
    return w.scene("退屈な教室",
            nao.look().d("わざとらしい木目がある机に肘を突きながら顎を載せて窓の外にぼんやりと視線を投げ出すと",
                "一年生たちが暑い中でだらだらサッカーボールを蹴っている様子が窺えた"),
            nao.be(w.stage.classroom),
            teacher.talk("夏休み").t("えー",
                "明日から夏休みに入る訳ですが……"),
            nao.look().d("終業式を終えた後のざわつきが消えるのを待ってから",
                "担任の$ln_teacherは事務連絡を始める"),
            nao.hear().d("内容は高校最後の夏休みだから羽目をはずしたい気持ちは分かるがしっかり勉強しておかないと受験があるだとか",
                "つい今し方蒸し暑くて何人か貧血で倒れた体育館の中で長々校長先生から聞かされたような言葉を濃縮したみたいな",
                "諸注意だった"),
            anzu.talk().t("ねえ"),
            nao.hear().d("その声は真後ろの席からだった"),
            nao.behav().d("まだ担任のプリント読みが続いていて",
                "安易に後ろを振り返る訳にはいかなかった$meは小声で「なに？」と",
                "$n_anzuに返す"),
            anzu.talk().t("下見",
                "$naoも行くでしょ？",
                "昼ご飯持ってきたし"),
            nao.think().d("シタミ",
                "というたった三文字の言葉で沢山の忘れていた",
                "あるいは忘れようとしていたことを思い出す"),
            nao.reply().t("あぁ……うん"),
            anzu.talk().t("大学行ったらみんなバラバラになるんだしさ",
                "だからその前にちょっとくらい",
                "いいよね別に"),
            nao.think().d("既に隣の市の看護学校に行くことを決めている$anzuはそう気楽に言ってくれるけれど",
                "どこでも良いから東京の大学に入ると決意を固めている$tamuraも$meも",
                "まだ確定的な未来なんて何も手にしていない"),
            nao.think().d("他の同好会メンバーはもうすっかり受験モードでＬＩＮＥグループに顔すら出さないし",
                "正直$meも$tamuraも",
                "たぶんあの旧校舎の噂については露も気にかけていない"),
            anzu.talk().t("思い出ってさあ",
                "たぶん無理矢理にでも作ろうとしないと何も残らないもんなんじゃないかな。",
                "$naoはどう思う？"),
            nao.look().d("それに答えるよりも早くに担任の視線に気づき",
                "$meは沈黙した"),
            )

def sc_gotooldschool(w: wd.World):
    nao, anzu, tamura = w.nao, w.anzu, w.tamura
    return w.scene("かつての学校",
            nao.deal().d("昼ご飯は学校近くのコンビニでサンドウィッチを買って済ませた"),
            tamura.talk().t("$anzuの奴", "自分だけしっかり弁当持ちでやんの"),
            nao.look().d("いつもの膝までまくり上げたジャージと体操シャツというスタイルで隣を歩く$n_tamuraは",
                "少し長くなったスポーツ刈りのツンツンとした前髪を触りながら",
                "焼きそばパンだけじゃ足りないと何度も愚痴る"),
            anzu.talk().t("ちゃんと言っておいたのに忘れるあんたたちがいけないんでしょ"),
            nao.look().d("急勾配になったアスファルトの舗装路を先頭を切って歩いていた$anzuが振り返ると",
                "リボンを取り去ってボタンが胸元まで外されたそこに",
                "水泳部で日焼けした肌が見えていた"),
            nao.talk().t("勘違いしただけだって説明しただろう？"),
            nao.think().d("それは咄嗟の言い訳だったけれど",
                "事実$meはよく勘違いをする。",
                "$i_na_club", "この$i_clubが最初は正規の部活動だと思い込んだのもそれだった"),
            anzu.talk().t("分かってるよ。", "分かってる。",
                "もうこんな同好会のことはさっさと見捨てて解散してしまえばいいってことは分かってるよ"),
            nao.look().d("彼女は何度も振り返りながら$meたちが付いてきているのを確認し",
                "古い金網フェンスの扉を開けて",
                "雑草が生い茂る野道へと分け入って行く"),
            anzu.talk().t("でもずっと続いていた伝統を$meたちの代で消しちゃうなんてなんか悲しいじゃない？"),
            tamura.talk().t("けどさ"),
            nao.think().d("$tamuraは一度$meを見てから", "話に口を挟む"),
            tamura.talk().t("$meらがどうこうしたところで",
                "来年には部員ゼロになって廃部するのは確定事項なんだろ？",
                "だったら今してることって単なる自己満足ってやつじゃないのか？"),
            nao.think().d("よく言ってくれた",
                "という思いだったが",
                "それは彼女が立ち止まって腰に手を当てた姿を目にしたことで",
                "間違った選択肢だったのだと分かった"),
            anzu.talk().t("じゃあさ",
                "あんたたちは$meがただ自分がやりたいからって旧校舎跡地の現地調査をしようとしていると",
                "そう言いたいの？"),
            tamura.talk().t("そこまでは言ってないよ。", "なあ$nao"),
            nao.look().d("$tamuraは$meに助けを求めるように情けない視線を送ったが",
                "さっきの言葉じゃどう考えても$anzuは怒る。",
                "いつもそうだけれど",
                "$tamuraの言葉は少し乱暴だ"),
            nao.talk().t("何もこんな大切な時期にって話を",
                "$tamuraは言いたかったんだよ。", "なあ？"),
            nao.think().d("頼むから黙って頷いておいてくれ",
                "という祈りを込めてそうフォローしたが、"),
            tamura.talk().t("いや$meは時期とかじゃなくてこの取り組みそのものが無駄じゃないのかって話をだな"),
            nao.deal().d("更に油を注ぎそうな勢いだった$tamuraの口に手で蓋をして",
                "$meは必死に話題を逸した"),
            nao.talk().t("ところで本当にこの先に旧校舎が建っていたの？"),
            anzu.talk().t("$ln_teacher先生に古地図出してもらって確認したから間違いないはず"),
            nao.look().d("思い出すように見上げた後でそう言って$meと目線を合わせると",
                "彼女は再び先に立って歩き出す"),
            nao.look().d("その姿に$tamuraも$meと同じように安堵して小さな吐息を落としていたが",
                "目を合わせると$anzuの背を指差して「けどさ」と口を動かし始めたものだから",
                "首を横に振って苦笑するしかなかった"),
            )

def sc_oldlibmark(w: wd.World):
    nao, anzu, tamura = w.nao, w.anzu, w.tamura
    return w.scene("旧図書館跡",
            nao.look().d("野道に入って二百メートルほど進んだところで腰までの細い草が伸びているところに出た"),
            nao.ask().t("ここなの？"),
            anzu.talk().t("と思うんだけど"),
            nao.look().d("彼女は鞄から古地図を出して見ているが",
                "その脇を躊躇することなく$tamuraが歩いて行ってしまう"),
            tamura.talk().t("ほんと", "綺麗に野っ原だな"),
            nao.look().d("確かに$tamuraが言うように何もない。",
                "けれど不自然なほど綺麗に同じ草が生え揃っていて",
                "それの周囲を", "おそらく桜の木だと思うけれど",
                "それが四角く取り囲んでいる"),
            nao.talk().t("たぶん合ってる"),
            nao.move().d("だから$meはそう言って古地図を見返す$anzuの肩をちょんと叩いた"),
            anzu.talk().t("けど"),
            nao.talk().t("もう五年も前に校舎は取り壊されたんだよね？",
                "だったら何も残ってないどころか",
                "こんな風に自然に返っていても仕方ないんじゃない？"),
            nao.look().d("彼女が何を思って旧校舎跡を調査したいと言い出したのかは知らないけれど",
                "よく考えてみれば更地に戻した後で誰も使わないまま放置すれば草だらけになるのは当たり前だ"),
            anzu.talk().t("草とか生えてても家の庭くらいだと思ってた。",
                "ほんとはね",
                "何か学校が建ってた痕跡とか",
                "体育館脇のテニスコートとか",
                "プールの跡",
                "それに旧校舎脇にあったと云われている別館になっていた図書室のあった場所とかね",
                "そういうのが見てみたかったの"),
            nao.ask().t("ねえ。",
                "その別館になってた図書室って何？"),
            nao.think().d("普段だったらわざわざ彼女の発言に突っ込んで藪蛇になるようなことはしない"),
            anzu.talk().t("話してなかったっけ？"),
            nao.think().d("けれどその学校とは別の建物になっていたという図書室のことを",
                "別の場所で聞いて", "いや読んで知っていたのだ"),
            anzu.talk().t("$i_na_clubの前身が$i_oldclubだったって"),
            nao.talk().t("真夜中の……"),
            anzu.talk().t("あれ？",
                "やっぱり話したことあった？"),
            nao.behav().d("$meは首を横に振り", "$anzuに続けるよう促した"),
            anzu.talk().t("だからさ",
                "この$i_clubって三十年前に$i_oldclubとして作られたものなのよ。",
                "それも最初は部活動じゃなくて",
                "本好きな生徒たちが数名",
                "放課後に集まって本を読みながらお茶会をしていただけのものだったの。",
                "それを物好きな先生がどうせなら部活動にしなさいってことで",
                "本を読む同好会として発足したんだって"),
            nao.think().d("その話からは", "どうしてもあの本の内容を連想してしまう。",
                "あれはひょっとすると実話を元にして書かれた小説なのだろうか。",
                "もし仮に作者がこの町出身だったならその可能性だって考えられるし",
                "ひょっとすると同じ高校に通っていた先輩で$i_oldclubのメンバーだったということだって有り得る"),
            tamura.talk().t("おーい！",
                "あったぞ！"),
            nao.hear().d("何だろう。",
                    "$tamuraが小さくなって手を上げている"),
            anzu.talk().t("何よ？"),
            nao.move().d("草を掻き分けて歩いていく$anzuに続いて",
                    "$meも$tamuraの方に向かう。",
                    "足元が見えないことを恐がらない彼女の逞しさに少し羨ましさを覚えながらも",
                    "あの本の中の彼女とはやはり違うんだな", "と思ってしまう"),
            nao.move().d("百メートル以上は歩いたと思う"),
            tamura.talk().t("な、これ。",
                    "何かの建物の基礎部分だろ？"),
            nao.look().d("足元の草を一部だけ引っこ抜いて露出した地面には",
                    "古いコンクリートの長方形が埋まっていた。",
                    "ただそれは基礎というよりも建物の一部",
                    "それこそ床や入り口だったのではないかと$meには思えた"),
            anzu.talk().t("図面からするとちょうど図書室が建っていた場所だと思うんだけど"),
            nao.look().d("$anzuは古地図の中の小さな校舎とその脇の施設の位置関係を考えながら",
                    "何度も顔を上げては「たぶん」と繰り返す"),
            tamura.talk().t("じゃあここでその真夜中クラブ？　だかが誕生したって訳だな"),
            anzu.talk().t("$i_oldclubよ。",
                    "変な呼び方しないで"),
            tamura.talk().t("何ムキになってんだよ。",
                    "そもそも真夜中って付けるところからしてちょっと変だろ"),
            nao.think().d("言われてみれば確かにそうだ。",
                    "別に夜中に集会をしていた訳でもないだろうに",
                    "どうしてそんな名前にしたのだろう。",
                    "何か謂れでもあるんだろうか"),
            nao.look().d("そう思って$anzuを見たけれど",
                    "彼女もそこまでの事情は知らないようだった。",
                    "古地図を仕舞って代わりに細かな字がびっしりのノートを取り出して見ていたが",
                    "首を振ると「特に聞いてない」と苦笑した"),
            nao.deal().d("$meたちは他にも何か痕跡が残っているだろうかと草を掻き分けながら探してみたけれど",
                    "それ以外には基礎部分らしきコンクリ片すら見つけられなかった"),
            nao.think().d("無くなってしまうということはただ物が消えてしまうのではなく",
                    "こんな風にそこにあったという痕跡すら失われてしまうものなのだな",
                    "という感慨が自分の中に静かに広がった"),
            nao.be(w.stage.oldlib_mark),
            anzu.explain("旧校舎事情"),
            nao.think(w.i.oldschool_reason.flag()),
            )

def sc_herbook(w: wd.World):
    nao, akiko, mam, dad = w.nao, w.akiko, w.mam, w.dad
    return w.scene("彼女の同人誌",
            nao.think().d("結局あの後$anzuは学校の図書室で古い資料を探してみると言って別れ",
                "$tamuraの方はバスケ部の練習に顔出してくると別れ",
                "$meだけが何もすることもないまま先に家に帰った"),
            mam.talk().t("ちょっと$fn_nao。",
                "あんたこの当たり障りのない成績に何か言いたいことはないの？"),
            nao.look().d("通知表を母親に提出して小言めいた物言いをされながらも、"),
            nao.talk().t("悪くないなら別にいいんじゃないかな……"),
            nao.move().d("冷蔵庫に冷えていたラムネを手に",
                "さっさと二階の自室に引っ込んだ"),
            nao.come(w.stage.myroom),
            nao.behav().d("むっとした部屋の空気を追い出すように慌てて窓を開け",
                "扇風機を回す"),
            nao.deal().d("それからさっさと制服を脱いで半袖短パンに着替えると",
                "ラムネを開けて一口",
                "続いて本棚から『$i_booktitle1』を引き抜いてベッドに転がった"),
            nao.think().d("これも同じ真夜中という文字がタイトルに使われている。",
                "同じというのは$i_oldclubのことだ"),
            nao.think().d("物語のタイトルが似ているというだけで",
                "それが何だということもないのだけれど",
                "本の中にも図書室が出てくるし",
                "そこでは人間の代わりに本の霊だけれども部活動と同じようにお茶会を開いている"),
            nao.look().d("本は手作業で閉じられていて",
                "本の右側が和綴じのもののように綴じ紐でしっかりと留められている。",
                "一般流通している出版社から出されたものだと簡単な著者紹介が書かれていることも多いけれど",
                "表紙の右下に小さく作者名がある以外は",
                "この$fn_sayaという人物についての情報は一切書かれていなかった"),
            nao.think().d("名前からすると女性のように思えるし",
                "内容を読んでみても", "またその丁寧で繊細な言葉選びからも",
                "作者は女性なのだと$meには思えた"),
            nao.think().d("彼女が同じ高校の出身者であるなら$i_oldclubの存在を知っていたかも知れないし",
                "それを利用して小説を書いたということだって考えられる"),
            nao.look().d("参考書が平積みにしたまま置かれている勉強机の上のラムネの瓶はすっかり汗をかき",
                "もう半分しかソーダ水を残していない"),
            nao.think().d("二巻", "三巻と彼女の本を揃えていけば",
                "そこに何かしらヒントが隠されているだろうか"),
            nao.think().d("それともそんな面倒なことをせずに直接会う？"),
            nao.talk().t("いやいやそれは流石に無理だって"),
            nao.hear().d("思わず声に出してから",
                "残りのラムネを一気に飲み干す"),
            nao.feel().d("喉の痛みは現実の痛みだ"),
            nao.think().d("小さい頃から何かと夢見がちな妄想をしてきた自分は",
                "いつだってその思いを現実にはしてこなかった。",
                "だって現実なんて痛みを伴うことばかりだから"),
            nao.behav().d("ベッドの上で背中を丸めて屈み込む"),
            nao.think().d("来月分の小遣いはもう前借りして使ってしまっている"),
            nao.think().d("半年分を一気に貰うことは可能だろうか？"),
            nao.think().d("その想像をした途端",
                "頭の上には眉間に皺を寄せた母親の顔が浮かび上がった"),
            akiko.talk("その作家さん好きなんだ"),
            w.nao.think("全ての本を集める"),
            w.nao.deal("本を集める"),
            nao.think("金が足りない"),
                w.nao.deal("店が潰れるまでに収集しなきゃ"),
                w.nao.know(w.i.vanishshop),
                w.nao.deal("本を買い集める"),
                w.nao.know("金が足りない"),
            # XXX: target
            # TODO: 本屋でなく、家で本を読んで確認
            # TODO: 作家情報と本がここのみ
            )

def sc_findjob(w: wd.World):
    nao, mam = w.nao, w.mam
    return w.scene("仕事探し",
            nao.come(w.stage.dyning),
                w.nao.look("バイト探し"),
            nao.ask("仕事紹介", mam),
            mam.reply("聞いてみるけど"),
            nao.be(w.stage.myroom),
            nao.think("いくら掛かるか"),
            )

def sc_getjob(w: wd.World):
    nao, mam = w.nao, w.mam
    return w.scene("仕事は見つけたが",
            nao.be(w.stage.partfactory),
                w.nao.deal("働く"),
                w.nao.deal("金を貯める"),
            # TODO: 仕事内容
            # TODO: パートのおばちゃんたちの玩具
            nao.have("金を得る"),
            )

def sc_holdshop(w: wd.World):
    nao, akiko, sun = w.nao, w.akiko, w.akikosun
    return w.scene("店を閉める",
            nao.come(w.stage.bookshop),
                w.nao.know("閉店が早まる"),
            nao.meet(sun),
            akiko.talk("少し早くたたむことになって"),
            nao.ask("本は？"),
            akiko.talk("全部売れた"),
                w.nao.think("彼女に会いたい"),
                w.nao.know("全ては集められない"),
                w.nao.deal(w.akiko, "頼む"),
                w.nao.know(w.i.her_addr),
            )

def sc_gotoherhome(w: wd.World):
    nao = w.nao
    return w.scene("彼女の家に",
            nao.be(w.stage.bus),
            nao.think("彼女について"),
            nao.think("彼女が本を引き取った事情"),
            )

def sc_meether(w: wd.World):
    nao, saya = w.nao, w.saya
    return w.scene("彼女に出会う",
            nao.come(w.stage.herhome),
            w.nao.go(w.saya, "彼女に会う"),
            # TODO: 彼女の描写
                w.nao.go(w.saya),
                w.nao.know(w.i.her_addr),
                w.nao.meet(w.saya),
                w.nao.know(w.i.her_mind),
            )

def sc_getlastbook(w: wd.World):
    nao, saya = w.nao, w.saya
    return w.scene("最後の作品",
            # TODO: 彼女の部屋の描写
            nao.come(w.stage.herroom),
            nao.have("最後の本"),
            nao.know(w.i.oldschool_reason.deflag()),
            )

def sc_fanletter(w: wd.World):
    nao, saya = w.nao, w.saya
    return w.scene("ファンレター",
                w.nao.know(w.i.her_reason),
                w.nao.meet(w.saya),
                w.nao.ask(w.i.her_reason),
            )

def sc_confession(w: wd.World):
    nao, saya = w.nao, w.saya
    return w.scene("告白",
                w.nao.deal("想いを伝えた"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("本屋が無くなる町"),
            sc_myfavorite(w),
            sc_knownews(w),
            sc_checkclosed(w),
            )

def ep_buyout(w: wd.World):
    return (w.chaptertitle("買い占めなきゃ"),
            sc_lazyschool(w),
            sc_gotooldschool(w),
            sc_oldlibmark(w),
            sc_herbook(w),
            )

def ep_working(w: wd.World):
    return (w.chaptertitle("働く日々"),
            sc_findjob(w),
            sc_getjob(w),
            )

def ep_closedshop(w: wd.World):
    return (w.chaptertitle("閉店する"),
            sc_holdshop(w),
            sc_gotoherhome(w),
            )

def ep_lastbook(w: wd.World):
    return (w.chaptertitle("最後の本"),
            sc_meether(w),
            sc_getlastbook(w),
            )

def ep_remainheart(w: wd.World):
    return (w.chaptertitle("消えても残るもの"),
            sc_fanletter(w),
            sc_confession(w),
            )

# test data
def story_baseinfos(w: wd.World):
    return [
            ("story", story(w), w.nao, w.saya),
            ]

def story_outlines(w: wd.World):
    return [
            ("story", story(w),
                w.nao.think("全ての本を集める"),
                w.nao.know(w.i.vanishshop),
                w.nao.deal("本を集める"),
                w.nao.go(w.saya, "彼女に会う"),
                True),
            ("ep0", ep_intro(w),
                w.nao.think("彼女の本を全部そろえたい"),
                w.nao.think("人生を救われた"),
                w.nao.go(w.stage.bookshop),
                w.nao.know(w.i.vanishshop),
                True),
            ("ep1", ep_buyout(w),
                w.nao.deal("店が潰れるまでに収集しなきゃ"),
                w.nao.know(w.i.vanishshop),
                w.nao.deal("本を買い集める"),
                w.nao.know("金が足りない"),
                True),
            ("ep2", ep_working(w),
                w.nao.deal("働く"),
                w.nao.deal("金を貯める"),
                w.nao.look("バイト探し"),
                w.nao.have("金を得る"),
                True),
            ("ep3", ep_closedshop(w),
                w.nao.think("彼女に会いたい"),
                w.nao.know("全ては集められない"),
                w.nao.deal(w.akiko, "頼む"),
                w.nao.know(w.i.her_addr),
                True),
            ("ep4", ep_lastbook(w),
                w.nao.go(w.saya),
                w.nao.know(w.i.her_addr),
                w.nao.meet(w.saya),
                w.nao.know(w.i.her_mind),
                True),
            ("ep5", ep_remainheart(w),
                w.nao.know(w.i.her_reason),
                w.nao.meet(w.saya),
                w.nao.ask(w.i.her_reason),
                w.nao.deal("想いを伝えた"),
                True),
            ]

# main
def world():
    w = wd.World("Lost her book")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("彼女の本が、消えます"),
            ep_intro(w),
            ep_buyout(w),
            ep_working(w),
            ep_closedshop(w),
            ep_lastbook(w),
            ep_remainheart(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

