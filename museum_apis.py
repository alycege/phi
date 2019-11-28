#!/usr/bin/python3

met_endpoints = {
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


search_url = met_endpoints['search']['endpoint'] + '?' + met_endpoints['search']['params']['query'] + '&' + met_endpoints['search']['params']['images'].format(tf=True)
# check this out https://gist.github.com/terencewu/034e09f0e318c621516b






