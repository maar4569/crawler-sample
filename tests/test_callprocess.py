# -*- coding: utf-8 -*-

import unittest
from crawler.apps import callprocess
class TestCallProcess(unittest.TestCase):
    def setUp(self):
        print "setup"
    #success
    def test_success(self):
        ret = callprocess.callhoge("ls")
        self.assertEqual(ret,0)

    #error
    def test_err_processname_not_exists(self):
        with self.assertRaises(Exception):
            callprocess.callhoge("a","a","b")
 
    def test_err_lack_of_args(self):
        with self.assertRaises(Exception):
            callprocess.callhoge("ls -al","b")

if __name__ == "__main__":
    unittest.main()
