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
        ("yuno", "坂見悠乃", 21, "female", "大学生", "わたし"),
        ("kenjo", "剣城鋼太郎", 68, "male", "謎の老人", "私"),
        ("mitsuro", "剣城光朗", 6, "male", "当時の同級生", "ぼく"),
        ("girls", "大学の女子", 20, "female", "大学生"),
        )

STAGES = (
        ("univ", "九段下大学", "悠乃が通う大学"),
        ("train", "電車", "剣城と出遭う電車"),
        ("bus", "バス", "隣席に男が乗ってくる"),
        ("childcenter", "児童館", "小さい頃によく遊んだ場所"),
        )

DAYS = (
        ("meetday", "出会いの日", 4, 24, 2019,),
        ("pastday", "幼少期", 6, 1, 2004),
        )

ITEMS = (
        )

WORDS = (
        ("ghost_seat", "幽霊席", "悠乃の隣がいつも空席なので、こう呼ばれる"),
        ("forgotten", "悠乃が忘れていること"),
        ("promise", "彼との約束", "幼い日にした二人の約束"),
        ("sick", "病気", "悠乃が罹り、死亡する"),
        )


def sdb():
    return StoryDB(CHARAS, STAGES, DAYS, ITEMS, WORDS)


# episodes
def ep_intro(ma: Master,
        yuno: Person, girls: Person,
        gseat: Word, forgotten: Word,
        mday: DayTime,
        univ: Stage):
    return ma.story("冒頭",
            yuno.go(univ, on=mday),
            girls.talk(about=gseat).set_flag("ghost"),
            yuno.curious(about=gseat),
            yuno.know(forgotten).must(),
            )

def ep_oldman(ma: Master,
        yuno: Person, oldman: Person,
        gseat: Word, promise: Word,
        mday: DayTime,
        train: Stage):
    return ma.story("老紳士",
            yuno.ride(train, on=mday),
            yuno.meet(oldman),
            oldman.take(yuno, about=promise),
            yuno.remember(promise).set_deflag("ghost"),
            )

def ep_ordinary(ma: Master,
        yuno: Person, oldman: Person,
        sick: Word,
        bus: Stage):
    return ma.story("訪れた日常",
            yuno.be(sick),
            yuno.die().must(),
            yuno.talk("彼の隣に埋めて下さい", to=oldman),
            )

    
# main
def story():
    ma = Master("my side mystery")
    db = sdb()
    return ma.story("わたしの隣席はいつも不在",
            ep_intro(ma, db.yuno, db.girls,
                db.ghost_seat, db.forgotten,
                db.meetday,
                db.univ),
            ep_oldman(ma, db.yuno, db.kenjo,
                db.ghost_seat, db.promise,
                db.meetday,
                db.train),
            ep_ordinary(ma, db.yuno, db.kenjo,
                db.sick,
                db.bus),
            )


def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
