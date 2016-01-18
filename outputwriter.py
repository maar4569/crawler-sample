# -*- coding: utf-8 -*-
import csv
import json
#categorized url by categorydb

class OutputWriter:
    def __init__(self):
        self._i = 0
    def output(self):
        raise Exception('abstract method')

class Url2CsvWriter(OutputWriter):
    def output(self,filename,urls,srcurl):
        try:
            fo = csv.writer(open(filename,'a'),lineterminator='\n',quoting=csv.QUOTE_NONNUMERIC)
            for k,v in urls.items():
                fo.writerow([srcurl,k,v])
            return 0
        except Exception as e:
            raise Exception(e)

class Url2JsonWriter(OutputWriter):
    def output(self,filename,tid,urls,srcurl):
        try:
            catList = []
            relList = []
            for k,v in urls.items():
                catList.append(v)
                relList.append(k)
            #make dictionary
            evt2 = {"res":[{"id":tid},{"category":"あ"},{"srcURL":srcurl},{"r":relList},{"c":catList}]}

            json.dump(evt2,open(filename,'a'),ensure_ascii=False)

            return 0
        except Exception as e:
            raise Exception(e)

class List2File(OutputWriter):
    def output(self,filename,datalist):
        try:
            fo = csv.writer(open(filename,'w'),lineterminator='\n',quoting=csv.QUOTE_NONNUMERIC)
            for v in datalist:
                fo.writerow([v])
            return 0
        except Exception as e:
            raise Exception(e)


