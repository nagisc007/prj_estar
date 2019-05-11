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
        ("soldier", "兵士１", 30, "male", "兵士"),
        ("people", "国民", 99, "male", "国民"),
        ("believer", "信者", 50, "male", "信者"),
        ("albert", "アルバート", 25, "male", "近衛兵", "me:オレ"),
        ("runolf", "ルノルフ", 68, "male", "近衛兵長", "me:儂"),
        ("marf", "マルフ", 52, "male", "宰相", "me:私"),
        )

STAGES = (
        # country
        ("kingdom", "アワローヌ"),
        ("randole", "ランドール"),
        # places
        ("castle", "アワローヌ城"),
        ("hisroom", "ヘレウドの居室"),
        ("office", "執務室"),
        ("balcony", "バルコニィ"),
        ("hall", "玄関ホール"),
        ("cathedral", "聖堂"),
        ("lab", "実験室"),
        )

DAYS = (
        ("returnemp", "帰還日"),
        ("dead", "崩御日"),
        ("ceremony", "儀式日"),
        )

ITEMS = (
        ("tsword", "宝剣"),
        ("god", "マルダ神"),
        )

INFOS = (
        # themes
        ("which_important", "国の繁栄か己の最愛の人か"),
        # common
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
        ("lion_word", "前王の言葉"),
        ("emp_ceremony", "皇位継承の儀式"),
        ("moon", "白磁の月"),
        # event
        ("murder_mam", "母殺害疑惑"),
        )

FLAGS = (
        )

