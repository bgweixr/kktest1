


# 状态码(与前端协商好的。)
class ReturnCode:
    SUCCESS = 0
    FAILED = -100
    UNAUTHORIZED = -500
    BROKEN_AUTHORIZED_DATA = -501
    WRONG_PARMAS = -101
    RESOURCE_NOT_EXISTS = 104

    @classmethod
    def message(cls, code):
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorized'
        elif code == cls.WRONG_PARMAS:
            return 'wrong params'
        elif code == cls. RESOURCE_NOT_EXISTS:
            return 'resource not exists'
        else:
            return ''


def wrap_json_response(data=None, code=None, message=None):
    response = {}
    if not code:
        code = ReturnCode.SUCCESS
    if not message:
        message = ReturnCode.message(code)
    if data:
        response['data'] = data
    response['result_code'] = code
    response['message'] = message
    return response


class CommonResponseMixin(object):
    @classmethod
    def wrap_json_response(cls, data=None, code=None, message=None):#注意：跟普通方法不一样的地方是，需要加入参数cls
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not message:
            message = ReturnCode.message(code)
        if data:
            response['data'] = data
        response['result_code'] = code
        response['message'] = message
        return response