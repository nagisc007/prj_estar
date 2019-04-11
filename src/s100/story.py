# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.master import Master
from storybuilder.builder.subject import Something
from storybuilder.builder.tools import build_to_story


# configs
CHARAS = (
        )

STAGES = (
        )

DAYS = (
        )

ITEMS = (
        )

WORDS = (
        )


# episodes
def ep1(ma: Master):
    return ma.story("Intro")

def ep2(ma: Master):
    return ma.story("Middle")

def ep3(ma: Master):
    return ma.story("Climax")

def ep4(ma: Master):
    return ma.story("End")


# main
def master():
    ma = Master("100 stories")
    ma.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    return ma

def story(ma: Master):
    return ma.story("百妄想騙り",
            ep1(ma),
            ep2(ma),
            ep3(ma),
            ep4(ma),
            )

def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

