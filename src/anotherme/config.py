# -*- coding: utf-8 -*-
"""Config: The another me
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("kyoko", "岩根,今日子", 20, "female", "大学生", "me:私:shota:翔太郎:sayama:幸子:child:きょう子:student:キョウコ:minori:鈴森さん:saito:斉藤さん"),
        ("shota", "宮内,翔太郎", 25, "male", "無職", "me:ボク:kyoko:今日子"),
        # univ
        ("sayama", "砂山,幸子", 20, "female", "大学生", "me:わたし:kyoko:今日子"),
        ("matsumoto", "松本,亘", 20, "male", "大学生", "me:俺:kyoko:岩根:kunugi:椚木さん"),
        ("takamura", "高村,滋", 44, "male", "大学教員", "me:僕"),
        ("kunugi", "椚木,円香", 22, "female", "大学生", "me:私"),
        ("saito", "斉藤,三紀", 21, "female", "大学生（浪人）", "me:わたし:kyoko:岩根さん"),
        ("isoya", "磯谷,教授", 48, "male", "ドイツ語教授", "me:ボク"),
        # work
        ("arase", "荒瀬,省二", 40, "male", "現場監督", "me:ボク:kyoko:今日子ちゃん"),
        ("minori", "鈴森,実里", 45, "female", "ベテラン派遣社員", "me:私"),
        # others
        ("asumi", "金井,亜純", 19, "female", "パート"),
        ("hotta", "堀田,優一", 50, "male", "理科教員", "me:ぼく"),
        ("miura", "三浦,啓司", 58, "male", "精神科医", "me:私"),
        # family
        ("mother", "岩根,朝子", 40, "female", "パート"),
        ("father", "岩根,雪雄", 50, "male", "電気店"),
        # family (shota)
        ("sho_mam", "宮内,母", 45, "female", "母"),
        ("sho_dad", "宮内,父", 52, "male", "父"),
        # anothers
        ("child_kyoko", "岩根,きょう子", 10, "female", "小学生", "me:わたし:my:きょう子:kyoko:きょうこお姉ちゃん:student:キョウコ姉:shota:ショータロ"),
        ("student_kyoko", "岩根,キョウコ", 15, "female", "中学生", "me:ワタシ:kyoko:今日子:child:きょう子:shota:翔太郎"),
        ("univ_kyoko", "岩根,明日子", 20, "female", "大学生", "me:私"),
        )

STAGES = (
        # Area
        ("Hokkaido", "北海道"),
        ("Sapporo", "札幌"),
        # Place
        ("univ", "大学"),
        ("apart", "アパート"),
        ("manshion", "マンション"),
        ("office", "アクセルリンクス"),
        ("famires", "ファミレス"),
        ("ma_apart", "松本のアパート"),
        ("hishome", "翔太郎の実家"),
        # Part
        ("myapart", "二〇四号室"),
        ("living", "リビング"),
        ("classroom", "教室"),
        ("lechall", "講堂"),
        )

DAYS = (
        # main
        ("childhood", "幼少期"),
        ("current", "現在", 6,20, 2019),
        ("encounter", "松本と出会った日", 6,21, 2019),
        ("shotaro", "翔太郎と出会った日", 6,25, 2019),
        ("proposed", "プロポーズされた日", 7,7, 2019),
        ("dadvisit", "父が来た日", 7,14, 2019),
        ("seaday", "海の日", 7,15, 2019),
        ("empty", "誰もいなくなった日"),
        ("married", "結婚した未来"),
        ("shotadead", "翔太郎が亡くなった日"),# NOTE: 10年前
        # sub
        ("encounter_next", "出会った日", 6,21, 2019),
        )

ITEMS = (
        # main
        ("another", "もう一人の自分"),
        ("his_phone", "翔太郎の携帯（ガラケー）"),
        # sub
        )

INFOS = (
        # main
        ("imagefriend", "イマジナリーフレンド"),
        ("IF", "ＩＦ"),
        ("meeting", "私会議"),
        # chapter 1
        ("relation", "人付き合い"),
        ("circle", "環境保全同好会"),
        ("cir_name", "カンポカ"),
        ("vanish_another", "アナザー消したい"),
        ("partwork", "パートの仕事"),
        ("stalker", "ストーカーの噂"),
        # chapter 2
        ("proposed", "プロポーズされた"),
        # chapter 3
        ("meeting", "自分会議"),
        ("birth_another", "アナザー誕生"),
        # chapter 4
        ("look_another", "アナザー感知人"),
        # chapter 5
        ("shota_truth", "翔太郎の真実"),
        ("another_truth", "アナザーの意味"),
        )

FLAGS = (
        )

THEMES = {
        "problem": "自分の分身をどうにかする",
        }

MOTIFS = {
        "imagefriend": "イマジナリーフレンド",
        }

TITLE = {
        "chap1": "第１話　私とワタシ",
        "chap2": "第２話　私と彼",
        "chap3": "第３話　私とわたしたち",
        "chap4": "第４話　私と父",
        "chap5": "第５話　私とわたし",
        }
