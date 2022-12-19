# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:11:43 2022

@author: ANKUR
"""
#{'username': 'brainyHeron5', 'mac_address': '74:73:4E:09:DE:6F', 'start_time': '04-11-2022 15:43:33', 'usage_time': '04:50:20', 'upload': '3512752.28', 'download': '7462017.97', 'start_date': '04-11-2022'}

from connection import Session
from datetime import *

csv_mapping_list = []
with open("user_internet_session_dataset.csv") as my_data:
    line_count = 0
    for line in my_data:
        row_list = [val.strip() for val in line.split(",")]
        if line_count == 0:
            header = row_list
        else:
            row_dict = {}
            for i, key in enumerate(header):
                row_dict[key] = row_list[i]
            #val = row_dict['start_time'].split(' ')[0]
            #row_dict['start_date'] = ''.join(val.split('-'))
            row_dict['start_date'] = row_dict['start_time'].split(' ')[0]
            csv_mapping_list.append(row_dict)
        line_count += 1

for i in csv_mapping_list:
    stTime = datetime.strptime(i['start_time'], '%d-%m-%Y %H:%M:%S')
    dt = list(map(int,i['start_date'].split('-')))
    data = Session(username=i['username'],mac_address=i['mac_address'],start_time=stTime,usage_time=i['usage_time'],upload=float(i['upload']),download=float(i['download']),start_date=date(dt[2],dt[1],dt[0]))
    data.save()