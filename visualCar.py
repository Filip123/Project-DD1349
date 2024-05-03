from urllib.request import urlopen
import json

def getDataApiRequest(apiRequest: str) -> any:
    response = urlopen(apiRequest)
    data = json.loads(response.read().decode('utf-8'))
    return data

def getPositionsOverTimeInterval(session, driverNumber,startTime: str, timeInterval: int) -> list:
    positionsList = []
    positionsData= getDataApiRequest(f'https://api.openf1.org/v1/location?session_key={session}&driver_number={driverNumber}&date>2023-03-05T16:00:00&date<2023-03-05T16:00:10')

    for position in positionsData:
        positionsList.append([position["x"], position["y"]])

    return positionsList

def main():
    position_list = getPositionsOverTimeInterval(7953, 1, "2023-03-05T16:00:00", 10)

    print(position_list)

main()



