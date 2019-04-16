# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.master import Master
from storybuilder.builder.subject import Something
from storybuilder.builder.tools import build_to_story


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

WORDS = (
        ("hiyori", "田川日和"),
        ("myhiyori", "自分日和"),
        ("reason", "サボる理由"),
        ("fam_reason", "家族の事情", "祖父が昨年秋に腰をやって入退院繰り返す"),
        ("circs", "田川の事情"),
        ("myfuture", "自分の将来"),
        )

FLAGS = (
        ("hiyori", "田川日和の謎"),
        ("future", "夕子の将来"),
        )

# episodes
def ep_intro(ma: Master):
    yuko, tagawa, boys, eri, takemura = ma.yuko, ma.tagawa, ma.boys, ma.eri, ma.takemura
    sunnyday = ma.sunnyday
    nextday = sunnyday.elapsed_day(day=1)
    classroom, school, town = ma.classroom, ma.school, ma.town
    reason, hiyori = ma.reason, ma.hiyori
    tractor, uniform, futurepaper = ma.tractor, ma.uniform, ma.futurepaper
    sc1 = ma.scene("田川のいない日",
            ma.comment("夕子の一人称"),
            ma.comment("田川はep2まで登場させない"),
            classroom.explain("教室の様子"),
            yuko.be(classroom, sunnyday),
            sunnyday.explain("午前の休み時間"),
            yuko.explain("同じ制服に同じようなもっさり", uniform),
            yuko.have(futurepaper, ma.f_future),
            boys.talk(tagawa, "またサボり"),
            boys.explain(uniform, "制服の前を全開にした男子"),
            yuko.hear(eri, reason),
            eri.reply(yuko, "知らない"),
            eri.explain("長い黒髪が暑そう"),
            eri.look("読書"),
            eri.talk(yuko, reason, "今年は多い"),
            yuko.know(tagawa, reason).want(),
            yuko.look(sunnyday, "驚くほどの晴天"),
            town.explain("見渡す限り閑散とした町並み"),
            takemura.come(classroom, "授業の鐘"),
            takemura.explain("担任", "定年間際で白髪混じり"),
            )
    sc2 = ma.scene("抜け出す夕子",
            nextday.explain("翌日も晴れ"),
            tagawa.be(classroom).non(),
            yuko.look(tagawa, "サボる"),
            boys.talk(hiyori, "笑う", ma.f_hiyori),
            yuko.think("サボる決断"),
            yuko.talk(eri, "田川を探す"),
            yuko.go(school, "抜け出す"),
            school.explain("授業中の学校は静か"),
            )
    return ma.story("田川日和", sc1, sc2)

