# -*- coding: utf-8 -*-
"""Config: the letter
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("hiroki", "平松,博樹", 35, "male", "技師", "me:僕:S:博樹"),
        ("yoko", "平松,葉子", 34, "female", "SE", "me:私"),
        # sub
        ("chief", "課長", 45, "male", "上司", "me:俺"),
        ("sister", "葉子の妹", 30, "female", "保育士", "me:わたし"),
        ("myson", "息子", 10, "male", "子ども", "me:ぼく"),
        ("hiroshi", "平松,博史", 35, "male", "技師", "me:僕:S:博史"),
        ("helper", "助手", 29, "female", "助手", "me:わたし"),
        # mob
        ("doctor", "医師", 44, "male", "医師", "me:私"),
        )

STAGES = (
        # Area
        # Place
        ("myhome", "自宅"),
        ("myoffice", "会社", "金型工場"),
        ("hospital", "病院"),
        ("labo", "研究所"),
        # Part
        ("onstreet", "路上"),
        ("living", "リビング"),
        ("wooddeck", "ウッドデッキ"),
        ("consulroom", "診察室"),
        ("ceremonyhall", "葬儀場"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("warming", "幸せだった日々"),
        ("consul1", "診察結果日"),
        ("model1", "モデリング初日"),
        ("dead", "彼女が亡くなった日"),
        ("birth", "息子が生まれた日"),
        ("future", "息子が大きくなった未来"),
        # sub
        )

ITEMS = (
        # main
        # sub
        )

INFOS = (
        # theme
        # main
        ("ALS", "筋萎縮性側索硬化症"),
        ("als", "ALS"),
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
