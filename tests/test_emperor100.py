# -*- coding: utf-8 -*-
"""Test: emperor100
"""
import unittest
from storybuilder.builder import testutils as utl
from src.emperor100.story import world, story, ep_intro, ep_preparation, ep_ceremony


_FILENAME = "emperor100.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "emperor 100 project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.ep1 = ep_intro(self.w)
        self.ep2 = ep_preparation(self.w)
        self.ep3 = ep_ceremony(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.hero, self.w.garneth),
                    ("ep1", self.ep1, self.w.hero, self.w.lion),
                    ("ep2", self.ep2, self.w.hero, self.w.milea),
                    ("ep3", self.ep3, self.w.hero, self.w.garneth),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.hero.be(w.i.throne, w.i.emperor100),
                        w.lion.be("dead"),
                        w.hero.do(w.i.enthrone),
                        w.hero.be(w.i.portchara),
                        True),
                    ("ep1", self.ep1,
                        w.hero.be(w.i.throne, "次期皇帝"),
                        w.hero.be("皇帝の息子"),
                        w.lion.be("dead"),
                        w.hero.know(w.i.throne),
                        True),
                    ("ep2", self.ep2,
                        w.hero.be(w.i.throne, "$must"),
                        w.hero.know(w.i.lion_dead),
                        w.hero.talk(w.milea, w.i.emperor_bug),
                        w.hero.know(w.i.milea_mind),
                        True),
                    ("ep3", self.ep3,
                        w.hero.think("whether", w.i.throne),
                        w.hero.be(w.i.ceremony, "時間が迫る"),
                        w.hero.do(w.i.his_mind),
                        w.hero.be(w.i.portchara, "強制的に"),
                        True),
                ])

