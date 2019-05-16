# -*- coding: utf-8 -*-
"""Config: the golden girl
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("kana", "吹尾香奈恵", 18, "female", "患者", "me:わたし"),
        ("fukuo", "吹尾清二郎", 40, "male", "技師", "me:僕"),
        ("hiroko", "吹尾博子", 39, "female", "研究助手", "me:私"),
        ("kurogane", "黒鉄章介", 55, "male", "研究者", "me:私"),
        )

STAGES = (
        # Area
        # Place
        ("home", "吹尾家"),
        ("lab", "研究所"),
        )

DAYS = (
        ("current", "現在"),
        )

ITEMS = (
        ("kanacell", "黄金細胞"),
        ("fund", "資金"),
        )

INFOS = (
        ("goldsyndrome", "黄金化症候群"),
        )

FLAGS = (
        )

THEMES = {
        }
