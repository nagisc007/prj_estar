# -*- coding: utf-8 -*-
"""Config: Today I've lived
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("ito", "蔦貝,糸", 17, "female", "学生", "me:わたし"),
        ("shima", "島,航大", 25, "male", "技師", "me:俺"),
        ("george", "島,条志", 30, "male", "技師", "me:僕"),
        # sub
        ("miyuki", "蔦貝,美幸", 25, "female", "研究者", "me:私"),
        # family
        ("mam", "蔦貝,母", 40, "female", "母親"),
        ("dad", "蔦貝,父", 50, "male", "父親"),
        # mob
        )

STAGES = (
        # Area
        ("tokyo", "旧東京"),
        ("kofu", "旧甲府"),
        # Place
        ("ruintown", "町"),
        ("tower", "鉄塔"),
        ("home", "家"),
        # Part
        )

DAYS = (
        # base
        ("current", "現在"),
        ("voyage", "旅立ちの日"),
        # other
        )

ITEMS = (
        )

INFOS = (
        # main
        ("suicide", "自殺しようとしたこと"),
        # sub
        ("broadcast", "生存放送"),
        ("george_gone", "条志の行方"),
        )

FLAGS = (
        )

THEMES = {
        "alive": "生きること",
        }

MOTIFS = {
        "report": "報告",
        }
