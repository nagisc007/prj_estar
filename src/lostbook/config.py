# -*- coding: utf-8 -*-
"""Config: Lost her book
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("nako", "朝川,奈子", 18, "female", "高校生", "me:わたし"),
        ("saya", "葛城,沙夜", 28, "female", "作家", "me:私"),
        ("somei", "館林,宗明", 68, "male", "本屋", "me:僕"),
        # sub
        # mob
        )

STAGES = (
        # Area
        ("tochigi", "栃木県"),
        # Place
        ("town", "本宮町"),
        # Part
        ("home", "朝川家"),
        ("myroom", "奈子の部屋"),
        ("school", "県立高校"),
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
        ("vanishshop", "本屋が無くなる"),
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
