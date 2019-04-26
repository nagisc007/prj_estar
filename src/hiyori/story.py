# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd


# configs
CHARAS = (
        ("yuko", "浅見夕子", 18, "female", "高校生"),
        ("tagawa", "田川昼男", 18, "male", "高校生"),
        ("takemura", "竹村紀行", 56, "male", "数学教師"),
        ("boys", "男子生徒", 18, "male", "高校生"),
        ("eri", "足立衣里", 18, "female", "高校生"),
        ("granpa", "浅見健三", 78, "male", "農家", "夕子の祖父"),
        ("mam", "浅見晶子", 40, "female", "レジ打ち", "夕子の母"),
        )

STAGES = (
        ("town", "衣保川町", "地方都市（岐阜県・揖斐川がモデル）の田舎町"),
        ("school", "高校", "県立高校"),
        ("classroom", "教室"),
        ("tanbo", "田んぼ"),
        ("tahouse", "田川家"),
        ("myhouse", "自宅"),
        )

DAYS = (
        ("sunnyday", "天気な日", 4, 15, 2019),
        ("rainyday", "雨の日", 4, 20, 2019),
        ("examday", "試験日", 4, 24, 2019),
        ("gwday", "ゴールデンウィーク", 5, 3, 2019),
        )

ITEMS = (
        ("tractor", "トラクター"),
        ("cycle", "自転車", "夕子が通学に利用する自転車"),
        ("uniform", "学生服"),
        ("futurepaper", "進路予定表"),
        )

INFOS = (
        ("hiyori", "田川日和"),
        ("myhiyori", "自分日和"),
        ("reason", "サボる理由"),
        ("fam_reason", "家族の事情"),
        ("circs", "田川の事情"),
        ("myfuture", "自分の将来"),
        )

FLAGS = (
        ("hiyori", "田川日和の謎"),
        ("future", "夕子の将来"),
        )

# episodes
def ep_intro(w: wd.World):
    yuko, tagawa, boys, eri, takemura = w.yuko, w.tagawa, w.boys, w.eri, w.takemura
    sunnyday = w.day.sunnyday
    nextday = sunnyday.elapsed(day=1)
    classroom, school, town = w.stage.classroom, w.stage.school, w.stage.town
    reason, hiyori = w.i.reason, w.i.hiyori
    tractor, uniform, futurepaper = w.tractor, w.uniform, w.futurepaper
    sc1 = w.scene("田川のいない日",
            w.tag.comment("夕子の一人称"),
            w.tag.comment("田川はep2まで登場させない"),
            w.combine(
                classroom.explain("教室の様子").d("教室だった"),
                yuko.be(classroom, sunnyday).d("よく晴れた日"),
                ),
            sunnyday.explain("午前の休み時間").d("休み時間"),
            yuko.explain("同じ制服に同じようなもっさり", uniform),
            yuko.have(futurepaper, w.flag.future),
            boys.talk(tagawa, "またサボり"),
            boys.explain(uniform, "制服の前を全開にした男子"),
            yuko.hear(eri, reason),
            eri.reply(yuko, "知らない"),
            eri.explain("長い黒髪が暑そう"),
            eri.look("読書"),
            eri.talk(yuko, reason, "今年は多い"),
            yuko.know(tagawa, reason, "$want"),
            yuko.look(sunnyday, "驚くほどの晴天"),
            town.explain("見渡す限り閑散とした町並み"),
            takemura.come(classroom, "授業の鐘"),
            takemura.explain("担任", "定年間際で白髪混じり"),
            )
    sc2 = w.scene("抜け出す夕子",
            nextday.explain("翌日も晴れ"),
            tagawa.be(classroom, "$not"),
            yuko.look(tagawa, "サボる"),
            boys.talk(hiyori, "笑う", w.flag.hiyori),
            yuko.think("サボる決断"),
            yuko.talk(eri, "田川を探す"),
            yuko.go(school, "抜け出す"),
            school.explain("授業中の学校は静か"),
            )
    return (w.chaptertitle("田川日和"),
            sc1, sc2)

def ep_tagawa(w: wd.World):
    yuko, tagawa, granpa = w.yuko, w.tagawa, w.granpa
    nextday = w.day.sunnyday.elapsed(day=1)
    tanbo, town = w.stage.tanbo, w.stage.town
    reason, fam_reason, myfuture = w.i.reason, w.i.fam_reason, w.i.myfuture
    cycle, tractor = w.cycle, w.tractor
    sc1 = w.scene("田川の居場所",
            yuko.go(cycle, town),
            town.explain("田畑が多い", "のどか"),
            yuko.look(tagawa, "どこにいるか"),
            yuko.know(tagawa, reason, "$want"),
            yuko.look(granpa, tractor),
            granpa.explain("目元がぼさぼさの毛で覆われ背中が曲がる"),
            granpa.ask(yuko, "もう学校終わったのか"),
            yuko.ask(granpa, tagawa, "見なかったか"),
            granpa.reply(yuko, tagawa, tanbo),
            yuko.ask(granpa, tagawa, "知ってるの？"),
            granpa.talk("田川は小さい頃からの喧嘩仲間"),
            yuko.hear(granpa, tagawa, "居場所"),
            )
    sc2 = w.scene("田川の秘密",
            yuko.go(tanbo, tagawa),
            nextday.explain("日が高くなる"),
            yuko.look(tagawa, tanbo),
            tanbo.explain("土が耕された広大な区画"),
            tractor.explain("真っ赤なボディは既に泥まみれ"),
            tagawa.explain("頭に手ぬぐいをまきつけ、野良作業着"),
            yuko.talk(tagawa),
            yuko.ask(tagawa, reason),
            tagawa.reply(yuko, "終わるまで待ってくれ"),
            yuko.be("待つ"),
            yuko.look(tagawa, "普段見せない顔"),
            )
    sc3 = w.scene("田川日和",
            tagawa.do("農作業終わる", nextday),
            yuko.have(tagawa, "ジュース"),
            tagawa.reply(yuko, "ありがとう"),
            yuko.feel(tagawa, w.X()),
            yuko.ask(tagawa, reason),
            tagawa.reply(yuko, reason, w.deflag.hiyori),
            tagawa.talk(yuko, reason, "農業を継ぐ"),
            tagawa.talk(yuko, "家族の事情", fam_reason),
            yuko.know(tagawa, reason),
            tagawa.talk(yuko, "将来農家やりたい"),
            tagawa.ask(yuko, myfuture),
            yuko.talk(tagawa, myfuture, "$not"),
            )
    return (w.chaptertitle("学校外の田川"),
            sc1, sc2, sc3)

