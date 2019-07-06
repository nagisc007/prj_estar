# -*- coding: utf-8 -*-
"""Config: The red emergence
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("miyako", "斎賀,美耶古", 16, "female", "高校生", "me:わたし"),
        ("kirimura", "霧村,豊", 35, "male", "教師", "me:俺"),
        # sub
        ("aya", "千覧,彩", 16, "female", "高校生", "me:私"),
        ("kikyo", "千覧,桔梗", 32, "female", "教祖", "me:私"),
        )

STAGES = (
        # Area
        ("Shizuoka", "静岡県"),
        # Place
        ("highschool", "県立高校"),
        # Part
        ("ayaroom", "親友の部屋"),
        )

DAYS = (
        # main
        ("discover1", "発見日", 7,5, 2019),
        # sub
        )

ITEMS = (
        # main
        ("sanagi", "蛹"),
        # sub
        )

INFOS = (
        # theme
        # main
        ("ijime", "虐め問題"),
        ("aya_mind", "彼女の気持ち"),
        # sub
        ("herstatus", "彼女の状態"),
        ("herrefusal", "彼女の不登校"),
        ("hercause", "彼女たちの原因"),
        ("ajin", "亜人"),
        ("virginbirth", "処女受胎"),
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
