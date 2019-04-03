# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.subject import Master, Stage, DayTime, Item, Word, something
from storybuilder.builder.person import Person
from storybuilder.builder.tools import build_to_story


# story configs


# episodes


# main
def story():
    ma = Master("my side mystery")
    return ma.story("わたしの隣席はいつも不在",
            )


def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())
