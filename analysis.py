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
    # 5: 운행 시간
    # 6: 등급
    # 7: 안전/위험
    # 8: 벌점 penalty
    # 9, 10, 11 급정거/방지턱/스쿨존 누적벌점 penalty_sub

    penalty_sub = []

    penalty = str(int(response.json()["m2m:cin"]["con"].split(" ")[6]) + 1)
    penalty_sub[0] = str(int(response.json()["m2m:cin"]["con"].split(" ")[9]) + 1)
    penalty_sub[1] = str(int(response.json()["m2m:cin"]["con"].split(" ")[10]) + 1)
    penalty_sub[2] = str(int(response.json()["m2m:cin"]["con"].split(" ")[11]) + 1)

    