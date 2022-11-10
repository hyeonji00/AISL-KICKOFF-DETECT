pothole_ID = []
buff_ID = []
school_ID = []

import requests

url = "http://203.253.128.161:7579/Mobius/kick/web_gps/fopt"

payload={}
headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
}

response = requests.request("GET", url, headers=headers, data=payload)


for i in range(len(response.json()["m2m:agr"]["m2m:rsp"][0]["pc"]["m2m:uril"])) :
    pothole_ID.append(response.json()["m2m:agr"]["m2m:rsp"][0]["pc"]["m2m:uril"][i].split("/")[3])

print(pothole_ID)

for i in range(len(response.json()["m2m:agr"]["m2m:rsp"][1]["pc"]["m2m:uril"])) :
    buff_ID.append(response.json()["m2m:agr"]["m2m:rsp"][1]["pc"]["m2m:uril"][i].split("/")[3])

print(buff_ID)

for i in range(len(response.json()["m2m:agr"]["m2m:rsp"][2]["pc"]["m2m:uril"])) :
    school_ID.append(response.json()["m2m:agr"]["m2m:rsp"][2]["pc"]["m2m:uril"][i].split("/")[3])

print(school_ID)