def ep_future(w: wd.World):
    yuko, tagawa, takemura, eri = w.yuko, w.tagawa, w.takemura, w.eri
    classroom, myhouse, school, tanbo = w.stage.classroom, w.stage.myhouse, w.stage.school, w.stage.tanbo
    rainyday, examday = w.day.rainyday, w.day.examday
    myfuture, reason, hiyori, myhiyori = w.i.myfuture, w.i.reason, w.i.hiyori, w.i.myhiyori
    cycle, futurepaper = w.cycle, w.futurepaper
    sc1 = w.scene("夕子の将来",
            yuko.be(myhouse, rainyday),
            yuko.hear(tagawa, reason),
            yuko.think(myfuture, "$must"),
            yuko.think(myfuture, "$not"),
            )
    sc2 = w.scene("試験の日",
            yuko.go(school, examday),
            tagawa.be(classroom, examday, "$not"),
            yuko.ask(eri, tagawa,"いない"),
            eri.reply(yuko, hiyori),
            yuko.talk(eri, "馬鹿じゃないの"),
            examday.explain("試験が終わる"),
            tagawa.come(school, "$not"),
            yuko.go(tanbo, cycle),
            yuko.look(tagawa, tanbo),
            yuko.ask(tagawa, "試験をサボったことを咎める"),
            tagawa.reply(yuko, hiyori),
            )
    sc3 = w.scene("学業と仕事",
            yuko.talk(tagawa, "将来"),
            tagawa.talk(yuko, "将来に試験が大事か"),
            yuko.reply(tagawa, "大事と思う"),
            tagawa.talk(yuko, "大事と思わない"),
            tagawa.talk(yuko, "日和の方が大事だ"),
            tagawa.ask(yuko, myhiyori),
            yuko.reply(tagawa, "$not"),
            yuko.be(myhouse, examday.elapsed(hour=20)),
            yuko.think(myfuture),
            yuko.talk("わかんない"),
            yuko.have(futurepaper, "お嫁さんを消す"),
            )
    return (w.chaptertitle("自分の将来"),
            sc1, sc2, sc3)

def ep_myhiyori(w: wd.World):
    yuko, tagawa, eri, granpa, mam = w.yuko, w.tagawa, w.eri, w.granpa, w.mam
    gwday = w.day.gwday
    tahouse, myhouse = w.stage.tahouse, w.stage.myhouse
    myhiyori, myfuture = w.i.myhiyori, w.i.myfuture
    futurepaper = w.futurepaper
    sc1 = w.scene("答えは見えない",
            yuko.be(myhouse, gwday),
            gwday.explain("どこにも出かけないGW"),
            myhouse.explain("参考書が並ぶ本棚", "布団をかけたベランダ"),
            yuko.hear(mam, "ご飯よ"),
            yuko.go(myhouse, "食堂"),
            mam.explain("白髪混じりの髪", "ぼさぼさ頭", "染みが多い"),
            yuko.deal("食事"),
            yuko.ask(granpa, "仕事のこと"),
            granpa.reply("そんなもん考えなかった"),
            yuko.think(myfuture),
            yuko.look(myfuture, "$want"),
            )
    sc2 = w.scene("告白と自分日和",
            yuko.go(tahouse, gwday.elapsed(day=1)),
            tahouse.explain("大きな古い木造平屋"),
            yuko.go("田川の部屋"),
            tagawa.ask(yuko, "何の用？"),
            yuko.reply(tagawa, "この前の話", myhiyori),
            tagawa.talk(yuko, "自分の日和を持てよ"),
            yuko.talk(tagawa, myhiyori, "自分の考え"),
            yuko.talk(tagawa, "告白"),
            yuko.have(tagawa, futurepaper),
            futurepaper.be("十年後に結婚日和がみたい"),
            tagawa.talk(yuko, "馬鹿なのか？"),
            yuko.reply(tagawa, "十年あったら何でもできるかもよ"),
            tagawa.look(yuko, "笑顔"),
            yuko.look(myhiyori),
            futurepaper.be("看護師と書かれている", w.deflag.future),
            )
    return (w.chaptertitle("自分日和"),
            sc1, sc2)


# main
def world():
    w = wd.World("project hiyori")
    w.set_db(CHARAS, STAGES, DAYS, ITEMS, INFOS, FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("田川日和と恋の雨"),
            ep_intro(w),
            ep_tagawa(w),
            ep_future(w),
            ep_myhiyori(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

