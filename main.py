from urllib.request import urlopen
import json

response = urlopen('https://api.openf1.org/v1/laps?session_key=9161&driver_number=1&lap_number=8')
data = json.loads(response.read().decode('utf-8'))
print(data)