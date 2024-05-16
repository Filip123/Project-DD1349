from urllib.request import urlopen
import json
from datetime import datetime, timedelta
import math

def getEndTime(startTime: str, timeInterval: int) -> str:
    end_time = datetime.strptime(startTime, '%Y-%m-%dT%H:%M:%S') + timedelta(seconds=timeInterval)
    return end_time.strftime('%Y-%m-%dT%H:%M:%S')


def getDataApiRequest(apiRequest: str) -> any:
    response = urlopen(apiRequest)
    data = json.loads(response.read().decode('utf-8'))
    return data

def getPositionsOverTimeInterval(session, driverNumber,startTime: str, timeInterval: int) -> list:
    endTime = getEndTime(startTime, timeInterval)
    framesNeeded = timeInterval * 2 #To display new frame every 0.5 sec 
    positionsList = []
    positionsData= getDataApiRequest(f'https://api.openf1.org/v1/location?session_key={session}&driver_number={driverNumber}&date>{startTime}&date<{endTime}')

    index = 0
    while len(positionsList) < framesNeeded:
        position = positionsData[math.floor(index)]
        positionsList.append([position["x"], position["y"]])
        index += len(positionsData) / framesNeeded

    return positionsList

   