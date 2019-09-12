# -*- coding: utf-8 -*-
"""Config: vanish cat
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("kisaragi", "如月,祐司", 30, "male", "SE", "me:僕:S:僕:ary:アリィ:arisa:有紗:kieth:キースi:kase:加瀬:aisaka:逢坂"),
        # sub
        ("ary", "アリィ", 10, "female", "猫", "me:私:kisa:祐司"),
        ("arisa", "日陰,有紗", 28, "female", "会社員", "me:私"),
        ("kieth", "ベーカー,キース", 36, "male", "研究者", "me:オレ:kisa:ユージ"),
        ("aisaka", "逢坂,豊", 40, "male", "チーフ", "me:私:kisa:如月君"),
        ("kase", "加瀬,周伍", 28, "male", "SE", "me:俺"),
        # mob
        )

STAGES = (
        # Area
        ("Atami", "熱海市"),
        # Place
        ("myhome", "自宅"),
        ("office", "会社"),
        ("park1", "葛西臨海公園"),
        ("ramen", "ラーメン店"),
        # Part
        ("living", "リビング"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("vanishold", "アイリーンの消えた日"),
        ("deadold", "アイリーンの亡くなった日"),
        ("first", "最初の日"),
        ("working", "仕事で忙しくする日"),
        ("vanish1", "最初の失踪日"),
        ("revive1", "蘇った日１"),
        ("vanish2", "複数回失踪後のある日"),
        ("visitjap", "キース来日した日"),
        # sub
        )

ITEMS = (
        # main
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
