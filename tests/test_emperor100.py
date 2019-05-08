# -*- coding: utf-8 -*-
"""Test: emperor100
"""
import unittest
from storybuilder.builder import testutils as utl
from src.emperor100.story import world, story


_FILENAME = "emperor100.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "emperor 100 project")

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
                    ("story", self.story, self.w.hero, self.w.garneth),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.hero.be(w.i.throne, w.i.emperor100),
                        w.lion.be("dead"),
                        w.hero.do(w.i.enthrone),
                        w.hero.be(w.i.portchara),
                        True),
                ])

