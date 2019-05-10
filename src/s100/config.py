# -*- coding: utf-8 -*-
"""Config: the 100 stories
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("hero", "秋川正悟", 36, "male", "作家", "me:私:fuyumi:冬美"),
        ("osaki", "大崎亮介", 38, "male", "編集者", "me:オレ"),
        ("fuyumi", "田村冬美", 36, "female", "会社員", "me:私:hero:秋川君"),
        ("futureman", "未来の秋川", 37, "male", "無職", "me:俺"),
        ("pastman", "過去の秋川", 16, "male", "高校生", "me:僕"),
        ("ft_fuyumi", "未来の冬美", 37, "female", "主婦", "me:私"),
        ("nishikawa", "仁志川貴信", 27, "male", "作家", "me:僕"),
        )


STAGES = (
        ("apart", "アパート"),
        ("school", "学校"),
        ("bar", "飲み屋"),
        ("subway", "地下鉄"),
        ("sea", "海"),
        ("bookstore", "本屋"),
        ("conveni", "コンビニ"),
        ("indream", "夢の中"),
        )


DAYS = (
        ("current", "現在", 4, 15, 2019),
        ("childhood", "幼少期", 4, 20, 1999),
        ("schoolday", "学生時代", 6, 20, 2002),
        )


ITEMS = (
        ("terminal", "不思議端末"), # t3
        ("coffee", "コーヒー"),
        ("tobacoo", "煙草"),
        ("ichioku", "一億円"), # t7
        ("megane", "メガネ"),
        ("choco", "チョコレート"),
        ("fear_mail", "恐怖メール"), # t1
        ("future_mail", "未来メール"),
        ("sakura", "桜"),
        ("abook", "本"),
        ("cat", "猫"),
        )


INFOS = (
        ("novel", "小説"),
        ("promise", "子供の日の約束"),
        ("his_reason", "書く理由"),
        ("future_mail", "一年後の私からメール"), # t12
        ("help_mail", "たすけてメール"), # t24
        ("hiyori", "小説日和"), # t99
        ("fuyumi_call", "冬美の電話"),
        ("lostmemory", "記憶喪失"),
        ("absencemaster", "店主が常に不在"),
        )

# 100 themes
THEMES = {
        "1": "メールを開いたら恐怖",
        "2": "無口なあいつが一言",
        "3": "不思議な道具",
        "4": "優しい彼女が豹変",
        "5": "水場の恐怖",
        "6": "教室の戸を開けたらそこには",
        "7": "一億円を手に入れて",
        "8": "隣に引っ越してきた",
        "9": "これが全てのはじまりだった",
        "10": "秋の学校",
        "11": "完璧な彼女の欠点",
        "12": "一年後の私からのメール",
        "13": "時間を巻き戻す力",
        "14": "子供の頃の約束",
        "15": "あの時を思い返すと",
        "16": "最悪だ……この世の終わりだ……",
        "17": "透明人間になって",
        "18": "ずっと待ってるから",
        "19": "記憶喪失の僕の前に",
        "20": "コーヒーと煙草",
        "21": "誰にもいえない秘密の趣味",
        "22": "なくしてしまった大事なもの",
        "23": "どうしても勝てない相手",
        "24": "誰か助けて！",
        "25": "あれから一年",
        "26": "ちぐはぐな二人",
        "27": "嘘……でしょ……",
        "28": "墓場まで持っていく秘密",
        "29": "おかえり",
        "30": "だから旅に出た",
        "31": "夏なんてなくなればいいのに",
        "32": "もうやめてやる！",
        "33": "トンデモ上司",
        "34": "その奇妙な店は",
        "35": "極上の美味",
        "36": "おやすみ",
        "37": "目を開けると、そこには",
        "38": "猫",
        "39": "疲れた……もうイヤだ……",
        "40": "メガネ",
        "41": "悲鳴",
        "42": "またね",
        "43": "チョコレート",
        "44": "桜",
        "45": "ギリギリ",
        "46": "ごめんなさい",
        "47": "な誕生日",
        "48": "感染",
        "49": "夜空への願い事",
        "50": "半分",
        "51": "地下鉄に乗って",
        "52": "海",
        "53": "本屋さん",
        "54": "文化祭",
        "55": "SNS",
        "56": "アルバム",
        "57": "恋のはじまり",
        "58": "コンビニ",
        "59": "夫婦",
        "60": "動画",
        "61": "夢の叶え方",
        "62": "お気に入りのあの店",
        "63": "嫉妬",
        "64": "最強パーティ",
        "65": "プレゼント",
        "66": "お年玉で買ったアレ",
        "67": "こたつ",
        "68": "バレンタイン大嫌い！！",
        "69": "雪の夜",
        "70": "今日は特別な日だ",
        "71": "奇妙な同居生活",
        "72": "お風呂のしあわせ",
        "73": "桜の木の下で",
        "74": "今も忘れない",
        "75": "眠る",
        "76": "優しい嘘",
        "77": "神様",
        "78": "雨の日",
        "79": "私が死んだ理由",
        "80": "気になるあの人",
        "81": "夏がきた",
        "82": "真夜中",
        "83": "青",
        "84": "さよならの理由",
        "85": "あの日捨てたもの",
        "86": "目が覚めるとそこには……",
        "87": "男同士",
        "88": "そして空を見上げた",
        "89": "一冊の本",
        "90": "待つ",
        "91": "白",
        "92": "ぬくもり",
        "93": "新しい",
        "94": "発覚",
        "95": "チョコかと思ったら",
        "96": "とける",
        "97": "お返し",
        "98": "となり",
        "99": "日和",
        "100": "100",
        }

