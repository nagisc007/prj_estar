# -*- coding: utf-8 -*-
"""Config: moonlight
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("goro", "皆井,吾朗", 41, "male", "会社員", "me:俺:S:吾朗:luna:瑠那さん:takahashi:高橋:tsukada:塚田"),
        ("luna", "皆井,瑠那", 35, "female", "ハープ奏者", "me:私:goro:吾朗さん"),
        # sub
        ("takahashi", "高橋,優太", 32, "male", "ヴァイオリニスト", "me:僕:luna:皆井さん"),
        ("tsukada", "塚田,善司", 51, "male", "会社員", "me:オレ:goro:皆井"),
        # mob
        ("satou", "佐藤,麻美", 40, "female", "チェリスト", "me:わたし"),
        ("helpgirl", "ヘルプマークの女性", 35, "female", "会社員", "me:わたし"),
        )

STAGES = (
        # Area
        ("Tokyo", "東京都"),
        ("Meguro", "目黒区"),
        # Place
        ("myhome", "皆井家"),
        ("company", "吾朗の勤務する会社"),
        # Part
        ("living", "リビング"),
        ("balcony", "ベランダ"),
        ("onstreet", "路上"),
        ("intrain", "電車内"),
        ("office", "会社オフィス"),
        )

DAYS = (
        # main
        ("firstday", "最初の帰宅日"),
        ("goout", "仕事にでかける日"),
        ("current", "現在"),
        ("fight", "喧嘩した日"),
        ("working", "仕事日"),
        # sub
        )

ITEMS = (
        # main
        # sub
        ("helpmark", "ヘルプマーク"),# NOTE:赤字に白で＋と♡
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
