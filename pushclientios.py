#!/usr/bin/env python
#coding=utf-8

import time
import json
import hashlib
import requests
import cache

def md5(s):
    m = hashlib.md5(s)
    return m.hexdigest()

appKey = '57fb52eb67e58efa03001584'
appMasterSecret  ='jgd0wnxwdvaz0a642gqzuat8fyr6azr0'

def send(body, appmastersecret, url = 'http://msg.umeng.com/api/send', method = 'POST'):
    post_body = json.dumps(body)
    sign = md5('{}{}{}{}'.format(method, url, post_body, appmastersecret))
    r = requests.post(url + '?sign=' + sign, data=post_body)


def message(text, alias, ext):
    timestamp = int(time.time() * 1000)
    body = {'appkey': appKey,
          'timestamp': timestamp,
          'type': 'customizedcast',
          'alias_type': 'QQ',
          'alias': alias,
          'payload': {'aps': {'alert': text,
                              'badge': +1,
                              'sound': "default"
                              },
                      'ext': ext
                     },
          "production_mode":"false"
          }

    send(body, appMasterSecret)

if __name__ == '__main__':
    message("我要一百万", '1000000348', "")
