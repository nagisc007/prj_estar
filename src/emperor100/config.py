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
        ("child", "リドリー", 5, "male", "王子", "me:ボク"),
        )

STAGES = (
        ("kingdom", "アワローヌ"),
        ("castle", "アワローヌ城"),
        ("hisroom", "ヘレウドの居室"),
        ("balcony", "バルコニィ"),
        ("hall", "玄関ホール"),
        )

DAYS = (
        ("returnemp", "帰還日"),
        ("dead", "崩御日"),
        ("ceremony", "儀式日"),
        )

ITEMS = (
        ("tsword", "宝剣"),
        )

INFOS = (
        ("pope", "教皇"),
        ("marda", "マルダ教"),
        ("pregnancy", "妊娠"),
        ("childbirth", "息子出産"),
        ("peace_nego", "和平交渉"),
        ("badcondition", "体調不良"),
        ("ceremony", "儀式"),
        ("enthrone", "即位の儀式"),
        ("throne", "即位"),
        ("emperor100", "百代目皇帝"),
        ("portchara", "人格移植"),
        ("lion_dead", "皇帝の死"),
        ("emperor_bug", "皇帝継承のバグ"),
        ("milea_mind", "ミレアの決意"),
        ("his_mind", "彼の決意"),
        # event
        ("murder_mam", "母殺害疑惑"),
        )

FLAGS = (
        )

