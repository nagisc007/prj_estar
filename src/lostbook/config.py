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
        ("nao", "朝川,那緒", 18, "male", "高校生", "me:僕:akiko:明子さん:anzu:高田さん:tamura:田村:sanae:奥貫さん:saya:沙夜さん"),
        ("saya", "山本,沙夜", 28, "female", "作家", "me:わたし:nao:朝川那緒君:asakawa:朝川君"),
        ("akiko", "葛城,明子", 68, "female", "本屋", "me:私:nao:朝川君"),
        # sub
        ("anzu", "高田,杏", 18, "female", "高校生", "me:わたし:nao:朝川"),
        ("tamura", "田村,典行", 18, "male", "高校生", "me:オレ:nao:朝川:anzu:杏"),
        ("ak_sun", "葛城,正人", 30, "male", "会社員", "me:ぼく:nao:朝川君"),
        ("yamamoto", "山本,真夜", 68, "female", "元教員", "me:私"),
        # family
        ("dad", "朝川,父", 48, "male", "会社員", "me:俺:nao:那緒:y_nao:お前"),
        ("mam", "朝川,母", 47, "female", "事務員", "me:私:nao:那緒:y_nao:あんた"),
        # school
        ("teacher", "担任", 35, "male", "教師", "me:おれ"),
        # mob
        ("sanae", "奥貫,早苗", 42, "female", "パート", "me:あたし:nao:朝川君"),
        ("sy_mam", "山本,母親", 60, "female", "母親", "me:あたし"),
        ("rekishi", "仁村,孝則", 55, "male", "歴史教師", "me:ぼく"),
        # book
        ("bookhero", "雨宮,月子", 17, "female", "高校生", "me:わたし"),
        ("bookrival", "日下,希子", 17, "female", "高校生", "me:私"),
        )

STAGES = (
        # Area
        ("tochigi", "栃木県"),
        # Place
        ("town", "田倉町"),# NOTE: さくら市と那須川町をベースに
        ("bookshop", "かつらぎ書店"),
        ("school", "県立高校"),
        ("home", "朝川家"),
        ("partfactory", "弁当工場"),
        ("herhome", "葛城家"),
        # Ride
        ("bus", "バス"),
        # Part
        ("myroom", "那緒の部屋"),
        ("dyning", "食堂"),
        ("oldlib_mark", "旧図書室跡"),
        ("classroom", "教室"),
        ("libroom", "資料室"),
        ("partroom", "仕事控室"),
        ("partline", "工場のライン"),
        ("herroom", "彼女の部屋"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("known", "潰れることを知った日", 7, 12, 2019),
        ("termend1", "一学期の終業式", 7,19, 2019),
        ("workfirst", "初出勤日", 7,23, 2019),
        ("closed", "閉店日", 7,31, 2019),
        ("schoolday", "登校日", 8,9, 2019),
        # sub
        )

ITEMS = (
        # main
        ("herbook", "真夜中のロンド"),
        ("rondoseries", "ロンドシリーズ"),
        ("rondo1", "薔薇のロンド"),
        ("rondo4", "睡蓮のロンド"),
        # sub
        ("poetbook", "詩の手帖"),
        ("areahistory", "田倉町風俗史"),
        )

INFOS = (
        # theme
        # main
        ("vanishshop", "本屋が無くなる"),
        ("her_addr", "彼女の住所"),
        ("her_mind", "彼女の決意"),
        ("her_reason", "彼女の事情"),
        ("anothername", "月乃夜"),
        # sub
        ("oldschool_reason", "旧校舎が消えた事情"),
        ("club", "歴史研究同好会"),
        ("na_club", "歴研"),
        ("oldclub", "真夜中の図書研究会"),
        ("our_memory", "私たちの思い出"),
        # books
        ("booktitle1", "真夜中のロンド"),
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
