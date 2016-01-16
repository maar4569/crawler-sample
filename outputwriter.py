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
            fo = csv.writer(open(filename,'w'),lineterminator='\n',quoting=csv.QUOTE_NONNUMERIC)
            for k,v in urls.items():
                fo.writerow([srcurl,k,v])
            return 0
        except Exception as e:
            raise Exception(e)

class Url2JsonWriter(OutputWriter):
    def output(self,filename,urls,srcurl):
        try:
            catList = []
            relList = []
            for k,v in urls.items():
                catList.append(v)
                relList.append(k)
            evt = json.dumps({"res":[{"id":self._i+1},{"category":"あああ"},{"srcURL":srcurl},
                             {"r":relList},{"c":catList}]},ensure_ascii=False)
            print evt
            json.dump({"res":[{"id":self._i+1},{"category":"あああ"},{"srcURL":srcurl},
                             {"r":relList},{"c":catList}]},open(filename,'a'),ensure_ascii=False)
            self._i=self._i+1
  
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


