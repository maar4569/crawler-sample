# -*- coding: utf-8 -*-

from __future__ import with_statement
import os
import re
import time
from categorymatcher import CategorySetterExe,CategoryValidator
from config import CrawlerConfig
import contrib.JSONStreamWriter.JSONStreamWriter as JSONStreamWriter
import outputformatter
import outputwriter
from scoreler import StdScoreler
from scrapyer import GoogSearchScrapyer
if __name__ == "__main__":

    print u"main start!" 
    try:
        scraper        = GoogSearchScrapyer()
        categorysetter = CategorySetterExe()
        scoreler       = StdScoreler()
        configger      = CrawlerConfig("/crawler_config.yml")
        config         = configger.load()
        exepath        = config["settings"]["exepath"]
        tmpdir         = config["settings"]["transactiondir"]
        result_json    = config["settings"]["outputjson"]
        no_cat_url_list = config["settings"]["noncaturls"]
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

                        #output jsonformat
                        evt = fmter.Urls2Json(url,category,wkValidator.getDetail(),transaction_id)
                        jstream.write(evt)

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
