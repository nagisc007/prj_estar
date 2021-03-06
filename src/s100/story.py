# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.s100 import config as cnf
THM = cnf.THEMES


# episodes
def ep_intro(w: wd.World):
    h, osaki, fuyumi, ft_fuyumi = w.hero, w.osaki, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("追い詰められた作家の苦悩",
                w.tag.comment("主人公の人間性紹介と彼女との状況設定"),
                w.tag.comment("主人公の一人称"),
                h.do("write", THM["41"]).d("書く",
                    "という行為は時に悲鳴にも似た狂気を孕んでいる",
                    "と$meなんかは思う"),
                h.talk().t("あぁもう！",
                    "何だよお題『１００』で小説一本書けってのはよお"),
                h.be(w.stage.apart, w.day.current).d("視界を思い切りパソコンのモニタから天井",
                    "そして狭苦しいアパートの玄関へと移動させると",
                    "スチール製のドアが申し訳なさそうに開くのを目撃した"),
                h.deal(fuyumi, "普段メールよこさない彼女から", THM["2"]).t("……ごめん"),
                h.look().d("聞き取れないほどの声でそう言って入ってきたのは",
                    "同棲してこの春で三年目になる$fuyumiだった"),
                h.talk().t("何か忘れ物か？",
                    "それともまた仕事嫌になったから戻ってきたのか"),
                h.look().d("義姉のスナックの手伝いに散々嫌気が差しているらしいが",
                    "それでも生活資金の為と日々苦手な化粧をしては出かけていく。",
                    "そんな彼女の背を見送る度に自分の不甲斐なさに泣きたくなるが",
                    "いつかは立派な作家先生として店で一番高い酒を頼んでやるつもりだ"),
                fuyumi.come().d("彼女は何も言わないままドアを閉めると",
                    "そのまま上がってきてコートを脱いだ"),
                h.do("phone", w.osaki, "原稿締め切り", w.stage.indream).d("ちょうどそのタイミングで携帯電話が鳴り出す"),
                h.do("wake", "メール着信音").t("あ、はい", "もしもし$myです"),
                h.think().d("相手は編集の$na_osakiだった。",
                    "内容は案の定原稿の締め切りの話で",
                    "パソコンの画面にはまだ一行しか書けていなかったが",
                    "百枚の原稿の既に半分は終わっていると上手く誤魔化しておいた"),
                h.reply().t("はいはい", "大丈夫ですって",
                    "$meのこと信用してないんですか？"),
                h.think().d("そりゃあ何度も原稿を落としたことのある底辺作家を信頼なぞ出来ないだろう"),
                h.talk().t("え？",
                    "あの$na_nishikawaですか？",
                    "彼が直川賞候補に……そうですか"),
                h.do("返信しない").d("$nishikawaは同じ新人賞出身の作家だったが",
                    "今やＴＶにも顔出しをする人気作家になってしまった"),
                h.deal(THM["23"]).d("プレッシャーを掛けるつもりだったのだろうが",
                    "既に比べ物にならないだけに",
                    "悔しさよりもただ気落ちさせただけだということを伝える気力すらないまま",
                    "$meは$na_osakiからの電話を切った"),
                fuyumi.talk().t("$hero……"),
                h.ask().t("何だよ$her"),
                h.look().d("彼女は真っ赤な唇にお化けのようなアイシャドウでじっと見下ろしたまま",
                    "手にしたスマートフォンをただ差し出す"),
                h.talk().t("それがどうかしたのか？"),
                h.look("押入れの中から"),
                h.look(w.terminal, THM["3"]).d("だがよく見れば彼女のスマホにしては何ともゴテゴテとデコレーションされている。",
                    "おまけに画面が虹色に閃いたかと思うと、"),
                h.talk().t("あん！？"),
                h.hear("再度着信音").d("それは女の泣き声のような音をかき鳴らした"),
                h.have(w.terminal),
                h.deal(w.fear_mail, THM["1"]).d("見ればどうやらメールが着信しただけらしいが、"),
                h.ask().t("なあ$her。",
                        "これって誰のだ？"),
                h.do("write", "$must").d("そこには差出人が空白のまま、"),
                h.look(THM["100"]).t("百個のお題全てを使って小説を書かなければ大切なものを失う"),
                h.do("write", w.i.novel).d("と書かれていた"),
                fuyumi.talk().t("だから作家になるなんて夢さっさと捨てれば良かったのよ！"),
                h.reply().t("ふ、$her？"),
                h.look(ft_fuyumi, "冷たく豹変", THM["4"]).d("突然声を上げた彼女は一つに括っていた髪を解いてこちらを向くと",
                        "般若の面のモデルにでもなったかのように目を剥き出しにして",
                        "こう言った"),
                fuyumi.talk().t("それね",
                        "底辺作家に届く呪いのメールなんだよ！",
                        "実際に店に来てた先生がそれ貰ったって笑ってた次の日から全然来なくなって",
                        "そしたら一月後に心筋梗塞で亡くなってたんだから……"),
                ),
            w.scene("未来人の隣人",
                h.hear("インタフォン"),
                h.look(fuyumi),
                h.ask(fuyumi, "ごめんまだメール見てない"),
                ft_fuyumi.talk("何のこと？"),
                ft_fuyumi.ask("中に入れてくれない？"),
                ),
            ]
    return [w.chaptertitle("冒頭"),
            *scenes,
            ]


