# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd


# configs
CHARAS = (
        ("my", "自分", 30, "male", "会社員"),
        ("you", "あなた", 30, "female", "読者"),
        )

STAGES = (
        ("apart", "アパート"),
        )

DAYS = (
        ("day1", "ある日"),
        )

ITEMS = (
        ("phone", "スマートフォン"),
        )

INFOS = (
        ("firstword", "はじめまして"),
        ("estar", "エブリスタ"),
        ("website", "交流サイト"),
        ("contest", "コンテスト"),
        )

FLAGS = (
        ("first", "最初の言葉"),
        )

# main
def world():
    w = wd.World("100 characters")
    w.set_db(CHARAS, STAGES, DAYS, ITEMS, INFOS, FLAGS)
    return w

def story(w: wd.World):
    return (w.maintitle("はじめましての百文字"),
        w.scene("百文字",
            w.day.day1.explain("外は雨").d("外はしっとりと雨に濡れている").omit(),
            w.combine(
                w.my.be(w.stage.apart, w.day.day1).d("天井を見上げて", "ぼんやりと思い出す"),
                w.my.remember(w.you, w.i.website),
                ),
            w.combine(
                w.my.talk(w.you, "$not").d("もう言葉を交わすことのないあなたは",
                    "消えてしまったサイトで幽霊のように笑っているだろうか"),
                w.my.deal("伝える", "$want", w.you, w.X()),
                ),
            w.my.look(w.i.estar, w.i.contest).d("ふと見かけたサイトの小説のコンテスト").omit(),
            w.my.know(w.i.estar).d("知らないサイトだが",
                "そこにはあなたの想いを作品にしてみませんか",
                "と書かれている").omit(),
            w.my.think("何もない").d("だが$Sには何もない").omit(),
            w.my.think("気づく", "原稿も真っ白").d("けれど思うのだ",
                "原稿用紙も最初は白じゃないか。",
                "何かしらの言葉を埋めれば",
                "あなたがどこかで見てくれるかも知れない"
                ).omit(),
            w.my.deal(w.phone).d("$Sはスマートフォンを前に指を挙げる").omit(),
            w.combine(
                w.my.remember(w.you, "小説好き").d("それでも小説好きなあなたに向け",
                    "この言葉から書き出そう"),
                w.my.do(w.i.firstword, "書く").d("最初に書く言葉は決めてある。",
                "あなたに一番最初に伝えた言葉だ。",
                "それは").omit(),
            ),
            w.my.do(w.i.firstword, "書く"),
            w.i.firstword.explain().d("――はじめまして"),
            ),
        )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

