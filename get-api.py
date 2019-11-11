import requests
import json
from datetime import datetime


pset = {
    "lat":34.2541,
    "lon":6.5890
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=pset)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

pass_time=response.json()['response']
risetime=[]
for d in pass_time:
    time=d['risetime']
    risetime.append(time)

times=[]
for rt in risetime:
    time= datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

