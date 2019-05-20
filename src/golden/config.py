# -*- coding: utf-8 -*-
"""Config: the golden girl
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("kana", "吹尾,香奈恵", 18, "female", "患者", "me:わたし"),
        ("fukuo", "吹尾,清二郎", 40, "male", "技師", "me:僕"),
        ("hiroko", "吹尾,博子", 39, "female", "研究助手", "me:私"),
        # sub
        ("doc", "黒鉄,章介", 55, "male", "研究者", "me:私"),
        # mob
        ("medic1", "医師", 49, "male", "内科医"),
        ("medic2", "医師", 45, "male", "内科医"),
        )

STAGES = (
        # Area
        ("niigata", "新潟"),
        ("sado", "佐渡"),
        # Place
        ("home", "吹尾家"),
        ("kanaroom", "香奈恵の部屋"),
        ("hospital", "地元病院"),
        ("univhospital", "大学病院"),
        ("labo", "研究所"),
        )

DAYS = (
        ("current", "現在"),
        ("case1", "最初の事件日"),
        ("takehome", "連れ帰った日"),
        ("goddess", "女神になった日"),
        )

ITEMS = (
        ("kanacell", "黄金細胞"),
        ("fund", "資金"),
        )

INFOS = (
        ("goldsyndrome", "黄金化症候群"),
        ("god", "神"),
        ("killkana", "娘殺し"),
        ("golden", "黄金化"),
        ("neurosis", "ノイローゼ"),
        ("heal", "治療"),
        )

FLAGS = (
        )

THEMES = {
        }
