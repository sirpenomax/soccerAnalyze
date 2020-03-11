import requests
import json
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd
import logging

x=6

logging.basicConfig(level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical(x)