# -*- coding: utf-8 -*-
"""Config: The night umbrella
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("miyu", "霧野,美由", 25, "female", "会社員", "me:わたし"),
        ("gentleman", "謎の紳士", 50, "male", "謎の男", "me:私"),
        # sub
        )

STAGES = (
        # Area
        ("Tokyo", "東京"),
        # Place
        ("building", "ビル"),
        # Part
        ("rooftop", "屋上"),
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
        ("myfinish", "全てを終わりにしたい"),
        ("worklimit", "仕事の限界"),
        ("meaning", "光の意味"),
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
