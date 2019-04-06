# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.subject import Master, Stage, DayTime, Item, Word, something
from storybuilder.builder.person import Person
from storybuilder.builder.storydb import StoryDB
from storybuilder.builder.tools import build_to_story


# story configs
CHARAS = (
        ("yuno", "坂見悠乃", 21, "female", "大学生", "me:わたし:mitsuro:ミッツ:kenjo:剣城"),
        ("kenjo", "剣城鋼太郎", 68, "male", "謎の老人", "me:私:mitsuro:光朗:yuno:坂見様"),
        ("mitsuro", "剣城光朗", 6, "male", "当時の同級生", "me:ぼく:yuno:ゆの"),
        ("girls", "大学の女子", 20, "female", "大学生"),
        ("bigman", "大柄な男", 30, "male", "会社員"),
        ("suitman", "スーツの男", 40, "male", "剣城コーポ社員"),
        ("doctor", "医者", 47, "male", "医者"),
        ("lecture", "講師", 52, "male", "大学講師"),
        )

STAGES = (
        ("univ", "九段下大学", "悠乃が通う大学"),
        ("hall", "大学講堂", "大きな階段教室"),
        ("train", "電車", "剣城と出遭う電車"),
        ("station", "最寄り駅"),
        ("bus", "バス", "隣席に男が乗ってくる"),
        ("chicenter", "児童館", "小さい頃によく遊んだ場所"),
        ("hospital", "病院", "刺されて入院する病院"),
        ("cemetary", "墓地"),
        )

DAYS = (
        ("meetday", "出会いの日", 4, 24, 2019,),
        ("nextday", "翌日", 4, 25, 2019),
        ("pastday", "幼少期", 6, 1, 2004),
        ("futureday", "五年後", 11, 1, 2024),
        )

ITEMS = (
        )

WORDS = (
        ("ghost", "幽霊席", "悠乃の隣がいつも空席なので、こう呼ばれる"),
        ("forgotten", "悠乃が忘れていること"),
        ("promise", "彼との約束", "幼い日にした二人の約束"),
        ("sick", "病気", "悠乃が罹り、死亡する"),
        ("yunowill", "悠乃の遺言", "彼の隣に埋葬してもらうこと"),
        ("rumor", "通り魔の噂", "大学近くで殺人事件があった"),
        )


def sdb():
    return StoryDB(CHARAS, STAGES, DAYS, ITEMS, WORDS)


