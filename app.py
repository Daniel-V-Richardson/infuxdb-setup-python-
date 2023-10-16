from flask import Flask, request, jsonify, url_for
import BAC0
import os
import logging
from influxdb import InfluxDBClient
from datetime import datetime

app = Flask(__name__)
app.secret_key = "da_engine_key"


# setting up influx
client = InfluxDBClient('localhost', 8086, 'admin', 'root', 'zedge')
client.create_database('zedge')
client.get_list_database()
client.switch_database('zedge')


list = []
data = {
    "measurements": "stocks",
    "tags": {
        "ticker": "edge"
    },
    "time": datetime.now(),
    "fields": {
        "open": 100,
        "close": 500,
    }
}
list.append(data)

# Write Data to DB
client.write_points(list)

result = client.query('Select * from stocks')
