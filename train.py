# !/usr/bin/python
# -*-coding:utf-8 -*-
import requests
import json
requests.packages.urllib3.disable_warnings()

const_url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s'

def train_ticket(from_station, to_station, data):
    global const_url
    url = const_url % (data, from_station, to_station)
    r = requests.get(url, verify=False);
    data = r.json()['data']['datas']
    for t in data:
        print "%s\t%s\t%s" % (t['station_train_code'], t['ze_num'], t['yw_num'])
        ze = t['ze_num']
        yw = t['yw_num']
        if ze != u'无' and ze != u'--':
            return True
        if yw != u'无' and yw != u'--':
            return True

if __name__ == '__main__':
    while True:
        if train_ticket("HFH", "GZQ", "2016-02-13"):
            print "快去抢票啦"
            break
