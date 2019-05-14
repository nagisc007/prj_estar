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
        )

STAGES = (
        ("office", "会社"),
        ("thesite", "事件現場"),
        )

DAYS = (
        ("incident", "火災事件翌日"),
        )

ITEMS = (
        ("deadbody", "遺体"),
        )

INFOS = (
        ("case_fire", "火災事件"),
        ("interview", "取材"),
        ("truth", "紅崎秀子の真実"),
        )

FLAGS = (
        )

THEMES = {
        "chain": "繋がり",
        }
