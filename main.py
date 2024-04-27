# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)
def get_weather(city, date_from, date_to):
    api_key = os.environ.get('JNS9HZ9FXJB6G5YRKBL6NDT9X')
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date_from}/{date_to}?key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/info', methods=['GET'])
def weather_info():
    version = os.environ.get('0.1')
    service = "weather"
    author = "Yaroslavcev Dmitry"

    return jsonify({
        "version": version,
        "service": service,
        "author": author
    })

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'New York')
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')
    if not date_from or not date_to:
        date_from = 'yesterday'
        date_to = 'today'
    weather_data = get_weather(city, date_from, date_to)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8000))
