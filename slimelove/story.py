# -*- coding: utf-8 -*-
"""Story that a mercenary's heart was melted by something.
"""
# import path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')

# import libs
from storybuilder.builder.base import ActType, Act, Must, Done, Title, Description
from storybuilder.builder.base import Person, Stage, Item, DayTime
from storybuilder.builder.tools import output, output_md

# define characters

# define stages

# define items

# define daytimes


# episodes
def ep_():
    '''Episode builded.
    '''
    return (
            )


# main
def story():
    '''Story builded.

    Returns:
        tuple:obj:`Act`: story actions.
    '''
    return (
            )


def main(is_debug=True):
    '''Main function.

    Returns:
        True: if completed the process to build and output a story.
    '''
    STORY_FILE = 'slimelove'

    mystory = story()

    output(mystory, is_debug=is_debug) # output to the console
    output_md(mystory, STORY_FILE, is_debug=is_debug) # output to a markdown file

    return True


if __name__ == '__main__':
    import sys
    sys.exi(main())

