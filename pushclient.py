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

appKey = '57a30b2ce0f55a041f00241d'
appMasterSecret  ='gu1fclnfuetgtmoytedges8bomeo7lb9'

def send(body, appmastersecret, url = 'http://msg.umeng.com/api/send', method = 'POST'):
    post_body = json.dumps(body)
    sign = md5('{}{}{}{}'.format(method, url, post_body, appmastersecret))
    r = requests.post(url + '?sign=' + sign, data=post_body)


def message(msgtype, text, alias, url = 'http://www.66boss.com'):
    timestamp = int(time.time() * 1000)
    title = cache.msgtypes.get(msgtype)
    body = {'appkey': appKey,
          'timestamp': timestamp,
          'type': 'customizedcast',
          'alias_type': 'QQ',
          'alias': alias,
          'payload': {'body': {'ticker': '老板找你:)',
                               'title': title,
                               'text': text,
                               'url': url,
                               'custom':msgtype,
                               'after_open': 'go_app'},
                     'display_type':'notification'
                     }
          }

    send(body, appMasterSecret)

if __name__ == '__main__':
    message("chat", "我要一百万", '1000001653')
