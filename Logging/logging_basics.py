# =============================================================================
# logging basics I
# =============================================================================
# default level is warning, meaning if the program is running only logs of level warning and higher will be 
# reported. the order is printed as below 
# logg have levels each with nueric values assigned to them

import logging

# logging has default format as --Level --Name --Message
# i.e. --Level(WARNING:) --Name(root:) --Message(This is a warning message)
# the root logger is the default logger and the base logger 
# you can also setup your own level and assign number level value

logging.debug('This is a debug message')            #--> numerical level 10
logging.info('This is a info message')              #--> numerical level 20
logging.warning('This is a warning message')        #--> numerical level 30
logging.error('This is a error message')            #--> numerical level 40
logging.critical('This is a critical message')      #--> numerical level 50

# can format level and set it accordingly
# once level is set, you cannot change it until you restart your python script
# if the level is not defined, the configuration will run the default at the background 

logging.basicConfig(level = logging.DEBUG) # can only be configured once with the wraper

logging.debug('This is a debug message')            
logging.info('This is a info message')             
logging.warning('This is a warning message')        
logging.error('This is a error message')            
logging.critical('This is a critical message')      

# if you want to change the level of the root logger you have to access the root logger itself
# you can make changes to the basicConfig, but can't use the basicConfig wraper
# now if the program is restarted and run again only the Critical mssegaes will be displayed

logging.root.setLevel(logging.CRITICAL) # can change and re-run

logging.debug('This is a debug message')            
logging.info('This is a info message')             
logging.warning('This is a warning message')        
logging.error('This is a error message')            
logging.critical('This is a critical message')      

# you can turn off logging by using a set numeric value of 60
# since logs displayed will be from 60 and higher, and nothing exists at that level
# ultimately nothing will be displayed, which in essence we turned it off 

logging.root.setLevel(60) # log value does not exist

logging.debug('This is a debug message')            
logging.info('This is a info message')             
logging.warning('This is a warning message')        
logging.error('This is a error message')            
logging.critical('This is a critical message') 

# to get the leve of where are you at this point can be found using

logging.root.getEffectiveLevel()

# when getting log output in IDE is stdout, or standard out, method.
# you can get logs written to log files
# to write information to log files is via basicConfic

import logging
# since you can run baicConfig once, all output will go to the below file name 'test'log'
# once the file is run, nothing will be outputted on the screen as everything is in the log file
# check directory an dthe log file will be present with the log printouts

logging.basicConfig(filename = 'example.log', level = logging.DEBUG)
logging.debug('This is a debug message')            
logging.info('This is a info message')             
logging.warning('This is a warning message') 

# adding more configurations
# filemode is the default and set to append 'a'
# format is how the message is displayed: 
    #first is the name of the logger, in this case is logger name is root
    #level name is any of the 5 levels (debug, info, etc.)
    #message is the message you want to display

logging.basicConfig(filename = 'example2.log', filemode = 'a', 
                    format = '%(name)s - %(levelname)s - %(message)s')        
logging.warning('Log with special format') 

# adding more configurations II
# using process ID of python

logging.basicConfig(filename = 'example3.log', format = '%(process)d - %(levelname)s - %(message)s')        
logging.warning('Log with process format') 

# adding more configurations III
# logginh using datetime
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')


## logging does not work like print statement

x = 2
y = 5

logging.critical('Addition of {} and {} produces {}'.format(x, y, x+y))

# logging EXCEPTIONS

a = 99
b = 199

try:
    assert a == b
except Exception as x:
    logging.error("log Exception", exc_info = True)

# =============================================================================
# Logging basics II
# =============================================================================
# import logger and sys
# build logger objects
import logging
import sys

# important to note that with each logger you need to ALWAYS create handelers and
# set logger alert level to lowest

logger = logging.getLogger('Logger1')
logger2 = logging.getLogger('logger2')

# Handlers forward events from loggers to outputs, such as
# your consol (IDE), file, or syslog server
# loggers can have multiple or zero handlers assigned to them to logg events 
# to multiple destinations simultaneously

### different types of habdlers
    #1) fileHandler logs to file
    #2) StreamHandler (sys.stdout, sys.stderr (default)) logs to consol

# set level to lowest
logger.setLevel(logging.DEBUG)

# =============================================================================
# # CREATEING FILE HANDLER
# =============================================================================
handler1 = logging.FileHandler('info.log', mode = 'a') #default mode is append
handler1.setLevel(logging.INFO)

handler2 = logging.FileHandler('error.log', mode = 'a')
handler2.setLevel(logging.ERROR)

# Attache HANDLER to LOGGERS
logger.addHandler(handler1)
logger.addHandler(handler2)

# if the log is info level it will be logged by handler1
# if the log is error level it will be logged by handler2
logger.info('This is a info level log')

# =============================================================================
# # CREATING STREAM HANDLER
# =============================================================================
# as oppose to file output, will setup consol output
handler3 = logging.StreamHandler(sys.stdout) 
handler3.setLevel(logging.INFO)
logger.addHandler(handler3)

logger.info('This is a info level log')
logger.critical('This is a cretical level log')

### CREATED 3 HANDLERS to 1 LOGGER with 2 diffent output messages to FILE and SYS

# Formatting
# each handler ca have its own formatting, using the format function

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
formatter2 = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# assign format to handler
handler3.setFormatter(formatter)

# test output of formatter
logger.info('This is a info level log')
logger.critical('This is a cretical level log')

# assign new formatter and test output
handler3.setFormatter(formatter2)
logger.info('This is a info level log')
logger.critical('This is a cretical level log')