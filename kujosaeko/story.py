# -*- coding: utf-8 -*-
"""The story program of kujo saeko doesn't back anything.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import ActionGroup, Stage, Item, DayTime, Word, Master
from storybuilder.builder.person import Person
from storybuilder.builder.tools import build_to_story


# characters


# stages


# items


# words


# daytimes


# episodes


# story
def story() -> ActionGroup:
    '''Define main story.
    '''
    ma = Master("my story")

    return ma.story(
            ma.title("九条冴子は返さない"),
            )


# main
def main() -> bool:
    '''main program.
    '''
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