# episodes
def ep_intro(ma: Master,
        yuno: Person, kenjo: Person, girls: Person, lecture: Person,
        ghost: Word, forgotten: Word, rumor: Word,
        meetday: DayTime,
        univ: Stage, hall: Stage, station: Stage, bus: Stage, train: Stage):
    sc1 = ma.scene("悠乃の日常",
            ma.comment("悠乃の一人称"),
            univ.explain("都内。目黒区あたり"),
            univ.explain("大学の前で人だかり").desc("キャンパスの入り口のところが騒然としていた"),
            yuno.thinkof(about="人だかり").desc("新入生たちへの時期外れなオリエンテーションでもやっているのだろうか"),
            yuno.go(univ, on=meetday),
            yuno.look("警官の姿").desc("よく見れば複数の警官が立っていて", "規制線と言うのだろう",
                "テレビなんかでよく見るあの黄色いテープが貼られていた"),
            ma.comment("悠乃の性格が人を避けがちと示す"),
            girls.look("集まっている"),
            yuno.feel("貧血").set_flag("cancer").desc("あまりに沢山の人を見たからだろうか", "ふっと目の前が暗くなる"),
            yuno.thinkof("いつもの").desc("また例のやつだ"),
            yuno.curious().non().desc("そう思ったが気にしない"),
            yuno.care("治まる").desc("一分ほど地面を見ているとすぐに血の気が戻り", "顔を上げた"),
            yuno.enter(univ, to=hall).desc("講堂に急ぐ"),
            yuno.look("スマホ", meetday).desc("スマートフォンを取り出して時刻を確認すると", "もう一限の開始時刻まで十分もなかった"),
            )
    sc2 = ma.scene("幽霊席",
            hall.explain("階段教室に生徒はまばら").desc("二百五十人ほどが収容できる大きな階段教室だったが", "開始時刻間際になっても一割ほどしか埋まっていない"),
            lecture.come(hall, "一時間目開始", on=meetday).desc("それでも予鈴が鳴るとバタバタと電車にでも駆け込むようにして", "生徒の数が増えた"),
            yuno.thinkof("野次馬だった？").desc("ひょっとすると外で見ていた子たちだろうか"),
            girls.sit().desc("誰もが知り合いと", "あるいはカップルで席に就いていく"),
            yuno.sit(something(), "隣に").non().desc("けれど決してわたしの隣には誰も座らない"),
            girls.laugh(yuno, "くすくすと").desc("そんなわたしをちらちらと見て", "彼女たちは口元を押さえる"),
            girls.thinkof(yuno).desc("声こそ出さないが", "笑っているのだ"),
            girls.talk(about=ghost).set_flag("ghost").desc("誰かが隣に座っているんじゃない？　幽霊？"),
            yuno.thinkof().desc("そんなことを言って笑っているのが見なくても分かる"),
            yuno.be("慣れている", of="色々言われること").desc("でもそれは今日に始まったことじゃない"),
            yuno.thinkof(ghost).desc("わたしの右隣はいつも", "空席で埋まっている"),
            ghost.explain("彼女の隣に誰も座らないことからこう呼ばれた").desc("それはまるで幽霊が座っているかのように", "どこの場所であっても",
                "決してわたしの隣の席には誰も座らない"),
            girls.tell().desc("ねえ聞いた？　今朝の"),
            girls.explain().desc("階段教室の右手側の真ん中辺りに座っている", "よく学内で見かける女子二人組だった"),
            girls.talk(about=rumor).set_flag("murder").desc("どうやらあの警察沙汰について", "ＬＩＮＥで情報が回ってきているようだ"),
            girls.enjoy("男子と談笑するカップル").desc("わたしの二段下の席だった"),
            girls.talk().desc("楽しげに話している男女のカップルもまた", "スマートフォンを見ながら「通り魔だって」と笑っている"),
            yuno.remember("通り魔").desc("つい先週にも", "近くの公園でナイフによる傷害事件があったばかりだ"),
            yuno.thinkof("羨ましくないし").set_flag("lover").desc("ただそんなことよりも", "自分たちに関係ない話だと笑っている二人が並んで座るのがやたらと視界に入り",
                "なんだか講義に集中できないでいた"),
            lecture.talk("栄枯盛衰", "剣城財閥も破産申請").set_flag("money").desc("先生は経済と同じように経済学にも栄枯盛衰があると言い",
                "その代表例としてこの近所に本社がある剣城コーポレーションが破産申請をした話を持ち出したが",
                "誰一人としてそれに耳を傾けていると思える学生はいなかった"),
            )
    sc3 = ma.scene("老紳士は座る",
            yuno.curious(about=ghost),
            yuno.know(forgotten).must(),
            meetday.explain("今日は午前中だけだった").d("午後からの授業は休講の知らせが出ていた"),
            yuno.go("自宅").want().d("サークルに入っていない$Sにとって", "大学に長い間いる意味はあまりない"),
            yuno.go(station).d("授業が終わればさっさと駅に向かう"),
            yuno.ride(bus).d("キャンパスを出たところでバスに乗り込むと", "そのまま文庫本を開いて空いた席に座る"),
            yuno.sit(something()).non().d("相変わらず右隣には誰も座らず", "その不自然さに乗客の目線が泳ぐ"),
            yuno.stand().d("だから結局いたたまれなくなり", "$Sは立ち上がる"),
            girls.sit().d("空いた二つの席には慌てて乗り込んできた女子大生が", "気にすることなく腰を下ろした"),
            yuno.notice(kenjo, "不審者").set_flag("oldman").d("一人の白い髭の老人だった"),
            yuno.thinkof(kenjo).d("彼はその小さなサングラスの目線を", "ずっと$Sに向けている", "ように思えた"),
            yuno.thinkof().d("黒い帽子にとても春物とは思えない重そうな黒コートを着込んでいて", "どうにも普通の老紳士とは思えない"),
            yuno.thinkof().d("ただ周りの人間は気にしていないようで", "それぞれに自分のスマートフォンを弄りながらバスに揺られていた"),
            station.explain("駅前の人の多さ").d("交差点の信号が変わると", "駅前のターミナルに進んでいく"),
            yuno.arrive(station).d("バスが止まると乗客が下りる波に任せて", "$Sもステップを下りた"),
            yuno.notice(kenjo, "ついてきている").d("バス停を離れても", "その老紳士の姿は$Sから離れることはなく", "一定の距離を保ってついてくる"),
            yuno.thinkof().d("偶然だろうか"),
            yuno.ride(train).d("改札を抜け", "ホームにちょうど滑り込んできた電車に", "慌てて乗り込んだ"),
            yuno.feel().d("流石の人の多さであの老人の姿も見つけられず", "ほっとして空いている席に腰を下ろした"),
            kenjo.tell().d("すみません"),
            yuno.sit(by=kenjo).ps().set_deflag("oldman").d("そう言って$Sの右隣に座ったのは", "あの老紳士だった"),
            )
    return ma.story("冒頭", sc1, sc2, sc3)

