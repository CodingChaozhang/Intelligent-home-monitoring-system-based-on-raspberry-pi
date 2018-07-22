#coding=utf8
import cv2
import cv2.cv as cv
import requests
import json
 

url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
payload = {'api_key': 'exccXS6H_ALX8m0_jiIehLhz4GkBBa7O',
           'api_secret': 'x1cjkP8PdABqGL4soZBDzUyz-91uuJky',
           'faceset_token':'46d95e8476db6af0a051fa3812a7258e',
           }
files = {'image_file':open('owner2.jpg', 'rb')}
r = requests.post(url,files=files,data=payload)
data=json.loads(r.text)
print r.text
if data["results"][0]["face_token"] == "b779a9efaf159af7054ead0144306073" and data["results"][0]["confidence"]>=data["thresholds"]["1e-5"]:
    print'\n主人'
else:
    print '\n闯入者'
