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

    return suite
