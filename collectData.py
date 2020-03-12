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

    """ def __init__ (self) :
        self.team_ID = -1
        self.game_count = -1 """

        # logging.error(print(self.team_ID)) #log


    def get_last_Games ( self , team_ID , game_count=13 ):

        self.team_ID = team_ID
        self.game_count = game_count

        logging.critical(print(self.team_ID)) #log
       
        #request Last N fixture of a spesefic team statics
        url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/%d/last/%d" %(team_ID,game_count)
        querystring = { "timezone" : "Asia/Tehran" }
        # logging.critical(print(querystring))
        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # response = requests.request("GET", url, headers=headers)
        last_fixtures = response.json()

        return last_fixtures



    def stat_by_f_id ( self , last_fixtures ):

        self.file_Name = f"TeamID{self.team_ID}_{self.game_count}Fixtures_By_ID_Statics.json" 

        # logging.critical(print(self.file_Name)) #log

        with open(self.file_Name, "w+") as f:
            f.flush()
            f.write('{"FixtureByID": [')

        results = last_fixtures['api']['results']
        # print(results)


        for x in range(results):

            fixtureId = last_fixtures['api']['fixtures'][x]['fixture_id']
            
            # print(x)
            # print(fixtureId)

            url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/id/%d" % fixtureId

            querystring = {"timezone": "Asia/Tehran"}

            headers = {
                'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
                'x-rapidapi-key': "356212470bmsh2d49b62b4020477p151d3ajsn11df6fb74648"
                }

            response3 = requests.request("GET", url, headers=headers, params=querystring)
            # response3 = requests.request("GET", url, headers=headers)
            
            staticByFixtureID = response3.json()

            if  staticByFixtureID['api']['results'] != 0:
                with open(self.file_Name, "a") as f:
                    json.dump(staticByFixtureID, f)
                    if x!=(results-1):
                        f.write(',')

            if x==20 or x==40 or x==60 or x==80 or x==100:
                time.sleep(30)


        with open(self.file_Name, "a") as f:
            f.write(']}')


    ######################################################### version  0.2  ############################################################


    def depart_statics(self):
        
        logging.critical(print(self.file_Name)) #log
        
        with open(self.file_Name) as f:
            data=json.load(f)

        statics=[]

        for x in range (len(data["FixtureByID"])):
            stLIst={} #Inner dict
            if data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"] is not None:
                
                stLIst["fixtureId"] = data["FixtureByID"][x]["api"]["fixtures"][0]["fixture_id"]
                stLIst["statics"  ] = data["FixtureByID"][x]["api"]["fixtures"][0]["statistics"]
                statics.append(stLIst)

        Fstatics = {"statics":statics}

        with open('finalyRightfinalyTEST.json', "w+") as ff:
            ff.flush()
            json.dump(Fstatics,ff)

        # dFrame = pd.DataFrame(statics)
        
        return statics

    ###########################################      version 1.1        #########################################

""" cd = CollectData()
res = cd.get_last_Games(40,13)
cd.stat_by_f_id ( res )
cd.depart_statics() """