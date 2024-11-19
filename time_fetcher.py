import requests as r
import json
# import constants

def get_time(base_url, time_zone):

    headers = {"User-Agent": "XY"}
    time_url = base_url + time_zone
    response = r.get(time_url, headers=headers)
    time_data = response.json()
    current_datetime = time_data['dateTime']
    current_time_zone = time_data['timeZone']

    if response.status_code in [200,201]:

        print("fetching data from: {}".format(base_url+time_zone))
        print("status code: {}".format(response.status_code))
        # print(time_data)
        print("Current date and time is: " + current_datetime + ' ' + current_time_zone)

    else:
        print("unable to get time")

base_url = ('https://timeapi.io/api/time/current/zone?timeZone=')
time_zone1 = ('America/New_York')
time_zone2 = ('America/Los_Angeles')

print(get_time(base_url, time_zone1))