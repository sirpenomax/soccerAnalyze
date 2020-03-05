import requests
import json
import time

team1 = 33
team2 = 34
fileName = "H2H_%d_%d.json" %(team1 , team2)

url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/h2h/%d/%d" %(team1 , team2)

querystring = {"timezone":"Europe%2FLondon"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()

# print(data['api']['fixtures'][0]['fixture_id'])

with open(fileName, "a") as f:
  json.dump(data, f)


f.close

