
import requests

url = "http://203.253.128.161:7579/Mobius/kick_user/Account/4-20221110042857955"

payload = ""
headers = {
  'Accept': 'application/xml',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': '{{aei}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
