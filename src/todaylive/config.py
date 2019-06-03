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
        ("george", "大垣,条志", 30, "male", "技師", "me:僕"),
        # sub
        ("miyuki", "蔦貝,美幸", 25, "female", "研究者", "me:私"),
        # family
        ("uncle", "斉藤,誠治", 52, "male", "伯父", "me:俺",
            "糸を引き取って育てている"),
        ("mam", "蔦貝,母", 40, "female", "母親", "me:私", "災害で亡くなった"),
        ("dad", "蔦貝,父", 50, "male", "父親", "me:僕", "災害で亡くなった"),
        # mob
        ("man1", "野麦,太輔", 38, "male", "漁師", "me:オレ"),
        )

STAGES = (
        # Area
        ("tokyo", "旧東京"),
        ("kofu", "旧甲府"),
        # Place
        ("ruintown", "町"),
        ("city", "荒廃した都内"),
        ("tower", "鉄塔"),
        ("home", "家"),
        ("barrack", "バラック"),
        # Part
        ("broadroom", "放送室"),
        )

DAYS = (
        # main
        ("disastar", "災害日"),
        ("voyage", "旅立ちの日"),
        ("current", "現在"),
        ("reporting", "放送日"),
        # sub
        )

ITEMS = (
        # main
        ("mybag", "伯父の登山用リュック"),
        ("broadbox", "放送設備"),
        ("portableradio", "ポータブルラジオ"),
        # sub
        )

INFOS = (
        # theme
        ("reporting", "伝えること"),
        # main
        ("suicide", "自殺しようとしたこと"),
        ("radio", "ラジオの放送の仕方"),
        ("myalive", "生存報告"),
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
