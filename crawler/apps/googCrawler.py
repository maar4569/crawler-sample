# -*- coding: utf-8 -*-

from __future__ import with_statement
import os
import re
import time
from crawler.apps.categorymatcher import CategorySetterExe,CategoryValidator
from crawler.apps.scoreler import StdScoreler
from crawler.apps.scrapyer import GoogSearchScrapyer
from crawler.apps.outputwriter import Url2JsonWriter
from crawler.config.crawlersetting import configureCrawler
#import contrib.JSONStreamWriter.JSONStreamWriter as JSONStreamWriter

GLOBAL_SETTINGS = configureCrawler()

if __name__ == "__main__":

    print u"main start!" 
    try:
        scraper        = GoogSearchScrapyer()
        categorysetter = CategorySetterExe()
        scoreler       = StdScoreler()
        writer         = Url2JsonWriter()
        exepath        = GLOBAL_SETTINGS["subprocess"]["name"]
        tmpdir         = GLOBAL_SETTINGS["directory"]["transaction"]
        result_json    = GLOBAL_SETTINGS["directory"]["jsonoutput"]
        no_cat_url_list = GLOBAL_SETTINGS["directory"]["noncategorizedurls"]
    except Exception as e:
        raise Exception

    i=0
    with open(self._no_cat_url_list) as fo:
        with JSONStreamWriter.ArrayWriter(result_json) as jstream:
            for url in fo:
                if url.strip()== "" : continue
                    
                    transaction_id = str(time.time()).replace(".","_")
                    try:
                        #set categorysetter
                        infile  = tmpdir + "/" + self._transaction_id + str(i+1) + ".scraped"
                        outfile = tmpdir + "/" + self._transaction_id + str(i+1) + ".categorized"
                        categorysetter = CategorySetterExe(exepath,infile,outfile)
                    
                        #validate URL
                        wkValidator  = CategoryValidator(url,tmpdir + "/" + transaction_id + str(i))
                        category = wkValidator.do(scraper,scoreler,categorysetter)

                        #output result to a jsonformatted file.
                        writer.output(result_json,wkValidator)
                        #evt = fmter.Urls2Json(url,category,wkValidator.getDetail(),transaction_id)
                        #jstream.write(evt)

                        #delete tmpfile .straped and .categorized
                        #under construction
                        os.remove(infile)
                        os.remove(outfile)

                        i=i+1
                    except Exception as e:
                        print e
                        print "skip this process. transactionid=" + str(transaction_id)
                        continue


    print u"main finished"
