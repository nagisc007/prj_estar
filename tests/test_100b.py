# -*- coding: utf-8 -*-
"""Test the story of 100 chars
"""
import unittest
import storybuilder.builder.testutils as utl
from src.s100b.story import story, world


_FILENAME = "100b.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "100 characters")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    @unittest.skip('wip')
    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))

    def test_has_basic_infos(self):
        w = self.w
        data = [
                ("story", self.story, w.my, w.you),
                ]
        utl.exists_basic_infos_by_data(self, data)

    def test_has_outline_infos(self):
        w = self.w
        data = [
                ("story", self.story,
                    w.my.deal("伝える", "$want", w.you, w.X()),
                    w.my.know(w.i.estar),
                    w.my.deal(w.phone),
                    w.my.do(w.i.firstword, "書く"), True,
                    ),
                ]
        utl.exists_outline_infos_by_data(self, data)

