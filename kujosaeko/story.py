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

class KujoDad(Person):
    def __init__(self):
        super().__init__("九条父", 44, "male", "強盗", "オレ", "冴子の実父。小さい頃に離婚している")


# stages
class MasatoApart(Stage):
    def __init__(self):
        super().__init__("正人のアパート", "正人が住むアパート")


class UnivHakata(Stage):
    def __init__(self):
        super().__init__("博多大学", "架空の大学。福岡にある私立大学。")

class WestPark(Stage):
    def __init__(self):
        super().__init__("西公園", "実在する公園。福岡中央区の海べりにあり、桜の名所。")


# items
class Gun(Item):
    def __init__(self):
        super().__init__("拳銃", "重要なアイテム")

class ToyBox(Item):
    def __init__(self):
        super().__init__("おもちゃ箱", "九条冴子が大事にしている玩具の金庫")


# words
class Blagger(Word):
    def __init__(self):
        super().__init__("強盗事件")


# daytimes
class WhiteDay(DayTime):
    def __init__(self):
        super().__init__("ホワイトディ", 3, 14, 2019)

class IncidentDay(DayTime):
    def __init__(self):
        super().__init__("事件日", 3, 23, 2019, note="事件の起こる日")


# episodes
def ep_intro(ma: Master):
    return ma.story(
            )


def ep_relationship(ma: Master):
    return ma.story(
            )


def ep_incident(ma: Master):
    return ma.story(
            )

# story
def story() -> ActionGroup:
    '''Define main story.
    '''
    ma = Master("my story")
    kujo, masato, misa, dad = Kujo(), Masato(), Misa(), KujoDad()
    apart, univi, park = MasatoApart(), UnivHakata(), WestPark()
    gun = Gun()
    blagger = Blagger()
    wday, iday = WhiteDay(), IncidentDay()

    return ma.story(
            ma.title("九条冴子は返さない"),
            ep_intro(ma),
            ep_relationship(ma),
            ep_incident(ma),
            masato.be("付き合っている", kujo),
            kujo.think("何も返さない"),
            wday.explain("薄曇りの日の午後"),
            park.explain("公園の桜は雨に打たれて散々"),
            masato.want("何か返して", kujo),
            kujo.give("ない", masato),
            masato.ask("返さない理由"),
            kujo.talk("誰か別の人に返せばいつか大きくなって戻ってくる"),
            masato.tell("じゃあ俺には？"),
            kujo.tell("返さない"),
            masato.talk("口論", kujo),
            masato.go("他の女"),
            iday.explain("雨の冷たい日"),
            blagger.explain("ニュースで事件報道"),
            masato.find("彼女の部屋",gun).set_deflag(gun.name),
            kujo.talk("父親の話",masato),
            kujo.tell("いつもいっぱいあげてた", masato),
            dad.shoot("", kujo),
            masato.guard("", kujo),
            dad.catch("警察").passive(),
            )


# main
def main() -> bool:
    '''main program.
    '''
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

