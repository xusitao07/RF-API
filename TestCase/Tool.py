# coding=utf-8
import requests
class Tool(object):
    def test_login(self,url,header,body):

        self.url = url
        self.header = header
        self.date = body
        self.r = requests.post(self.url,data=self.date,headers=self.header)
        return self.r

    def get_decorator(errors=(Exception,), default_value=''):
        def decorator(func):
            def new_func(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except errors as e:
                    print ("Assert error! ", repr(e))
                    return default_value
            return new_func
        return decorator
    try_except = get_decorator(default_value='default')




