# -*- coding: utf-8 -*-
"""Test: I'm my mine
"""
import unittest
from storybuilder.builder import testutils as utl
from src.mymine.story import world, story
from src.mymine.config import THEMES


_FILENAME = "mymine.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "my mine project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        pass

    def test_has_outline_infos(self):
        pass

    def test_has_themes(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))
