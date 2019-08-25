# -*- coding: utf-8 -*-
"""Config: for hitogomi
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("hero", "リオン", 15, "male", "男の子", "me:僕:S:リオン:miko:ロメルダ"),
        ("miko", "ロメルダ", 18, "female", "巫女", "me:私:hero:リオン"),
        # sub
        ("granpa", "爺さん", 67, "male", "農夫", "me:儂"),
        ("bro", "ジギータ", 28, "male", "兵士", "me:俺"),
        # mob
        ("soldier", "兵士", 25, "male", "兵士", "me:俺"),
        )

STAGES = (
        # Area
        # Place
        ("hill", "丘"),
        # Part
        )

DAYS = (
        # main
        ("current", "現在"),
        # sub
        )

ITEMS = (
        # main
        ("thestar", "神宿の星"),
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
