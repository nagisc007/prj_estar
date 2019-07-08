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
        ("miyako", "斎賀,美耶古", 16, "female", "高校生", "me:わたし:aya:彩"),
        ("kirimura", "霧村,豊", 35, "male", "教師", "me:俺"),
        # sub
        ("aya", "千覧,彩", 16, "female", "高校生", "me:私"),
        ("kikyo", "千覧,桔梗", 32, "female", "教祖", "me:私"),
        # family
        ("mam", "斎賀,母", 40, "female", "会社員", "me:私"),
        ("dad", "斎賀,父", 45, "male", "会社員", "me:僕"),
        ("sister", "斎賀,伽耶", 14, "female", "中学生", "me:ワタシ"),
        # mob
        ("nogi", "野木,若葉", 40, "female", "信者", "me:私"),
        )

STAGES = (
        # Area
        ("Shizuoka", "静岡県"),
        # Place
        ("highschool", "県立高校"),
        ("myhome", "斎賀家"),
        ("ayahome", "千覧家"),
        # Part
        ("myroom", "自室"),
        ("ayaroom", "親友の部屋"),
        ("classroom", "教室"),
        ("artroom", "美術室"),
        )

DAYS = (
        # main
        ("bloodmoon", "皆既月食日", 1,21, 2019),
        ("vanishnext", "消えた翌日", 1,22, 2019),
        ("valentain", "バレンタイン", 2,14, 2019),
        ("discover1", "発見日", 7,5, 2019),
        # sub
        )

ITEMS = (
        # main
        ("sanagi", "蛹"),
        ("aya_letter", "彼女の手紙"),
        ("hermessage1", "※美耶古へのメッセージ"),# TODO: メッセ内容
        ("spider", "※蜘蛛の名前"),# TODO:妖魔名
        # sub
        )

INFOS = (
        # theme
        # main
        ("rescue_aya", "彼女を助ける"),
        ("rebirth", "生まれ変わり"),
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
