#!/usr/bin/python
#!-*- coding:utf8 -*-

from flask import Flask
from flask import jsonify
from flask import Response
from mrt import *
import json
import re
app = Flask(__name__)
M = MRTStation()
@app.route('/')
def printStation():
    return Response(json.dumps(M.station, ensure_ascii=False,indent=2),  mimetype='application/json')

@app.route('/<station>')
def getTrainTime(station):
    if re.match("\d+",station):
        if any(i["id"]==station for i in M.station):
            return Response(json.dumps(M.getTrainTime(Id=str(station)), ensure_ascii=False, indent=2), mimetype='application/json')
    else:
        if any(unicode(i["name"].decode('utf8')) == unicode(station) for i in M.station):
            return Response(json.dumps(M.getTrainTime(name=unicode(station)), ensure_ascii=False, indent=2), mimetype='application/json')
    return Response(json.dumps(["Error"]),mimetype='application/json')

if __name__ == '__main__':
    app.run()
