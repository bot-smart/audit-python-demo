#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid
import time
import json
import hashlib
import requests
import threading

"""
运行前请修改 APP_ID,APP_KEY,BUSINESS_ID 为对应申请到的值
"""

API_URL = 'https://api.botsmart.cn/v1/check/send'
APP_ID = '请输入您的appId'
APP_KEY = '请输入您的appKey'
BUSINESS_ID = '请输入您的businesID'

def sign(param):
    list_param = []
    for item in sorted(param.items()):
        if item[0] == 'signature' or not item[1]:
            continue
        list_param.append(item[0] + '=' + str(item[1]))

    return hashlib.sha1(('&'.join(list_param) + APP_KEY).encode(encoding='utf-8')).hexdigest()

def sed(business_id, task_id):
    param = {
        'app_id': APP_ID,
        'business_id': business_id,
        'timestamp': str(int(time.time() * 1000)),
        'taskIds': json.dumps([task_id]),
        'signature': ''
    }
    param['signature'] = sign(param)

    response = requests.post(url=API_URL, data=param)
    print(response.text)

task_id = 1274944876489449474

















