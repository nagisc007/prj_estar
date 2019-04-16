# -*- coding: utf-8 -*-
"""Test the story of hiyori
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.hiyori.story import master, story, ep_intro, ep_tagawa, ep_future, ep_myhiyori
from src.hiyori.story import CHARAS, STAGES


_FILENAME = "hiyori.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "hiyori project")

    def setUp(self):
        self.ma = master()
        self.story = story(self.ma)
        self.ep1 = ep_intro(self.ma)
        self.ep2 = ep_tagawa(self.ma)
        self.ep3 = ep_future(self.ma)
        self.ep4 = ep_myhiyori(self.ma)

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    @unittest.skip('use each current')
    def test_exists_looking(self):
        self.assertTrue(testtools.exists_looking_from_master(self.story, self.ma))

    def test_exists_looking_each(self):
        for key in [v[0] for v in CHARAS] + [v[0] for v in STAGES]:
            with self.subTest(key=key):
                self.assertEqual(testtools.exists_looking_of_the_subject(self.story, self.ma[key]), True)

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))

    def test_has_basic_infos(self):
        data = [
                ("story", self.story, self.ma.yuko, self.ma.tagawa),
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
                ("story", self.story,
                    ma.yuko.know(ma.tagawa, ma.reason).want(),
                    ma.yuko.look(ma.tagawa, "サボる"),
                    ma.yuko.go(ma.tagawa, ma.tanbo),
                    ma.yuko.talk(ma.myhiyori)),
                ("ep1", self.ep1,
                    ma.yuko.know(ma.tagawa, ma.reason).want(),
                    ma.yuko.look(ma.tagawa, "サボる"),
                    ma.yuko.think("サボる決断"),
                    ma.yuko.go(ma.school, "抜け出す")),
                ("ep2", self.ep2,
                    ma.yuko.look(ma.tagawa, "どこにいるか"),
                    ma.yuko.know(ma.tagawa, ma.reason).want(),
                    ma.yuko.hear(ma.granpa, ma.tagawa, "居場所"),
                    ma.yuko.know(ma.tagawa, ma.reason)),
                ("ep3", self.ep3,
                    ma.yuko.think(ma.myfuture).must(),
                    ma.yuko.hear(ma.tagawa, ma.reason),
                    ma.yuko.talk(ma.tagawa, "将来"),
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

