from flask import request, jsonify
from tigereye.helper.code import Code
import functools


class Validator(object):
    def __init__(self, **parameter_template):
        self.pt = parameter_template

    def __call__(self, f):
        # 保留被装饰函数的信息
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                request.params = {}
                for k, v in self.pt.items():
                    # tuple = (1,2,3)
                    # a, *b = tuple *返回的是列表
                    # a = 1, b = [2, 3]
                    request.params[k] = v(request.values[k])
            except Exception:
                response = jsonify(
                    rc=Code.required_parameter_missing.value,
                    msg=Code.required_parameter_missing.name,
                    data={'require_param': k}
                )
                response.status_code = 400
                return response
            return f(*args, **kwargs)
        return decorated_function


class ValidationError(Exception):
    def __init__(self, message, values):
        super().__init__(message)
        self.values = values


def multi_int(values, sperator=','):
    return [int(i) for i in values.split(sperator)]


# 1-200-5000,2-200-5000
def comlex_int(values, sperator='-'):
    digits = values.split(sperator)
    print(values)
    result = []
    for digit in digits:
        # isdigit() 判断是否是纯数字
        if not digit.isdigit():
            raise ValidationError('comlex int error: %s' % values, values)
        result.append(int(digit))
    return result


def multi_comlex_int(values, sperator=','):
    return [comlex_int(i) for i in values.split(sperator)]
