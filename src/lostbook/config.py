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
        ("nao", "朝川,那緒", 18, "female", "高校生", "me:俺"),
        ("saya", "葛城,沙夜", 28, "female", "作家", "me:わたし"),
        ("akiko", "館林,明子", 68, "male", "本屋", "me:私"),
        # sub
        # mob
        )

STAGES = (
        # Area
        ("tochigi", "栃木県"),
        # Place
        ("town", "本宮町"),# NOTE: さくら市と那須川町をベースに
        ("bookshop", "本屋"),
        # Part
        ("home", "朝川家"),
        ("myroom", "那緒の部屋"),
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
        ("her_addr", "彼女の住所"),
        ("her_mind", "彼女の決意"),
        ("her_reason", "彼女の事情"),
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
