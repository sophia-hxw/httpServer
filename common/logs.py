import os
import logging
from logging.handlers import TimedRotatingFileHandler

class Log(object):
    def __init__(self, logfilename='default.log', loglevel='info'):
        self.logfilename = logfilename
        pathname = os.path.join(os.getcwd(),"logs")
        filename = os.path.join(pathname, self.logfilename)
        
        if (not os.path.exists(pathname)):
            os.mkdir(pathname)
        
        log = logging.getLogger()
        if loglevel=='debug':
            log.setLevel(logging.DEBUG)
        elif loglevel=='warning':
            log.setLevel(logging.WARNING)
        elif loglevel=='error':
            log.setLevel(logging.ERROR)
        elif loglevel=='critical':
            log.setLevel(logging.CRITICAL)
        else:
            log.setLevel(logging.INFO)

        
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s','%Y-%m-%d %H:%M:%S')  
        fileTimeHandler = TimedRotatingFileHandler(filename, when='midnight')
        
        fileTimeHandler.suffix = "%Y_%m_%d.out" 
        fileTimeHandler.setFormatter(formatter)
        # fileTimeHandler.setLevel(logging.INFO)
        
        log.addHandler(fileTimeHandler)
        
        self.log = log
        
    def info(self, message) :
        self.log.info(message)
        
    def error(self, message) :
        self.log.error(message)

    def warn(self, message):
        self.log.warn(message)
    
    def debug(self, message):
        self.log.debug(message)

    def critical(self, message):
        self.log.critical(message)