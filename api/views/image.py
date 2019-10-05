
# =============
# 测试
import os
import base64
from kktest import settings
from django.http import HttpResponse, Http404, JsonResponse, FileResponse
from django.views import View

#引入自己写的文件时，引进完整路径，使用时也是使用完整路径。
import utils.response
from utils.response import CommonResponseMixin
#
# def image(request):
#     if request.method == 'GET':
#         md5 = request.GET.get('md5')
#         imageFile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
#         if not os.path.exists(imageFile):
#             return Http404()
#         else:
#             data = open(imageFile, 'rb').read()
#             # result = base64.b64encode(data)
#             # 注意：如果用HttpResponse返回，需要打开文件后再读取出来成为二进制文件。
#             # return HttpResponse(content=data, content_type='image/jpg')
#             # 注意:如果用FileResponse返回，则直接打开文件就可以了。
#             return FileResponse(open(imageFile, 'rb'), content_type='image/jpeg')


class imageView(View, CommonResponseMixin):
    def get(self,request):
        md5 = request.GET.get('md5')
        imageFile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imageFile):
            return Http404()
        else:
            data = open(imageFile, 'rb').read()
            # result = base64.b64encode(data)
            # 注意：如果用HttpResponse返回，需要打开文件后再读取出来成为二进制文件。
            # return HttpResponse(content=data, content_type='image/jpg')
            # 注意:如果用FileResponse返回，则直接打开文件就可以了。
            return FileResponse(open(imageFile, 'rb'), content_type='image/jpeg')

    def post(self, request):
        message = 'post method success'
        response = self.wrap_json_response(message=message)

        return JsonResponse(data=response, safe=False)

    def put(self, request):
        message = 'put method success'
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        pass




def image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(code=utils.response.ReturnCode.RESOURCE_NOT_EXISTS)
        else:
            response_data = {}
            response_data['name'] = md5 + '.jpg'
            response_data['url'] = '/image?md5=%s' % (md5)
            weichatresponse = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=weichatresponse, safe=False)

