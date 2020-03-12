import requests
import json
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd
import logging
import numpy
import matplotlib.pyplot as plt
logging.basicConfig(level=logging.DEBUG)


team1 = 40
matches = 40 
fileName = "TeamID%d_%dFixtures_By_ID_Statics.json" %(team1 , matches)


""" logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical(x) """



""" with open(fileName) as f:
    data=json.load(f) """

""" stat={}
stat = data["FixtureByID"][39]["api"]["fixtures"][0]["statistics"]
print(stat)

dFrame = pd.DataFrame(stat)
dFrame.to_excel("output2.xlsx") """

""" statics=[]

for x in range (len(data["FixtureByID"])):
    stLIst={} #Inner dict
    stLIst["fixtureId"] = data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]
    stLIst["Static" ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]
    statics.append(stLIst)


Fstatics = {"static":statics}

with open('finalyRightfinaly.json', "w+") as ff:
    # ff.truncate()
    ff.flush()
    json.dump(Fstatics,ff)


dFrame = pd.DataFrame(statics)
dFrame.to_excel("output3.xlsx") """

    #####################################################    Version 1.0   ###########################################################


# dFrame = pd.DataFrame(statics)

# dFrame.to_excel("output.xlsx")

class CollectData :
    
    def last_Games (self, team_ID , game_count=10 ):
        print(team_ID)
        print(game_count)


cl=CollectData()

cl.last_Games(40)