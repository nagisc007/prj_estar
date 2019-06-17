# -*- coding: utf-8 -*-
"""Test: I'm my mine
"""
import unittest
from storybuilder.builder import testutils as utl
from src.anotherme.story import world, story, base_infos, outline_infos
from src.anotherme.config import THEMES, MOTIFS
from src.anotherme import chapter01 as chap1
from src.anotherme import chapter02 as chap2
from src.anotherme import chapter03 as chap3
from src.anotherme import chapter04 as chap4
from src.anotherme import chapter05 as chap5


_FILENAME = "anotherme.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "The another me project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self, base_infos(self.w))

    def test_has_outline_infos(self):
        utl.exists_outline_infos_by_data(self, outline_infos(self.w))

    def test_has_themes(self):
        utl.followed_themes(self, self.story, THEMES)

    def test_has_motifs(self):
        utl.followed_motifs(self, self.story, MOTIFS)
