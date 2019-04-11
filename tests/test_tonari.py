# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.tonari.story import Something
from src.tonari.story import master, story, ep_intro, ep_oldman, ep_ordinary


_FILENAME = "tonari.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "story")

    def setUp(self):
        self.story = story()
        self.ma = master()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            self.ma.yuno, self.ma.kenjo))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            self.ma.yuno.know(self.ma.forgotten).must(),
            self.ma.yuno.feel(self.ma.ghost),
            self.ma.yuno.do("meet", self.ma.kenjo),
            self.ma.yuno.remember(self.ma.promise),
            ))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "episodes")

    def setUp(self):
        self.ma = master()
        self.ep1 = ep_intro(self.ma)
        self.ep2 = ep_oldman(self.ma)
        self.ep3 = ep_ordinary(self.ma)

    def test_has_basic_infos(self):
        data = [
                ("ep1", self.ep1, self.ma.yuno, self.ma.kenjo),
                ("ep2", self.ep2, self.ma.yuno, self.ma.kenjo),
                ("ep3", self.ep3, self.ma.yuno, self.ma.mitsuro),
                ]
        for title, ep, hero, rival in data:
            with self.subTest(title=title, ep=ep, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, ep, hero, rival))

    def test_has_outline_infos(self):
        data = [
                ("ep1", self.ep1,
                    self.ma.yuno.feel(self.ma.ghost),
                    self.ma.yuno.behav(Something(), "隣に").non(),
                    self.ma.yuno.move(self.ma.train),
                    self.ma.yuno.behav("座る", self.ma.kenjo).ps(),
                    ),
                ("ep2", self.ep2,
                    self.ma.yuno.hear(self.ma.ghost, self.ma.kenjo),
                    self.ma.kenjo.talk(self.ma.yuno, self.ma.ghost),
                    self.ma.kenjo.talk("教える", self.ma.yuno, self.ma.suitman),
                    self.ma.yuno.remember(self.ma.mitsuro),
                    ),
                ("ep3", self.ep3,
                    self.ma.yuno.do("死").must(),
                    self.ma.yuno.be(self.ma.sick),
                    self.ma.yuno.talk("お願い", self.ma.kenjo, self.ma.yunowill),
                    self.ma.yuno.do("埋葬", "彼の隣", self.ma.mitsuro).ps(),
                    ),
                ]

        for title, ep, what, why, how, result in data:
            with self.subTest(title=title, ep=ep, what=what, why=why, how=how,
                    result=result):
                self.assertTrue(testtools.has_outline_infos(self, ep, what, why, how, result, True))

