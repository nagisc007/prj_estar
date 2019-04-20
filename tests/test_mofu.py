# -*- coding: utf-8 -*-
"""Test the story of mofu life
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.mofu.story import story, master


_FILENAME = "mofu.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "mofu life project")

    def setUp(self):
        self.m = master()
        self.story = story(self.m)

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))

    def test_has_basic_infos(self):
        pass

    def test_has_outline_infos(self):
        pass
