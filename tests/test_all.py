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
        # next fantasy
        unittest.makeSuite(test_lv1yusha.StoryTest),
        # writing cheer
        ))

    return suite
