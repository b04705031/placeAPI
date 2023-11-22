# 23.5033841,119.812974

# curl -L -X GET 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?location=22.9882641,%20120.1873306&radius=10000&type=lodging&rankby=prominence&key=AIzaSyBc4CEv_OjF4AE536UWYiJKP38jd0zPylg'

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY'

import requests
import json
from pdb import set_trace as st
import time
from pprint import pprint

# 24.092800427982823,%20120.729736010647&radius=10000&type=restaurant


def getjson(token):
    prefix = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    # location = '24.092800427982823,%20120.729736010647'
    location = '24.5691507,120.9332615'
    location = location.replace(',', ',%20')
    print(location)
    radius = '2000'
    type = 'lodging',  # 'establishment'  # 'lodging'  # , 'restaurant'
    key = 'AIzaSyBc4CEv_OjF4AE536UWYiJKP38jd0zPylg'
    # keyword = 'hotel'

    # url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=23.001549,%20120.160592&radius=10000&type=lodging&rankby=prominence{}&key=AIzaSyBc4CEv_OjF4AE536UWYiJKP38jd0zPylg'
    # url = f'{prefix}location={location}&radius={radius}&type={type}&rankby=prominence{token}&key={key}'
    url = f'{prefix}location={location}&radius={radius}&type={type}&rankby=prominence&{token}&key={key}'
    print(url)

    resp = requests.get(url=url)
    data = resp.json()
    return data


rlist = []

data = getjson('')
rlist.extend(data['results'])
if 'next_page_token' in data:
    next_page_token = data['next_page_token']
    print(0, next_page_token)

    for i in range(10):
        time.sleep(3)
        data = getjson(token=f'&pagetoken={next_page_token}')

        if 'next_page_token' in data.keys():
            next_page_token = data['next_page_token']
            rlist.extend(data['results'])
            print(i+1, next_page_token)
        else:
            print(i+1)
            break

    print(len(rlist))

# st()


rlist = sorted(rlist, key=lambda d: d['rating'])

for i, d in enumerate(rlist):
    pprint(d)
    print('-------------------')
st()

# for d in r
# st()
