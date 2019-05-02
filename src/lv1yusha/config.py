# -*- coding: utf-8 -*-
"""Config: lv1 yusha.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        ("hero", "アリエル", 16, "male", "勇者", "me:僕", "英雄の息子"),
        ("hero99", "アリエル９９", 20, "male", "勇者", "me:俺", "レベル99になったアリエル"),
        ("mother", "ウリア", 36, "female", "針子", "me:私:hero:アリエル"),
        ("father", "オルンガ", 40, "male", "英雄", "me:ワシ:mother:お前:hero:マイサン"),
        ("king", "アルアバン王", 46, "male", "国王", "me:儂", "アルアバンの国王"),
        ("vern", "ヴェルン", 35, "male", "宰相付秘書官", "me:私"),
        ("cornel", "コーネル", 59, "male", "宰相", "me:私"),
        # chapter1
        ("diana", "ダイナ", 27, "female", "戦士", "me:アタイ"),
        ("kult", "クルト", 25, "male", "僧侶", "me:私"),
        ("maririn", "マリリン", 22, "female", "魔法使い", "me:わたし"),
        ("daemon1", "アークド・ダエモン", 99, "monster", "魔物", "me:オレサマ"),
        ("bazem", "バーゼム", 65, "male", "神官", "me:私"),
        ("marc", "マーク", 35, "male", "傭兵", "me:俺"),
        ("monster1", "化けガラス", 99, "monster", "魔物"),
        ("gandof", "ガンドフ", 39, "male", "武器屋", "me:俺"),
        ("gatekeeper1", "門番１", 28, "male", "兵士（門番）", "me:私"),
        )


STAGES = (
        ("alaban", "アルアバン", "英雄が生まれた島国"),
        ("castle", "アルアバン城"),
        ("town", "アルアバン城下町"),
        ("myhome", "勇者の家"),
        ("church", "教会"),
        ("bar", "酒場"),
        ("field1", "アルアバン周辺"),
        ("tower1", "次元の塔"),
        )


DAYS = (
        ("childhood", "幼少の頃"),
        ("dadvoyage", "父旅立ちの日"),
        ("first", "旅立ちの日"),
        )


ITEMS = (
        ("brokens", "折れた剣", "父の形見"),
        )


INFOS = (
        ("monster", "魔物"),
        ("voyage", "旅立ち"),
        ("bustered", "魔王退治"),
        ("coop", "協力"),
        ("deadly", "死にそうになる"),
        ("reviveboss", "魔王復活"),
        ("callhero", "王の呼び出し"),
        ("worldsecret", "世界の秘密"),
        ("dadlost", "オルンガの死"),
        ("becomeyusha", "勇者になる"),
        ("gatherally", "仲間集め"),
        ("massacre", "仲間虐殺"),
        ("herosun", "英雄の子"),
        ("worldinfo", "世界の現状"),
        ("case_caravan", "商隊全滅事件"),
        )


FLAGS = (
        ("increasing", "増える魔物"),
        )

