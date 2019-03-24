# -*- coding: utf-8 -*-
"""The story program of kujo saeko doesn't back anything.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import ActionGroup, Stage, Item, DayTime, Word, Master
from storybuilder.builder.person import Person
from storybuilder.builder.tools import build_to_story


# characters
class Kujo(Person):
    def __init__(self):
        super().__init__("九条冴子", 21, "female", "大学生", "私", "決して返さない女")


class Masato(Person):
    def __init__(self):
        super().__init__("市村正人", 20, "male", "大学生", "俺", "九条冴子と付き合う男子")


class Misa(Person):
    def __init__(self):
        super().__init__("古峰未沙", 20, "female", "専門学校生", "わたし", "正人のバイト先の女性")

def kujo_dad():
    return Person("九条父", 44, "male", "強盗", "オレ", "冴子の実父。小さい頃に離婚している")


# stages
def masato_apart():
    return Stage("正人のアパート", "正人が住むアパート")

def univ_hakata():
    return Stage("博多大学", "架空の大学。福岡にある私立大学。")

def west_park():
    return Stage("西公園", "実在する公園。福岡中央区の海べりにあり、桜の名所。")

def misa_manshion():
    return Stage("未沙のマンション")

def kujo_apart():
    return Stage("九条のアパート")

def tutor_center():
    return Stage("家庭教師事務所")


# items
def dad_gun():
    return Item("拳銃", note="冴子が隠し持っていた父の形見")

def toy_box():
    return Item("玩具箱", "九条冴子が大事にしている玩具の金庫")


# words
def blagger():
    return Word("強盗事件")


# daytimes
def white_day():
    return DayTime("ホワイトディ", 3, 14, 2019)

def parted_day():
    return DayTime("別々の日", 3, 15, 2019, note="数日間、二人は別れたまま")

def incident_day():
    return DayTime("事件日", 3, 23, 2019)


# episodes
def ep_intro(ma: Master,
        masato: Masato, kujo: Kujo,
        park: Stage,
        day: DayTime):
    return ma.story(
            ma.title("彼女は返さない"),
            ma.comment("九条冴子の特殊性と、二人の関係性の描写"),
            masato.be("付き合っている", kujo),
            masato.want("お返し", kujo),
            masato.give("チョコ", kujo),
            masato.invite("デート", kujo),
            kujo.think("何も返さない"),
            day.explain("薄曇りの日の午後"),
            park.explain("公園の桜は雨に打たれて散々"),
            masato.want("何か返して", kujo),
            kujo.give("ない", masato),
            masato.ask("返さない理由"),
            kujo.talk("誰か別の人に返せばいつか大きくなって戻ってくる"),
            masato.tell("じゃあ俺には？"),
            kujo.tell("返さない"),
            masato.give("サンドウィッチ", kujo),
            kujo.returns("もらったサンドウィッチ", masato).negative(),
            masato.talk("口論", kujo),
            )


def ep_relationship(ma: Master,
        masato: Masato, kujo: Kujo, misa: Misa,
        toybox: Item, gun: Item,
        kapart: Stage, mapart: Stage, manshion: Stage, tutor: Stage,
        day: DayTime):
    return ma.story(
            ma.title("離れた心は取り戻せない"),
            ma.comment("二人の関係の決裂と、冴子父の事件の伏線"),
            day.explain("後日"),
            tutor.explain("バイト先の家庭教師派遣事務所"),
            masato.meet("", misa),
            misa.ask("関係", kujo),
            misa.talk("彼女の噂", kujo),
            masato.want("彼女の考え", kujo),
            masato.think("事情がある", kujo),
            masato.visit("", kapart),
            masato.ask("", toybox),
            masato.open("", toybox),
            kujo.angry("触るな", toybox).set_flag(gun.name),
            masato.talk("口論", kujo),
            kujo.talk("他の女と付き合えばいい", masato),
            misa.phone("", masato),
            misa.invite("デート", masato),
            masato.accept("彼女の申し出", misa),
            masato.go("他の女", misa),
            masato.visit("", manshion),
            masato.love("", misa),
            )


def ep_incident(ma: Master,
        masato: Masato, kujo: Kujo, misa: Misa, dad: Person,
        gun: Item, blag: Word,
        mapart: Stage, kapart: Stage,
        day: DayTime):
    return ma.story(
            ma.title("その絆は離せない"),
            ma.comment("事件と彼女が与えたもの"),
            day.explain("雨の冷たい日"),
            mapart.explain("湿気った自分の部屋"),
            masato.watch("ぼんやりとTVを"),
            blag.explain("ニュースで事件報道"),
            masato.know("", blag),
            masato.contact("", kujo),
            masato.want("助ける", kujo),
            masato.find("彼女の部屋",gun).set_deflag(gun.name),
            kujo.talk("父親の話",masato),
            kujo.tell("いつもいっぱいあげてた", masato),
            dad.shoot("", kujo),
            masato.guard("", kujo),
            dad.catch("警察").passive(),
            )

# story
def story() -> ActionGroup:
    '''Define main story.
    '''
    ma = Master("my story")
    kujo, masato, misa, dad = Kujo(), Masato(), Misa(), kujo_dad()
    mapart, kapart, manshion = masato_apart(), kujo_apart(), misa_manshion()
    park, tutor = west_park(), tutor_center()
    gun, toybox = dad_gun(), toy_box()
    blag = blagger()
    wday, pday, iday = white_day(), parted_day(), incident_day()

    return ma.story(
            ma.title("九条冴子は返さない"),
            ep_intro(ma, masato, kujo,
                park, wday),
            ep_relationship(ma, masato, kujo, misa,
                toybox, gun,
                kapart, mapart, manshion, tutor, pday),
            ep_incident(ma, masato, kujo, misa, dad,
                gun, blag,
                mapart, kapart, iday),
            )


# main
def main() -> bool:
    '''main program.
    '''
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

