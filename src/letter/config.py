# -*- coding: utf-8 -*-
"""Config: the letter
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        # main
        ("hiroki", "平松,博樹", 35, "male", "技師", "me:僕:S:博樹:yoko:葉子:mizu:課長:ono:大野さん:myson:博史"),
        ("yoko", "平松,葉子", 34, "female", "SE", "me:私:hiroki:あなた:hirosan:博樹さん"),
        # sub
        ("mizuguchi", "水口,賢介", 45, "male", "課長", "me:俺:hiroki:平松"),
        ("sister", "田端,亮子", 30, "female", "保育士", "me:わたし:hiroki:博樹さん"),
        ("tabata", "田端,優平", 34, "male", "会社員", "me:オレ:ryoko:亮子"),
        ("ta_son", "田端,悠斗", 10, "male", "小学生", "me:ぼく"),
        ("myson", "息子", 10, "male", "子ども", "me:ぼく"),
        ("ono", "大野,善司", 55, "male", "技師", "me:儂"),
        # future
        ("hiroshi", "平松,博史", 35, "male", "技師", "me:僕:S:博史"),
        ("helper", "助手", 29, "female", "助手", "me:わたし"),
        # mob
        ("doctor", "西部,浩介", 44, "male", "医師", "me:私"),
        )

STAGES = (
        # Area
        # Place
        ("myhome", "自宅"),
        ("myoffice", "会社", "金型工場"),
        ("hospital", "病院"),
        ("labo", "研究所"),
        # Part
        ("onstreet", "路上"),
        ("living", "リビング"),
        ("wooddeck", "ウッドデッキ"),
        ("consulroom", "診察室"),
        ("ceremonyhall", "葬儀場"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("warming", "幸せだった日々"),
        ("consul1", "診察結果日"),
        ("work1", "出社して上司に相談した日"),
        ("talkmodel", "妻にモデリングの話をした日"),
        ("model1", "モデリング初日"),
        ("dead", "彼女が亡くなった日"),
        ("birth", "息子が生まれた日"),
        ("future", "息子が大きくなった未来"),
        # sub
        )

ITEMS = (
        # main
        # sub
        )

INFOS = (
        # theme
        # main
        ("ALS", "筋萎縮性側索硬化症"),
        ("als", "ALS"),
        # sub
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
