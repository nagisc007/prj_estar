# -*- coding: utf-8 -*-
"""Config: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("masuda", "枡田延彦", 27, "male", "記者", "me:私"),
        ("hideko", "紅崎秀子", 60, "female", "主婦", "me:私"),
        ("benio", "紅緒", 40, "female", "無職", "me:ワタシ"),
        ("doc", "室笠仙三", 79, "male", "医者", "me:儂"),
        ("priest", "左海青州", 58, "male", "住職", "me:私"),
        # office
        ("tanabe", "田辺厚司", 48, "male", "上司", "me:俺"),
        # town
        ("hino", "日野勝子", 45, "female", "役場職員", "me:わたし"),
        ("takamori", "高森信幸", 29, "male", "警官", "me:オレ"),
        ("sugioka", "杉岡卓馬", 36, "male", "新聞記者", "me:俺"),
        # family
        ("mam", "枡田百合枝", 57, "female", "農家", "me:あたし"),
        ("dad", "枡田武彦", 60, "male", "農家", "me:おれ"),
        # hideko history
        ("h_idol", "光咲紅", 17, "female", "アイドル", "me:ベニ"),
        ("h_actor", "茅ヶ崎紅香", 30, "female", "女優", "me:私"),
        ("h_later", "原崎秀子", 50, "female", "主婦", "me:ワタシ"),
        ("manager", "園原謙太", 55, "male", "芸能事務所社長", "me:僕"),
        ("actoress", "由比ヶ浜凜", 59, "female", "劇団員", "me:アタシ"),
        )

STAGES = (
        # Areas
        ("tokyo", "東京"),
        ("niigata", "新潟"),
        # Places
        ("office", "会社"), # web新聞社
        ("thesite", "事件現場"),
        ("town", "糸川町"),
        ("theater", "小劇場"),
        ("idoloffice", "芸能事務所"),
        ("medicals", "診療院"),
        ("policestation", "警察署"),
        ("townoffice", "町役場"),
        ("temple", "寺院"),
        ("bar", "居酒屋"),
        # Rides
        ("car", "車"),
        ("train", "電車"),
        )

DAYS = (
        ("incident", "火災事件当日"),
        ("nextday", "火災事件翌日"),
        ("interview1", "取材日1"),
        ("interview2", "取材日2"),
        ("interview3", "取材日3"),
        )

ITEMS = (
        ("deadbody", "遺体"),
        ("anotherbody", "もう一つの遺体"),
        ("movie", "秀子を有名にした映画"),
        )

INFOS = (
        ("case_fire", "火災事件"),
        ("life", "生活"),
        ("interview", "取材"),
        ("truth", "紅崎秀子の真実"),
        ("doc_secret", "医者の内緒話"),
        ("retire_business", "芸能界引退"),
        # NOTE: 自力で出産して子育てした女の物語
        ("moviename", "ほむらの女"),
        ("deal_deads", "遺体の扱い"),
        )

FLAGS = (
        )

THEMES = {
        "chain": "繋がり",
        }
