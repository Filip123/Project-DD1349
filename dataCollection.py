from urllib.request import urlopen
import json
import pandas as pd


#Session
responseSession = urlopen('https://api.openf1.org/v1/sessions?year=2023&session_name=Race')
dataSession = json.loads(responseSession.read().decode('utf-8'))

keysToIncludeSession = ['session_key', 'country_key', 'year', 'date_start', 'date_end']

filteredDataSession = {key: [entry[key] for entry in dataSession] for key in keysToIncludeSession}

dfSession = pd.DataFrame(filteredDataSession)
sessions2023 = dfSession['session_key'].tolist()
print("--------Session Data---------")
print(dfSession)


#Country
keysToIncludeCountry = ['country_key', 'country_name']

filteredDataCountry = {key: [entry[key] for entry in dataSession] for key in keysToIncludeCountry}

dfCountry = pd.DataFrame(filteredDataCountry)
print("--------Country Data---------")
print(dfCountry)

#Driver
sessions2023 = dfSession['session_key'].tolist()
allSessionData = []
for session in sessions2023:
    response = urlopen(f'https://api.openf1.org/v1/drivers?session_key={session}')
    dataDriver = json.loads(response.read().decode('utf-8'))
    allSessionData.extend(dataDriver)

keysToIncludeDriver = ['driver_number','name_acronym', 'full_name']

#Delete Dublicates
dfDriver = pd.DataFrame(allSessionData)
dfDriver = dfDriver[keysToIncludeDriver]
dfDriver.drop_duplicates(inplace=True)
print("--------Driver Data---------")
print(dfDriver)


#Driver Position

# print(sessions2023)
# print(sessions2023[0])
# response = urlopen(f'https://api.openf1.org/v1/location?session_key={sessions2023[0]}&driver_number=1&date>2023-03-05T15:00:00&date<2023-03-05T17:00:00')
# dataPosition = json.loads(response.read().decode('utf-8'))

# keysToIncludePosition = ['driver_number', 'session_key', 'date', 'x', 'y', 'z']

# filteredDataPosition = {key: [entry[key] for entry in dataPosition] for key in keysToIncludePosition}

# dfPosition = pd.DataFrame(filteredDataPosition)
# print("--------Position Data---------")
# print(dfPosition.shape)







