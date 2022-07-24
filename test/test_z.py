"""
    Test the test python module 'z.py' These tests will be built out into different test modules in the future.
    Made by jjheffernan on week 5 of Zip Code Wilmington
"""

import unittest
from statzcw import z

class test_z(unittest.TestCase):

    def test_count(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 5)


        ]
        # build these into test for different types
        # {0: 1, 1:, 2},
        # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

        for filepath, expected in test_cases:
            expected
            actual = len(test_cases[0])
            self.assertEquals(expected,actual)

    def test_mean(self):
        pass

    def test_mode(self):
        pass

    def test_median(self):
        pass

    def test_variance(self):
        # test_list = [6, 7, 3, 9, 10, 15]
        pass

    def test_stddev(self):
        pass

    def test_stderr(self):
        pass

    def test_corr(self):
        pass
