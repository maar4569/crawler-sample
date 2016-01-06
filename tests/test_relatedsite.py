# -*- coding: utf-8 -*-

import unittest
import relatedsite


class TestRelatedSite(unittest.TestCase):

    def setUp(self):
        self.relsite= relatedsite.RelatedSite('http://mydomain.com')

    def test_length(self):
        self.relsite.append("http://google.com")
        self.assertEqual(self.relsite.length(),1)

    def test_length_multi_sites(self):
        self.relsite.append("http://google.com")
        self.relsite.append("http://google2.com")
        self.relsite.append("http://google3.com")
        self.relsite.append("http://google4.com")
        self.assertEqual(self.relsite.length(),4)

    def test_next_with_a_data_in_list(self):
        testurl = "http://google5.com"
        self.relsite.append(testurl)
        url = self.relsite.next()
        self.assertEqual(url,testurl)
    
    def test_next_with_multi_data_in_list(self):
        self.relsite.append("http://google.com")
        self.relsite.append("http://google2.com")
        self.relsite.append("http://google3.com")
        l=0
        while True:      
            try:
                url = self.relsite.next()
                l+=1
            except StopIteration:
                self.assertEqual(l,self.relsite.length())               
                break

    def test_next_nodata_in_list(self):
        #refer to http://stackoverflow.com/questions/9599610/
        self.assertRaises(StopIteration,lambda: self.relsite.next())

if __name__ == "__main__":
    unittest.main()
