
# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest
import storybuilder.builder.testtools as testtools

from src.tonari.story import Master,story, sdb, something
from src.tonari.story import ep_intro, ep_oldman, ep_ordinary


_FILENAME = "tonari.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _print_title(_FILENAME, "story")

    def setUp(self):
        self.story = story()
        self.db = sdb()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            self.db.yuno, self.db.kenjo))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            self.db.yuno.know(self.db.forgotten).must(),
            self.db.yuno.curious(about=self.db.ghost),
            self.db.yuno.meet(self.db.kenjo),
            self.db.yuno.remember(about=self.db.promise),
            ))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _print_title(_FILENAME, "episodes")

    def setUp(self):
        self.ma = Master('test')
        self.db = db = sdb()
        self.ep1 = ep_intro(self.ma, self.db)
        self.ep2 = ep_oldman(self.ma, self.db)
        self.ep3 = ep_ordinary(self.ma, self.db)

    def test_has_basic_infos(self):
        data = [
                ("ep1", self.ep1, self.db.yuno, self.db.kenjo),
                ("ep2", self.ep2, self.db.yuno, self.db.kenjo),
                ("ep3", self.ep3, self.db.yuno, self.db.mitsuro),
                ]
        for title, ep, hero, rival in data:
            with self.subTest(title=title, ep=ep, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, ep, hero, rival))

    def test_has_outline_infos(self):
        db = self.db
        data = [
                ("ep1", self.ep1,
                    db.yuno.curious(db.ghost),
                    db.yuno.sit(something(), "隣に").non(),
                    db.yuno.ride(db.train),
                    db.yuno.sit(by=db.kenjo).ps(),
                    ),
                ("ep2", self.ep2,
                    db.yuno.hear(db.ghost, frm=db.kenjo),
                    db.kenjo.talk(to=db.yuno, about=db.ghost),
                    db.kenjo.teach(db.yuno, about=db.suitman),
                    db.yuno.remember(db.mitsuro),
                    ),
                ("ep3", self.ep3,
                    db.yuno.die().must(),
                    db.yuno.be(db.sick),
                    db.yuno.beg(db.kenjo, of=db.yunowill),
                    db.yuno.bury("彼の隣", of=db.mitsuro),
                    ),
                ]

        for title, ep, what, why, how, result in data:
            with self.subTest(title=title, ep=ep, what=what, why=why, how=how,
                    result=result):
                self.assertTrue(testtools.has_outline_infos(self, ep, what, why, how, result))


def _print_title(fname: str, title: str):
    print("\n**** TEST: {} - {} ****".format(fname, title))
