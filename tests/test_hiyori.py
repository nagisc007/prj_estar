# -*- coding: utf-8 -*-
"""Test the story of hiyori
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.hiyori.story import Something
from src.hiyori.story import master, story, ep_intro, ep_tagawa, ep_future, ep_myhiyori


_FILENAME = "hiyori.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "hiyori project")

    def setUp(self):
        self.ma = master()
        self.st = story(self.ma)
        self.ep1 = ep_intro(self.ma)
        self.ep2 = ep_tagawa(self.ma)
        self.ep3 = ep_future(self.ma)
        self.ep4 = ep_myhiyori(self.ma)

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.st))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.st))

    def test_has_basic_infos(self):
        data = [
                ("story", self.st, self.ma.yuko, self.ma.tagawa),
                ("ep1", self.ep1, self.ma.yuko, self.ma.tagawa),
                ("ep2", self.ep2, self.ma.yuko, self.ma.tagawa),
                ("ep3", self.ep3, self.ma.yuko, self.ma.tagawa),
                ("ep4", self.ep4, self.ma.yuko, self.ma.tagawa),
                ]

        for title, story, hero, rival in data:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        ma = self.ma
        data = [
                ("story", self.st,
                    ma.yuko.know(ma.tagawa, ma.reason).want(),
                    ma.yuko.look(ma.tagawa, "サボる"),
                    ma.yuko.go(ma.tagawa, ma.tanbo),
                    ma.yuko.talk(ma.myhiyori)),
                ("ep1", self.ep1,
                    ma.yuko.know(ma.tagawa, ma.reason).want(),
                    ma.yuko.look(ma.tagawa, "サボる"),
                    ma.yuko.think("サボる決断"),
                    ma.yuko.go("学校を抜け出す")),
                ("ep2", self.ep2,
                    ma.yuko.look(ma.tagawa, "どこにいるか"),
                    ma.yuko.know(ma.tagawa, ma.reason).want(),
                    ma.yuko.go(ma.tagawa, "尾行"),
                    ma.yuko.know(ma.tagawa, ma.reason)),
                ("ep3", self.ep3,
                    ma.yuko.think(ma.myfuture),
                    ma.yuko.hear(ma.tagawa, ma.reason),
                    ma.yuko.talk(ma.takemura, "相談"),
                    ma.yuko.think(ma.myfuture)),
                ("ep4", self.ep4,
                    ma.yuko.look(ma.myfuture).want(),
                    ma.yuko.think(ma.myfuture),
                    ma.yuko.talk(ma.tagawa, "告白"),
                    ma.yuko.look(ma.myhiyori)),
                ]

        for title, story, what, why, how, result in data:
            with self.subTest(title=title, story=story, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, story, what, why, how, result, True))

