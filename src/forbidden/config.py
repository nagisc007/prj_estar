# -*- coding: utf-8 -*-
"""Config: The forbidden love
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("doc", "椙村,迅", 45, "male", "博士", "me:僕:mirei:実麗:eri:大滝さん"),
        ("eri", "大滝,衣里", 27, "female", "研究助手", "me:わたし:S:衣里:momoko:桃子さん:doc:教授:nabe:田辺"),
        # sub
        ("momoko", "村野,桃子", 30, "female", "研究助手", "me:私:eri:衣里:doc:椙村さん:nabe:田辺さん"),
        ("mirei", "椙村,実麗", 35, "female", "彼女", "me:私"),
        ("nabe", "田辺,裕三", 44, "male", "研究助手", "me:俺:doc:椙村:momoko:村野:eri:大滝"),
        # family
        ("dad_doc", "椙村父", 78, "male", "研究者", "me:私"),
        # mob
        )

STAGES = (
        # Area
        # Place
        ("labo", "代替臓器研究所"),
        ("myhome", "椙村の家"),
        # Part
        ("mainroom", "椙村研究チーム研究室Ａ"),
        ("canfroom", "カンファレンスルーム"),
        ("lab_short", "代臓研"),
        ("cafe", "カフェテリア"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("image", "回想"),
        # sub
        )

ITEMS = (
        # main
        # sub
        )

INFOS = (
        # theme
        # main
        ("AGE", "AGEs生成"),
        ("name_age", "advanced glycation end products"),# NOTE: 終末糖化産物、後期糖化生成物
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
