import requests
import logging
import json
import csv
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd
from collectData import collectData

cd = collectData()
res = cd.get_last_Games(40,10)
cd.stat_by_f_id ( res )
stat = cd.depart_statics()

with open ('stat4010.json' , 'w+') as f:
    json.dump(stat,f)

####################################  V  0.0 ################################