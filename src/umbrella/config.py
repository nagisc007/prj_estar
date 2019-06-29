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
        ("miyu", "霧野,美由", 25, "female", "会社員", "me:わたし:senpai:水無月先輩:M:Ｍ先輩"),
        ("ryuichi", "高山,龍一", 50, "male", "ＡＩ指導員", "me:私"),
        # sub
        ("senpai", "水無月,朝陽", 30, "female", "会社員", "me:私:miyu:霧野"),
        # mob
        ("joshi", "三田村,佐和子", 45, "female", "上司", "me:私"),
        ("asobi", "湯村,ゆう子", 28, "female", "会社員", "me:ウチ"),
        ("sensity", "井浦,東子", 24, "female", "会社員", "me:わたし"),
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
        ("senpaiword1", "先輩の言葉"),
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
