# -*- coding: utf-8 -*-
"""Config: The another me
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
        ("sayama", "砂山,幸子", 20, "female", "大学生", "me:わたし"),
        ("matsumoto", "松本,亘", 20, "male", "大学生"),
        # work
        ("arase", "荒瀬,省二", 40, "male", "現場監督", "me:ボク"),
        ("minori", "鈴森,実里", 45, "female", "ベテラン派遣社員", "me:私"),
        # others
        ("asumi", "金井,亜純", 19, "female", "パート"),
        # family
        ("mother", "岩根,朝子", 40, "female", "パート"),
        ("father", "岩根,雪雄", 50, "male", "電気店"),
        # family (shota)
        ("sho_mam", "宮内,母", 45, "female", "母"),
        ("sho_dad", "宮内,父", 52, "male", "父"),
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
        ("office", "パート事務所"),
        ("famires", "ファミレス"),
        ("ma_apart", "松本のアパート"),
        ("hishome", "翔太郎の実家"),
        # Part
        ("living", "リビング"),
        ("classroom", "教室"),
        )

DAYS = (
        # main
        ("childhood", "幼少期"),
        ("current", "現在", 6,20, 2019),
        ("encounter", "出会った日"),
        ("proposed", "プロポーズされた日", 7,7, 2019),
        ("empty", "誰もいなくなった日"),
        ("married", "結婚した未来"),
        ("shotadead", "翔太郎が亡くなった日"),# NOTE: 10年前
        # sub
        )

ITEMS = (
        # main
        ("another", "もう一人の自分"),
        ("his_phone", "翔太郎の携帯（ガラケー）"),
        # sub
        )

INFOS = (
        # chapter 1
        ("relation", "人付き合い"),
        ("circle", "サークル（ゴミ拾い）"),
        ("vanish_another", "アナザー消したい"),
        ("partwork", "パートの仕事"),
        ("stalker", "ストーカーの噂"),
        # chapter 2
        ("proposed", "プロポーズされた"),
        # chapter 3
        ("meeting", "自分会議"),
        ("birth_another", "アナザー誕生"),
        # chapter 4
        ("look_another", "アナザー感知人"),
        # chapter 5
        ("shota_truth", "翔太郎の真実"),
        ("another_truth", "アナザーの意味"),
        )

FLAGS = (
        )

THEMES = {
        "problem": "自分の分身をどうにかする",
        }

MOTIFS = {
        }
