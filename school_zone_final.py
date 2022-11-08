## 어린이 보호구역(자이로 사용)
## 2022/10/02
## az의 기준치를 정하면 끝.(직접 타면서 테스트 해야함.)


import requests
from math import sin, cos, sqrt, atan2, radians

url1 = "http://203.250.148.120:20519/Mobius/kick/gps/la"

url2 = "http://203.250.148.120:20519/Mobius/kick/schoolzone/4-20221002104818772"



kick_id="MFBE29"
#heder and payload
payload={}
headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
}

#get mobious data
def getdata(url):
    response = requests.request("GET", url, headers=headers, data=payload)
    lst=response.text.split(":")
    for i in range(0,len(lst)):
        if "con" in lst[i]:
            lst[i+1]=lst[i+1].replace('}','').replace('"','')

            
            if kick_id in lst[i+1]:
                
                return lst[i+1]

def schooldata(url):
    response = requests.request("GET", url, headers=headers, data=payload)
    lst=response.text.split(":")
    for i in range(0,len(lst)):
        if "con" in lst[i]:
            lst[i+1]=lst[i+1].replace('}','').replace('"','')
            return lst[i+1]


# 스쿨존 과 킥보드 간 거리 구하는 함수
def lat_long_dist(lat1,lon1,lat2,lon2):
    # 
    # function for calculating ground distance between two lat-long locations
    R = 6373.0 # approximate radius of earth in km. 
    lat1 = radians( float(lat1) )
    lon1 = radians( float(lon1) )
    lat2 = radians( float(lat2) )
    lon2 = radians( float(lon2) )
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = round(R * c, 6)
    return distance


while True:
    
    school_zone=schooldata(url2).split(" ")
    gps_list=getdata(url1).split(" ")

    #실시간 킥보드 데이터
    kick_lat=gps_list[1]   
    kick_lon=gps_list[2]
    kick_speed=gps_list[3]
    
    school_lat_1=school_zone[1]
    school_lon_1=school_zone[2]


    distance_0=lat_long_dist(kick_lat,kick_lon,school_lat_1,school_lon_1)

    print(distance_0)
    if distance_0 < float(300/1000):  # 학교 정문(출입문) 과의 거리 300m
        if float(kick_speed) > float(15):   # 킥보드의 속도 15 km/h 보다 
            print("warning")
        else:
            print("normal")
