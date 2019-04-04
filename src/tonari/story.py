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
            yuno.go(univ, on=meetday),
            univ.explain("都内。目黒区あたり"),
            univ.explain("キャンパスは騒然"),
            girls.look("集まっている"),
            yuno.look("警官の姿"),
            ma.comment("悠乃の性格が人を避けがちと示す"),
            yuno.feel("貧血").set_flag("cancer"),
            yuno.enter(univ, to=hall),
            hall.explain("階段教室に生徒はまばら"),
            meetday.explain("一時間目が始まる"),
            yuno.sit(something(), "隣に").non(),
            girls.talk(about=ghost).set_flag("ghost"),
            yuno.be("慣れている", of="色々言われること"),
            girls.talk(about=rumor).set_flag("murder"),
            girls.enjoy("男子と談笑するカップル"),
            yuno.thinkof("羨ましくないし").set_flag("lover"),
            lecture.talk("栄枯盛衰", "剣城財閥も破産申請").set_flag("money"),
            )
    sc2 = ma.scene("幽霊席",
            ghost.explain("彼女の隣に誰も座らないことからこう呼ばれた"),
            yuno.curious(about=ghost),
            yuno.know(forgotten).must(),
            meetday.explain("今日は午前中だけだった"),
            yuno.go(station),
            yuno.ride(bus),
            ma.combine(
                yuno.sit().non(),
                yuno.be("自分の隣がいつも空くから"),
                ),
            yuno.notice(kenjo, "不審者").set_flag("oldman"),
            )
    sc3 = ma.scene("老紳士は座る",
            station.explain("駅前の人の多さ"),
            yuno.arrive(station),
            yuno.notice(kenjo, "ついてきている"),
            yuno.ride(train),
            kenjo.sit(by=yuno).set_deflag("oldman"),
            )
    return ma.story("冒頭", sc1, sc2, sc3)

def ep_oldman(ma: Master,
        yuno: Person, kenjo: Person, mitsuro: Person, suitman: Person,
        ghost: Word, promise: Word,
        meetday: DayTime, pastday: DayTime,
        train: Stage, chicenter: Stage):
    sc1 = ma.scene("自己紹介",
            yuno.ride(train, on=meetday),
            yuno.meet(kenjo),
            ma.comment("丁寧な印象を与えること"),
            kenjo.greet(yuno),
            kenjo.ask(yuno, about=ghost),
            yuno.reply(),
            yuno.ask(kenjo, "記者かどうか"),
            kenjo.deny(),
            kenjo.talk(yuno, about=ghost),
            yuno.hear(ghost, frm=kenjo),
            )
    sc2 = ma.scene("幽霊席の事情",
            kenjo.talk(yuno, about="剣城財閥"),
            kenjo.talk(yuno, about="跡継ぎがいない").set_deflag("lover"),
            kenjo.talk(yuno, "ある事情で隣の席に誰も座らせないようにしていた"),
            yuno.wonder("事情", "方法"),
            kenjo.teach(yuno, about=suitman),
            suitman.greet(yuno),
            yuno.remember("今までに見たことがある", suitman),
            kenjo.talk("今日で終わり", ghost),
            kenjo.explain("資金が尽きた").set_deflag("money"),
            kenjo.talk(yuno, "ある方の依頼だった"),
            yuno.wonder("過去形"),
            kenjo.ask(yuno, "彼のことを覚えているか", mitsuro),
            kenjo.explain(yuno, "彼の遺言", mitsuro),
            yuno.reply("聞き返す"),
            kenjo.talk(yuno, "彼は亡くなった", mitsuro),
            )
    sc3 = ma.scene("遺言と約束",
            kenjo.ask(about=pastday),
            kenjo.talk(yuno, pastday, chicenter, "当時通っていた"),
            kenjo.talk(yuno, "彼の隣", of=mitsuro),
            yuno.remember(promise).set_deflag("ghost"),
            yuno.remember(mitsuro),
            mitsuro.explain("女の子みたいな線の細い少年"),
            mitsuro.be(yuno, "いつも隣だった"),
            yuno.promise(mitsuro, promise, on=pastday),
            mitsuro.tell(yuno, "ずっと隣で君を守ってあげるね"),
            yuno.sad("泣いていた"),
            )
    return ma.story("老紳士", sc1, sc2, sc3)

def ep_ordinary(ma: Master,
        yuno: Person, kenjo: Person, mitsuro: Person, bigman: Person, doctor: Person,
        sick: Word, yunowill: Word,
        nextday: DayTime, futureday: DayTime,
        bus: Stage, hospital: Stage, cemetary: Stage):
    sc1 = ma.scene("隣に座る男",
            yuno.ride(bus, on=nextday),
            bigman.sit(by=yuno),
            bigman.stick(yuno, by="ナイフ").set_deflag("murder"),
            yuno.bleed(),
            yuno.do("倒れた"),
            )
    sc2 = ma.scene("発覚する病",
            yuno.wake(hospital),
            doctor.talk(yuno, "症状"),
            yuno.ask("傷のこと"),
            doctor.reply("それは問題ない"),
            yuno.wonder(),
            doctor.talk(sick),
            yuno.be(sick, on=futureday),
            doctor.talk(yuno, sick, "進行性のガン").set_deflag("cancer"),
            sick.explain("進行性の胃がん", "未分化型で遅いと五年生存率が10％未満"),
            yuno.die().must(),
            )
    sc3 = ma.scene("眠る場所は",
            ma.comment("ここから視点は剣城に"),
            cemetary.explain("沢山の墓石が整然と並んでいる"),
            yuno.talk("彼の隣に埋めて下さい", of=mitsuro, to=kenjo),
            yuno.beg(kenjo, of=yunowill),
            kenjo.remember(yunowill),
            yuno.bury("彼の隣", of=mitsuro),
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
