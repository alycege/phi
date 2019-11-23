#!/usr/bin/python3

from ast import literal_eval
from io import BytesIO
from PIL import Image
import requests
import time

endpt_dict = {
        'objects': {
            'endpoint': 'https://collectionapi.metmuseum.org/public/collection/v1/objects',
            'params': {
                    'dates': 'metadataDate={date}',
                    'dept_ids': 'departmentIds={ids}'
                    }
            },
        'object': {
            'endpoint': 'https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}',
            },
        'departments': {
            'endpoint': 'https://collectionapi.metmuseum.org/public/collection/v1/departments',
            },
        'search': {
            'endpoint': 'https://collectionapi.metmuseum.org/public/collection/v1/search',
            'params': {
                    'query': 'q={query}',
                    'permanent': 'isHighlight={tf}',
                    'dept_ids': 'departmentId={id}',
                    'in_museum': 'isOnView={tf}',
                    'artist_or_culture': 'artistOrCulture={tf}',
                    'medium': 'medium={media_list}', #e.g. Ceramics|Furniture|Paintings|Sculpture|Textiles
                    'images': 'hasImages={tf}',
                    'geo': 'geoLocation={geo_list}', #e.g. Europe|France|Paris|China|New York
                    'begin': 'dateBegin={date}',
                    'end': 'dateEnd={date}'
                    }
            }
        }

search_url = endpt_dict['search']['endpoint'] + '?' + endpt_dict['search']['params']['query'].format(query='sunflowers') + '&' + endpt_dict['search']['params']['images'].format(tf=True)_
resp = requests.get(search_url)
resp_dict = literal_eval(resp.content.decode('utf-8'))

for obj_id in resp_dict['objectIDs']:
    resp = requests.get(endpt_dict['object'].format(obj_id=obj_id))
    obj_dict = literal_eval(resp.content.decode('utf-8'))

    image_url = obj_dict['primaryImage']
    resp = requests.get(image_url)
    img = Image.open(BytesIO(resp.content))

    time.sleep(20)








