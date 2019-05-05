# -*- coding: utf-8 -*-
"""Config: the emperor 100
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("hero", "ヘレウド", 25, "male", "王子"),
        ("milea", "ミレア", 23, "female", "王妃"),
        ("lion", "リオン", 55, "male", "皇帝"),
        )

STAGES = (
        ("kingdom", "アワローヌ"),
        ("castle", "アワローヌ城"),
        )

DAYS = (
        ("dead", "崩御日"),
        ("ceremony", "儀式日"),
        )

ITEMS = (
        ("tsword", "宝剣"),
        )

INFOS = (
        )

FLAGS = (
        )

