# -*- coding: utf-8 -*-
"""Config: the golden girl
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("kana", "吹尾,香奈恵", 18, "female", "患者", "me:わたし"),
        ("fukuo", "吹尾,清二郎", 42, "male", "技師", "me:僕"),
        ("hiroko", "吹尾,博子", 39, "female", "塾講師", "me:私"),
        # sub
        ("doc", "黒鉄,章介", 55, "male", "研究者", "me:私"),
        ("suzuno", "厚木,鈴乃", 42, "female", "研究助手", "me:私"),
        ("believer", "正木,爽秋", 49, "male", "宗教家", "me:私"),
        # mob
        ("medic1", "医師", 49, "male", "内科医"),
        ("medic2", "医師", 45, "male", "内科医"),
        )

STAGES = (
        # Area
        ("niigata", "新潟"),
        ("sado", "佐渡"),
        # Place
        ("home", "吹尾家"),
        ("hospital", "地元病院"),
        ("univhospital", "大学病院"),
        ("labo", "研究所"),
        # Part
        ("kanaroom", "香奈恵の部屋"),
        ("hirokoroom", "博子の部屋"),
        ("docroom", "博士の研究室"),
        )

DAYS = (
        ("current", "現在"),
        ("case1", "最初の事件日"),
        ("takehome", "連れ帰った日"),
        ("goddess", "女神になった日"),
        )

ITEMS = (
        ("kanacell", "黄金細胞"),
        ("fund", "資金"),
        )

INFOS = (
        ("goldsyndrome", "黄金化症候群"),
        ("god", "神"),
        ("killkana", "娘殺し"),
        ("golden", "黄金化"),
        ("neurosis", "ノイローゼ"),
        ("heal", "治療"),
        ("gatherfund", "資金集め"),
        ("nogod", "無宗教"),
        ("coupleproblem", "夫婦問題"),
        ("truancy", "不登校"),
        ("infection", "感染方法"),
        ("wifetrouble", "妻の悩み"),
        ("wifecircle", "ヨガサークル"),
        ("docnews", "博士たち逮捕"),
        ("injustice", "博士たちの不正"),
        )

FLAGS = (
        )

THEMES = {
        "means": "黄金の意味",
        "money": "お金の問題",
        "relation": "金による人間関係の崩壊",
        }
