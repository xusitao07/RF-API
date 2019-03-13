# coding=utf-8
import unittest
import Tool,date

class myTest(unittest.TestCase):
    def setUp(self):
        print("start test")

    def tearDown(self):
        print("end test")


class tjs_app_login(myTest):
    '''接口名称：同金社app登录接口-100'''
    # def test_login(self):
    #     '''case1：账号正常登录'''
    #
    #     self.url = "192.168.111.113:8090/app"
    #     self.header = {
    #         "User-Agent":"ios_Simulator;11.4;6BC7AA24-D8D5-4BA7-92BA-B3740ECDCFB2;10010_v1_100;b22d502937bbdf4bdbb20a707765498a",
    #         "Content-Type":"application/x-www-form-urlencoded"
    #     }
    #     self.date = {
    #         "mobile":"18770053344",
    #         "password":"aa111111",
    #         "local":"1"
    #         # "csrf_token","9127522457f5e6724fdc29671b17ef5b"
    #     }
    #     self.r = requests.post(self.url,data=self.date,headers=self.header)
    #     print(self.r.text)
    #     print(self.r.status_code)
    #     self.assertEqual(self.r.status_code,200)
    #     self.assertIn("",self.r.text)
    #     self.assertIn(u"成功",self.r.text)


    def test_login2(self):
        '''case2:不存在账号登录'''
        url = date.url["url"]
        header = date.header["headers"]
        body = date.body["mobile_null"]
        self.text = Tool.test_login(url,header,body)
        print (self.text)
        self.assertIn(u"参数不能为空",self.text)


