# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest
from storybuilder.builder import testutils as utl
from src.s100.story import world, story, ep_intro, ep_middle, ep_climax, ep_end
from src.s100.config import THEMES


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
                    ("ep1", self.ep1, self.w.hero, self.w.osaki),
                    ("ep2", self.ep2, self.w.hero, self.w.fuyumi),
                    ("ep3", self.ep3, self.w.hero, self.w.futureman),
                    ("ep4", self.ep4, self.w.hero, self.w.pastman),
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
                    ("ep1", self.ep1,
                        w.hero.do("write", "$must"),
                        w.hero.deal(w.fear_mail),
                        w.hero.have(w.terminal),
                        w.hero.meet(w.ft_fuyumi),
                        True),
                    ("ep2", self.ep2,
                        w.hero.talk("説得", w.fuyumi),
                        w.hero.talk("別離", w.fuyumi),
                        w.hero.look(w.fuyumi, "自分の小説"),
                        w.hero.have(w.i.help_mail),
                        True),
                    ("ep3", self.ep3,
                        w.hero.do("help", w.futureman),
                        w.hero.know(w.futureman, "dead"),
                        w.hero.do(w.futureman, "小説を書く"),
                        w.hero.be("dead"),
                        True),
                    ("ep4", self.ep4,
                        w.hero.go("過去に戻る"),
                        w.hero.be("dead"),
                        w.hero.deal(w.terminal),
                        w.hero.look(w.pastman),
                        True),
                    ])

    def test_has_themes(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))
