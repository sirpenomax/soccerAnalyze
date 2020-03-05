import requests
import json
import time

lastTeamId = i = 1100
j = i+300

fileName = "TEAM%d.json" %i

with open(fileName, "a") as f:
  f.write('{"TEAM": [')

while i<lastTeamId :

  for x in range(i,j):
    
    print(x)

    url = "https://api-football-v1.p.rapidapi.com/v2/teams/team/%d" %x
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
        }
    response = requests.request("GET", url, headers=headers)

    data = response.json()
    
    with open("fileName", "a") as f:
      json.dump(data, f)
      f.write(',')

    if response.status_code == 200:
      print('Success!')
    elif response.status_code == 404:
      print('Not Found.')   

  i+=30
  j+=30
  
  time.sleep(120)
  
with open("fileName", "a") as f:
  f.write(']}')

f.close()

 