def ep_oldman(ma: Master,
        yuno: Person, kenjo: Person, mitsuro: Person, suitman: Person,
        ghost: Word, promise: Word,
        meetday: DayTime, pastday: DayTime,
        train: Stage, chicenter: Stage):
    sc1 = ma.scene("自己紹介",
            yuno.ride(train, on=meetday).d("思わず$Sは席を立とうとしたが", "電車は動き出してしまった"),
            yuno.meet(kenjo).d("その老紳士は$Sを見て", "にこりと笑みを浮かべる"),
            ma.comment("丁寧な印象を与えること"),
            kenjo.greet(yuno).d("それから「はじめまして」と軽く挨拶をした"),
            kenjo.ask(yuno, about=ghost).d("彼はわたしが答えるよりも早く", "こんなことを尋ねる"),
            kenjo.tell().d("幽霊席のお話をご存知ですかな？"),
            yuno.tell().d("ええ"),
            kenjo.tell(ghost).d("ある女性の右側の席に何故か誰も座らない",
                "それがいつしか”幽霊が座っているんじゃないか”と言われるようになった", "そんな都市伝説のようなものですが"),
            yuno.tell().d("知っています"),
            yuno.feel().d("おそらく$Sのことだと知った上で訊いているのだろう"),
            yuno.see(kenjo).d("老人は表情一つ変えず続ける"),
            kenjo.tell().d("けれど幽霊など", "実在するのでしょうか"),
            yuno.tell(kenjo, "記者かどうか").d("ひょっとして新聞記者か何かなんですか？"),
            kenjo.deny().tell("もし$Sが記者であるなら些か年を取りすぎている", "とは思われませんか"),
            yuno.reply().tell("そうかも知れません。", "けれど$Sが知らない世界なら常識が通用しない", "ということもありえますから"),
            kenjo.smile().d("彼は微笑し", "「確かに」と頷いた"),
            kenjo.talk(yuno, about=ghost).tell("ともかく記者やライターといった類の人種ではありません。", "まずはこちらをどうぞ"),
            yuno.apply(kenjo, "名刺").d("彼が差し出したのは名前と役職のみの簡素な名刺だった"),
            yuno.see().d("そこには「{}」という彼の名前と、その右隣に小さく「剣城コーポレーション代表取締役」とだけ書かれていた".format(kenjo.name)),
            yuno.hear(ghost, frm=kenjo).tell("そんな方がどうして$Sに？"),
            yuno.remember(kenjo).d("剣城コーポレーションといえば服飾品を中心に業績を上げている地元の大企業だった"),
            )
    sc2 = ma.scene("幽霊席の事情",
            kenjo.talk(yuno, about="剣城財閥").tell("既に新聞各紙で発表されていますが", "多くの腕利きの職人たちが皆定年を迎え", "残っていた者も中国や東南アジアといった国々に出て行ってしまい", "剣城のブランド力の礎となっていた宝飾、服飾業界ではもうその力を発揮することが叶いません"),
            kenjo.talk(yuno, about="跡継ぎがいない").set_deflag("lover").tell("そしてこれが一番の問題なのですが", "私たちには跡継ぎがいないのです"),
            yuno.ask().tell("別に血縁に拘らなければ誰でも良いんじゃないですか？"),
            kenjo.reply().tell("まずはそのことについて", "お話しなければならないようですね"),
            kenjo.talk(yuno, "ある事情で隣の席に誰も座らせないようにしていた").tell("我々が何故あなた様のお隣に誰も座らせないようにしていたのか", "ということについて"),
            yuno.surprise().tell("え？　あなたの仕業だったんですか？"),
            kenjo.reply().tell("そうでございます"),
            yuno.wonder("事情", "方法").tell("そんなこと", "可能なのですか？"),
            kenjo.teach(yuno, about=suitman).d("小さく頷くと", "彼はわたしに同じ色のスーツを着た乗客を見るように言った"),
            suitman.greet(yuno).d("彼らはわたしと目が合うと小さく手を挙げ", "剣城の知人であることを示した"),
            yuno.sound().d("「あ」と思わず声を上げてしまう"),
            yuno.remember("今までに見たことがある", suitman).d("そういえば今まで気にしなかったが", "確かにいつも同じスーツの人間が視界の端々に目に付いた。",
                "それはここが剣城コーポレーションの地元であり", "そこで働く人間が多いからだ", "としか考えなかった"),
            yuno.ask().tell("それじゃあ社員の方なんですか？"),
            kenjo.reply().tell("ええ、そうです"),
            kenjo.talk("今日で終わり", ghost).tell("しかしそれも今日までです。", "明日から彼らは別の会社の人間となり", "我々の手から離れていってしまいます"),
            yuno.ask().tell("倒産……"),
            kenjo.explain("資金が尽きた").set_deflag("money").tell("はい、左様です。", "端的に言って資金が尽きました"),
            yuno.ask().tell("仕事だった、と？"),
            kenjo.reply().tell("そうでございます"),
            yuno.confuse().tell("あの", "意味が分かりません。", "そもそもどうして$Sなんかに？"),
            kenjo.talk(yuno, "ある方の依頼だった").tell("ある方のご依頼でした"),
            yuno.wonder("過去形").d("剣城の言葉は何故か過去形だった"),
            yuno.ask().tell("その”ある方”って？"),
            kenjo.ask(yuno, "彼のことを覚えているか", mitsuro).tell("$mitsuro様でございます"),
            yuno.thinkof().d("その名前に", "正直覚えはなかった"),
            kenjo.explain(yuno, "彼の遺言", mitsuro).tell("$mitsuro様の遺言なのでございます"),
            yuno.reply("聞き返す").tell("遺言……ですか"),
            kenjo.talk(yuno, "彼は亡くなった", mitsuro).tell("はい。そうでございます。", "全てはあの方との約束なのです"),
            )
    sc3 = ma.scene("遺言と約束",
            yuno.see().d("そう言ってから剣城はまだ$Sの記憶がおぼろげな頃の話を始めた"),
            kenjo.ask(about=pastday).tell("あれはまだ$mitsuro様が幼稚園に通われている頃でした"),
            kenjo.talk(yuno, pastday, chicenter, "当時通っていた").tell("当時から両親は仕事が忙しく",
                "家に帰っても誰もいない家庭だった為に", "暗くなるまでを近所にあった児童館で過ごされたのです"),
            kenjo.talk(yuno, "彼の隣", of=mitsuro).tell("その時に").tell("その当時",
                "$yuno様はいつも図書コーナーの小さな椅子に座り", "絵本を読まれていましたね"),
            yuno.reply().tell("……ええ"),
            yuno.remember().d("うちも両親が共働きで", "外が暗くなるまで児童館で時間を潰していたことを思い出す"),
            yuno.remember(mitsuro).d("いつも彼のことは$mitsuroと呼んでいた"),
            yuno.remember(mitsuro).d("色素の薄い少年で", "髪も細くまるで濃いブロンドのようにも見えた。",
                "彼はいつも$Sの右隣の椅子に座って", "同じように本を読んでいた",
                "実はそのことが内心でちょっとだけ周囲の子たちに対しての自慢でもあった"),
            yuno.remember().d("そうだ。", "あの頃はまだ$Sの隣には普通に誰かが座っていたのだ"),
            yuno.remember(promise).set_deflag("ghost").d("その彼とある日", "$Sは一つの約束をしたのだ"),
            mitsuro.talk().tell("$yunoちゃん。", "$Sがずっと隣にいても良い？"),
            yuno.thinkof().d("その問いかけに$Sは何て答えただろう"),
            yuno.promise(mitsuro, promise, on=pastday).d("$Sは必死に彼の言葉を思い出そうとしたが",
                "記憶はうまく形を成してくれない"),
            kenjo.ask(yuno).tell("思い出されましたかな？"),
            yuno.reply().tell("それが……肝心の約束の内容を忘れてしまいました"),
            mitsuro.tell(yuno, "ずっと隣で君を守ってあげるね").tell("ずっと隣で君を守ってあげるね"),
            yuno.thinkof().d("一瞬彼の声が聴こえたのかと思ったが", "隣を見ると$kenjoがひらがなだけの手紙を広げ",
                "それを音読しただけだった"),
            yuno.ask().tell("それが……遺言状ですか"),
            kenjo.reply().tell("はい。これがずっとあなた様の隣の席を我々に守らせた", "そのお言葉でございます"),
            yuno.sad("泣いていた").d("何故だろう。", "その$kenjoの言葉に", "$Sの目からは留まることのない涙が落ちていった"),
            )
    return ma.story("老紳士", sc1, sc2, sc3)

