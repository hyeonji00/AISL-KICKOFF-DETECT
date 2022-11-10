import requests

all_url = "http://203.253.128.161:7579/Mobius/kick_user/Account?fu=1&ty=4"

payload={}
headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
}

ID = []

response = requests.request("GET", all_url, headers=headers, data=payload)

for i in range(len(response.json()["m2m:uril"])) :
    ID.append(response.json()["m2m:uril"][i].split("/")[3])


# ID별 정보 가져오기

for i in range(len(ID)) :

    detail_url = "http://203.253.128.161:7579/Mobius/kick_user/Account/" + ID[i]

    payload={}
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'SOrigin'
    }

    response = requests.request("GET", detail_url, headers=headers, data=payload)

    # 4: 면허증 취득일
    license_date = response.json()["m2m:cin"]["con"].split(" ")[4]

    # 5: 운행 시간
    drive_time = response.json()["m2m:cin"]["con"].split(" ")[5]

    # 6: 등급
    rating = response.json()["m2m:cin"]["con"].split(" ")[6]

    # 7: 안전/위험
    safety_danger = response.json()["m2m:cin"]["con"].split(" ")[7]

    # 8: 벌점 penalty
    penalty = response.json()["m2m:cin"]["con"].split(" ")[8]

    # 9, 10, 11 급정거/방지턱/스쿨존 누적벌점 penalty_sub
    penalty_sub = []
    penalty_sub[0] = response.json()["m2m:cin"]["con"].split(" ")[9]
    penalty_sub[1] = response.json()["m2m:cin"]["con"].split(" ")[10]
    penalty_sub[2] = response.json()["m2m:cin"]["con"].split(" ")[11]

    