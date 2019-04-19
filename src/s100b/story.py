# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.master import Master
from storybuilder.builder.tools import build_to_story


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

WORDS = (
        ("firstword", "はじめまして"),
        ("estar", "エブリスタ"),
        ("website", "交流サイト"),
        ("contest", "コンテスト"),
        )

FLAGS = (
        ("first", "最初の言葉"),
        )

# main
def master():
    m = Master("100 characters")
    m.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    m.set_flags(FLAGS)
    return m

def story(m: Master):
    return m.story("はじめましての百文字",
            m.day1.explain("外は雨").d("外はしっとりと雨に濡れている").omit(),
            m.combine(
                m.my.be(m.apart, m.day1).d("天井を見上げて", "ぼんやりと思い出す"),
                m.my.remember(m.you, m.website),
                ),
            m.combine(
                m.my.talk(m.you).non().d("もう言葉を交わすことのないあなたは",
                    "消えてしまったサイトで幽霊のように笑っているだろうか"),
                m.my.deal("伝える", m.you, m.some()).want(),
                ),
            m.my.look(m.estar, m.contest).d("ふと見かけたサイトの小説のコンテスト").omit(),
            m.my.know(m.estar).d("知らないサイトだが",
                "そこにはあなたの想いを作品にしてみませんか",
                "と書かれている").omit(),
            m.my.think("何もない").d("だが$Sには何もない").omit(),
            m.my.think("気づく", "原稿も真っ白").d("けれど思うのだ",
                "原稿用紙も最初は白じゃないか。",
                "何かしらの言葉を埋めれば",
                "あなたがどこかで見てくれるかも知れない"
                ).omit(),
            m.my.deal(m.phone).d("$Sはスマートフォンを前に指を挙げる").omit(),
            m.combine(
                m.my.remember(m.you, "小説好き").d("それでも小説好きなあなたに向け",
                    "この言葉から書き出そう"),
                m.my.do(m.firstword, "書く").d("最初に書く言葉は決めてある。",
                "あなたに一番最初に伝えた言葉だ。",
                "それは").omit(),
            ),
            m.firstword.explain().d("――はじめまして"),
            )

def main(): # pragma: no cover
    return build_to_story(story(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

