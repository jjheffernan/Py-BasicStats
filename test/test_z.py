"""
    Test the test python module 'z.py' These tests will be built out into different test modules in the future.
    Made by jjheffernan on week 5 of Zip Code Wilmington
"""

import unittest

import statzcw.z
from statzcw import z


class testZ(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_count(self):
        # expected
        test_cases = [
            ((1, 2, 3, 4, 5), 5),
            ((1, 4, 9, 16), 4),
            ((1,1,1,1,1,1,1,1), 8)

        ]
        # actual
        # build these into test for different types
        # {0: 1, 1:, 2},
        # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

        # asserting when=then
        # for expected in test_cases:
        expected = [item[1] for item in test_cases]
        # actual = len(test_cases[0])
        actual = statzcw.z.count([list(item[0]) for item in test_cases])
        self.assertEqual(expected, actual)

    def test_mean(self):
        # expected results
        test_cases = [
            ((), 0),
            ((), 0),
            ((), 0),
        ]

        expected = [item[1] for item in test_cases]
        for test in test_cases:
            with self.subTest:
                test_data = list(test_cases(test))
                actual = statzcw.z.mean(test_data)
                self.assertEquals(expected, actual)
        # pass

    def test_mode(self):
        # expected results
        test_cases = [
            ((), 0),
            ((), 0),
            ((), 0),
        ]

        expected = [item[1] for item in test_cases]

        actual = statzcw.z.mean(test_cases)
        self.assertEquals(expected, actual)
        pass

    def test_median(self):
        # expected results
        test_cases = [
            ((), 0),
            ((), 0),
            ((), 0),
        ]

        expected = [item[1] for item in test_cases]

        actual = statzcw.z.mean(test_cases)
        self.assertEquals(expected, actual)
        pass

    def test_variance(self):
        # test_list = [6, 7, 3, 9, 10, 15]
        # expected results
        test_cases = [
            ((), 0),
            ((), 0),
            ((), 0),
        ]

        expected = [item[1] for item in test_cases]

        actual = statzcw.z.mean(test_cases)
        self.assertEquals(expected, actual)
        pass

    def test_stddev(self):
        # test_list = [4, 5, 8, 9, 10]
        # expected results
        test_cases = [
            ((), 0),
            ((), 0),
            ((), 0),
        ]

        expected = [item[1] for item in test_cases]

        actual = statzcw.z.mean(test_cases)
        self.assertEquals(expected, actual)
        pass

    def test_stderr(self):
        # data = [3, 4, 4, 5, 7, 8, 12, 14, 14, 15, 17, 19, 22, 24, 24, 24, 25, 28, 28, 29]
        # data = [3, 4, 4, 5, 7, 8, 12, 14, 14, 15, 17, 19, 22, 24, 24, 24, 25, 28, 28, 150]
        # expected results
        test_cases = [
            ((), 0),
            ((), 0),
            ((), 0),
        ]

        expected = [item[1] for item in test_cases]

        actual = statzcw.z.mean(test_cases)
        self.assertEquals(expected, actual)
        pass

    def test_covariance(self):
        # x_coordinates = [1, 2, 3, 4, 5]
        # y_coordinates = [1, 2, 3, 4, 5]
        # expected results
        test_cases = [
            ((), 0),
            ((), 0),
            ((), 0),
        ]

        expected = [item[1] for item in test_cases]

        actual = statzcw.z.mean(test_cases)
        self.assertEquals(expected, actual)
        pass

    def test_corr(self):
        # expected results
        test_cases = [
            ([], [], 0),
            ([], [], 0),
            ([], [], 0),
        ]

        expected = [item[1] for item in test_cases]

        actual = statzcw.z.corr(test_cases[0][0], test_cases[0][1])
        self.assertEquals(expected, actual)
        pass


if __name__ == '__main__':
    unittest.main()
