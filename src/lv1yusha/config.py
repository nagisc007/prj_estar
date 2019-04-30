# -*- coding: utf-8 -*-
"""Config: lv1 yusha.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        ("hero", "アリエル", 16, "male", "勇者", "me:僕", "英雄の息子"),
        ("hero99", "アリエル９９", 20, "male", "勇者", "me:俺", "レベル99になったアリエル"),
        ("king", "アルアバン王", 46, "male", "国王", "me:儂", "アルアバンの国王"),
        ("daemon1", "アークド・ダエモン", 99, "monster", "魔物", "me:オレサマ"),
        )


STAGES = (
        ("alaban", "アルアバン", "英雄が生まれた島国"),
        ("castle", "アルアバン城"),
        ("herohome", "勇者の家"),
        ("field1", "アルアバン周辺"),
        )


DAYS = (
        ("first", "旅立ちの日"),
        )


ITEMS = (
        ("brokens", "折れた剣", "父の形見"),
        )


INFOS = (
        ("voyage", "旅立ち"),
        ("coop", "協力"),
        ("deadly", "死にそうになる"),
        ("reviveboss", "魔王復活"),
        ("callhero", "王の呼び出し"),
        ("worldsecret", "世界の秘密"),
        )


FLAGS = (
        )

