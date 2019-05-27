# -*- coding: utf-8 -*-
"""Test: Today I've lived
"""
import unittest
from storybuilder.builder import testutils as utl
from src.todaylive.story import world, story
from src.todaylive.config import THEMES, MOTIFS


_FILENAME = "todaylive.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "today lived project")

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
                    ("story", self.story, self.w.ito, self.w.ito),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.ito.be(),
                        w.ito.be(),
                        w.ito.be(),
                        w.ito.be(),
                        True),
                ])

    def test_has_themes(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))

    def test_has_motifs(self):
        for k, v in MOTIFS.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in_description_in(self.story, MOTIFS[k]))

