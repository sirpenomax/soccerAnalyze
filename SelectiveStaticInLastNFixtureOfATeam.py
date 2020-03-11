import requests
import json
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd

team1 = 40
matches = 40 
fileName = "TeamID%d_%dFixtures_By_ID_Statics.json" %(team1 , matches)

#request Last N fixture of a spesefic team statics
url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/%d/last/%d" %(team1,matches)
querystring = {"timezone":"Asia%2FTehran"}
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
    }
# response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.request("GET", url, headers=headers)
lastNFixture = response.json()

with open(fileName, "w+") as f:
    f.flush()
    f.write('{"FixtureByID": [')

results = lastNFixture['api']['results']
print(results)



for x in range(results):

    fixtureId = lastNFixture['api']['fixtures'][x]['fixture_id']
    
    print(x)
    print(fixtureId)

    url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/id/%d" %fixtureId

    querystring = {"timezone":"Asia%2FTehran"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
        }

    # response3 = requests.request("GET", url, headers=headers, params=querystring)
    response3 = requests.request("GET", url, headers=headers)
    
    staticByFixtureID = response3.json()

    if  staticByFixtureID['api']['results'] != 0:
        with open(fileName, "a") as f:
            json.dump(staticByFixtureID, f)
            if x!=39:
                f.write(',')

    if x==20:
        time.sleep(30)


with open(fileName, "a") as f:
    f.write(']}')


with open(fileName) as f:
    data=json.load(f)

statics=[]

for x in range (len(data["FixtureByID"])):
    stLIst={} #Inner dict
    if data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"] is not None:
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
        stLIst["fixtureId"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]
        stLIst["shotOnGoal" ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]
        stLIst["shotOffGoal"] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"] 
        stLIst["totalGoal"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"] 
        statics.append(stLIst)
        # print(json.dumps(statics,indent=4) )
        # time.sleep(10)


Fstatics = {"static":statics}

with open('finalyRightfinaly.json', "w+") as ff:
    # ff.truncate()
    ff.flush()
    json.dump(Fstatics,ff)


    #version zero



dFrame = pd.DataFrame(statics)

dFrame.to_excel("output.xlsx")