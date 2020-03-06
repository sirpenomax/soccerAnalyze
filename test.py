import requests
import json
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd



with open('Team40_10FIXTURE_BY_ID.json') as f:
    data=json.load(f)

# print(data["FixtureByID"][4]["api"]["fixtures"][0]["statistics"]["Shots on Goal"].get("home"))

print(data["FixtureByID"][4]["api"]["fixtures"][0]["statistics"])









""" def flatten_dict(dd, separator ='_', prefix =''): 
    return { prefix + separator + k if prefix else k : v 
             for kk, vv in dd.items() 
             for k, v in flatten_dict(vv, separator, kk).items() 
             } if isinstance(dd, dict) else { prefix : dd } 

flatenData = flatten_dict(data)

with open ('flatenDATA.json', "w") as ff:
    json.dump(flatenData,ff) """

# print(json.dumps(flatenData, indent=4))

# print(len(flatenData))


