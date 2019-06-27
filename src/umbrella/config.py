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
        ("miyu", "霧野,美由", 25, "female", "会社員", "me:わたし:senpai:日岡先輩"),
        ("ryuichi", "高山,龍一", 50, "male", "ＡＩ指導員", "me:私"),
        # sub
        ("senpai", "日岡,葉月", 30, "female", "会社員", "me:私"),
        )

STAGES = (
        # Area
        ("Tokyo", "東京"),
        # Place
        ("building", "ビル"),
        # Part
        ("rooftop", "屋上"),
        ("office", "オフィス"),
        )

DAYS = (
        # main
        ("current", "現在"),
        # sub
        )

ITEMS = (
        # main
        ("umbrella", "真っ黒な傘"),
        # sub
        )

INFOS = (
        # theme
        # main
        ("myfinish", "全てを終わりにしたい"),
        ("worklimit", "仕事の限界"),
        ("meaning", "光の意味"),
        ("miyu_truth", "彼女はＡＩだった"),
        ("starlight", "落ちてくる光"),
        ("feature", "傘の機能"),
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
