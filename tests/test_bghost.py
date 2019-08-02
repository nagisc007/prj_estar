# -*- coding: utf-8 -*-
"""Test: The blue ghost
"""
import unittest
from storybuilder.builder import testutils as utl
from src.bghost.story import world, story, story_baseinfos, story_outlines
from src.bghost.config import THEMES, MOTIFS


_FILENAME = "bghost.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "The blue ghost project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self, story_baseinfos(self.w))

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self, story_outlines(self.w))

    def test_has_themes(self):
        utl.followed_themes(self, self.story, THEMES)

    def test_has_motifs(self):
        utl.followed_motifs(self, self.story, MOTIFS)
