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
            # TODO: 季節描写（７月）
            nao.behav().d("本を開く"),
            nao.think().d("ただそれだけの行為が",
                "こんなにも$meの心を震わせる"),
            nao.be("bed").d("俯せになったまま右手を伸ばして枕元のスタンドライトの角度を変える。",
                "薄暗闇の中に煌々とした読書空間を作り出して",
                "開いた本は勿論",
                "最近見つけた個人的な掘り出し物の一冊だ"),
            nao.look().d("サイズはＢ５より少し大きい程度。",
                "淡い花柄が印刷された厚紙をカバーにして綴じられた",
                "およそ百ページほどの同人誌で",
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
                "続きを買いに行こう"),
            nao.think().d("本棚に並ぶものには途中までしか揃っていないものが多かったけれど",
                "この作者の本だけは何としても全巻揃えたい。",
                "そう思わせるだけの手触りがあった"),
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
            # TODO: 台所情景
            nao.be(w.stage.dyning, w.day.known),
            mam.ask("夏休みのこと"),
            dad.talk("本屋潰れる"),
            w.nao.know(w.i.vanishshop),
            )

def sc_checkclosed(w: wd.World):
    nao, akiko = w.nao, w.akiko
    return w.scene("潰れるんですか！？",
            # TODO: 主人紹介
            # TODO: 本屋描写
            akiko.talk("閉店のこと"),
            nao.look("残りの本"),
            )

def sc_lazyschool(w: wd.World):
    nao, teacher = w.nao, w.teacher
    return w.scene("退屈な教室",
            # TODO: 学校のこと、学校での那緒
            # TODO: かつて旧校舎があった
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

