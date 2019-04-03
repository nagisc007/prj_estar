# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import each tests
#import test_slimelove
#import test_kujosaeko
import test_tonari


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    # story of the slime love
    #suite.addTest(unittest.makeSuite(test_slimelove.StoryTest))
    #suite.addTest(unittest.makeSuite(test_slimelove.EpisodeTest_brokenbody))
    #suite.addTest(unittest.makeSuite(test_slimelove.EpisodeTest_comeloose))
    #suite.addTest(unittest.makeSuite(test_slimelove.EpisodeTest_meltsomething))

    # story of the kujo saeko
    #suite.addTest(unittest.makeSuite(test_kujosaeko.StoryTest))
    #suite.addTest(unittest.makeSuite(test_kujosaeko.EpisodeTest))

    # tonari
    suite.addTest(unittest.makeSuite(test_tonari.StoryTest))
    suite.addTest(unittest.makeSuite(test_tonari.EpisodesTest))

    return suite
