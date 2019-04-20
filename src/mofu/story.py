# -*- coding: utf-8 -*-
"""Story program.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.master import Master
from storybuilder.builder.tools import build_to_story


# configs
CHARAS = (
        ("tanabe", "田辺守", 31, "male", "会社員"),
        ("mofu", "モフ", 1, "female", "謎の生物"),
        )

STAGES = (
        ("apart", "田辺のアパート"),
        ("office", "田辺の会社"),
        )

DAYS = (
        ("meetday", "モフを拾った日"),
        )

ITEMS = (
        )

WORDS = (
        )

FLAGS = (
        )

# main
def master():
    m = Master("Mofu life")
    m.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    m.set_flags(FLAGS)
    return m


def story(m: Master):
    return m.story("もふもふのきもち",
            )


def main(): # pragma: no cover
    return build_to_story(story(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

