#coding=utf8
import requests
url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
payload = {'api_key': 'exccXS6H_ALX8m0_jiIehLhz4GkBBa7O',
           'api_secret': 'x1cjkP8PdABqGL4soZBDzUyz-91uuJky',
           'display_name':'jiankong_lcz',
           'outer_id':'jiankong_lcz',
           'face_tokens':'b779a9efaf159af7054ead0144306073'
           }
r = requests.post(url,data=payload)
print r.text

