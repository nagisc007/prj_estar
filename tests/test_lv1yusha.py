# -*- coding: utf-8 -*-
"""Test: lv1yusha.py
"""
import unittest
from storybuilder.builder import testutils as utl
from src.lv1yusha.story import world, story, ep_intro, ep_heros_sun, ep_allies, ep_destruction, ep_anotherhero


_FILENAME = "lv1yusha.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "lv1 yusha project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.ep1 = ep_intro(self.w)
        self.ep2 = ep_heros_sun(self.w)
        self.ep3 = ep_allies(self.w)
        self.ep4 = ep_destruction(self.w)
        self.ep5 = ep_anotherhero(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_exists_looking(self):
        pass

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags(self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.hero, self.w.father),
                    ("ep1", self.ep1, self.w.hero, self.w.father),
                    ("ep2", self.ep2, self.w.hero, self.w.king),
                    ("ep3", self.ep3, self.w.hero, self.w.diana),
                    ("ep4", self.ep4, self.w.hero, self.w.daemon1),
                    ("ep5", self.ep5, self.w.hero, self.w.hero99),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.hero.go(w.i.voyage, "$must"),
                        w.hero.know(w.i.reviveboss),
                        w.hero.be(w.i.deadly),
                        w.hero.have(w.hero99, w.i.coop),
                        True),
                    ("ep1", self.ep1,
                        w.hero.go(w.i.voyage),
                        w.hero.know(w.i.dadlost),
                        w.hero.be(w.i.becomeyusha),
                        w.hero.talk(w.mother, w.i.callhero),
                        True),
                    ("ep2", self.ep2,
                        w.hero.go(w.stage.castle, "$must"),
                        w.hero.deal(w.i.callhero),
                        w.hero.go(w.stage.myhome),
                        w.hero.deal(w.king, w.i.bustered),
                        True),
                    ("ep3", self.ep3,
                        w.hero.deal(w.i.gatherally),
                        w.hero.know(w.marc, w.i.gatherally),
                        w.hero.go(w.stage.bar),
                        w.hero.talk(w.diana),
                        True),
                    ("ep4", self.ep4,
                        w.hero.go(w.stage.tower1, "$must"),
                        w.hero.know(w.diana, w.stage.tower1),
                        w.hero.go("walk", w.stage.tower1),
                        w.hero.be(w.i.massacre),
                        True),
                    ("ep5", self.ep5,
                        w.hero.do("生き延びる"),
                        w.hero.be(w.i.massacre),
                        w.hero.go("runaway"),
                        w.hero.have(w.hero99, w.i.coop),
                        True),
                ])

    @unittest.skip('wip')
    def test_exists_keywords(self):
        utl.exists_keywords_by_data(self,
                [
                    "test",
                ])

