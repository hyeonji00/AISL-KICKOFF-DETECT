## 급제동 판단 (자이로 사용)
## 2022/10/02
## ax의 기준치를 정하면 끝.(직접 타면서 테스트 해야함.)

import requests

url2 = "http://203.250.148.120:20519/Mobius/kick/gyro/la"

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



gyro_list=getdata(url2).split(" ")
gx=gyro_list[1]
gy=gyro_list[2]
gz=gyro_list[3]
ax=gyro_list[4]
ay=gyro_list[5]
az=gyro_list[6]



## 킥보드 속도 
# kick_speed=float(all_speed_gps[-1][-1])
# check_speed=float(all_speed_gps[-2][-1])
# kick_change_speed=(kick_speed - check_speed)

# # 킥보드 현재 위치 및 속도 출력
# print('current kickboard speed =',kick_speed)
# print('previous kickboard spped =', check_speed)
# print('kickboard speed rate of change =',kick_changespeed)

# (현재 속도 - 1초 전 속도)/(0.1초) > n 이상이면 급제동
# n을 10 또는 15 정도로 생각중
#if kick_change_speed > 10 and ax < -5.5:


if float(ax) < -5.5:  # ax 값 테스트
    print('warning')
else:
    print('normal')