def ep_middle(w: wd.World):
    h, fuyumi, ft_fuyumi = w.hero, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("もう一人の冬美",
                w.combine(
                    h.remember().d("その語気がヒステリックにどんどん荒く強くなるのを聞きながら、"),
                    h.remember(fuyumi, "隣に越してきた", THM["8"]).d("彼女が隣に越してきた日のことを$meは思い出していた"),
                    ),
                w.tag.symbol("◆"),
                fuyumi.ask().t("今朝からずっと気になっているんですけど……ひょっとして$meのストーカーさんですか？"),
                h.talk().t("失礼ですが初対面です。",
                    "一体どうして$meをストーカーなんかだと？"),
                fuyumi.talk().t("だって朝からずっと君を好きだとか満月のようだとか夜の街でも輝く宝石とか",
                    "必死に口説こうとされていたから……"),
                h.think().d("それは自分が書いていた小説の中の情けないが憎めない",
                    "とにかく女にだらしない男の台詞だった"),
                fuyumi.talk().t("え？　そうだったんですか。",
                    "あ、やだ。$meだったら完全に恥ずかしい人じゃないですか"),
                h.look(THM["57"]).d("そう言って口元を両手で覆った彼女の",
                    "拳の上で覗いていた目がリスのように見えて",
                    "恋を始めるのに充分な事情となった"),
                h.think("自分にはもったいない完璧", "ちぐはぐなカップル", THM["26"]).d("彼女",
                    "$fuyumiはこんな風に早とちりな部分や天然ボケなところがあったけれど",
                    "料理や洗濯といった生活能力は非常に高くて",
                    "小粒な目になだらかな卵型の顔こそ美人とは呼べなかったが",
                    "$meにはもったいないくらいの素晴らしい女性だった"),
                h.think().d("当時も$meの編集だった$na_osakiに話すと",
                    "食べ物の好みから経済観念まで正反対なのによく一緒に暮らせるな",
                    "と驚かれたものだ"),
                h.look(ft_fuyumi, THM["71"]).d("それでも始まってしまった同棲生活は",
                    "ささやかながら幸せの意味を$meに教えてくれるのに充分な甘さがあった"),
                ft_fuyumi.talk("相談").d("だがそんな甘い暮らしは長くは続かないものだ"),
                h.know(ft_fuyumi, w.ichioku, THM["7"]).d("ある日$herは重そうな革のバッグを持って帰ってきた。",
                    "中には古い紙幣で一億円が詰め込まれていて",
                    "それを彼女は「もらった」と言う"),
                h.deal().d("相手は全然知らない男性で",
                    "とにかく世界平和に役立ててくれという訳の分からないことを言って押し付けられたと言うが",
                    "どうせ何か怪しい金に違いない。",
                    "そう思ったから警察に電話しようとしたのだが",
                    "何故か彼女はそれを承諾しない"),
                h.remember(fuyumi, "強欲", THM["9"], THM["11"]).d("彼女が「このまま自分たちで使おう」と言った時から",
                    "全ては始まっていたのかも知れない"),
                h.know(ft_fuyumi, w.i.future_mail),
                ),
            w.scene("現在の自分は",
                h.have("コーヒーと煙草", THM["20"]).d("ひとまずインスタントだがコーヒーを淹れて",
                    "煙草に火を点けた。",
                    "漂う紫煙に$fuyumiは顔を顰めながらも「どうするの？」と溜息を零す"),
                h.talk().t("書けばいいんじゃないのか？"),
                fuyumi.reply().t("え？　それ本気で言ってるの？"),
                h.think().d("彼女は$meにそんな能力はないと考えているのだろうが",
                    "話にならない企画書を九十九個も作って提出してきたという経歴は",
                    "無駄な自信になっていた"),
                h.talk().t("ゼロから作るよりも何かしらお題があった方がずっと楽だよ"),
                fuyumi.ask().t("けど百個もあるのよ？",
                    "単なる罰ゲームだって亡くなった作家さんも言ってたのに"),
                h.think().d("不可能かも知れない"),
                h.remember("当時は言えなかった秘密の趣味＝妄想小説", THM["61"], THM["21"]).d("それでも学生当時",
                    "仲間も友達もなく",
                    "ただ一人ノートの片隅に書き散らしていた物語の断片たちは",
                    "今や趣味や将来の夢ではなく仕事になっている"),
                h.talk().t("自信がないなら作家なんて続けていないよ"),
                h.look().d("コーヒーを口にしながら答えたが",
                    "カップの端から覗き見た彼女の表情は固いままだ"),
                h.talk(THM["89"]).t("何だよ？",
                    "$meがまだまともに一冊の本も出せていないことがそんなに不満か？"),
                fuyumi.reply().t("いつもそうやって無駄に自信ある振りだけしていれば誤魔化せるなんて考えてるから",
                    "$meたちこんなことになってるって気づかないの？"),
                h.look().d("見れば$herの目元がいつの間にか化粧が崩れている"),
                fuyumi.talk(THM["46"]).t("ごめんなさい"),
                h.look().d("彼女はそれだけ言うとかつて一億円が入っていた空っぽの鞄に自分の荷物を詰め込み始める"),
                h.talk().t("おい", "何だよ。",
                    "大丈夫だって",
                    "な？",
                    "こんなどこの誰が仕掛けたか分からない悪戯",
                    "本当に信じてるのか？"),
                fuyumi.talk().t("信じてるとか信じてないとか",
                    "もうそういう話じゃないって気づかないの？"),
                h.think("あの頃のキラキラがない", THM["22"]).d("振り返った彼女の瞳には",
                    "愛を交換し合った日々に灯っていた煌めきはすっかり失われているのだと",
                    "手遅れながら今やっと気づく"),
                h.talk().t("なあ",
                    "$meたちまだやり直せるよな？"),
                h.think().d("なんて定番の台詞しか吐き出せないんだ"),
                h.look().d("彼女はもう何も言い返さずに淡々と詰物を終わらせると",
                    "羽織ったコートの襟を立て",
                    "夏が苦手だという彼女の為に$na_osakiからお年玉だと貰った商品券で買ってやった",
                    "大きなプリムの白い帽子を目深に被る"),
                h.talk().t("なあ……"),
                h.look().d("けれど$meの呼び止めようとする声に力はなく",
                    "黙って出て行った彼女が閉めたドアの金属音だけが冷たく響いた"),
                h.have(w.nishikawa, "著作"),
                ),
            w.scene("未来からの警告",
                h.be(w.stage.apart, w.day.current),
                h.think(w.i.future_mail),
                h.have(fuyumi, w.i.fuyumi_call),
                h.talk(fuyumi, "別離"),
                h.talk("説得", fuyumi),
                h.look(fuyumi, "自分の小説", "彼女に自分の才能を示す"),
                h.hear().d("呆然として膝を突いた$meを",
                    "再び悲鳴のような着信が襲った"),
                h.talk().t("んだよ！"),
                h.have(w.i.help_mail, "助けて", THM["24"]).d("見ればまたメールだ。",
                    "それも「タスケテ」とだけ書かれている"),
                h.look("未来の自分からだった", THM["15"], THM["12"]).d("だがその液晶画面を注意深く見てみれば",
                    "それは一年後の彼女",
                    "つまり$fuyumiから送られたものだった"),
                ),
            ]
    return [w.chaptertitle("展開"),
            *scenes,
            ]


