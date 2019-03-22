# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from kujosaeko.story import story


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("**** TEST: Kujo saeko ****")

    def setUp(self):
        pass

    def test_is_all_actions(self):
        pass

    def test_has_basic_infos(self):
        pass

    def test_has_outline_infos(self):
        pass


class EpisodeTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_ep1_is_all_actions(self):
        pass

    def test_ep1_has_basic_infos(self):
        pass

    def test_ep1_has_outline_infos(self):
        pass
