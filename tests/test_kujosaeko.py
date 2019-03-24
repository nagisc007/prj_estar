# -*- coding: utf-8 -*-
"""Test the story of kujo saeko
"""
import unittest

from storybuilder.builder.acttypes import ActType
from storybuilder.builder.behavior import Behavior
from storybuilder.builder.base import Master
import storybuilder.builder.testtools as testtools

from kujosaeko.story import story
from kujosaeko.story import ep_incident, ep_intro, ep_relationship
from kujosaeko.story import Kujo, Masato, Misa
from kujosaeko.story import kujo_dad
from kujosaeko.story import masato_apart, kujo_apart, misa_manshion, west_park, tutor_center
from kujosaeko.story import toy_box, dad_gun, blagger
from kujosaeko.story import incident_day, parted_day, white_day


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("**** TEST: Kujo saeko ****")

    def setUp(self):
        self.story = story()

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story,
            Masato(), Kujo()))

    def test_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            Masato().want("何か返して", Kujo()),
            Kujo().give("", Masato()).negative(),
            Masato().go("他の女", Misa()),
            Masato().guard("", Kujo())))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))


class EpisodeTest(unittest.TestCase):

    def setUp(self):
        self.ma = Master("test")
        self.ep1 = ep_intro(self.ma,
                Masato(), Kujo(),
                west_park(), white_day())
        self.ep2 = ep_relationship(self.ma,
                Masato(), Kujo(), Misa(),
                toy_box(), dad_gun(),
                kujo_apart(), masato_apart(), misa_manshion(), tutor_center(), parted_day())
        self.ep3 = ep_incident(self.ma,
                Masato(), Kujo(), Misa(), kujo_dad(),
                dad_gun(), blagger(),
                masato_apart(), kujo_apart(), incident_day())

    def test_ep1_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep1))

    def test_ep2_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep2))

    def test_ep3_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self, self.ep3))

    def test_ep1_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep1,
            Masato(), Kujo()))

    def test_ep2_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep2,
            Masato(), Kujo()))

    def test_ep3_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.ep3,
            Masato(), Kujo()))

    def test_ep1_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.ep1,
            Masato().want("お返し", Kujo()),
            Masato().give("チョコ", Kujo()),
            Masato().invite("デート", Kujo()),
            Kujo().returns("もらったサンドウィッチ", Masato()).negative(),
            ))

    def test_ep2_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.ep2,
            Masato().want("彼女の考え", Kujo()),
            Masato().think("事情がある", Kujo()),
            Masato().open("", toy_box()),
            Masato().go("他の女", Misa()),
            ))

    def test_ep3_has_outline_infos(self):
        self.assertTrue(testtools.has_outline_infos(self, self.ep3,
            Masato().want("助ける", Kujo()),
            Masato().know("", blagger()),
            Masato().contact("", Kujo()),
            Masato().guard("", Kujo()),
            ))
