import requests
import json
import time

team1 = 40
matches = 10
fileName = "Team%d_%dFIXTURE_Statics.json" %(team1 , matches)
fileName2 = "Team%d_%dFIXTURE_BY_ID.json" %(team1 , matches)





url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/%d/last/%d" %(team1,matches)
querystring = {"timezone":"Asia%2FTehran"}
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
    }
# response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.request("GET", url, headers=headers)
data = response.json()

if response.status_code == 200:
      print('Success!')
elif response.status_code == 404:
      print('Not Found.')  

with open('test.json', "a") as ff:
        json.dump(data, ff)


""" with open(fileName, "a") as f:
    f.write('{"teamStatic": [')

results = data['api']['results']

print(results)
time.sleep(3)

x=0

for x in range(results):

    fixtureId = data['api']['fixtures'][x]['fixture_id']
    
    print(x)
    print(fixtureId)

    url = "https://api-football-v1.p.rapidapi.com/v2/statistics/fixture/%d/" %fixtureId

    querystring = {"timezone":"Asia%2FTehran"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
        }

    response2 = requests.request("GET", url, headers=headers, params=querystring)

    if response2.status_code == 200:
      print('Success!')
    elif response2.status_code == 404:
      print('Not Found.')  


    data2 = response2.json()


    if  data2['api']['results'] != 0:
        with open(fileName, "a") as f:
            json.dump(data2, f)
            f.write(',')



with open(fileName, "a") as f:
    f.write(']}')


f.close """





with open(fileName2, "a") as f2:
    f2.write('{"FixtureByID": [')

results = data['api']['results']

print(results)
time.sleep(3)

x=0

for x in range(results):

    fixtureId = data['api']['fixtures'][x]['fixture_id']
    
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
    
    


    if response3.status_code == 200:
      print('Success!')
    elif response3.status_code == 404:
      print('Not Found.')  


    data3 = response3.json()


    # if  data3['api']['results'] != 0:
    with open(fileName2, "a") as f2:
        json.dump(data3, f2)
        f2.write(',')



with open(fileName2, "a") as f2:
    f2.write(']}')


f2.close



print(response3)



""" # sorting data after get request
#
#
#


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


print(statics) """








print('\n\n\n******************DONE!!!!!!!!!!!!!!!!!!!!!!!!!****************\n\n\n\n\n\n\n\n\n\n')