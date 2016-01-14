# -*- coding: utf-8 -*-
import subprocess

def callhoge(cmd,infile,outfile):
    try:
        ret = subprocess.check_call( cmd.split(" ") )
        return ret

    except Exception as e:
        raise Exception(e)


