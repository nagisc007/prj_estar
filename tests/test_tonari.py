
# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest
import storybuilder.builder.testtools as testtools

from src.tonari.story import story


_FILENAME = "tonari.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _print_title(_FILENAME, "story")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    @unittest.skip('in preparation')
    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            testtools.Item('hero'), testtools.Item('rival')))

    @unittest.skip('in preparation')
    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            testtools.Info('what'),
            testtools.Info('why'),
            testtools.Info('how'),
            testtools.Info('result'),
            ))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _print_title(_FILENAME, "episodes")

    def setUp(self):
        self.ma = Master('test')
        self.ep1 = ()
        self.ep2 = ()
        self.ep3 = ()

    @unittest.skip('in preparation')
    def test_has_basic_infos(self):
        data = [
                (self.ep1, Info("hero"), Info("rival")),
                (self.ep2, Info("hero"), Info("rival")),
                (self.ep3, Info('hero'), Info('rival')),
                ]
        for ep, hero, rival in data:
            with self.subTest(ep=ep, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, ep, hero, rival))

    @unittest.skip('in preparation')
    def test_has_outline_infos(self):
        data = [
                (self.ep1,
                    Info('what'),
                    Info('why'),
                    Info('how'),
                    Info('result')),
                (self.ep2,
                    Info('what'),
                    Info('why'),
                    Info('how'),
                    Info('result')),
                (self.ep3,
                    Info('what'),
                    Info('why'),
                    Info('how'),
                    Info('result')),
                ]

        for ep, what, why, how, result in data:
            with self.subTest(ep=ep, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, ep, what, why, how, result))


def _print_title(fname: str, title: str):
    print("\n**** TEST: {} - {} ****".format(fname, title))
