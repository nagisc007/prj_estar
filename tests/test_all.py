# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import each tests
import test_slimelove

def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    # add each tests
    suite.addTest(unittest.makeSuite(test_slimelove.StoryTest))
    suite.addTest(unittest.makeSuite(test_slimelove.EpisodeTest_brokenbody))
    suite.addTest(unittest.makeSuite(test_slimelove.EpisodeTest_comeloose))
    suite.addTest(unittest.makeSuite(test_slimelove.EpisodeTest_meltsomething))

    return suite
