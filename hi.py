import requests
import json
import time


url = "https://api-football-v1.p.rapidapi.com/v2/leagues/current/"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()
    
with open("league.json", "a") as f:
    json.dump(data, f)


f.close()