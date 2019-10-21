# -*- coding: utf-8 -*-
"""Config: the understander
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("beni", "紅男", 17, "female", "高校生",
            "me:ボク:saku:桜庭:mia:美亜"),
        ("saku", "桜庭,名前", 17, "male", "高校生",
            "me:俺:beni:ベニ"),
        ("mia", "美亜", 17, "female", "高校生",
            "me:わたし:beni:紅男:saku:桜庭"),
        # sub
        # mob
        )

STAGES = (
        # Area
        ("Saitama", "埼玉県"),
        ("saitama", "さいたま市"),
        # Place
        ("highschool", "高校"),
        # Part
        ("classroom", "教室"),
        ("beniroom", "紅男の部屋"),
        ("sakuhome", "桜庭の家"),
        ("miaroom", "美亜の部屋"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("date1", "紅男と桜庭のデート日", 11,23, 2019),
        ("famires1", "ファミレス会議日", 11,27, 2019),
        ("xmaseve", "クリスマスイブ", 12,24, 2019),# NOTE: 火曜
        # sub
        )

ITEMS = (
        # main
        ("megane", "眼鏡"),
        ("frill", "フリル"),
        # sub
        )

INFOS = (
        # theme
        # main
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
