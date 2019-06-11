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
        self.ch1 = chap1.story(self.w)
        self.ch2 = chap2.story(self.w)
        self.ch3 = chap3.story(self.w)
        self.ch4 = chap4.story(self.w)
        self.ch5 = chap5.story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self, base_infos(self.w))

    def test_has_outline_infos(self):
        utl.exists_outline_infos_by_data(self, outline_infos(self.w))

    def test_has_themes(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))

    def test_has_motifs(self):
        for k, v in MOTIFS.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, MOTIFS[k]))
