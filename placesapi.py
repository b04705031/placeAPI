# 23.5033841,119.812974

# curl -L -X GET 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?location=22.9882641,%20120.1873306&radius=10000&type=lodging&rankby=prominence&key=AIzaSyBc4CEv_OjF4AE536UWYiJKP38jd0zPylg'

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY'

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=24.810278%2C121.043333&radius=1500&type=restaurant&keyword=cruise&key=AIzaSyBc4CEv_OjF4AE536UWYiJKP38jd0zPylg

import requests

import time
import os
import json
from pprint import pprint
from pdb import set_trace as st


def get_place_data(location, radius, place_type, token=None):
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    key = 'AIzaSyBc4CEv_OjF4AE536UWYiJKP38jd0zPylg'

    location_str = '%2C'.join(map(str, location))
    params = {
        'location': location_str,
        'radius': radius,
        'type': place_type,
        'key': key,
    }
    # 'keyword'

    if token:
        params['pagetoken'] = token

    url = base_url + \
        '&'.join([f'{key}={value}' for key, value in params.items()])
    print(url)

    resp = requests.get(url=url)
    data = resp.json()
    return data


def write_out_result(result_list):
    os.makedirs('./json', exist_ok=True)
    for i, place_data in enumerate(result_list):
        with open(f'./json/{place_data["place_id"]}.json', 'w', encoding='utf8') as f:
            json.dump(place_data, f, indent=4, ensure_ascii=False)

        # 	pprint(place_data)
        # 	print('-------------------')


def run_with_location(location=(24.5691507, 120.9332615)):

    # params
    # location = (24.5691507, 120.9332615)
    radius = '2000'
    place_type = 'restaurant'

    count = 0
    result_list = []
    next_page_token = 'initial'

    while next_page_token:
        # print(count, next_page_token)
        count += 1
        time.sleep(3)
        if next_page_token == 'initial':
            next_page_token = None

        data = get_place_data(location, radius, place_type, next_page_token)
        result_list.extend(data.get('results', []))
        next_page_token = data.get('next_page_token')

    # result_list = sorted(result_list, key=lambda d: d.get('rating', 0))
    write_out_result(result_list)
    print(f'location: {location} has {len(result_list)} results')


def main():
    
    for i in range(-2, 3):
        for j in range(-2, 3):
            # run_with_location((24.57 + i * 0.03, 121.02 + j * 0.03)) # 苗栗
            # run_with_location((25.10 + i * 0.03, 121.32 + j * 0.03)) # 陽明山
            # run_with_location((24.6 + i * 0.05, 121.6 + j * 0.05))  # 宜蘭
            # run_with_location((23.48 + i * 0.03, 119.45 + j * 0.03))  # 澎湖
            # run_with_location((23.3 + i * 0.02, 119.46 + j * 0.02))  # 澎湖望安
            # run_with_location((24.810278 + i * 0.01, 121.043333 + j * 0.01))  # 新竹高鐵
            # run_with_location((25.015 + i * 0.01, 121.214444 + j * 0.01))  # 桃園高鐵
            # run_with_location((24.6818054 + i * 0.02, 121.3146895 + j * 0.02))  # 桃園高鐵



# run_with_location((24.57, 121.02))

# 23.698103, 119.457304


# 23.696429, 119.696193

# 23.487000, 119.451819

# 25°10′39″N 121°32′51″E
# 宜蘭
# 24.838933, 121.599566
# 24.834537, 121.930872
# 24.625124, 121.928935
# 24.612794, 121.593754


if __name__ == "__main__":
    main()


# https://maps.googleapis.com/maps/api/place/details/json?fields=name%2Crating%2Cformatted_phone_number&place_id=ChIJAQvJcBn7ZzQRTkBj8vz9SI0&key=AIzaSyBc4CEv_OjF4AE536UWYiJKP38jd0zPylg
