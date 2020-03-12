import requests
import logging
import json
import csv
import time
from collections import defaultdict
from io import StringIO
import numpy as np
import pandas as pd

class CollectData :
    
    def last_Games ( self , team_ID , game_count=10 ):

        global file_Name = f"TeamID{team_ID}_{game_count}Fixtures_By_ID_Statics.json" 
        #request Last N fixture of a spesefic team statics
        url = f"https://api-football-v1.p.rapidapi.com/v2/fixtures/team/{team_ID}/last/{game_count}"
        querystring = {"timezone":f"Asia{/}Tehran"}
        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # response = requests.request("GET", url, headers=headers)
        last_fixtures = response.json()

        return last_fixtures



    def stat_by_f_id ( self , last_fixtures ):

        with open(fileName, "w+") as f:
            f.flush()
            f.write('{"FixtureByID": [')

        results = last_fixtures['api']['results']
        # print(results)


        for x in range(results):

            fixtureId = last_fixtures['api']['fixtures'][x]['fixture_id']
            
            # print(x)
            # print(fixtureId)

            url = f"https://api-football-v1.p.rapidapi.com/v2/fixtures/id/{fixtureId}"

            querystring = {"timezone":f"Asia{/}Tehran"}

            headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
                }

            response3 = requests.request("GET", url, headers=headers, params=querystring)
            # response3 = requests.request("GET", url, headers=headers)
            
            staticByFixtureID = response3.json()

            if  staticByFixtureID['api']['results'] != 0:
                with open(fileName, "a") as f:
                    json.dump(staticByFixtureID, f)
                    if x!=(results-1):
                        f.write(',')

            if x==20:
                time.sleep(30)


        with open(fileName, "a") as f:
            f.write(']}')