def ep_climax(w: wd.World):
    h, fuyumi, ft_fuyumi = w.hero, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("未来からの指示",
                h.talk(w.day.current, THM["27"]).t("嘘……だろ？"),
                h.look().d("けれど続け様にメールが着信する。",
                    "そこには短い文章ばかりで構成された指示が書かれていて",
                    "最後には、"),
                fuyumi.talk(THM["39"]).t("疲れた……もう嫌……"),
                h.look(THM["60"]).d("そう呟いた彼女がビルの屋上から落ちていく動画が添付されていた"),
                h.do("help", fuyumi),
                h.know("dead", fuyumi),
                ),
            w.scene("外出",
                h.talk().t("何なんだよ！"),
                h.go().d("上着も手に取らずそのおかしな端末だけ持って靴を履いた"),
                h.go(w.stage.subway, THM["51"]).d("ドアを押しのけて飛び出ると",
                    "一目散に最寄りの地下鉄の駅を目指して走る"),
                h.go().d("日曜日だからか道は混み合っていて",
                    "何度も「すみません」と頭を下げながら",
                    "人を掻き分けて地下へと滑り込んだ").omit(),
                h.talk().t("ま、待ってくれ！"),
                h.go().d("閉まりそうなドアを押しのけて電車に乗り込み",
                    "それから次の指示を確認する"),
                h.talk(THM["52"]).t("は？",
                    "海が付く駅って何だよ？",
                    "お台場か葛西臨海公園？"),
                h.think().d("他にも青海があるか。",
                    "ただそんなに遠くまで移動させるとは思えない"),
                h.remember().d("そうだ。",
                    "葛西臨海公園……"),
                h.think().d("あれは彼女との初めてのデートだ"),
                h.think().d("$meは途中で京葉線に乗り換えて公園に向かうことに決めた"),
                h.go(w.stage.school),
                ),
            w.scene("望んでいた過去",
                fuyumi.ask(THM["53"]).t("$heroは学生時代",
                    "途中まで登校しているんだけど突然行きたくなくなって本屋とかに立ち寄る",
                    "みたいなことなかった？"),
                h.think().d("そんなことを突然言い出して",
                    "彼女は葛西臨海公園で途中下車した"),
                h.go().d("あれほど楽しみにしていたネズミの国を諦めた理由を教えないまま",
                    "ベンチに座って彼女は自分の学生時代の思い出話を始めた"),
                fuyumi.talk("文化祭", THM["54"], THM["55"], THM["10"]).t("高校の秋の文化祭でね",
                    "それぞれ班を分けて展示物を製作していたの。",
                    "その頃はまだ今ほどＳＮＳなんて流行ってなくて",
                    "自分が周りから何て思われていたか全然知らなくて"),
                h.think().d("彼女が自分の過去について語るのは",
                    "この時が初めてだった。",
                    "だから$meはただ相槌を返しながら",
                    "話したいだけいつまでも付き合おうと心に決めていた"),
                fuyumi.talk("学生時代のアルバム", THM["79"], THM["56"]).t("この前ね",
                    "その文化祭の時のアルバムが出てきたの。",
                    "そしたらそこに知らない間に落書きされててね",
                    "虐めで転校していったという噂の子の名前で",
                    "”あんたが私の死んだ理由だ”って"),
                h.look().d("寂しげに笑った彼女は大きく首を横に振ってから続ける"),
                fuyumi.talk(THM["87"], THM["92"]).t("$meが周りの子たちのこと何も理解してなかったからいけないんだろうけど",
                    "中途半端に関わって偽りの温もりを与えるだけなら",
                    "最初から見捨ててしまっていた方がきっと女同士",
                    "ううん",
                    "人間同士うまくやっていけたんじゃないかなって思うの"),
                h.think(THM["83"]).d("彼女の学生時代で実際に何があったのかは",
                    "未だに聞けていない。",
                    "泣くでもなく",
                    "憤るでもなく",
                    "ただ真っ青だけが染める海と空の境界線を黙って見つめた彼女の横顔を目にしただけで",
                    "立ち入ることは必要ないと感じたからだ"),
                fuyumi.talk(THM["28"]).t("ほんとはこの話",
                    "$meが死ぬまで誰にも話すつもりなかったんだけど何でかな。",
                    "$heroが優しすぎるからかな？"),
                h.look().d("いつも少しだけ寂しげに笑う。",
                    "そうしていれば無事に人生を歩いて来られたのだろう。",
                    "けれど$meはそれが彼女を苦しめていると思ったから",
                    "言わなくても良かった一言を口にしたんだ"),
                h.talk(fuyumi).t("もし今ここにタイムマシンがあったら",
                    "その時の$herに会いに行って$meが言ってやる。",
                    "本当は泣きたい時に笑うな。",
                    "苦しいことや悔しいこと悲しいことを",
                    "口に出すことを恐れるなって"),
                ),
            w.scene("彼女はいない",
                h.go("公園").d("あの時二人で日が暮れるまで話した公園にやってきた"),
                h.look().d("だがそこに彼女の姿はない"),
                h.look().d("あの不可思議なスマートフォンを見ても",
                    "そこには新しいメールは送られてきていなかった"),
                h.talk().t("何だってんだよ！",
                    "$meにどうしろってんだ！",
                    "この野郎"),
                h.do().d("思い切り手にしたそいつを芝生の上に投げつける"),
                h.look().d("転がって割れた画面が突然発光した"),
                h.talk().t("うぉい！？"),
                h.look().d("その光に包まれて",
                    "$meは自分の体が重力から解放されるような浮遊感を味わっていた"),
                ),
           ]
    return [w.chaptertitle("これ以上書けない"),
            *scenes,
            ]


