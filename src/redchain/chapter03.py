# -*- coding: utf-8 -*-
"""Chapter 03: the red-chain
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
def ep_idolyears(w: wd.World):
    ma, cafemas, manager, owner = w.masuda, w.cafemaster, w.manager, w.shopowner
    scenes = [
            w.scene("喫茶店にて",
                ma.be(w.stage.cafe).d("池袋の西口を出て狭い路地を抜けて行った先に",
                    "彼に指定された喫茶店はあった"),
                ma.look().d("ガラスが格子状に嵌ったドアを開けると鈍いドアベルが鳴り",
                    "エプロンをつけた体格の良い女性が「いらっしゃい」とよく通る声で迎えてくれる"),
                ma.talk().t("えっと待ち合わせで……"),
                ma.look().d("店内を見回す。",
                    "十ほどのテーブル席は半分程度埋まっていたが",
                    "どれも女性客ばかりで",
                    "カウンターの一番奥に座っている彼だけが男性だった"),
                ma.ask().t("$n_managerさんですか？"),
                manager.reply().t("そうだがあんたが何を知りたいか知らんが",
                    "もう$meからは$namehideのことは何も出てこんぞ"),
                ma.look().d("小刻みに右膝が揺れている。",
                    "白くなった頭髪の右の一部だけが黒く",
                    "首がぐっと下がった猫背で",
                    "濃い狐色のジャケットの襟元が汚れていた"),
                ma.do().d("彼の左隣りに座り", "とりあえず珈琲のブレンドを注文しようとすると、"),
                manager.talk().t("ここのは不味いからココアにしておきなさい"),
                ma.deal().d("そう言われたので仕方なく", "苦手な甘い飲み物を頼んだ"),
                ma.look().d("$na_managerは誰かを待っているのか何度も店の外側に視線を振っていたが",
                    "十五分程度という約束で",
                    "$n_hidekoについて話を聞かせてくれると言ってくれた"),
                manager.talk().t("それで$namehideの何を知りたいんだ？"),
                ma.look().d("七十は超えていると聞いていたが",
                    "皺と染みの多い肌や潰れたような声", "その落ち着きのない仕草からは",
                    "もっと歳がいっているように感じられる"),
                ma.talk().t("実は今回$n_hidekoさんについてうちで特集記事を書くことになりまして",
                    "それであなたが以前彼女が所属していた事務所の社長だったと聞いたので",
                    "謎の多い彼女のその人となりや",
                    "引退後も未だ多くの人の心に刻まれている$n_hidekoという女優について",
                    "忌憚ないご意見をお聞かせ願えればと"),
                ma.think().d("上滑りするような紋切り型の言葉だ。",
                    "けれどまだ確定していない事実を口にして",
                    "彼女が何故そんな場所で亡くなっていたのかの理由を探りたい",
                    "等とは口が避けても言うことは出来なかった"),
                manager.talk().t("何を勉強してきたのか知らないが$meにとって彼女",
                    "$n_hidekoというのは将来この日本を代表する女優になる逸材だと今でも思っているし",
                    "おそらく彼女に会ったことのあるこの業界の人間であればその名を決して忘れることはないと思うよ。",
                    "華もない器量も良い訳じゃない人が好い訳でもなくただ真面目であるというだけの人間が",
                    "役者という最高の仕事を得てスポットライトが当たるその一瞬だけは周囲の誰よりも輝きを見せる。",
                    "それはね彼女が運良く掴んだ初主演の映画$i_movienameで既に完成されていたと言える"),
                ma.look().d("$na_managerは先程までの貧乏ゆすりや落ち着かない視線を止め",
                    "まるで長い長い台本があるかのように$heroの方を一度たりとも見ずに話を続ける"),
                manager.talk().t("あの映画主演当時の彼女はまだ生娘だったよそれがだ",
                    "突如身籠ってしまった少女の驚きと悲哀と絶望から最終的には覚悟を決めて一人荒屋に篭って出産をしたという",
                    "常人では経験し得ないその物語を見事に演じ切りスクリーンにそれをリアルとして投影することに成功したんだ。",
                    "監督による特別な演技指導があった訳じゃないしベテラン俳優たちに助けを求めた訳でもない。",
                    "彼女の台本は撮影初日から既にボロボロで$meは新しいものを用意させようとしたくらいだったよ。",
                    "けれど彼女はそれを拒否してもうその拒否するところから既に役になりきっていた",
                    "いやあれは$i_movienameの$i_movieheroineそのものだったんだ"),
                ma.ask().t("役者として凄かったというのも真面目だったというのも",
                        "昔のお仲間さんたちから沢山聞かされましたよ。",
                        "ただ彼らはあまり$namehideの私生活については語らなかったんです。",
                        "当時", "公私ともに付き合いが深かったという$na_managerさんから見て",
                        "普段はどんな人だったんですか？"),
                ma.think().d("このままだと約束の十五分の大半を独演会に持って行かれてしまうと思い",
                        "何とか方向修正しようと口を挟む"),
                manager.talk().t("売れるようになるまでは確かに$meの家で一緒に暮らしていたよ。",
                        "そのことで当時かなり週刊誌には色々と書かれてね。",
                        "一体君等というのは売れれば何でもいいのか？",
                        "人権も彼女らの人生も何もかも踏み躙ってそれで儲けて嬉しいのかね？"),
                ma.talk().t("ごもっともな話だと思いますよ。",
                        "ただそれだけ買う人間がいるということは",
                        "やはり彼女たちについて何でも良いから知りたい",
                        "知った上で近づきたいという願望があるんじゃないでしょうか"),
                ma.look().d("咄嗟の思いつきだったが",
                        "$na_managerはその言葉に小さく頷いてから初めてしっかりと$heroの方に顔を向けた"),
                ma.talk().t("確かに適当なことを書いて儲けようという輩も当然います。",
                        "そんな人間はゴミだと自分も思いますよ。",
                        "けどそんな奴らよりはただ純粋に知りたくて取材をして記事を書いている",
                        "その記事によってそこにはこんな真実が眠っていたんだって知らしめたいと考える人間だって",
                        "同じかそれ以上にいると思うんですよ"),
                ma.think().d("どうして自分の口からそんな熱の入った言葉が出てくるのだろう"),
                ma.think().d("別に今更もう新聞記者に戻ろうなんて思っていないし",
                        "仕事も私生活も適当にしてなあなあで暮らしていって", "死んでいけばいいやと",
                        "その程度にしか考えていなかったはずなのに。",
                        "何だこれは"),
                ma.think().d("それでも$heroの言葉は止まらなかった"),
                ma.talk().t("だってですね",
                        "誰かが真実を書かないと他人は勝手にああだこうだ適当なことを喋って",
                        "恰もそれが本当のことだったみたいに彼らの記憶の中には埋没してしまうんですよ？",
                        "他人の人生に責任なんて持てないはずなのに",
                        "自分の人生にだって責任の一つも取れしない癖に",
                        "好き勝手で都合の良い醜聞に仕立てて酒の肴にされるんですよ？",
                        "それでもいいんですか？"),
                ma.hear().d("ざわついていたと思った店内が",
                        "いつの間にか静まり返っていた"),
                ma.look().d("二十代から五十代くらいまでの女性客全ての視線が自分に集まっていることに気づいて",
                        "$heroはわざとらしく咳払いをして膜の張ったココアに口を付ける"),
                manager.talk().t("……あんたも$n_hidekoにやられた人間なんだな。",
                        "これで安心して案内できるよ"),
                ma.look().d("$na_managerの言葉の意味は理解出来なかったが",
                        "彼は急に好々爺な笑みを浮かべるとカップの残りを飲み干して立ち上がる"),
                ma.ask().t("あの……"),
                manager.talk().t("店長。",
                        "彼の分も$meに付けといてね"),
                cafemas.talk().t("あいよ。",
                        "良かったねお兄さん。",
                        "この人気に入らないと奢ったりしないんだよ"),
                ma.reply().t("はあ"),
                ma.think().d("どこがどうなって$na_managerの心を掴めたのか分からないが",
                        "席を離れて入り口の方に向かった彼を見て",
                        "$heroも慌てて残りを飲み干すと",
                        "慌ただしく鞄を手にして店を出て行った"),
                ),
            w.scene("アイドル時代のこと",
                ma.look("アイドル時代の資料を持っている人とやり取り"),
                ma.come().d("連れて来られたのは十分ほど歩いたところに並ぶ五階建て雑居ビルの一つだった"),
                ma.ask().t("あの", "ここは？"),
                ma.look().d("エレベータは無く",
                    "階段を登って四階まで行くと",
                    "暗くなっている磨りガラスのドアを開けて中に入り",
                    "$na_managerは電気を点けた"),
                manager.talk().t("ここがね$meの今のオフィスなの"),
                ma.look().d("そこはパーテーションで区切られた二十平米ほどの空間の片側に",
                    "事務机が四つとプリンタやＦＡＸや書類棚が並べられているだけの",
                    "$heroの会社とそう大差ないように見える代物だった"),
                ma.look().d("辛うじて芸能事務所らしさを感じさせるアイドルや映画のポスターが壁に貼られている程度で",
                    "事務員すらいなくて何とも物悲しい。",
                    "聞いていた話では$n_hidekoが所属していた頃には都内の一等地に持ちビルがあったというから",
                    "その頃を知る人間がいたらあまりの落差にそっとドアを閉じて階段を駆け下りて行ってしまうことだろう"),
                manager.talk().t("驚いたかい？",
                    "でも世の中というのはこんなものだよ。",
                    "良い時だけ見るから何だかとても日常とはかけ離れたきらびやかな世界に思われることが多いけれど現実なんてみんな風呂すらまともに入れずに",
                    "水道で背中を流してご飯の上にはフリカケでもあればご馳走だなんて笑って話し合うような人間の集まりなんだよ"),
                ma.think().d("そう笑って話す$na_managerはパソコンの電源を入れると",
                    "インスタントコーヒーの粉を自分のカップに適当に振り落として", "ポットのお湯を注ぐ"),
                manager.talk().t("その日を生きるにも大変な思いをしながらどうしてみんな舞台をやったり映画やドラマに出ようと躍起になってるか分かるかい？"),
                ma.look().d("ティースプーンで適当に掻き回し",
                    "まだ湯気を上げるそれを一口飲みながら彼は$heroを見る。",
                    "どうやら一人で思いの丈を語ることはもう止めにしたらしい"),
                ma.reply().t("夢だから", "ですか？"),
                ma.think().d("なんてありきたりな答えなんだと思いながらも",
                    "それ以外の言葉は$heroには見つけられない"),
                manager.talk().t("夢だなんて綺麗な言葉じゃ現実が隠れちゃうよ。",
                    "だから挨拶に来て「わたしの夢なんです」とか言う奴がいたら$meはこう言い直させることにしているんだ。",
                    "それは夢じゃない。",
                    "自分は有名になってみんなに認めてもらいたいんです。",
                    "ここにいて自分はいいんだ。",
                    "スポットライトを浴びてみんなが今の自分を愛してくれているんだ。",
                    "ただそれが欲しいからがんばります……ってね"),
                ma.think().d("先程まで年寄りの皺塗れの目をしていると思っていたそれは",
                    "子供のような輝きで$heroへと向けられていた"),
                manager.talk().t("何も芸能の仕事だけじゃないよあんただってそうだ。",
                    "どんなに耳障りの良い口実を言ってみたところでその本質は自分を認めて欲しいっていうただそれだけの単純な動機なんだよ。",
                    "それぞれにその実現方法が違うだけで誰しもが最初に誰かに認めてもらったという原体験の再現を目指しているだけなんだ"),
                ma.think().d("自分の認められた原体験は", "一体何だったろうかと$heroは考える"),
                ma.think().d("$n_hidekoにとってのそれは何だったのだろうかとも", "考える"),
                ma.think().d("もし誰にも認められたことがなかったとしたら",
                    "それは不幸な人生なのだろうか"),
                ma.look().d("$na_managerは自分の席に座ると",
                    "パソコンで作業を始めた"),
                ma.talk().t("あの", "一つ訊いてもいいですか？"),
                manager.talk().t("どうぞ。",
                    "$meで答えられることなら"),
                ma.ask().t("$n_hidekoはあなたが見つけて事務所に引き抜いたと教わったんですが",
                        "彼女は元々何をしている人だったんですか？"),
                ma.think().d("器用にマウスを動かしながら$na_managerは先程までの熱量を全く感じさせない淡々とした口調でこう返した"),
                manager.talk().t("なんだ知らないのかい。",
                        "彼女はね元アイドルだよ。",
                        "若い人は聞いたことないかな。",
                        "$i_idolnameっていうグループの$n_h_idolとしてそれなりに人気もあったんだよ"),
                ),
            w.scene("元マネージャー",
                ma.look().d("既に辺りは看板の電飾がよく目立つ時間帯に変わっていた"),
                ma.come().d("$na_managerに連絡を取ってもらい",
                    "当時のアイドルグループのマネージャーをやっていたという男に会いにやってきたのだが",
                    "神田の駅の裏手をずっと歩いても一向にそれらしきビデオ店は見つからなかった"),
                ma.ask().t("あの、すみません"),
                ma.deal().d("仕方なくスーツ姿の男性に店の名前を出して場所を聞いてみる"),
                w.man1.talk().t("それってさレンタルビデオじゃなくて",
                    "ああいうのだよ"),
                ma.look().d("男が指した方角を見ると赤と黄色の派手な看板に『個室ビデオ』と書かれていて",
                    "$heroは思わずその男性に頭を下げた"),
                ma.go().d("すれ違うには互いが体を傾けなければならないような狭い階段を登っていくと",
                    "赤玉屋という屋号が書かれたドアが現れる。",
                    "そっとそれを開けて中に入ったが",
                    "狭い通路とその壁に沢山の女性のポスターが貼られているのがまず目に付いた。",
                    "個室防音完備とあるが",
                    "ＶＲというのは何だろう"),
                ma.deal().d("応対する店員は$heroと視線を合わせないまま呪文のようにぶつぶつと早口で注意点やメニューを呟いた後で",
                    "どの個室を利用するのか尋ねてきた"),
                ma.talk().t("あ、えっと$me",
                    "オーナーの$na_shopownerさんに用があって。",
                    "取り次いでもらえますかね？"),
                ma.look().d("店員の男性は一瞬睨むように$heroを見たが",
                    "「少々お待ち下さい」と口走ると暖簾を潜って奥の部屋に行き",
                    "電話だろうか", "ぼそぼそとした話し声を響かせた"),
                ma.deal().d("暫くして戻ってきた店員から店の裏手に行くように言われる。",
                    "別の場所を管理室として借りていると説明された"),
                ma.go().d("再び狭い階段を降り", "建物の裏手に回る。",
                    "ビルとビルの間に入るようにして行くと", "何も書かれていないドアが突然現れた"),
                ma.deal().d("それに手を掛けようとすると", "ドアノブが勝手に回り",
                    "金属音の悲鳴を上げながらゆっくり開く"),
                ma.look().d("そこにはドアから無事に出られるのだろうかと心配になるような横幅のしっかりした革ジャンの男性が",
                    "たっぷりの無精髭を掻きながら出現した"),
                owner.talk().t("あんた$na_managerさん紹介の人？"),
                ma.reply().t("はいそうです。",
                    "$st_officeの$na_masudaと言います"),
                ma.deal().d("慌てて名刺を差し出したが、"),
                owner.talk().t("もうそういうのはいいんだわ"),
                ma.look().d("男はそう言って受け取らずに手で押し返した"),
                ma.talk().t("えっと$na_managerさんから$n_hidekoのアイドル時代のマネージャーだったと聞いたのですけれど"),
                ma.look().d("名刺を胸ポケットに仕舞いながら尋ねたが",
                    "彼は小首を傾げてしばらく考え込んでから",
                    "別の名前を口にする"),
                owner.ask().t("それって$n_h_idolのことだよね？",
                    "$i_idolnameの"),
                ma.think().d("ここで押し問答するのも面倒だったので",
                    "「そうです」と頷き", "中に入れてもらった"),
                ma.look().d("中は十畳ほどの空間で",
                    "そのうちの半分は畳が敷かれて一段高くなっており",
                    "壁際に仮眠用だと思われる布団が追いやられていた"),
                ma.move().d("その畳敷きの方に上がるよう言われ",
                        "隅の黒くなったスニーカーを脱ぐ"),
                ma.talk().t("こういう店を利用したことないんですけど",
                        "その",
                        "結構お客さんて多い方なんですかね"),
                ma.behav().d("会話の緒が掴めないまま$heroは胡座で$na_shopownerの対面に坐った"),
                owner.talk().t("防音効いてるし",
                        "泊まったりもできるからね。",
                        "漫画喫茶とそう変わらないよ"),
                ma.look().d("彼は$heroの方を見ずに答えると",
                        "テレビのリモコンを操作してバラエティ番組に切り替える。",
                        "画面からは間断なく作られた笑い声が流れてきて不快だったが",
                        "$na_shopownerは分厚い唇を歪ませてへらへらと声を出さずに笑っていた"),
                ma.ask().t("それでお尋ねしたいのは$n_hidekoのアイドル時代についてなんですが"),
                ma.think().d("まただった"),
                ma.look().d("彼女のことを$n_hidekoと呼んだ途端に表情が険しくなる"),
                owner.talk().t("そんな名前の女は知らない。",
                        "$meが知ってるのはね",
                        "$i_idolnameで活躍していた$n_h_idolだけだよ"),
                ma.look().d("素手で袋に手を突っ込み", "掴んだポテチを口に放り込んでバリバリと音をさせる。",
                        "テレビに合わせて鼻息を出すように笑い", "またポテチを食べる"),
                ma.look().d("$na_managerから聞かされた人柄とは随分違っていた。",
                        "当時アイドルたちをサポートするのに必死だった青年は",
                        "一体どういう経緯で今個室ビデオ店のオーナーなんてやっているのだろう"),
                ma.think().d("暫く待ってみたが何も話し出してくれる様子がないので",
                        "資料には全然なかったそのアイドル時代の$n_hidekoについて尋ねてみる"),
                ma.ask().t("その$n_h_idolさんですが",
                        "グループの中でも人気があった方なんですか？"),
                owner.talk().t("そんなことも調べないで来たの？",
                        "まあ三人の中では断トツだったよ。",
                        "そもそもね",
                        "他の二人には悪いけど彼女一人だけ素質が違ったよ。",
                        "何よりその姿勢。",
                        "お客様に対する態度。",
                        "そしてこれが一番大切なことだといつも言い聞かせていたんだけど",
                        "普通の人間の女の子じゃ駄目だってこと。",
                        "$beniはね",
                        "触れると消えてしまいそうな儚さを持った妖精のようなアイドルだったよ。",
                        "それがどうして女優なんてつまらないものに……"),
                ma.hear().d("小さな舌打ちだった"),
                ma.look().d("それを聞いた時に彼が$n_hidekoではなく$n_h_idolという名前に拘りを持っている理由の欠片が掴めたような気がした"),
                ma.think().d("名前というものは彼女たちにとって自分そのものなのだろう。",
                        "顔や出演した作品に番組", "出した曲や立った舞台",
                        "実際にイベントやライブで対面したお客さんたちとの関係性も大事だが",
                        "大多数の人間にとっては彼女というのは$n_hidekoであり$n_h_idolなのだ。",
                        "それは今でも$n_shopownerの中で彼女というのは$n_h_idolであるように",
                        "$n_managerや$n_coworkerにとっては$n_hidekoなのだろう"),
                ma.ask().t("その$n_h_idolさんはあなたが見つけられたんですか？"),
                ma.look().d("そう質問した時に初めて彼の目が一度だけだったが", "$heroに向けられた"),
                owner.talk().t("そうだよ。",
                        "地味な黒い制服姿で一人だけ街に埋もれるようにして立っていたんだ。",
                        "当時はまだ中学生だった。",
                        "何をしているのかと声を掛けたら",
                        "彼女は真剣な表情でこう言ったんだ"),
                w.h_idol.talk().d("$myは何もできません"),
                owner.talk().t("最初は何か勘違いされたんだろうと思って",
                        "自分はそういう人間じゃなくてアイドルのスカウトをしているけれど",
                        "君みたいな子が一人でぶらついているのは危険だから声を掛けたと言ったんだ。",
                        "そしたら彼女", "急に頭を下げてね",
                        "こう言うんだよ"),
                w.h_idol.talk().d("$myを何者かにして下さい"),
                owner.talk().t("この子は一体何なんだろうって",
                        "ちょっと言うとアレだけれど",
                        "心を病んだ子なんじゃないだろうかって勘繰った。",
                        "とにかく危ない気がして",
                        "それでつい事務所に連れて帰ったんだ"),
                ma.look().d("アイドルとしての$n_hidekoを語る姿は",
                        "先程までとは別人だった。",
                        "出会いのきっかけから家庭の事情を聞いた上での事務所通いの了承",
                        "そしてグループとしてデビューさせるまでの苦労と彼女の努力。",
                        "そういったものを話す内にテレビのバラエティ番組は終わり",
                        "ベテラン女優の秘話をドキュメンタィ風に扱う番組へと内容が切り替わっていた"),
                ma.ask().t("母子家庭で",
                        "妹さんが一人いらしたんですか？"),
                owner.talk().t("ああ、そうだよ。",
                        "実際に一度も彼女の家族には会っていない。",
                        "書類も全部彼女から手渡されたから",
                        "ひょっとしたら全てが作り話で判子とかも勝手に使ったのかも知れない",
                        "なんて当時は考えたりもしたよ。",
                        "けど結果的に問題になったのはグループを組んだ他二人の方で",
                        "$n_h_idolの家族は電話すらしてきたことはなかったね"),
                ma.think().d("家族についての記述は集めたどの資料にも載っていなかったから",
                        "今初めて母子家庭だったことを知った。",
                        "それに加えてあまり家族仲も良くなかったようで",
                        "連絡先も一切分からないと言われた"),
                owner.talk().t("今でも時々考えるよ。",
                        "彼女がどうしてアイドルを辞めて女優を選んだのかってね。",
                        "だってその時の彼女にはソロデビューの話まで来てて",
                        "アイドル映画だったけれど主演ドラマの企画も持ち上がっていたんだ。",
                        "それを全て蹴ってまで女優を選んだ理由を",
                        "今でも聞き出したいって思っているよ。",
                        "$na_managerさんからは何も聞いてないんだよね？"),
                ma.reply().t("ええ。そんな話は一切ありませんでしたから"),
                ma.think().d("そこまで話し終えると",
                        "$heroは$na_managerに訊けなかったことを口にしてみた"),
                ma.ask().t("ところで今からニ十年前",
                        "どうして彼女が突然芸能界を引退したのか。",
                        "その件について何かご存知ではないですか？"),
                owner.talk().t("それこそ$na_managerさんから訊いたんじゃないの？"),
                ma.reply().t("自分の所為じゃない。",
                        "これだけしか教えてもらえませんでしたよ。",
                        "何か事務所とトラブルがあったとかなんですか？"),
                ma.look().d("$na_shopownerは一瞬表情を曇らせたが",
                        "それを振り払うように頭を横に振り",
                        "一つだけ教えてくれた"),
                owner.talk().t("あくまで噂話の一つだと思って聞いて欲しいんだが",
                        "彼女",
                        "不倫相手の子を身籠ったんだ。",
                        "それもある大物俳優の子だって話で",
                        "中絶を迫られて色々事務所も含めてゴタゴタがあったとか。",
                        "本当に週刊誌レベルのネタだが",
                        "当時この界隈じゃかなり信憑性が高いネタとして誰も表立っては口にしなかったんだ"),
                ma.think().d("仮にそれが事実だったとすれば",
                        "$n_hidekoはあの映画の女性と同じようにシングルマザーとして自分の子を育てながら生きた",
                        "ということだろうか"),
                ma.think().d("だとしても",
                        "どういう経緯であの町に流れ着いたのか",
                        "そして何故空き家で亡くなったのかについての疑問は何も解消されない"),
                ma.think().d("その大物俳優の名は教えてもらえなかったが",
                        "ただで一晩泊まらせてくれるというので",
                        "$heroは個室ビデオの部屋の一つで夜を明かした"),
                ma.look().d("準備されていたＤＶＤの中には$n_hidekoの出演作なんて当然無く",
                        "何となく写真から想像した$n_hidekoに似た女優のアダルトな作品を借りて",
                        "彼女の人生を想像しながら眠りに就いた"),
                ma.look().d("眠る前にメールを確認したが",
                        "$n_tanabeからは何の言葉もなく",
                        "$n_mikiにもう一日東京で調べる旨を送っておいた。",
                        "すぐに返ってきたメールに驚きながらも許可は既に$n_tanabeから貰ってあると書かれていて",
                        "相変わらずの卒の無さに彼女のような女性が伴侶だったらという妄想が湧き上がったが",
                        "場所が場所だけに何だか不埒なものになりそうだと",
                        "すぐにかき消して瞼を閉じた"),
                ma.know(w.h_idol),
                ma.look(w.h_idol, w.i.life),
                ma.come(w.stage.idoloffice, w.day.interview2),
                ma.deal(w.i.interview, "当時を知る人"),
                w.manager.talk(w.h_idol),
                w.manager.talk("辞めてからも付き合いがあった"),
                w.manager.talk("事情があって芸能界引退"),
                ma.know(w.i.retire_business),
                ),
            ]
    return [w.chaptertitle("アイドル時代"),
            *scenes,
            ]



# main
def story(w: wd.World):
    return ep_idolyears(w)


def main(): # pragma: no cover
    from src.redchain.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

