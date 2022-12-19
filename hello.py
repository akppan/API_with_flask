# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:33:43 2022

@author: ANKUR
"""
from connection import Session
#from populate import Session
from flask_caching import Cache
from datetime import *

config={'CACHE_TYPE': 'SimpleCache'}
from flask import Flask,jsonify,request
app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

@cache.cached(timeout=50)

@app.route('/user/search')
def user():
    uname = request.args.get('username')
    alldata = Session.objects(username=uname)
    st = []
    for i in alldata:
        st.append([i.usage_time,i.upload,i.download])
    return {'data':st}

@app.route('/analytics')
def analytics():
    dt = request.args.get('date')
    dte = date(int(dt[4:]),int(dt[2:4]),int(dt[:2]))
    dte7 = dte + timedelta(days=-7)
    dte30 = dte + timedelta(days=-30)
    limit = request.args.get('limit')
    page = request.args.get('page')
    lst1 = Session.objects(start_date=dte)
    lst7 = Session.objects(start_date__lte=dte,start_date__gt=dte7)
    lst30 = Session.objects(start_date__lte=dte,start_date__gt=dte30)
    st1 = []
    for i in lst1:
        st1.append([i.username,i.usage_time,i.start_date])
    st7 = []
    for i in lst7:
        st7.append([i.username,i.usage_time,i.start_date])
    st30 = []
    for i in lst30:
        st30.append([i.username,i.usage_time,i.start_date])
    return {'data1':st1,'data7':st7,'data30':st30}