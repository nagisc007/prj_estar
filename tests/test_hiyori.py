# -*- coding: utf-8 -*-
"""Test the story of hiyori
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.hiyori.story import Something
from src.hiyori.story import master, story, ep1, ep2, ep3, ep4


_FILENAME = "hiyori.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "hiyori project")

    def setUp(self):
        self.ma = master()
        self.st = story(self.ma)
        self.ep1 = ep1(self.ma)
        self.ep2 = ep2(self.ma)
        self.ep3 = ep3(self.ma)
        self.ep4 = ep4(self.ma)

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.st))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.st))

    @unittest.skip("in preparation")
    def test_has_basic_infos(self):
        data = [
                ("story", self.st, "hero", "rival"),
                ("ep1", self.ep1, "hero", "rival"),
                ("ep2", self.ep2, "hero", "rival"),
                ("ep3", self.ep3, "hero", "rival"),
                ("ep4", self.ep4, "hero", "rival"),
                ]

        for title, story, hero, rival in data:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    @unittest.skip("in preparation")
    def test_has_outline_infos(self):
        data = [
                ("story", self.st, "what", "why", "how", "result"),
                ("ep1", self.ep1, "what", "why", "how", "result"),
                ("ep2", self.ep2, "what", "why", "how", "result"),
                ("ep3", self.ep3, "what", "why", "how", "result"),
                ("ep4", self.ep4, "what", "why", "how", "result"),
                ]

        for title, story, what, why, how, result in data:
            with self.subTest(title=title, story=story, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, story, what, why, how, result))

