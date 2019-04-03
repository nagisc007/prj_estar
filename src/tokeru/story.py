# -*- coding: utf-8 -*-
"""Story that a mercenary's heart was melted by something.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')

# import libs
from storybuilder.builder.base import ActType, Act, Must, Done, Title, Description
from storybuilder.builder.base import Person, Stage, Item, DayTime
from storybuilder.builder.tools import output, output_md

# define characters
class Romus(Person):
    def __init__(self):
        super().__init__("ロムス", 28, "male", "傭兵")


class Milia(Person):
    def __init__(self):
        super().__init__("ミリア", 20, "female", "漁師の娘")


class Mila(Person):
    def __init__(self):
        super().__init__("ミラ", 108, "female", "スライム")


class Monsters(Person):
    def __init__(self):
        super().__init__("魔物たち", 99, "male", "魔物")


# define stages
class ArmgardContinent(Stage):
    def __init__(self):
        super().__init__("アルムガルド大陸", "巨大な島国。中央に魔の島が出現した。")


class RathoreKingdom(Stage):
    def __init__(self):
        super().__init__("ラトレー王国", "アルムガルドを治める王国")


class DoraVila(Stage):
    def __init__(self):
        super().__init__("ドーラ村", "ラトレー王国の西側にある漁村")


class MtMegido(Stage):
    def __init__(self):
        super().__init__("メギド山脈", "ラトレー南方に広がる険しい山脈")


class ACave(Stage):
    def __init__(self):
        super().__init__("洞窟", "メギド山脈にある横穴")


class MerleVila(Stage):
    def __init__(self):
        super().__init__("メルレ村", "メギド山脈の麓の村")


# define items
class KnightSword(Item):
    def __init__(self):
        super().__init__("騎士の剣", "ラトレー騎士団の者に与えられる支給品。柄に紋章がある")


class EngageRing(Item):
    def __init__(self):
        super().__init__("婚約指輪", "ロムスの造った不格好な金属製の指輪")


class HerbSoup(Item):
    def __init__(self):
        super().__init__("薬草スープ", "薬草を似た汁")


# define daytimes
class MonsterDay(DayTime):
    def __init__(self):
        super().__init__("魔物に囲まれた日", mon=2, day=20, year=999+8)


class NurseDays(DayTime):
    def __init__(self):
        super().__init__("介抱された日々", mon=2, year=999+8)


class DevilsDay(DayTime):
    def __init__(self):
        super().__init__("魔物が現れた日", mon=9, day=9, year=999)


class FindDay(DayTime):
    def __init__(self):
        super().__init__("見つけた日", mon=3, day=10, year=999+8)


# episodes
def ep_brokenbody(megido, monsd, romus, monsters):
    '''Episode builded as a broken body.
    '''
    return (
            Must(romus, "魔物退治"),
            Done(romus, "落下した"),
            megido.desc("雪が降り積もる険しい山中"),
            monsd.desc("魔物が泳いでいるような分厚い雪雲の下"),
            romus.act("山に入った"),
            monsters.act("{}を取り囲んだ".format(romus.name)),
            romus.act("応戦した"),
            romus.act("崖から足を踏み外した"),
            )


def ep_comeloose(cave, nursd, romus, mila, milia, soup):
    '''Episode builded as a come loose his heart.
    '''
    return (
            Must(romus, "体力回復"),
            Done(romus, "回復した"),
            cave.desc("薄暗く何も見えないが、岩肌から洞窟と感じた"),
            nursd.desc("何日眠っていたか分からない"),
            romus.act("目覚める"),
            mila.act("{}に{}を与えた".format(romus.name, soup.name)),
            )

def ep_meltsomething(cave, findd, romus, mila, milia, ring):
    '''Episode builded as a melt something.
    '''
    return (
            Must(romus, "敵討ち"),
            Done(romus, "スライムに溶かされる"),
            romus.act("外に出た"),
            findd.desc("少し雪が溶けかかっていた"),
            cave.desc("洞窟の外は麓の緑が広がっていた"),
            mila.act("女の姿をしていた"),
            romus.tell("お前は……魔物だったのか"),
            romus.act("{}の体内に{}を見つけた".format(mila.name, ring.name)),
            romus.tell("お前が{}を！".format(milia.name)),
            )


# main
def story():
    '''Story builded.

    Returns:
        tuple:obj:`Act`: story actions.
    '''
    # characters
    romus = Romus()
    milia = Milia()
    mila = Mila()
    monsters = Monsters()
    # stages
    dora = DoraVila()
    merle = MerleVila()
    megido = MtMegido()
    cave = ACave()
    # items
    ksword = KnightSword()
    ring = EngageRing()
    soup = HerbSoup()
    # days
    monsd = MonsterDay()
    nursd = NurseDays()
    findd = FindDay()

    return ep_brokenbody(megido, monsd, romus, monsters) \
           + ep_comeloose(cave, nursd, romus, mila, milia, soup) \
           + ep_meltsomething(cave, findd, romus, mila, milia, ring)


def main(is_debug=True):
    '''Main function.

    Returns:
        True: if completed the process to build and output a story.
    '''
    STORY_FILE = 'slimelove'

    mystory = story()

    output(mystory, is_debug=is_debug) # output to the console
    output_md(mystory, STORY_FILE, is_debug=is_debug) # output to a markdown file

    return True


if __name__ == '__main__':
    import sys
    sys.exi(main())

