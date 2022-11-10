import requests

# 벌점이 누적된 gps 불러오기
url = "http://203.253.128.161:7579/Mobius/kick_user/penalty_zone?fu=1&ty=4"

payload={}
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SOrigin'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.json())


# ID 뽑기
ID = []

for i in range(len(response.json()["m2m:uril"])):
    ID.append(response.json()["m2m:uril"].split("/")[3])


cnt = 0

for i in range(len(ID)):
    change = 0
    detail_url = "http://203.253.128.161:7579/Mobius/kick_user/penalty_zone/" + ID[i]

    payload={}
    headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    lat_1 = response.json()["m2m:cin"]["con"][1]
    long_1 = response.json()["m2m:cin"]["con"][2]

    cnt_list = response.json()["m2m:cin"]["con"].split("/")

    for j in range(len(ID)):
        url = "http://203.253.128.161:7579/Mobius/kick_user/penalty_zone/" + ID[j]

        payload={}
        headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'SOrigin'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        lat_2 = response.json()["m2m:cin"]["con"][1]
        long_2 = response.json()["m2m:cin"]["con"][2]

        if lat_1 == lat_2 and long_1 == long_2:
            change = 1
            cnt += 1


    if change == 1:
        cnt_str = " ".join(cnt_list) + " " + str(cnt)

        # 새로운 벌점으로 재생성
        create_url = "http://203.253.128.161:7579/Mobius/kick_user/penalty_zone"

        payload = "{\n    \"m2m:cin\": {\n        \"con\" : \""+cnt_str+"\"\n    }\n}"
        headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': '{{aei}}',
        'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
        }

        requests.request("POST", create_url, headers=headers, data=payload)

        # 원래 cin 삭제
        payload = ""
        headers = {
        'Accept': 'application/xml',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': '{{aei}}'
        }

        response = requests.request("DELETE", detail_url, headers=headers, data=payload)


# 5회 이상이면 위험 구역으로 설정

url = "http://203.253.128.161:7579/Mobius/kick_user/penalty_zone?fu=1&ty=4"

payload={}
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SOrigin'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.json())


# ID 뽑기
ID = []

for i in range(len(response.json()["m2m:uril"])):
    ID.append(response.json()["m2m:uril"].split("/")[3])

for i in range(len(ID)):
    change = 0
    detail_url = "http://203.253.128.161:7579/Mobius/kick_user/penalty_zone/" + ID[i]

    payload={}
    headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    danger_list = response.json()["m2m:cin"]["con"].split("/")

    if int(cnt_list[3]) > 5:
        
        danger_str = (" ").join(danger_list)

        create_url = "http://203.253.128.161:7579/Mobius/kick_user/danger_zone"

        payload = "{\n    \"m2m:cin\": {\n        \"con\" : \""+danger_str+"\"\n    }\n}"
        headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': '{{aei}}',
        'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
        }

        requests.request("POST", create_url, headers=headers, data=payload)