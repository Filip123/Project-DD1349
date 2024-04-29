from urllib.request import urlopen
import json
import pandas as pd


#Session
responseSession = urlopen('https://api.openf1.org/v1/sessions?year=2023&session_name=Race')
dataSession = json.loads(responseSession.read().decode('utf-8'))


keysToIncludeSession = ['session_key', 'country_key', 'year', 'date_start', 'date_end']

filteredDataSession = {key: [entry[key] for entry in dataSession] for key in keysToIncludeSession}

dfSession = pd.DataFrame(filteredDataSession)
print("--------Session Data---------")
print(dfSession)


#Country
keysToIncludeCountry = ['country_key', 'country_name']

filteredDataCountry = {key: [entry[key] for entry in dataSession] for key in keysToIncludeCountry}

dfCountry = pd.DataFrame(filteredDataCountry)
print("--------Country Data---------")
print(dfCountry)

