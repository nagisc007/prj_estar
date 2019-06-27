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
        ("nao", "朝川,那緒", 18, "male", "高校生", "me:僕:akiko:明子さん:anzu:高田さん:tamura:田村"),
        ("saya", "山本,沙夜", 28, "female", "作家", "me:わたし"),
        ("akiko", "葛城,明子", 68, "female", "本屋", "me:私:nao:朝川君"),
        # sub
        ("anzu", "高田,杏", 18, "female", "高校生", "me:わたし:nao:朝川"),
        ("tamura", "田村,典行", 18, "male", "高校生", "me:オレ:nao:朝川:anzu:杏"),
        ("akikosun", "葛城,息子", 30, "male", "会社員", "me:ぼく"),
        ("yamamoto", "山本,真夜", 68, "female", "元教員", "me:私"),
        # family
        ("dad", "朝川,父", 48, "male", "会社員", "me:俺:nao:お前"),
        ("mam", "朝川,母", 47, "female", "事務員", "me:私:nao:あんた"),
        # school
        ("teacher", "担任", 35, "male", "教師", "me:おれ"),
        # mob
        )

STAGES = (
        # Area
        ("tochigi", "栃木県"),
        # Place
        ("town", "本宮町"),# NOTE: さくら市と那須川町をベースに
        ("bookshop", "かつらぎ書店"),
        ("school", "県立高校"),
        ("home", "朝川家"),
        ("partfactory", "弁当工場"),
        ("herhome", "葛城家"),
        # Part
        ("myroom", "那緒の部屋"),
        ("dyning", "食堂"),
        ("oldlib_mark", "旧図書室跡"),
        ("classroom", "教室"),
        ("partroom", "仕事控室"),
        ("partline", "工場のライン"),
        ("bus", "バス"),
        ("herroom", "彼女の部屋"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("known", "潰れることを知った日", 7, 12, 2019),
        ("termend1", "一学期の終業式", 7,19, 2019),
        # sub
        )

ITEMS = (
        # main
        # sub
        ("poetbook", "詩の手帖"),
        )

INFOS = (
        # theme
        # main
        ("vanishshop", "本屋が無くなる"),
        ("her_addr", "彼女の住所"),
        ("her_mind", "彼女の決意"),
        ("her_reason", "彼女の事情"),
        # sub
        ("oldschool_reason", "旧校舎が消えた事情"),
        ("club", "歴史研究同好会"),
        ("na_club", "歴研"),
        ("oldclub", "真夜中の図書研究会"),
        # books
        ("booktitle1", "真夜中のロンド"),
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
