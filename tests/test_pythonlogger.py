# -*- coding: utf-8 -*-

import unittest
import contrib.pythonlogger.logger as MyLogger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self._logger = MyLogger.Logger()
    #success
    def test_success_info(self):
        self._logger.info("this is info lebel")
        #self.assertEqual(ret,0)

    #error
    def test_success_debug(self):
        self._logger.debug("this is debug level")
        #self.assertEqual(ret,0)

    #error
   # def test_err_processname_not_exists(self):
   #     with self.assertRaises(Exception):
   #         callprocess.callhoge("a","a","b")
# 
 #   def test_err_lack_of_args(self):
   #     with self.assertRaises(Exception):
    #        callprocess.callhoge("ls -al","b")

if __name__ == "__main__":
    unittest.main()
   # def test_err_processname_not_exists(self):
   #     with self.assertRaises(Exception):
   #         callprocess.callhoge("a","a","b")
# 
 #   def test_err_lack_of_args(self):
   #     with self.assertRaises(Exception):
    #        callprocess.callhoge("ls -al","b")

if __name__ == "__main__":
    unittest.main()
