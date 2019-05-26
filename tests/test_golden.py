# -*- coding: utf-8 -*-
"""Test: golden girl
"""
import unittest
from storybuilder.builder import testutils as utl
from src.golden.story import world, story, ep_intro, ep_unfortune, ep_decision
from src.golden.config import THEMES, MOTIFS


_FILENAME = "golden.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "golden girls project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.ep1 = ep_intro(self.w)
        self.ep2 = ep_unfortune(self.w)
        self.ep3 = ep_decision(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.fukuo, self.w.hiroko),
                    ("ep1", self.ep1, self.w.fukuo ,self.w.hiroko),
                    ("ep2", self.ep2, self.w.fukuo ,self.w.hiroko),
                    ("ep3", self.ep3, self.w.fukuo ,self.w.hiroko),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.fukuo.deal("guard", w.kana),
                        w.kana.be(w.i.goldsyndrome),
                        w.fukuo.deal(w.fund),
                        w.fukuo.deal(w.kana, w.i.god),
                        True),
                    ("ep1", self.ep1,
                        w.fukuo.deal("guard", w.kana),
                        w.kana.be(w.i.goldsyndrome),
                        w.fukuo.meet(w.stage.labo, w.doc),
                        w.fukuo.deal(w.kana, w.stage.labo, "預ける"),
                        True),
                    ("ep2", self.ep2,
                        w.fukuo.think(w.kana, "guard"),
                        w.kana.deal(w.kanacell, "奪われる"),
                        w.fukuo.go(w.stage.labo),
                        w.hiroko.be(w.i.neurosis),
                        True),
                    ("ep3", self.ep3,
                        w.fukuo.do("stop", w.hiroko),
                        w.hiroko.think(w.i.killkana),
                        w.fukuo.deal(w.hiroko, w.i.golden),
                        w.fukuo.deal(w.kana, w.i.god),
                        True),
                ])

    def test_has_themes(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))

    def test_has_motifs(self):
        for k, v in MOTIFS.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in_description_in(self.story, MOTIFS[k]))
