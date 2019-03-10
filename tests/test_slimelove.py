# -*- coding: utf-8 -*-
"""Test for story of slime-love
"""
import unittest

from storybuilder.builder.base import ActType, Act, Must, Done, Title, Description
from storybuilder.builder.base import Person, Stage, Item, DayTime
from storybuilder.builder.testtools import checked_if_all_actions
from storybuilder.builder.testtools import checked_has_basic_info

# import classes
from slimelove.story import Romus, Milia, Mila, Monsters
from slimelove.story import ArmgardContinent, RathoreKingdom, DoraVila, MtMegido, ACave, MerleVila
from slimelove.story import KnightSword, EngageRing, HerbSoup
from slimelove.story import MonsterDay, NurseDays, FindDay, DevilsDay
# import episodes
from slimelove.story import story
from slimelove.story import ep_brokenbody
from slimelove.story import ep_comeloose
from slimelove.story import ep_meltsomething

class StoryTest(unittest.TestCase):
    """Test the story.

    * Outline
        - Who: 傭兵ロムス
        - Whom: ミア（介抱する唖の女）
        - When: 魔物出現より８年後
        - Where: 洞窟
        - What: 婚約した女を殺した魔物を見つける
        - Why: 女を愛していた
        - How: 魔物退治をしながら旅をする
        - Result: スライムに溶かされる
    """
    def setUp(self):
        self.acts = story()

    def test_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Romus(), Mila()))

    def test_has_the_time(self):
        pass

    def test_has_the_place(self):
        pass

    def test_has_reason(self):
        pass

    def test_has_process(self):
        pass

    def test_has_result(self):
        pass


class EpisodeTest_brokenbody(unittest.TestCase):
    """Test the episode.
    * Outline
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    """
    def setUp(self):
        self.acts = ep_brokenbody(
                MtMegido(), MonsterDay(), Romus(), Monsters(),
                )

    def test_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Romus(), Monsters()))

    def test_has_the_time(self):
        pass

    def test_has_the_place(self):
        pass

    def test_has_reason(self):
        pass

    def test_has_process(self):
        pass

    def test_has_result(self):
        pass


class EpisodeTest_comeloose(unittest.TestCase):
    """Test the episode.
    * Outline
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    """
    def setUp(self):
        self.acts = ep_comeloose(
                ACave(), NurseDays(), Romus(), Mila(), Milia(), HerbSoup(),
                )

    def test_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Romus(), Mila()))

    def test_has_the_time(self):
        pass

    def test_has_the_place(self):
        pass

    def test_has_reason(self):
        pass

    def test_has_process(self):
        pass

    def test_has_result(self):
        pass


class EpisodeTest_meltsomething(unittest.TestCase):
    """Test the episode.
    * Outline
        - Who:
        - Whom:
        - When:
        - Where:
        - What:
        - Why:
        - How:
        - Result:
    """
    def setUp(self):
        self.acts = ep_meltsomething(
                ACave(), FindDay(), Romus(), Mila(), Milia(), EngageRing(),
                )

    def test_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Romus(), Mila()))

    def test_has_the_time(self):
        pass

    def test_has_the_place(self):
        pass

    def test_has_reason(self):
        pass

    def test_has_process(self):
        pass

    def test_has_result(self):
        pass

