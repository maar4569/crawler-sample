# -*- coding: utf-8 -*-
import subprocess

#def callhoge(cmd,infile,outfile):
def callhoge(cmd,*args):
    try:
        cmdline = str(cmd) + " " + " ".join(args)
        ret = subprocess.check_call( cmdline.strip() )
        return ret

    except Exception as e:
        raise Exception(e)