def ep_end(w: wd.World):
    h, osaki, fuyumi, ft_fuyumi = w.hero, w.osaki, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("学生時代",
                h.look().d("目を開くとどこかの学校の廊下だった"),
                h.remember(w.day.schoolday).d("懐かしい校舎の臭いと",
                    "教室から聞こえてくる生徒たちの談笑がすぐ様気分を学生時代に巻き戻したが",
                    "ふと気づいて自分の右の掌を見える位置に持ち上げてみる"),
                h.look().d("だがそこに$meの体はなかった"),
                h.talk().t("なあ", "ちょっと"),
                h.look().d("セーラー服のポニィテールの女子生徒が脇を駆け抜けていくところに声を掛けたが",
                    "彼女は急いでいるのか振り向くことすらせず",
                    "そのまま階段を登って行ってしまった"),
                h.think().d("けれどその子だけではなかった"),
                h.look().d("他の生徒たちも",
                    "名簿を手に歩いていく男性教師も",
                    "誰一人として$meのことを気にしない"),
                h.look().d("ひょっとして",
                    "という気持ちを確認するように窓ガラスを見やると",
                    "そこに自分の姿は映っていなかった"),
                h.think(THM["17"]).d("透明人間？"),
                h.think(THM["6"]).d("事実",
                    "先程の少女がいた教室の戸を開けて乱入してみたが",
                    "誰一人として騒ぎ出さない"),
                h.look().d("けれど透明人間になったと喜べたのは一瞬だけで",
                    "その彼女がすぐに学生時代の$herだと気づいた"),
                h.look(THM["40"]).d("今と違いこの当時は縁の大きな眼鏡を掛けていて",
                    "彼女から公園で聞かされた時の印象とは随分異なっていた"),
                h.look().d("それはどちらかといえば",
                    "そう",
                    "自殺したという噂の転校していった方の子に近い"),
                h.look().d("教壇に立っていた担任は一通り連絡事項を喋り終えると",
                    "前に彼女を呼んだ"),
                h.look().d("親の事情で今日この学校を辞め",
                    "別の高校に移っていくと説明した後",
                    "一言挨拶をするように言った"),
                h.look().d("$oldnameと呼ばれた彼女はぼそぼそとお世話になった等と話した後で",
                    "こんなことを唐突に明瞭な声で発言する"),
                fuyumi.talk(THM["74"]).t("……それでもあなたたちが$meを虐めていたことは今も忘れていませんし",
                    "たぶん一生忘れません"),
                h.feel(THM["48"]).d("ざわり",
                    "ともしなかった。",
                    "ただどこにも持っていきようのない胸が握られたような緊張感が",
                    "教室にいた人間全員に感染していくのが$meには分かった"),
                h.look().d("誰も何も口にしない中で後ろに括っていた髪が床に付くまで深々とお辞儀をすると",
                    "彼女は担任に一瞥もくれずに教室の外へと出て行ってしまった"),
                h.go().d("その後を慌てて追いかける"),
                h.go().d("だが階段を降りようとしたところで",
                    "足元が抜けた"),
                h.go().d("$meはそのまま暗闇へと呑み込まれていく"),
                h.be(w.i.lostmemory, THM["19"]),
                h.meet(ft_fuyumi, "あの時の女性"),
                h.deal(w.terminal, "時間を戻る"),
                ),
            w.scene("ありえた現在",
                h.look().d("次に目を開けると",
                    "いつも立ち寄るコンビニだった"),
                h.look().d("外は既に暗く",
                    "すぐ傍の交差点で信号が点滅している"),
                h.go(w.stage.conveni, THM["58"]),
                h.look("夫婦で働く姿", THM["59"]).d("よく寝間着のままやってくる$meを$herが追いかけてきては",
                    "大きめの上着を持ってきてそれで隠そうとするのだが",
                    "そのやり取りをオーナー夫婦に見られては苦笑されていた"),
                h.look().t("あ……"),
                fuyumi.come().d("彼女だった"),
                h.look().d("信号を渡り",
                    "店に入ってきて、"),
                fuyumi.talk().t("$heroまた締め切り間に合わなかったんだって？"),
                h.look().d("眉間に皺を寄せながら近づいてくる"),
                h.talk().t("だって満足行くもの書けないのに無理やり間に合わせみたいなもの出しても",
                    "相手だって困るだろう？"),
                fuyumi.talk().t("いつもそうやって自分に言い訳ばっかじゃない。",
                    "評価されるのが恐いってもっと正直に言えばいいのに"),
                h.think().d("もっと違う言葉を返したいのに",
                    "出てくるのは昨年の夏と同じ言葉ばかりだ"),
                h.talk(THM["31"], THM["81"]).t("夏が悪いんだよ。",
                    "クソ暑くていつまでも明るくて",
                    "夏がきた！　ってな具合にやたらと若い奴らが騒ぎ出す。",
                    "夏なんか無くなればいいんだ"),
                h.look().d("確かこの後……"),
                fuyumi.talk().t("さよなら"),
                h.look().d("引き止める間もなく店を出て行った彼女を",
                    "$meはただ呆然と見ていた"),
                h.think(THM["84"]).d("そして",
                    "あなたが夏の所為にしたから今日はさよなら記念日ね",
                    "とか自分の日記に書きなぐったんだ"),
                ),
            w.scene("悲しい現実",
                h.come(w.stage.bar, "神屋", THM["62"]).d("次に見たのは",
                    "よく$na_osakiが企画会議と称して$meを誘う彼お気に入りの小料理屋だった"),
                h.look().d("自分たちの母親くらいの年齢の女性がいつも一人だけでやっているのだが",
                    "彼曰く",
                    "最高級の家庭の味が楽しめる",
                    "とのことだ"),
                h.have("極上の突き出し", THM["35"]),
                h.think(w.i.absencemaster.flag(), THM["34"]).d("ただ店長は別にいるらしく",
                    "最初に紹介された時は「ちょっと奇妙な店でな」と言われたのだが",
                    "未だに$na_osaki自身もその謎の店長を見たことはないそうだ"),
                osaki.talk(THM["16"]).t("ところで今度の小説の企画なんだが",
                    "最悪だ……この世の終わりだ……から始まるアンソロジィを出そうってことになってさ"),
                h.reply().t("そういうの$meあんま向いてないっすよ？"),
                osaki.talk().t("何言ってるんだよ。",
                    "ちょうど彼女に振られたところだし",
                    "お前にはもってこいの企画だろ？"),
                h.think().d("そう。",
                    "担当編集の$na_osakiはいつもあれこれと考えてくれ",
                    "何とか$meに道を付けようとしてくれている。",
                    "それは分かっている。",
                    "けれどいざ原稿を前にすると「こんなつまらないもの誰が読むんだ」という気にしかならないのだ"),
                h.think(THM["76"]).d("だからいつも$meは嘘をつく。",
                    "ただひたすらに自分を悲しくさせる嘘を"),
                ft_fuyumi.talk("ずっと待ってる", THM["18"]),
                ),
            w.scene("そして自分が死ぬ",
                h.be(w.stage.apart, w.day.current).d("目覚めると今度こそは元の自分のアパートだった。",
                    "そのつまらないのっぺりとしたクリーム色の天井が迎えてくれている"),
                h.look().d("重い体を何とか起こして",
                    "パソコンに向かう"),
                h.look().d("依頼された小説は遅々として進んでいない。",
                    "それどころか削除して最初に書いていたものをどんどん無に返してしまっている"),
                h.look(THM["82"]).d("空腹を感じて時計を確認すると",
                    "既に真夜中だった"),
                h.look(THM["75"], THM["50"], THM["43"]).d("立ち上がり",
                    "冷蔵庫の中を覗き込んでみたが碌なものがない。",
                    "冷凍庫ならと一縷の望みを託したが",
                    "食べかけの半分残った板チョコが眠っていただけだ"),
                h.do().d("それでも口に突っ込むと",
                    "ただ甘ったるくなっただけだったが",
                    "それでもいくらかカロリィは摂取できたみたいで",
                    "ぼやけていた視界が明瞭になった"),
                h.think().d("死にたい"),
                h.think().d("と主人公に言わせながら",
                    "果たして今までにそんなことを考えたことがあったろうかと思い起こす"),
                h.think().d("あった"),
                h.remember("小学生のプールで溺れかけたのが最初", THM["5"]).d("あれは小学校五年の時の",
                    "プールの補習授業だ。",
                    "誰もが否定するのだが",
                    "絶対に誰かに足を引っ張られた。",
                    "そのまま溺れて危うくこの世から消えてしまうところだったのに",
                    "同級生の誰もが助けようとはしなかった"),
                h.think().d("その時に感じた恐怖と孤独が",
                    "$meの妄想の原点になっている"),
                h.think().d("そのことを$herにも話したが",
                    "何も言わずに薄っすらと涙を浮かべていたっけ"),
                h.think(w.i.help_mail).d("と、再びあのグロテスクな端末が唸りを上げた"),
                h.talk().t("今度は何なんだよ"),
                h.look().d("着信したメールは「時間ギレ」というもので",
                    "大量にスクロールさせた後でただ一言、"),
                h.look("おやすみ", THM["36"]).t("おやすみ"),
                h.look().d("と書かれていた"),
                h.do("help", w.futureman),
                h.look().d("唐突に周囲が暗くなる"),
                h.think().d("だから最初は停電したのだと思った"),
                h.do().d("けれどすぐに目の前からパソコンもテーブルも",
                    "食べかけたチョコレートの欠片すらも消え去ってしまったと気づいて",
                    "$meは唖然とした"),
                h.know(w.futureman, "dead").d("脳裏を過って行ったのは",
                    "冗談みたいな”死”という単語だ"),
                h.do(w.futureman, "小説を書く"),
                h.talk().t("嘘だろ……"),
                h.remember("小さい頃夜空に願った", THM["49"]).d("小さい頃に夜空の流れ星に願った「百歳まで生きたい」という$meの願いは叶えられないまま",
                    "その人生の帳を下ろすことになった"),
                h.be("dead"),
                ),
            w.scene("走馬灯",
                h.look().d("向こう岸が見えない大きな川の表面に",
                    "$meと$herが映し出されていた"),
                h.look("桜の木の下での告白", THM["73"]).d("どちらも学生服姿で",
                    "彼女を桜の木の下に呼び出して何か言おうとしている。",
                    "どうやら告白のようだったが",
                    "彼女は泣きながら頬を叩くと",
                    "走って行ってしまった"),
                h.have("桜の花びらをくれた", THM["44"]).d("その川面が大量の桜の花びらでかき消されると",
                    "次には保育園の小さなブランコに二人並んで乗っていた"),
                h.remember("こどもの日の約束だった", THM["14"]).d("どちらも漕がないまま",
                    "彼女が「やくそく」と言って小指を差し出すと",
                    "照れ臭そうに小さかった$meも指を出して絡ませようとするが",
                    "何か言って立ち上がり",
                    "そのまま走り去ってしまった"),
                h.look(THM["98"], THM["38"]).d("そんな色々な設定の$meと$herのすれ違いを見せられていた$meの隣に座り込んだのは",
                    "一匹の猫だった"),
                w.catgod.talk().t("どうして上手くいかないんだと思う？"),
                h.reply().t("猫に言われても分からないって"),
                w.catgod.talk().t("そういうとこだと思わんか？"),
                h.talk().t("隣に喋る猫が現れた時に信用しないのは",
                    "人間として正しいと思うけど"),
                w.catgod.talk().t("だが作家としては",
                    "いや",
                    "彼女の相手としてはどうかな"),
                h.talk().t("それは……"),
                h.look().d("言い淀んだ$meにその猫は炬燵を差し出す"),
                h.talk().t("どこから出したんだよ。",
                    "てかどうして炬燵なんだ？"),
                w.catgod.talk().t("蜜柑は自分で用意するんじゃぞ。",
                    "ちなみに彼女は少し酸っぱいのが好みらしい"),
                h.look().d("それだけ言うと$meに向かって小さく手を振り",
                    "そのまま川に飛び込んで消えてしまった"),
                h.talk().t("何だってんだよ……"),
                fuyumi.talk().t("ほんと",
                    "何かしらね"),
                h.look().d("$herだった"),
                fuyumi.talk().t("前いい？"),
                h.talk().t("あ、ああ"),
                h.look().d("小さな炬燵は二人で入ると一杯だったが",
                    "互いに向き合うには充分な広さな気がした"),
                fuyumi.ask().t("それでさ",
                    "結局『１００』は書けたの？"),
                h.talk().t("こ、これから良いとこなんだよ。",
                    "あとちょっとで何とかなるさ"),
                fuyumi.talk().t("また嘘。",
                    "お話の中で綺麗に嘘を書けないのに",
                    "現実は嘘塗れなの良くないよ"),
                h.talk().t("分かっているよ。",
                    "てか何なんだよ。",
                    "あの世でも説教か？",
                    "ここってどう見てもあの世の前のあそこ辺りだろ？"),
                fuyumi.talk().t("知らない"),
                h.look().d("そう言って川面を振り返った彼女の横顔は",
                        "少しだけ笑っていた"),
                h.talk().t("なあ。",
                        "これが本当でも夢でも小説でも",
                        "何でも良いんだけど",
                        "$meたちってまだやり直せるのか？"),
                fuyumi.talk().t("やり直したいの？"),
                h.talk().t("分からない。",
                        "ただ$fuyumiって女がどうしようもなく気になるんだよ。",
                        "もっと知りたい。",
                        "それにもっと……愛したい"),
                fuyumi.talk().t("なら一つだけ条件があるの"),
                h.talk().t("何だ？"),
                fuyumi.talk().t("『１００』のお題を使って最高の小説を書き上げて。",
                        "そうして$meを満足させて欲しい。",
                        "だって$meは",
                        "あなたの小説の神様だから"),
                h.hear().d("その言葉を聞いた瞬間",
                        "$meは自分の目の前にパソコンのモニタがあって",
                        "必死に原稿を書いている最中なのだと気づいた"),
                h.look().d("まだまだ道半ば。",
                        "けれどこの作品という旅を続けたい。",
                        "作家という旅を続けたい。",
                        "だから今日も$meは宛のない物語という旅に出かける。",
                        "その終わりを目指して"),
                h.talk("気になるやつ（作家）がいるんだ", THM["80"]),
                h.think("それに彼女は嫉妬した", THM["63"]),
                h.think("久々のデートが雪の夜に", THM["69"]),
                h.think("小さなこたつで二人", THM["67"]),
                fuyumi.talk("バレンタイン大嫌い", THM["68"]),
                h.think("最悪な誕生日", THM["47"]),
                h.think("その日のおかえりはなかった", THM["29"]),
                ),
            w.scene("過去の自分",
                h.be("dead"),
                h.deal(w.terminal, "時間を巻き戻せる", THM["13"]),
                h.go("過去に戻る", w.day.schoolday),
                h.think("だから幸福を取り戻す時間の旅に出た", THM["30"]),
                h.go(w.stage.school),
                h.meet(w.pastman),
                fuyumi.talk("またね", THM["42"]),
                h.remember("まだ気持ちが繋がっていると思っていた頃"),
                h.think("何度やり直しても死ぬ"),
                h.talk("もうやめてやる", THM["32"]),
                h.look("空", THM["88"]),
                h.think("小説日和だ", THM["99"]),
                h.know("ずっと見守ってくれていた", THM["94"]),
                h.know(w.i.absencemaster.deflag(), "神だった", THM["77"]),
                h.think("神からのお返し？", THM["97"]),
                ),
            w.scene("寝落ち！？",
                h.look("目を開けると", THM["37"]),
                h.do("wake", "風呂", THM["72"]),
                h.think("神に会ってから一年", THM["25"]),
                h.be("目覚めたらアイデア", THM["86"]),
                ),
            w.scene("走る",
                h.go(w.stage.bar, "向かう"),
                h.think("あの日捨てたちんけなプライド", THM["85"]),
                fuyumi.talk("今日は特別な日だったのに", THM["70"]),
                h.think("雨の日に別れた", THM["78"]),
                ),
            w.scene("小説を書く意味",
                h.go(w.stage.bar),
                h.think("トンデモ上司がいた", THM["33"]),
                osaki.talk("ギリギリだな", THM["45"]),
                osaki.talk("待ってた", THM["90"]),
                osaki.talk("二人で最強パーティだろ？", THM["64"]),
                h.ask("チョコじゃないんですか？", THM["95"]),
                h.talk("お年玉で父にプレゼントしたんです", THM["66"], THM["65"]),
                h.have("新しい小説の原稿", THM["93"]),
                h.look("真っ白", THM["91"]),
                h.know(w.i.his_reason),
                h.look("グラスの氷がとける", THM["96"]),
                ),
            ]
    return [w.chaptertitle("最後の作品"),
            *scenes,
            ]


# main
def world():
    w = wd.World("100 stories project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS)
    return w


def story(w: wd.World):
    return [w.maintitle("君の為に百の妄想を騙ろう"),
            ep_intro(w),
            ep_middle(w),
            ep_climax(w),
            ep_end(w),
            ]


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

