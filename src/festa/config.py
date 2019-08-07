# -*- coding: utf-8 -*-
"""Config: Night festa
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("hikawa", "氷川,夢美", 27, "female", "教師", "me:私:sudo:須藤君"),
        ("takao", "高雄,健輔", 25, "male", "かき氷売り", "me:俺"),
        ("sudo", "須藤,正嗣", 17, "male", "高校生", "me:僕"),
        # sub
        ("kirimura", "霧村,豊", 35, "male", "教師", "me:俺:hikawa:氷川:miyako:斎賀:aya:千覧"),
        # mob
        )

STAGES = (
        # Area
        ("Nagano", "長野県"),
        ("hometown", "瀬能市"),
        # Place
        ("shrine", "神社"),
        ("hightschool", "高校"),
        # Part
        ("classroom", "教室"),
        ("staffroom", "職員室"),
        )

DAYS = (
        # main
        ("current", "現在"),
        # sub
        )

ITEMS = (
        # main
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
