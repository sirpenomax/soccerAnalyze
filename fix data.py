import requests
import json
import time
from io import StringIO



with open('Team40_10FIXTURE_BY_ID.json') as f:
    # io = StringIO(f)
    data=json.load(f)

# data3=json.dumps(data, indent=3)

""" with open('test.json', "a") as f2:
        json.dump(data3, f2) """

# print(data["FixtureByID"][0]["api"]["fixtures"][0]["homeTeam"]["team_id"])

statics=[]
stLIst={} #primary list for complite statcs dict

for x in range (10):
    print(x)
    if data["FixtureByID"][x]["api"]["fixtures"][0]["homeTeam"]["team_id"] == 40 :

        stLIst["fixtureId"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]                           
        stLIst["shotOnGoal" ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots on Goal"]["home"]  
        stLIst["shotOffGoal"] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots off Goal"]["home"]  
        stLIst["totalGoal"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Total Shots"]["home"]
        statics.append(stLIst)     
    else:
        pass
        stLIst["fixtureId"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]                                
        stLIst["shotOnGoal" ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots on Goal"]["away"]     
        stLIst["shotOffGoal"] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Shots off Goal"]["away"]    
        stLIst["totalGoal"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]["Total Shots"]["away"]       
        statics.append(stLIst)

print(statics)

with open('test&test2.json', "a") as ff:
        json.dump(statics, ff)


        #second commit