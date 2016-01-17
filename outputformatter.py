# -*- coding: utf-8 -*-
#format categorized URLs
def Urls2csv(srcurl,category,urls,tid):
    try:
        if tid =="" : -9999
        csvList = []
        for k,v in urls.items():
            csvList.append(srcurl + "," + category + ","+ k + "," + v )
            return csvList
    except Exception as e:
        raise Exception(e)

def Urls2Json(srcurl,category,urls,tid):
    try:
        _tid = -9999 if tid =='' else tid
        catList = []
        relList = []
        for k,v in urls.items():
            catList.append(v)
            relList.append(k)
        #make dictionary
        evt = {"res":[{"id":_tid},{"category":category},{"srcURL":srcurl},{"r":relList},{"c":catList}]}
        return evt
    except Exception as e:
        raise Exception(e)



