# -*- coding: utf-8 -*-
"""Test: the red-chain
"""
import unittest
from storybuilder.builder import testutils as utl
from src.redchain.story import world, story
from src.redchain.config import THEMES

_FILENAME = "redchain.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "red-chain")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.masuda, self.w.hideko),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.masuda.think(w.hideko, "何か臭う"),
                        w.masuda.know(w.i.case_fire),
                        w.masuda.deal(w.i.interview),
                        w.masuda.know(w.i.truth),
                        True),
                ])

    def test_has_theme_words(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))
