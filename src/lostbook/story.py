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
            # TODO: 学校のこと、学校での那緒
            # TODO: かつて旧校舎があった
            nao.look().d("机に肘を突きながら顎を載せて窓の外にぼんやりと視線を投げ出すと",
                "一年生たちが暑い中でだらだらサッカーボールを蹴っている様子が窺えた"),
            nao.be(w.stage.classroom),
            teacher.talk("夏休み"),
            )

def sc_oldlibrary(w: wd.World):
    nao, teacher = w.nao, w.teacher
    return w.scene("かつての図書室",
            # TODO: 物語の舞台となったものが消えた場所
            # TODO: 先生から学校が消えたことを聞く
            nao.be(w.stage.oldlib_mark),
            teacher.explain("旧校舎事情"),
            nao.think(w.i.oldschool_reason.flag()),
            )

def sc_herbook(w: wd.World):
    nao, akiko = w.nao, w.akiko
    return w.scene("彼女の同人誌",
            # TODO: 作家情報と本がここのみ
            nao.come(w.stage.bookshop),
            akiko.talk("その作家さん好きなんだ"),
            w.nao.think("全ての本を集める"),
            w.nao.deal("本を集める"),
            nao.think("金が足りない"),
                w.nao.deal("店が潰れるまでに収集しなきゃ"),
                w.nao.know(w.i.vanishshop),
                w.nao.deal("本を買い集める"),
                w.nao.know("金が足りない"),
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
            sc_oldlibrary(w),
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

