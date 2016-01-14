# -*- coding: utf-8 -*-

import unittest
import os
import outputwriter


class TestOutputCsvWriter(unittest.TestCase):
    def setUp(self):
        self.csvwriter = outputwriter.Url2CsvWriter() 
        self.jsonwriter = outputwriter.Url2JsonWriter() 
        self._srcurl    = "http://mydomain.com"
        self._filename="./testurls.txt"
        self._jsonfile="./testurls_j.txt"
        self._urls   = {}
        self._urls["http://www.yahoo.co.jp"] = "portal"
        self._urls["http://www.facebook.com"] = "SNS"
        self._urls["http://www.amazon.com"] = "retail"
    #test Url2CsvWriter
    def test_error_outputfilename(self):
        self.assertRaises(Exception,lambda: self.csvwriter.output("",self._urls,self._srcurl))

    def test_error_urllist(self):
        self._urls2= []
 
        self.assertRaises(Exception,lambda: self.csvwriter.output("./dummy.txt",self._urls2,self._srcurl))

    def test_success_output(self):
        if os.path.exists(self._filename) : os.remove(self._filename)
        ret = self.csvwriter.output(self._filename,self._urls,self._srcurl)
        self.assertEqual(ret , 0)

    #test Url2JsonWriter
    def test_json_error_outputfilename(self):
        self.assertRaises(Exception,lambda: self.jsonwriter.output("",self._urls,self._srcurl))

    def test_json_error_urllist(self):
        self._urls2= []
 
        self.assertRaises(Exception,lambda: self.jsonwriter.output("./dummy.txt",self._urls2,self._srcurl))

    def test_json_success_output(self):
        if os.path.exists(self._jsonfile) : os.remove(self._jsonfile)
        ret = self.jsonwriter.output(self._jsonfile,self._urls,self._srcurl)
        self.assertEqual(ret , 0)

if __name__ == "__main__":
    unittest.main()
