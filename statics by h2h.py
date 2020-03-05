import requests
import json
import time

team1 = 33
team2 = 34
fileName = "H2H_%d_%d_Statics.json" %(team1 , team2)

url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/h2h/%d/%d" %(team1 , team2)

querystring = {"timezone":"Europe%2FLondon"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()

""" with open(fileName, "a") as f:
  json.dump(data, f)


f.close """

with open(fileName, "a") as f:
    f.write('{"H2Hstatic": [')



results = data['api']['results']

print(results)
time.sleep(12)

x=0

for x in range(results):

    fixtureId = data['api']['fixtures'][x]['fixture_id']
    
    print(x)
    print(fixtureId)

    url = "https://api-football-v1.p.rapidapi.com/v2/statistics/fixture/%d/" %fixtureId

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
        }

    response2 = requests.request("GET", url, headers=headers)

    if response2.status_code == 200:
      print('Success!')
    elif response2.status_code == 404:
      print('Not Found.')  


    data2 = response2.json()

        
    with open(fileName, "a") as f:
        json.dump(data2, f)
        f.write(',')



with open(fileName, "a") as f:
    f.write(']}')


f.close

