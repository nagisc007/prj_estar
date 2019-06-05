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
            "me:わたし"),
        ("shota", "宮内,翔太郎", 25, "male", "無職",
            "me:俺"),
        # univ
        ("matsumoto", "松本,亘", 20, "male", "大学生"),
        # others
        ("asumi", "金井,亜純", 19, "female", "パート"),
        # family
        ("mother", "岩根,朝子", 40, "female", "パート"),
        ("father", "岩根,雪雄", 50, "male", "電気店"),
        )

STAGES = (
        # Area
        ("Hokkaido", "北海道"),
        ("Sapporo", "札幌"),
        # Place
        ("univ", "大学"),
        ("apart", "アパート"),
        ("manshion", "マンション"),
        # Part
        ("living", "リビング"),
        )

DAYS = (
        # main
        ("childhood", "幼少期"),
        ("current", "現在"),
        ("encounter", "出会った日"),
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
        )

FLAGS = (
        )

THEMES = {
        "problem": "自分の分身をどうにかする",
        }

MOTIFS = {
        }
