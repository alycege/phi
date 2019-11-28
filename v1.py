#!/usr/bin/python3

from museum_apis import met_endpoints, search_url
from io import BytesIO
import json
import os
from PIL import Image
import requests


query = input('search query: ')
output_dir = f'/home/age/scripts/phi/{query}/'
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)


resp = requests.get(search_url.format(query=query))
resp_dict = json.loads(resp.content)


for obj_id in resp_dict['objectIDs']:
    obj_resp = requests.get(met_endpoints['object']['endpoint'].format(obj_id=obj_id))
    obj_dict = json.loads(obj_resp.content)
    print(obj_id, obj_dict['title'])

    img_url = obj_dict['primaryImage']
    img_resp = requests.get(img_url)
    try:
        img = Image.open(BytesIO(img_resp.content))
        img_title = '_'.join(obj_dict['title'].lower().split(' ')) + '.jpeg'
        img.save(output_dir + img_title, 'jpeg')
    except:
        continue

# check this out https://gist.github.com/terencewu/034e09f0e318c621516b






