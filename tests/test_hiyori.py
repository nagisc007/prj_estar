# -*- coding: utf-8 -*-
"""Test the story of hiyori
"""
import unittest
from storybuilder.builder import testutils as utl
from src.hiyori.story import world, story, ep_intro, ep_tagawa, ep_future, ep_myhiyori


_FILENAME = "hiyori.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "hiyori project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.ep1 = ep_intro(self.w)
        self.ep2 = ep_tagawa(self.w)
        self.ep3 = ep_future(self.w)
        self.ep4 = ep_myhiyori(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    @unittest.skip('use each current')
    def test_exists_looking(self):
        self.assertTrue(testtools.exists_looking_from_master(self.story, self.ma))

    @unittest.skip('wip')
    def test_exists_looking_each(self):
        for key in [v[0] for v in CHARAS] + [v[0] for v in STAGES]:
            with self.subTest(key=key):
                self.assertEqual(testtools.exists_looking_of_the_subject(self.story, self.ma[key]), True)

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags(self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                ("story", self.story, self.w.yuko, self.w.tagawa),
                ("ep1", self.ep1, self.w.yuko, self.w.tagawa),
                ("ep2", self.ep2, self.w.yuko, self.w.tagawa),
                ("ep3", self.ep3, self.w.yuko, self.w.tagawa),
                ("ep4", self.ep4, self.w.yuko, self.w.tagawa),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                ("story", self.story,
                    w.yuko.know(w.tagawa, w.i.reason, "$want"),
                    w.yuko.look(w.tagawa, "サボる"),
                    w.yuko.go(w.tagawa, w.stage.tanbo),
                    w.yuko.talk(w.i.myhiyori),
                    True),
                ("ep1", self.ep1,
                    w.yuko.know(w.tagawa, w.i.reason, "$want"),
                    w.yuko.look(w.tagawa, "サボる"),
                    w.yuko.think("サボる決断"),
                    w.yuko.go(w.stage.school, "抜け出す"),
                    True),
                ("ep2", self.ep2,
                    w.yuko.look(w.tagawa, "どこにいるか"),
                    w.yuko.know(w.tagawa, w.i.reason, "$want"),
                    w.yuko.hear(w.granpa, w.tagawa, "居場所"),
                    w.yuko.know(w.tagawa, w.i.reason),
                    True),
                ("ep3", self.ep3,
                    w.yuko.think(w.i.myfuture, "$must"),
                    w.yuko.hear(w.tagawa, w.i.reason),
                    w.yuko.talk(w.tagawa, "将来"),
                    w.yuko.think(w.i.myfuture),
                    True),
                ("ep4", self.ep4,
                    w.yuko.look(w.i.myfuture, "$want"),
                    w.yuko.think(w.i.myfuture),
                    w.yuko.talk(w.tagawa, "告白"),
                    w.yuko.look(w.i.myhiyori),
                    True),
                ])

