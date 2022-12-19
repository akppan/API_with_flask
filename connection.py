# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:00:49 2022

@author: ANKUR
"""

#from mongoengine import connect
from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/my_session_db")

class Session(Document):
    username = StringField()
    mac_address = StringField()
    start_time = DateTimeField()
    usage_time = StringField()
    upload = DecimalField()
    download = DecimalField()
    start_date = DateTimeField()
    meta = {'collection':'session_data'}
