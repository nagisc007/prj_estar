# -*- coding: utf-8 -*-
"""Config: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
CHARAS = (
        ("masuda", "枡田,延彦", 29, "male", "記者",
            "me:俺:my:私:sugisan:杉岡さん:chief:チーフ:nametaka:高森:neya:根屋さん:namehide:秀子"),
        ("hideko", "紅崎,秀子", 50, "female", "主婦", "me:私"),
        ("benio", "紅崎,紅緒", 19, "female", "無職", "me:ワタシ"),
        ("doc", "室笠,仙三", 79, "male", "医者", "me:儂"),
        ("priest", "左海,青州", 58, "male", "住職", "me:私"),
        # office
        ("tanabe", "田辺,厚司", 48, "male", "上司", "me:おれ:masu:枡田"),
        ("miki", "根屋,美希", 30, "female", "事務", "me:わたし:masu:枡田君"),
        # town
        ("hino", "日野,勝子", 45, "female", "役場職員", "me:わたし"),
        ("takamori", "高森,信幸", 30, "male", "警官", "me:オレ:masu:枡やん"),
        ("sugioka", "杉岡,卓馬", 36, "male", "新聞記者", "me:僕"),
        ("policechief", "警察署長", 55, "male", "警察署長"),
        # relations
        ("shoko", "三枝,祥子", 54, "female", "女優", "me:あたし"),
        ("manager", "園原,謙太", 72, "male", "芸能事務所社長", "me:僕:namehide:秀子"),
        ("coworker", "仙石,洋輔", 64, "male", "劇団座長", "me:オレ:hidesan:秀さん:yui:お凜"),
        ("actoress", "由比ヶ浜,凜", 55, "female", "劇団員", "me:アタシ"),
        ("cafemaster", "笹野,聖美", 58, "female", "喫茶店店長", "me:わたし"),
        ("shopowner", "伊勢谷,豊", 61, "male", "ビデオ店店長", "me:私:beni:紅"),
        # family
        ("mam", "枡田,百合枝", 57, "female", "農家", "me:あたし"),
        ("dad", "枡田,武彦", 60, "male", "農家", "me:おれ"),
        # hideko history
        ("h_idol", "光咲,紅", 17, "female", "アイドル", "me:ベニ:my:わたし"),
        ("h_actor", "紅崎,秀子", 30, "female", "女優", "me:私"),
        ("h_later", "原崎,秀子", 50, "female", "主婦", "me:ワタシ"),
        # mob
        ("woman1", "山本,静江", 48, "female", "野次馬", "me:あたし:masuda:あんた"),
        ("woman2", "江森,典代", 46, "female", "野次馬", "me:わたし"),
        ("man1", "山根,太蔵", 48, "male", "会社員", "me:僕"),
        )

STAGES = (
        # Areas
        ("tokyo", "東京"),
        ("niigata", "新潟"),
        # Places
        ("office", "ウェブ日報"), # web新聞社
        ("apart", "アパート"),
        ("thesite", "事件現場"),
        ("town", "糸川町"),
        ("theater", "小劇場"),
        ("idoloffice", "芸能事務所"),
        ("medicals", "診療院"),
        ("policestation", "警察署"),
        ("townoffice", "町役場"),
        ("temple", "寺院"),
        ("bar", "居酒屋"),
        ("cafe", "喫茶店"),
        # Rides
        ("car", "車"),
        ("train", "電車"),
        )

DAYS = (
        ("incident", "火災事件当日", 5, 15, 2019),
        ("nextday", "火災事件翌日", 5, 16, 2019),
        ("interview1", "取材日1", 5, 17, 2019),
        ("interview2", "取材日2", 5, 18, 2019),
        ("interview3", "取材日3", 5,19, 2019),
        # event
        ("changejob", "転職年", 4,1, 2017), # 2年前
        )

ITEMS = (
        ("deadbody", "遺体"),
        ("anotherbody", "もう一つの遺体"),
        ("movie", "秀子を有名にした映画"),
        ("newspaper", "新新日報"),
        # names
        ("hero", "枡田"),
        ("na_tanabe", "田辺"),
        ("na_sugioka", "杉岡"),
        ("na_takamori", "高森"),
        ("na_miki", "根屋"),
        ("na_coworker", "仙石"),
        ("na_masuda", "枡田"),
        ("na_manager", "園原"),
        ("na_shopowner", "伊勢谷"),
        ("na_hidol", "光咲"),
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
        ("movieheroine", "赤見聖子"),
        ("deal_deads", "遺体の扱い"),
        ("fox", "黒髪の女狐"),
        ("idolname", "レインボースターズ"),
        )

FLAGS = (
        )

THEMES = {
        "chain": "繋がり",
        }
