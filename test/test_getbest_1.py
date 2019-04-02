#!/usr/bin/env python3

import unittest

import getbest


class TestExclude(unittest.TestCase):

    def getCols(f):
        c1 = getbest.getCols(f)
        self.assertEqual(c1,1,2)

    def findTop(f,num_col, mark_col):
        
        c1 = getbest.findTop(f,num_col, mark_col)
        self.assertEqual(c1,1665909,99)

if __name__ == '__main__':


    unittest.main()
