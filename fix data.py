import requests
import json
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd



with open('Team40_10FIXTURE_BY_ID.json') as f:
    data=json.load(f)


statics=[]



for x in range (len(data["FixtureByID"])):
    stLIst={} #Inner dict
    print(x)
    if data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"] is not None:
        print("true")
        if data["FixtureByID"][x]["api"]["fixtures"][0]["homeTeam"]["team_id"] is 40 :
            
            stLIst["fixtureId"  ] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]                           )
            stLIst["shotOnGoal" ] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots on Goal"]["home"] )
            stLIst["shotOffGoal"] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots off Goal"]["home"]  )
            stLIst["totalGoal"  ] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Total Shots"]["home"])
            statics.append(stLIst)
            # print(json.dumps(statics,indent=4) )
            # time.sleep(10)     
            
        else:
            
            stLIst["fixtureId"  ] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]                           )     
            stLIst["shotOnGoal" ] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots on Goal"]["away"]  )   
            stLIst["shotOffGoal"] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots off Goal"]["away"] )   
            stLIst["totalGoal"  ] = int( data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Total Shots"]["away"]    )   
            statics.append(stLIst)
            # print(json.dumps(statics,indent=4) )
            # time.sleep(10)
    else:
        print("false")
        stLIst["fixtureId"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]
        stLIst["shotOnGoal" ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]
        stLIst["shotOffGoal"] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"] 
        stLIst["totalGoal"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"] 
        statics.append(stLIst)
        # print(json.dumps(statics,indent=4) )
        # time.sleep(10)



with open('finalyRight.json', "w+") as ff:
    # ff.truncate()
    ff.flush()
    json.dump(statics,ff)



# print(json.dumps(statics,indent=4) )


# print(len(data["FixtureByID"]))