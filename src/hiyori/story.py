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
        )

DAYS = (
        ("sunnyday", "天気な日", 4, 15, 2019),
        )

ITEMS = (
        ("tractor", "トラクター"),
        )

WORDS = (
        ("hiyori", "田川日和"),
        )


# episodes
def ep1(ma: Master):
    yuko, tagawa = ma.yuko, ma.tagawa
    sunnyday = ma.sunnyday
    classroom = ma.classroom
    tanbo = ma.tanbo
    return ma.story("Intro",
            yuko.be(classroom, sunnyday),
            yuko.look(tagawa, "サボる"),
            yuko.go(tagawa, tanbo),
            yuko.talk(tagawa, "将来"),
            yuko.know(tagawa, "サボる理由").want(),
            )

def ep2(ma: Master):
    return ma.story("Middle")

def ep3(ma: Master):
    return ma.story("Climax")

def ep4(ma: Master):
    yuko, tagawa = ma.yuko, ma.tagawa
    return ma.story("End",
            yuko.talk(tagawa, "自分日和"),
            )


# main
def master():
    ma = Master("project hiyori")
    ma.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    return ma

def story(ma: Master):
    return ma.story("田川日和と恋の雨",
            ep1(ma),
            ep2(ma),
            ep3(ma),
            ep4(ma),
            )

def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

