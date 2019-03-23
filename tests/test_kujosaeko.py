# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from kujosaeko.story import story
from kujosaeko.story import ep_incident, ep_intro, ep_relationship
from kujosaeko.story import Kujo, Masato


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("**** TEST: Kujo saeko ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            Masato(), Kujo()))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Masato().want("何か返して", Kujo()),
            Kujo().give("ない", Masato()),
            Masato().go("他の女"),
            Masato().guard("", Kujo())))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodeTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_ep1_is_all_actions(self):
        pass

    def test_ep1_has_basic_infos(self):
        pass

    def test_ep1_has_outline_infos(self):
        pass