def ep_tagawa(ma: Master):
    yuko, tagawa, granpa = ma.yuko, ma.tagawa, ma.granpa
    nextday = ma.sunnyday.elapsed_day(day=1)
    tanbo, town = ma.tanbo, ma.town
    reason, fam_reason, myfuture = ma.reason, ma.fam_reason, ma.myfuture
    cycle, tractor = ma.cycle, ma.tractor
    sc1 = ma.scene("田川の居場所",
            yuko.go(cycle, town),
            town.explain("田畑が多い", "のどか"),
            yuko.look(tagawa, "どこにいるか"),
            yuko.know(tagawa, reason).want(),
            yuko.look(granpa, tractor),
            granpa.explain("目元がぼさぼさの毛で覆われ背中が曲がる"),
            granpa.ask(yuko, "もう学校終わったのか"),
            yuko.ask(granpa, tagawa, "見なかったか"),
            granpa.reply(yuko, tagawa, tanbo),
            yuko.ask(granpa, tagawa, "知ってるの？"),
            granpa.talk("田川は小さい頃からの喧嘩仲間"),
            yuko.hear(granpa, tagawa, "居場所"),
            )
    sc2 = ma.scene("田川の秘密",
            yuko.go(tanbo),
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
    sc3 = ma.scene("田川日和",
            tagawa.do("農作業終わる", nextday),
            yuko.have(tagawa, "ジュース"),
            tagawa.reply(yuko, "ありがとう"),
            yuko.feel(tagawa, ma.some()),
            yuko.ask(tagawa, reason),
            tagawa.reply(yuko, reason).de(ma.f_hiyori),
            tagawa.talk(yuko, reason, "農業を継ぐ"),
            tagawa.talk(yuko, "家族の事情", fam_reason),
            yuko.know(tagawa, reason),
            tagawa.talk(yuko, "将来農家やりたい"),
            tagawa.ask(yuko, myfuture),
            yuko.talk(tagawa, myfuture).non(),
            )
    return ma.story("学校外の田川", sc1, sc2, sc3)

def ep_future(ma: Master):
    yuko, tagawa, takemura, eri = ma.yuko, ma.tagawa, ma.takemura, ma.eri
    classroom, myhouse, school, tanbo = ma.classroom, ma.myhouse, ma.school, ma.tanbo
    rainyday, examday = ma.rainyday, ma.examday
    myfuture, reason, hiyori, myhiyori = ma.myfuture, ma.reason, ma.hiyori, ma.myhiyori
    cycle, futurepaper = ma.cycle, ma.futurepaper
    sc1 = ma.scene("夕子の将来",
            yuko.be(myhouse, rainyday),
            yuko.hear(tagawa, reason),
            yuko.think(myfuture).must(),
            yuko.think(myfuture).non(),
            )
    sc2 = ma.scene("試験の日",
            yuko.go(school, examday),
            tagawa.be(classroom, examday).non(),
            yuko.ask(eri, tagawa,"いない"),
            eri.reply(yuko, hiyori),
            yuko.talk(eri, "馬鹿じゃないの"),
            examday.explain("試験が終わる"),
            tagawa.come(school).non(),
            yuko.go(tanbo, cycle),
            yuko.look(tagawa, tanbo),
            yuko.ask(tagawa, "試験をサボったことを咎める"),
            tagawa.reply(yuko, hiyori),
            )
    sc3 = ma.scene("学業と仕事",
            yuko.talk(tagawa, "将来"),
            tagawa.talk(yuko, "将来に試験が大事か"),
            yuko.reply(tagawa, "大事と思う"),
            tagawa.talk(yuko, "大事と思わない"),
            tagawa.talk(yuko, "日和の方が大事だ"),
            tagawa.ask(yuko, myhiyori),
            yuko.reply(tagawa).non(),
            yuko.be(myhouse, examday.elapsed_day(hour=20)),
            yuko.think(myfuture),
            yuko.talk("わかんない"),
            yuko.have(futurepaper, "お嫁さんを消す"),
            )
    return ma.story("自分の将来", sc1, sc2, sc3)

def ep_myhiyori(ma: Master):
    yuko, tagawa, eri, granpa, mam = ma.yuko, ma.tagawa, ma.eri, ma.granpa, ma.mam
    gwday = ma.gwday
    tahouse, myhouse = ma.tahouse, ma.myhouse
    myhiyori, myfuture = ma.myhiyori, ma.myfuture
    futurepaper = ma.futurepaper
    sc1 = ma.scene("答えは見えない",
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
            yuko.look(myfuture).want(),
            )
    sc2 = ma.scene("告白と自分日和",
            yuko.go(tahouse, gwday.elapsed_day(day=1)),
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
            futurepaper.be("看護師と書かれている").de(ma.f_future),
            )
    return ma.story("自分日和", sc1, sc2)


# main
def master():
    ma = Master("project hiyori")
    ma.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    ma.set_flags(FLAGS)
    return ma

def story(ma: Master):
    return ma.story("田川日和と恋の雨",
            ep_intro(ma),
            ep_tagawa(ma),
            ep_future(ma),
            ep_myhiyori(ma),
            )

def main(): # pragma: no cover
    return build_to_story(story(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

