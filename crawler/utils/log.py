import inspect
import sys
from  logging  import NOTSET,INFO,DEBUG,WARNING,ERROR,getLogger,Formatter,StreamHandler,FileHandler

class myLogger(object):
    def __init__(self,name):
         self._log = getLogger(name)
         self._classname = name
    
    def debug(self,message):
        try:
            methodname = sys._getframe(1).f_code.co_name
            self._log.debug(self._classname + "." + methodname + "() : " +  message)
        except Exception as e:
            self._log.exception("error occured.")
            raise Exception(e)

    def warning(self,message):
        try:
            methodname = sys._getframe(1).f_code.co_name
            self._log.warning(self._classname + "." + methodname + "() : " +  message)
        except Exception as e:
            self._log.exception("error occured.")
            raise Exception(e)

    def info(self,message):
        try:
            methodname = sys._getframe(1).f_code.co_name
            self._log.info(self._classname + "." + methodname + "() : " +  message)
        except Exception as e:
            self._log.exception("error occured.")
            raise Exception(e)

    def error(self,message):
        try:
            methodname = sys._getframe(1).f_code.co_name
            self._log.error(self._classname + "." + methodname + "() : " +  message)
        except Exception as e:
            self._log.exception("error occured.")
            raise Exception(e)


