#!/usr/bin/python3

import unittest

from core import chk_consecutive, chk_duplicates, compare
from util import precheck


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_chk_consecutive(self):
        self.assertEqual(chk_consecutive(['5', '1', '3']), ['2', '4'])
        self.assertEqual(chk_consecutive(['3', '2', '1']), [])
        self.assertRaises(ValueError, chk_consecutive, ['1', '2', 'a'])

    def test_chk_duplicates(self):
        data = ['1', '1', '2', '2', '2', '3']
        result = [('2', 3), ('1', 2)]
        self.assertEqual(chk_duplicates(data), result)
        self.assertEqual(chk_duplicates(['1', '2', '3']), [])

    def test_compare(self):
        data1 = ['1', '2', '3']
        data2 = ['1', '2', '3', '4']
        self.assertEqual(compare(data1, data2), [])
        self.assertEqual(compare(data2, data1), ['4'])
        self.assertEqual(compare(data1, data2, mode='comm'), ['1', '2', '3'])
        self.assertEqual(compare(data2, data1, mode='comm'), ['1', '2', '3'])

    def test_precheck(self):
        data = '''
        3

        1
        2
        a
        '''
        self.assertEqual(precheck(data), ['1', '2', '3', 'a'])


if __name__ == '__main__':
    unittest.main()
