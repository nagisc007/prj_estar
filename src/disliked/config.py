# -*- coding: utf-8 -*-
"""Config: Disliked
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("satomi", "大邑,聡美", 33, "female", "会社員", "me:私:ayano:文乃"),
        ("bot", "夫ボット", 99, "male", "緩和ボット", "me:ボク:satomi:聡美:ayano:文乃"),
        # sub
        ("taka", "大邑,隆文", 32, "male", "研究者", "me:僕"),
        ("brian", "田中,ブライアン", 35, "male", "研究者", "me:オレ:taka:隆文"),
        # family
        ("ayano", "大邑,文乃", 5, "female", "子供", "me:あや:satomi:ママ:taka:パパ:bot:ターくん"),
        # mob
        )

STAGES = (
        # Area
        ("Tokyo", "東京都"),
        ("Tamachi", "田町"),
        # Place
        ("myhome", "大邑家"),
        ("geosys", "ジオシステムズ"),
        # Part
        ("living", "リビング"),
        )

DAYS = (
        # main
        ("dead", "夫が死んだ日"),
        ("current", "現在"),
        # sub
        )

ITEMS = (
        # main
        ("aibot", "喪失緩和ボット"),
        ("botname", "ローレル"),
        ("botna_eng", "ＬｏＲｅｌ"),
        ("botna_long", "Lost Relieved bot"),
        ("suki", "嫌い"),
        ("kirai", "好き"),
        ("AI", "エキスパート型人工知能"),
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
