# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

# import each tests
#import test_slimelove
#import test_kujosaeko
import test_tonari
import test_hiyori
import test_100
import test_100b
import test_mofu


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

    # mousou contests
    suite.addTest(unittest.makeSuite(test_hiyori.StoryTest))
    suite.addTest(unittest.makeSuite(test_100.StoryTest))
    suite.addTest(unittest.makeSuite(test_100b.StoryTest))

    # writing cheer campains
    suite.addTest(unittest.makeSuite(test_mofu.StoryTest))

    return suite
