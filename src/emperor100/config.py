# -*- coding: utf-8 -*-
"""Config: the emperor 100
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("hero", "ヘレウド", 25, "male", "王子", "me:私"),
        ("milea", "ミレア", 23, "female", "王妃", "me:わたし"),
        ("lion", "リオン", 55, "male", "皇帝", "me:俺"),
        ("garneth", "ガーネス", 78, "male", "教皇", "me:私"),
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
        ("ceremony", "儀式"),
        ("enthrone", "即位の儀式"),
        ("throne", "即位"),
        ("emperor100", "百代目皇帝"),
        ("portchara", "人格移植"),
        # event
        ("murder_mam", "母殺害疑惑"),
        )

FLAGS = (
        )

