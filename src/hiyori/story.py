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
        )

STAGES = (
        ("school", "高校"),
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
        )

WORDS = (
        ("hiyori", "田川日和"),
        ("myhiyori", "自分日和"),
        ("reason", "サボる理由"),
        ("circs", "田川の事情"),
        ("myfuture", "自分の将来"),
        )


# episodes
def ep_intro(ma: Master):
    yuko, tagawa = ma.yuko, ma.tagawa
    sunnyday = ma.sunnyday
    classroom = ma.classroom
    tanbo = ma.tanbo
    reason = ma.reason
    return ma.story("田川日和",
            yuko.be(classroom, sunnyday),
            yuko.look(tagawa, "サボる"),
            yuko.go(tagawa, tanbo),
            yuko.talk(tagawa, "将来"),
            yuko.know(tagawa, reason).want(),
            sunnyday.explain("翌日もよく晴れた"),
            tagawa.be(classroom).non(),
            yuko.think("サボる決断"),
            yuko.go("学校を抜け出す"),
            )

def ep_tagawa(ma: Master):
    yuko, tagawa = ma.yuko, ma.tagawa
    sunnyday = ma.sunnyday
    tanbo = ma.tanbo
    reason = ma.reason
    return ma.story("学校外の田川",
            yuko.look(tagawa, "どこにいるか"),
            yuko.know(tagawa, reason).want(),
            yuko.go(tagawa, "尾行"),
            yuko.look(tagawa, tanbo, sunnyday),
            yuko.talk(tagawa, reason),
            tagawa.reply(yuko, reason),
            yuko.know(tagawa, reason),
            )

def ep_future(ma: Master):
    yuko, tagawa, takemura = ma.yuko, ma.tagawa, ma.takemura
    classroom = ma.classroom
    rainyday, examday = ma.rainyday, ma.examday
    myfuture, reason = ma.myfuture, ma.reason
    return ma.story("自分の将来",
            yuko.hear(tagawa, reason, rainyday),
            tagawa.be(classroom, examday).non(),
            examday.explain("試験が終わる"),
            yuko.look(tagawa),
            yuko.talk(tagawa, "試験をサボったことを咎める"),
            tagawa.talk(yuko, "将来に試験が大事か"),
            yuko.reply(tagawa, "大事と思う"),
            yuko.talk(takemura, "相談"),
            yuko.think(myfuture),
            )

def ep_myhiyori(ma: Master):
    yuko, tagawa = ma.yuko, ma.tagawa
    gwday = ma.gwday
    tahouse, myhouse = ma.tahouse, ma.myhouse
    myhiyori, myfuture = ma.myhiyori, ma.myfuture
    return ma.story("自分日和",
            yuko.be(myhouse, gwday),
            yuko.think(myfuture),
            yuko.look(myfuture).want(),
            yuko.go(tahouse, gwday),
            tagawa.talk(yuko, "自分の日和を持てよ"),
            yuko.talk(tagawa, myhiyori),
            yuko.talk(tagawa, "告白"),
            yuko.look(myhiyori),
            )


# main
def master():
    ma = Master("project hiyori")
    ma.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    return ma

def story(ma: Master):
    return ma.story("田川日和と恋の雨",
            ep_intro(ma),
            ep_tagawa(ma),
            ep_future(ma),
            ep_myhiyori(ma),
            )

def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

