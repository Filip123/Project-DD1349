from urllib.request import urlopen
import json
import pandas as pd
import sqlite3

def getDataApiRequest(apiRequest: str) -> any:
    response = urlopen(apiRequest)
    data = json.loads(response.read().decode('utf-8'))
    return data

def createDataFrame(data, keysToInclude: list[str]) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df = df[keysToInclude].drop_duplicates()
    return df


def addToTable(dataFrame: pd.DataFrame, table_name:str):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    dataFrame.to_sql(table_name, conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

def initialize_database(schema_file, db_file):
    conn = sqlite3.connect(db_file)
    with open(schema_file, 'r') as sql_file:
        sql_script = sql_file.read()
        conn.executescript(sql_script)
    conn.close()

# Call this function once at the initialization phase of your application
initialize_database('schema.sql', 'database.db')


#Session
dataSession = getDataApiRequest('https://api.openf1.org/v1/sessions?year=2023&session_name=Race')
keysToIncludeSession = ['session_key', 'country_key', 'year', 'date_start', 'date_end']

dfSession = createDataFrame(dataSession, keysToIncludeSession)
addToTable(dfSession, 'session')
sessions2023 = dfSession['session_key'].tolist()
print("--------Session Data---------")
print(dfSession)


#Country
keysToIncludeCountry = ['country_key', 'country_name']

filteredDataCountry = {key: [entry[key] for entry in dataSession] for key in keysToIncludeCountry}

dfCountry = createDataFrame(filteredDataCountry, keysToIncludeCountry)
addToTable(dfCountry, "country")
print("--------Country Data---------")
print(dfCountry)


#Driver
sessions2023 = dfSession['session_key'].tolist()
allSessionData = []
for session in sessions2023:
    allSessionData.extend(getDataApiRequest(f'https://api.openf1.org/v1/drivers?session_key={session}'))

keysToIncludeDriver = ['driver_number','name_acronym', 'full_name']
dfDriver = createDataFrame(allSessionData, keysToIncludeDriver)
print(dfDriver)
addToTable(dfDriver, "driver")


#Test data table:

# Create a SQLite connection
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query to retrieve a driver
cursor.execute("SELECT * FROM country LIMIT 1")
country = cursor.fetchone()

# Close the cursor and connection
cursor.close()
conn.close()

# Print the retrieved driver
print(country)

# Create a SQLite connection
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query to retrieve a driver
cursor.execute("SELECT * FROM driver LIMIT 1")
driver = cursor.fetchone()

# Close the cursor and connection
cursor.close()
conn.close()

# Print the retrieved driver
print(driver)

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







