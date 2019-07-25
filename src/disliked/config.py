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
        ("satomi", "大邑,聡美", 33, "female", "会社員", "me:私"),
        ("bot", "夫ボット", 99, "male", "緩和ボット", "me:ボク"),
        # sub
        ("taka", "大邑,隆文", 32, "male", "研究者", "me:僕"),
        ("brian", "田中,ブライアン", 35, "male", "研究者", "me:オレ"),
        # family
        # mob
        )

STAGES = (
        # Area
        ("Tokyo", "東京都"),
        ("Tamachi", "田町"),
        # Place
        ("myhome", "大邑家"),
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
