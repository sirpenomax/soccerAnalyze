import requests
import json
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd

team1 = 40
matches = 40 
fileName = "Team%d_%dFIXTURE_Statics.json" %(team1 , matches)

with open(fileName,"r+") as f2:
    data=json.load(f2)

print(data[936816])