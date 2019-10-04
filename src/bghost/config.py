# -*- coding: utf-8 -*-
"""Config: The blue ghost
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("ryoma", "涼風,良馬", 17, "male", "高校生", "me:僕"),
        ("miko", "水琴", 17, "female", "高校生", "me:わたし"),
        # sub
        ("ghost", "ゴースト", 10, "male", "幽霊", "me:ボク"),
        ("takeru", "土門,猛", 17, "male", "高校生", "me:俺"),
        ("akari", "柘植,灯里", 17, "female", "高校生", "me:私"),
        ("teacher2", "高校の担任", 32, "female", "高校教師", "me:私"),
        ("teacher1", "小学校の時の教師", 65, "male", "元小学校教師", "me:ぼく"),
        # family
        # mob
        )

STAGES = (
        # Area
        ("Nagano", "長野県"),
        # Place
        ("highschool", "県立高校"),
        ("myhome", "自宅"),
        # Part
        ("onstreet", "路上"),
        ("classroom", "教室"),
        ("myroom", "自室"),
        )

DAYS = (
        # main
        ("current", "現在"),
        # sub
        )

ITEMS = (
        # main
        # sub
        )

INFOS = (
        # theme
        # main
        ("oldclub", "同好会"),# NOTE: 小学生の時の科学倶楽部
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

TITLES = {
        "ch01": "同窓会ファースト",
        "ch02": "幽霊アシスト",
        "ch03": "崩壊バースト",
        "ch04": "思い出ダイジェスト",
        "ch05": "青春ゴースト",
        }
