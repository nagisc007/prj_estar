# -*- coding: utf-8 -*-
"""Test: the red-chain
"""
import unittest
from storybuilder.builder import testutils as utl
from src.redchain.story import world, story
from src.redchain.chapter01 import story as ep_intro
from src.redchain.chapter02 import story as ep_actoryears
from src.redchain.chapter03 import story as ep_idolyears
from src.redchain.chapter04 import story as ep_lateyears
from src.redchain.chapter05 import story as ep_truth
from src.redchain import chapter06 as chap6
from src.redchain.config import THEMES


_FILENAME = "redchain.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "red-chain")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.ep1 = ep_intro(self.w)
        self.ep2 = ep_actoryears(self.w)
        self.ep3 = ep_idolyears(self.w)
        self.ep4 = ep_lateyears(self.w)
        self.ep5 = ep_truth(self.w)
        self.ep6 = chap6.story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.masuda, self.w.hideko),
                    ("ep1", self.ep1, self.w.masuda, self.w.hideko),
                    ("ep2", self.ep2, self.w.masuda, self.w.h_actor),
                    ("ep3", self.ep3, self.w.masuda, self.w.h_idol),
                    ("ep4", self.ep4, self.w.masuda, self.w.h_later),
                    ("ep5", self.ep5, self.w.masuda, self.w.benio),
                    ("ep6", self.ep6, self.w.masuda, self.w.hideko),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.masuda.think(w.hideko, "何か臭う"),
                        w.masuda.know(w.i.case_fire),
                        w.masuda.deal(w.i.interview),
                        w.masuda.know(w.i.truth),
                        True),
                    ("ep1", self.ep1,
                        w.masuda.deal(w.i.interview, w.stage.thesite),
                        w.masuda.know(w.i.case_fire),
                        w.masuda.hear("関係者"),
                        w.masuda.know(w.deadbody, w.hideko),
                        True),
                    ("ep2", self.ep2,
                        w.masuda.look(w.h_actor, w.i.life),
                        w.masuda.know(w.h_actor),
                        w.masuda.deal(w.i.interview, "業界人"),
                        w.masuda.know(w.hideko, w.h_idol),
                        True),
                    ("ep3", self.ep3,
                        w.masuda.look(w.h_idol, w.i.life),
                        w.masuda.know(w.h_idol),
                        w.masuda.deal(w.i.interview, "当時を知る人"),
                        w.masuda.know(w.i.retire_business),
                        True),
                    ("ep4", self.ep4,
                        w.masuda.have(w.h_later, w.i.life),
                        w.masuda.know(w.h_later),
                        w.masuda.deal(w.i.interview, w.stage.town),
                        w.masuda.know(w.doc),
                        True),
                    ("ep5", self.ep5,
                        w.masuda.meet(w.doc),
                        w.masuda.know(w.doc),
                        w.masuda.talk(w.doc, w.i.doc_secret),
                        w.masuda.know(w.anotherbody, w.benio),
                        True),
                    ("ep6", self.ep6,
                        w.masuda.think(w.hideko, w.i.her_reason),
                        w.masuda.hear(w.movie, "舞台はこの町"),
                        w.masuda.look(w.stage.thesite),
                        w.masuda.think("仕事を続ける"),
                        True),
                ])

    def test_has_theme_words(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))
