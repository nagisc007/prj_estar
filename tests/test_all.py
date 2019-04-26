# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import each tests
#import test_slimelove
#import test_kujosaeko
#import test_tonari
import test_hiyori
#import test_100
import test_100b
#import test_mofu


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTests((
        unittest.makeSuite(test_100b.StoryTest),
        unittest.makeSuite(test_hiyori.StoryTest),
        ))

    return suite
