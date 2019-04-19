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
    return m.story("はじめましての百文字語り",
            m.my.be(m.apart, m.day1),
            m.my.remember(m.you, m.website),
            m.my.talk(m.you).non(),
            m.my.deal("伝える", m.you, m.some()).want(),
            m.my.look(m.estar, m.contest),
            m.my.know(m.estar),
            m.my.think("何もない"),
            m.my.think("気づく", "原稿も真っ白"),
            m.my.deal(m.phone),
            m.my.do(m.firstword, "書く"),
            )

def main(): # pragma: no cover
    return build_to_story(story(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

