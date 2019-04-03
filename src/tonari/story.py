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
        ("bigman", "大柄な男", 30, "male", "会社員"),
        ("suitman", "スーツの男", 40, "male", "剣城コーポ社員"),
        )

STAGES = (
        ("univ", "九段下大学", "悠乃が通う大学"),
        ("hall", "大学講堂", "大きな階段教室"),
        ("train", "電車", "剣城と出遭う電車"),
        ("station", "最寄り駅"),
        ("bus", "バス", "隣席に男が乗ってくる"),
        ("chicenter", "児童館", "小さい頃によく遊んだ場所"),
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
        )


def sdb():
    return StoryDB(CHARAS, STAGES, DAYS, ITEMS, WORDS)


# episodes
def ep_intro(ma: Master,
        yuno: Person, kenjo: Person, girls: Person,
        ghost: Word, forgotten: Word,
        meetday: DayTime,
        univ: Stage, hall: Stage, station: Stage, bus: Stage, train: Stage):
    return ma.story("冒頭",
            yuno.go(univ, on=meetday),
            yuno.enter(univ, to=hall),
            yuno.sit(something(), "隣に").non(),
            girls.talk(about=ghost).set_flag("ghost"),
            yuno.curious(about=ghost),
            yuno.know(forgotten).must(),
            yuno.go(station),
            yuno.ride(bus),
            yuno.notice(kenjo, "不審者"),
            yuno.arrive(station),
            yuno.ride(train),
            kenjo.sit(by=yuno),
            )

def ep_oldman(ma: Master,
        yuno: Person, kenjo: Person, mitsuro: Person, suitman: Person,
        ghost: Word, promise: Word,
        meetday: DayTime, pastday: DayTime,
        train: Stage):
    return ma.story("老紳士",
            yuno.ride(train, on=meetday),
            yuno.meet(kenjo),
            kenjo.ask(yuno, about=ghost),
            kenjo.talk(yuno, about=ghost),
            yuno.hear(ghost, frm=kenjo),
            kenjo.teach(yuno, about=suitman),
            suitman.greet(yuno),
            yuno.remember(promise).set_deflag("ghost"),
            yuno.remember(mitsuro),
            yuno.promise(mitsuro, promise, on=pastday),
            mitsuro.tell(yuno, "ずっと隣で君を守ってあげるね"),
            )

def ep_ordinary(ma: Master,
        yuno: Person, kenjo: Person, mitsuro: Person, bigman: Person,
        sick: Word, yunowill: Word,
        nextday: DayTime, futureday: DayTime,
        bus: Stage):
    return ma.story("訪れた日常",
            yuno.ride(bus, on=nextday),
            bigman.sit(by=yuno),
            yuno.be(sick, on=futureday),
            yuno.die().must(),
            yuno.talk("彼の隣に埋めて下さい", of=mitsuro, to=kenjo),
            yuno.beg(kenjo, of=yunowill),
            yuno.bury("彼の隣", of=mitsuro),
            )

    
# main
def story():
    ma = Master("my side mystery")
    db = sdb()
    return ma.story("わたしの隣席はいつも不在",
            ep_intro(ma, db.yuno, db.kenjo, db.girls,
                db.ghost, db.forgotten,
                db.meetday,
                db.univ, db.hall, db.station, db.bus, db.train),
            ep_oldman(ma, db.yuno, db.kenjo, db.mitsuro, db.suitman,
                db.ghost, db.promise,
                db.meetday, db.pastday,
                db.train),
            ep_ordinary(ma, db.yuno, db.kenjo, db.mitsuro, db.bigman,
                db.sick, db.yunowill,
                db.nextday, db.futureday,
                db.bus),
            )


def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
