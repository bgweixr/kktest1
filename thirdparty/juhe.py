#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/21
# @Filename       : juhe.py
# @Desc           :


import json
import requests


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    # cityname = '北京'
    key = '20d68abaec5f1fd17391a8f3ef734379'
    api = 'http://apis.juhe.cn/simpleWeather/query'
    params = 'city=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    # print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    # print('jsondata:')
    # print(json_data)
    result = json_data.get('result')


    realtime = result.get('realtime')
    response = dict()
    response['temperature'] = realtime.get('temperature')
    response['humidity'] = realtime.get('humidity')
    response['info'] = realtime.get('info')
    response['direct'] = realtime.get('direct')  # 湿度
    response['power'] = realtime.get('power')
    # print(response)
    return response


if __name__ == '__main__':
    data = weather('北京')
