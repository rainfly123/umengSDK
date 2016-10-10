#!/usr/bin/env python
#coding=utf-8

import Queue
import threading
import time
import datetime
import pushclient

##msgtype=chat, cheer, info
msgtypes = {'chat':'你有新消息',
           'cheer':'节日愉快',
           'info':'新通知',
           }

class Cache(threading.Thread):
    q = Queue.Queue(1000)
    def __init__(self):
        threading.Thread.__init__(self)
        self.users = dict()
        self.last = datetime.datetime.now()

    def run(self):
        while True:
            now = datetime.datetime.now()
            diff = now - self.last
            if diff.seconds > 5:
                # (user,msgtype,message)
                self.last = now
                while Cache.q.empty() != True:
                    get = Cache.q.get()
                    self.users[get[0]] = (get[1], get[2])

                for user, data in self.users.items():
                    title = msgtypes.get(data[0])
                    pushclient.message(title, data[1], user)
                    print user, data
                #clear
                self.users = dict()
            else:
                time.sleep(2)


if __name__ == '__main__':
    t=Cache()
    t.setDaemon(True)
    t.start()
    i = 0
    while 1:
        i += 1
        Cache.q.put((0, "chat", i))
        if i >10:
            time.sleep(10)

