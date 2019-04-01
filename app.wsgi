#!/usr/bin/env python3

import os
import json
import re
import requests
import csv
import time

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

# import bottle
from bottle import run, route, default_app, template, get, post, delete, request, static_file, response, debug


def fetch_weather_data_openweathermap_api():
    weather_forecast_api_url = "http://api.openweathermap.org/data/2.5/" \
                               "forecast?id=4508722&APPID=523d7208c52ada93fac8b64ede3f786f"

    weather_forecast_resp = requests.get(weather_forecast_api_url)

    weather_forecast_json = weather_forecast_resp.json()['list']

    curr_time = time.time()
    print(curr_time)

    weather_data = {}

    for item in weather_forecast_json:
        dt_date_str = time.strftime('%Y-%m-%d', time.gmtime(item['dt']))

        temp_min = item['main']['temp_min']
        temp_max = item['main']['temp_max']

        if dt_date_str not in weather_data:
            weather_data[dt_date_str] = [temp_min, temp_max]
        else:
            if temp_min < weather_data[dt_date_str][0]:
                weather_data[dt_date_str][0] = temp_min

            if temp_max > weather_data[dt_date_str][1]:
                weather_data[dt_date_str][1] = temp_max


    return weather_data

        #
        #
        # diff_time = dt - curr_time
        #
        # print(diff_time)
        #
        # formatted_time = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(diff_time))
        # print(formatted_time)

        # print(str(item))

    # weather_forecast_json = weather_forecast_resp.
    # forecast_data = []
    # current_date =

@route('/<path:path>/<filename:re:.*\.css>')
def send_static(path, filename):

    return static_file(filename, root='css/')


@route('/<path:path>/<filename:re:.*\.js>')
def send_static(path, filename):

    return static_file(filename, root='js/')


@route('/weatherui')
@route('/weatherui/')
def home():
    with open('index.html', 'r') as myfile:
        html_string = myfile.read()

    return template(html_string) #, select_opts=get_select_opts_genre())


@get('/weatherui/forecast/2/')
def getforecastdata2():
    response.content_type = 'application/json'
    return json.dumps(fetch_weather_data_openweathermap_api())


# fetch_weather_data_openweathermap_api()

run(reloader=True, debug=True)

