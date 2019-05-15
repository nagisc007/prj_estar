# -*- coding: utf-8 -*-
"""Config: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("masuda", "枡田延彦", 42, "male", "記者", "me:俺"),
        ("hideko", "紅崎秀子", 60, "female", "主婦", "me:私"),
        ("benio", "紅緒", 40, "female", "無職", "me:ワタシ"),
        ("doc", "室笠仙三", 79, "male", "医者", "me:儂"),
        # hideko history
        ("h_idol", "光咲紅", 17, "female", "アイドル", "me:ベニ"),
        ("h_actor", "茅ヶ崎紅香", 30, "female", "女優", "me:私"),
        ("h_later", "原崎秀子", 50, "female", "主婦", "me:ワタシ"),
        )

STAGES = (
        ("office", "会社"),
        ("thesite", "事件現場"),
        ("town", "糸川町"),
        ("theater", "小劇場"),
        ("idoloffice", "芸能事務所"),
        ("medicals", "診療院"),
        )

DAYS = (
        ("incident", "火災事件翌日"),
        ("interview1", "取材日1"),
        ("interview2", "取材日2"),
        ("interview3", "取材日3"),
        )

ITEMS = (
        ("deadbody", "遺体"),
        ("anotherbody", "もう一つの遺体"),
        )

INFOS = (
        ("case_fire", "火災事件"),
        ("life", "生活"),
        ("interview", "取材"),
        ("truth", "紅崎秀子の真実"),
        ("doc_secret", "医者の内緒話"),
        ("retire_business", "芸能界引退"),
        ("movie", "秀子を有名にした映画"),
        # NOTE: 自力で出産して子育てした女の物語
        ("moviename", "ほむらの女"),
        )

FLAGS = (
        )

THEMES = {
        "chain": "繋がり",
        }
