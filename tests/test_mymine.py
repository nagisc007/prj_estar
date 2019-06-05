# -*- coding: utf-8 -*-
"""Test: I'm my mine
"""
import unittest
from storybuilder.builder import testutils as utl
from src.mymine.story import world, story
from src.mymine.config import THEMES, MOTIFS
from src.mymine import chapter01 as chap1
from src.mymine import chapter02 as chap2
from src.mymine import chapter03 as chap3
from src.mymine import chapter04 as chap4
from src.mymine import chapter05 as chap5


_FILENAME = "mymine.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "my mine project")

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
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.kyoko, self.w.shota),
                    # chapter 01
                    ("chapter1", self.ch1, self.w.kyoko, self.w.shota),
                    # chapter 02
                    ("chapter2", self.ch2, self.w.kyoko, self.w.shota),
                    # chapter 03
                    ("chapter3", self.ch3, self.w.kyoko, self.w.shota),
                    # chapter 04
                    ("chapter4", self.ch4, self.w.kyoko, self.w.shota),
                    # chapter 05
                    ("chapter5", self.ch5, self.w.kyoko, self.w.shota),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.kyoko.think(THEMES["problem"]),
                        w.kyoko.look(w.another),
                        w.kyoko.meet(w.shota),
                        w.kyoko.deal("vanish", w.shota),
                        True),
                    # chapter 01
                    ("chapter1", self.ch1,
                        w.kyoko.think("他人と付き合えない"),
                        w.kyoko.look(w.another),
                        w.kyoko.go(w.circle, "逃げ出す"),
                        w.kyoko.meet(w.shota),
                        True),
                    # chapter 02
                    ("chapter2", self.ch2,
                        w.kyoko.think(w.shota, "知りたい"),
                        w.shota.look(w.another),
                        w.kyoko.deal("一緒に暮らす"),
                        w.kyoko.deal(w.shota, w.i.proposed),
                        True),
                    # chapter 03
                    ("chapter3", self.ch3,
                        w.kyoko.be(),
                        w.kyoko.be(),
                        w.kyoko.be(),
                        w.kyoko.be(),
                        True),
                    # chapter 04
                    ("chapter4", self.ch4,
                        w.kyoko.be(),
                        w.kyoko.be(),
                        w.kyoko.be(),
                        w.kyoko.be(),
                        True),
                    # chapter 05
                    ("chapter5", self.ch5,
                        w.kyoko.be(),
                        w.kyoko.be(),
                        w.kyoko.be(),
                        w.kyoko.be(),
                        True),
                ])

    def test_has_themes(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))

    def test_has_motifs(self):
        for k, v in MOTIFS.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, MOTIFS[k]))
