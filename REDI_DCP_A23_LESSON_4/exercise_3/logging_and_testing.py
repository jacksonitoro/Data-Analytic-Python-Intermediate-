import logging
#Exercise 1: Basic Logging Setup
#- **Objective**: Set up basic logging to log messages into a file.
#- **Task**: Create a Python script that logs messages of different severity levels (INFO, WARNING, ERROR, CRITICAL) into a file called `basic_log.log`.
logging.basicConfig(
    filename = 'basic_log.log',
    filemode='w',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)-8s - %(message)s',

)
logging.debug('Log this as information on level DEBUG')
logging.info('Log this as information on level INFO')
logging.warning('Log this as information on level WARNING')