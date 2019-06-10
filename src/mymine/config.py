# -*- coding: utf-8 -*-
"""Config: I am my mine
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("kyoko", "岩根,今日子", 20, "female", "大学生",
            "me:私"),
        ("shota", "宮内,翔太郎", 25, "male", "無職",
            "me:俺"),
        # univ
        ("matsumoto", "松本,亘", 20, "male", "大学生"),
        # others
        ("asumi", "金井,亜純", 19, "female", "パート"),
        # family
        ("mother", "岩根,朝子", 40, "female", "パート"),
        ("father", "岩根,雪雄", 50, "male", "電気店"),
        # anothers
        ("child_kyoko", "岩根,きょう子", 10, "female", "小学生", "me:わたし"),
        ("student_kyoko", "岩根,キョウコ", 15, "female", "中学生", "me:ワタシ"),
        ("univ_kyoko", "岩根,明日子", 20, "female", "大学生", "me:私"),
        )

STAGES = (
        # Area
        ("Hokkaido", "北海道"),
        ("Sapporo", "札幌"),
        # Place
        ("univ", "大学"),
        ("apart", "アパート"),
        ("manshion", "マンション"),
        ("famires", "ファミレス"),
        ("ma_apart", "松本のアパート"),
        # Part
        ("living", "リビング"),
        ("classroom", "教室"),
        )

DAYS = (
        # main
        ("childhood", "幼少期"),
        ("current", "現在"),
        ("encounter", "出会った日"),
        ("proposed", "プロポーズされた日"),
        ("married", "結婚した未来"),
        # sub
        )

ITEMS = (
        ("another", "もう一人の自分"),
        ("circle", "サークル"),
        )

INFOS = (
        # chapter 1
        # chapter 2
        ("proposed", "プロポーズされた"),
        # chapter 3
        ("meeting", "自分会議"),
        ("birth_another", "アナザー誕生"),
        # chapter 4
        ("look_another", "アナザー感知人"),
        )

FLAGS = (
        )

THEMES = {
        "problem": "自分の分身をどうにかする",
        }

MOTIFS = {
        }
