# -*- coding: utf-8 -*-

import unittest
import log
from  logging  import INFO,DEBUG,WARNING,ERROR

class TestLogger(unittest.TestCase):

    def setUp(self):
        self._filename="mylogger.txt"

    def test_success_all(self):
        mode = DEBUG
        self._log = log.myLogger(mode,__name__ + ".A",self._filename)

        self._log.debug("output debug log! pt1")
        self._log.info("output info log! pt1")
        self._log.debug("output info log! pt2")

        print self._log._log.parent
    def test_success_info(self):
        mode = INFO
        self._log2 = log.myLogger(mode,__name__ + ".B",self._filename)

        self._log2.debug("output debug log! pt1")
        self._log2.info("output info log! pt1")
        self._log2.debug("output debug log! pt2")
        print "log2 parent is"
        print self._log2._log.parent

    def test_success_info2(self):
        mode = DEBUG
        self._log3 = log.myLogger(mode,__name__ + ".C",self._filename)

        self._log3.debug("output debug log! pt10")
        self._log3.info("output info log! pt10")
        self._log3.debug("output debug log! pt20")


        print "loge parent is"
        print self._log3._log.parent
if __name__ == "__main__":
    unittest.main()
