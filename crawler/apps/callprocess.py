# -*- coding: utf-8 -*-
import subprocess
import sys
from crawler.utils import log
#def callhoge(cmd,infile,outfile):
def callhoge(cmd,*args):
    mylog = log.myLogger(sys._getframe().f_code.co_name)
    try:
        cmdline = str(cmd) + " " + " ".join(args)
        ret = subprocess.check_call( cmdline.strip() )
        return ret

    except Exception as e:
        mylog.error("exception raised!" + e.message + " cmdname=>" + cmdline)
        raise Exception(e)


