

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from thirdparty import juhe
import json
import simplejson
# Create your views here.

def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')#直接从请求头中的参数取出来
        data = juhe.weather(city)
        return JsonResponse(data=data, safe=False, status=200)
    elif request.method == 'POST':
        # print(request.body)
        #POST方法中，参数是放在body中的，先取出body，是json格式，然后转换成dict，再从dict中取出相关值。
        received_body = simplejson.loads(request.body)
        cities = received_body.get('cities')
        # print(cities)
        #返回给前端的数据，先构建一个数组，数组中的每个值是一个dict,返回给前端时再转换成json数据。
        response_data = []
        for city in cities:
            # print(city)
            result = juhe.weather(city)
            response_data.append(result)
        print(response_data)
        return JsonResponse(data=response_data, safe=False, status=200)