def ep_ordinary(ma: Master,
        yuno: Person, kenjo: Person, mitsuro: Person, bigman: Person, doctor: Person,
        sick: Word, yunowill: Word,
        nextday: DayTime, futureday: DayTime,
        bus: Stage, hospital: Stage, cemetary: Stage):
    sc1 = ma.scene("隣に座る男",
            yuno.walk(nextday).d("明日からはもう隣の席に幽霊は座らない。",
                "そう言われてもあまり実感は湧かなかった。",
                "そんなことよりも$mitsuroとの約束のことをずっと忘れてしまっていたことの方のが",
                "ショックは強かった"),
            yuno.ride(bus, on=nextday).d("大学に向かうバスに乗り込む"),
            bigman.sit(by=yuno).d("相変わらず狭い車内に人がわんさか入ってくるけれど",
                "なんとか座れた", "と思ったわたしの隣に大柄なマスクをした男性が腰を下ろした"),
            yuno.thinkof().d("ああ、本当にもう自分の隣には彼は座っていないのだな",
                "と思うと", "また泣いてしまいそうになる"),
            bigman.stick(yuno, by="ナイフ").set_deflag("murder").d("と、何だろう。",
                "右側の脇腹だった"),
            yuno.feel().d("熱い"),
            yuno.bleed().d("脇に触れてみるとべったりと赤いものが付着した"),
            yuno.thinkof().tell("え。嘘……"),
            yuno.do("倒れた").d("急激に思考は温度を失い", "$Sはそのまま席から崩れ落ちた"),
            )
    sc2 = ma.scene("発覚する病",
            yuno.wake(hospital).d("目が覚めるよりも早くに", "病院独特の綺麗にし過ぎた匂いが鼻を突いた"),
            yuno.see().d("真っ白な天井と$Sの心拍を測る機械音", "それに母親の泣き顔が視界に入る。",
                "母は$Sの名を何度も呼びながら「よかった」と繰り返したけれど",
                "$S自身は一命を取り留めたことよりも",
                "自分がずっと彼によって守られていたんだという驚きの方が",
                "何よりも$Sの中で支配的になっていた"),
            yuno.remember().d("ただその後", "$Sは決して自分が助かった訳じゃないという事実を知らされることになる"),
            doctor.talk(yuno, "症状").tell("すまないが実は"),
            yuno.ask("傷のこと").d("担当医師が神妙な顔つきでそんなことを言い出すので",
                "てっきりナイフの傷が酷いのだと思ったけれど", "それは違った"),
            doctor.reply("それは問題ない").tell("そうじゃないんだ"),
            yuno.wonder(),
            doctor.talk(sick).tell("実は君の体の中", "具体的に言えば胃に腫瘍が見つかった"),
            yuno.be(sick, on=futureday).d("腫瘍、という言い方だったが",
                "よくよく聞いてみればそれはガンだった。",
                "それも進行が早く", "$Sの五年生存率は10％未満という",
                "何とも酷い数字のものだった"),
            doctor.talk(yuno, sick, "進行性のガン").set_deflag("cancer"),
            sick.explain("進行性の胃がん", "未分化型で遅いと五年生存率が10％未満"),
            yuno.die().must(),
            )
    sc3 = ma.scene("眠る場所は",
            ma.comment("ここから視点は剣城に"),
            cemetary.explain("沢山の墓石が整然と並んでいる").d("石畳の上を落ち葉が走り抜けていく"),
            kenjo.thinkof().d("$Sはいつも思うのです。",
                "どうして人が亡くなるのは歳の順ではないのか、と"),
            kenjo.walk().d("霊園を歩いていた。",
                "$S以外には誰もいない。", "いなくなってしまったのだ。",
                "妻も、そして息子も"),
            kenjo.have().d("手にした花の中には",
                "あの方が好きだというかすみ草を入れてもらった。",
                "いつも自分の隣にいない誰かのことを",
                "あの方はまるでかすみ草みたいな存在だと思っていたそうだ"),
            kenjo.stop().d("その墓石の前に立ち止まる"),
            kenjo.see().d("刻まれているのは{}という名前と".format(mitsuro.name),
                "その隣に名字の異なる女性の名前だ。",
                "血縁すらない彼女が何故ここに収められているのか。",
                "その経緯を思い出すと今でも目頭が熱くなる。"),
            yuno.talk("彼の隣に埋めて下さい", of=mitsuro, to=kenjo).tell("彼の隣に、埋めてくれませんか"),
            yuno.beg(kenjo, of=yunowill).d("彼女に真実を告げたその一月後に", "呼び出された。",
                "そこでもう先が長くないことを告げられ", "言われたのだ。",
                "$mitsuroの隣に入れてくれないかと"),
            kenjo.reply().d("もう$S以外には大した血縁者もいない。",
                "反対する者もいないことを告げて快諾すると",
                "あの方は初めて笑顔を見せた"),
            kenjo.remember(yunowill),
            yuno.bury("彼の隣", of=mitsuro),
            kenjo.thinkof().d("きっとあちら側でもあの二人は一緒に並んで隣同士になっていることだろう"),
            kenjo.feel().d("そう思うと",
                "どうしようもなく二つの涙が滲んで目の前が霞んでいった"),
            )
    return ma.story("訪れた日常", sc1, sc2, sc3)

    
# main
def story():
    ma = Master("my side mystery")
    db = sdb()
    return ma.story("わたしの隣席はいつも不在",
            ep_intro(ma, db.yuno, db.kenjo, db.girls, db.lecture,
                db.ghost, db.forgotten, db.rumor,
                db.meetday,
                db.univ, db.hall, db.station, db.bus, db.train),
            ep_oldman(ma, db.yuno, db.kenjo, db.mitsuro, db.suitman,
                db.ghost, db.promise,
                db.meetday, db.pastday,
                db.train, db.chicenter),
            ep_ordinary(ma, db.yuno, db.kenjo, db.mitsuro, db.bigman, db.doctor,
                db.sick, db.yunowill,
                db.nextday, db.futureday,
                db.bus, db.hospital, db.cemetary),
            )


def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
