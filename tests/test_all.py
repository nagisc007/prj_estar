# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import each tests
#import test_slimelove
#import test_kujosaeko
#import test_tonari
import test_hiyori
import test_100
import test_100b
import test_emperor100
#import test_mofu
import test_lv1yusha
import test_redchain
import test_golden
import test_anotherme
import test_todaylive
import test_lostbook
import test_umbrella
import test_emergence
import test_disliked
import test_festa
import test_bghost
import test_forbidden
import test_hiyari
import test_hitogomi
import test_vanishcat


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTests((
        # mo-con
        unittest.makeSuite(test_100.StoryTest),
        unittest.makeSuite(test_100b.StoryTest),
        unittest.makeSuite(test_hiyori.StoryTest),
        unittest.makeSuite(test_emperor100.StoryTest),
        unittest.makeSuite(test_golden.StoryTest),
        unittest.makeSuite(test_todaylive.StoryTest),
        unittest.makeSuite(test_umbrella.StoryTest),
        unittest.makeSuite(test_emergence.StoryTest),
        unittest.makeSuite(test_disliked.StoryTest),
        unittest.makeSuite(test_festa.StoryTest),
        unittest.makeSuite(test_hiyari.StoryTest),
        unittest.makeSuite(test_hitogomi.StoryTest),
        unittest.makeSuite(test_vanishcat.StoryTest),
        # next fantasy
        unittest.makeSuite(test_lv1yusha.StoryTest),
        # writing cheer
        unittest.makeSuite(test_redchain.StoryTest),
        unittest.makeSuite(test_lostbook.StoryTest),
        unittest.makeSuite(test_forbidden.StoryTest),
        # others
        unittest.makeSuite(test_anotherme.StoryTest),
        unittest.makeSuite(test_bghost.StoryTest),
        ))

    return suite
