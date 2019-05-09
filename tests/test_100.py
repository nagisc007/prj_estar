# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest
from storybuilder.builder import testutils as utl
from src.s100.story import world, story, ep_intro, ep_middle, ep_climax, ep_end


_FILENAME = "100.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "100 stories")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.ep1 = ep_intro(self.w)
        self.ep2 = ep_middle(self.w)
        self.ep3 = ep_climax(self.w)
        self.ep4 = ep_end(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.hero, self.w.osaki),
                    ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.hero.do("write", "$must"),
                        w.hero.deal(w.fear_mail),
                        w.hero.do("write", w.i.novel),
                        w.hero.know(w.i.his_reason),
                        True),
                    ])

