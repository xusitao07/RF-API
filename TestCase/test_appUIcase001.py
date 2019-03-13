# coding=utf-8
import time
import unittest


# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, traceback
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from appium.webdriver.webelement import WebElement
# from uitool import uiTool
# import Android_data,Android_data2,Android_data3

from appium import webdriver

class appTests(unittest.TestCase):
    # 测试开始前执行的方法

    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        # 'platformVersion': '6.0.1',  # 系统版本号
                        #'deviceName': '83c4caa7',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        #'platformVersion': '4.4.2',  # 系统版本号
                        #'deviceName': '127.0.0.1:62001',  #nox_adb.exe connect 127.0.0.1:62001 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        # 'platformVersion': '4.4.4',  # 系统版本号
                        # 'deviceName': '0acb291f',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'platformVersion': '5.1.1',
                        'deviceName': 'Y9K0215204005433',
                        'appPackage': 'com.shuniuyun.tjs',  # apk的包名
                        'appActivity': 'com.shuniuyun.tjs.ui.main.activity.StartActivity',  # activity 名称
                        'unicodeKeyboard': 'True',#使用unicode编码方式发送字符串
                        'resetKeyboard': 'True'#将键盘隐藏起来
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(10) #隐式等待10秒

    # def test_login_case1(self):
    #     """使用账号密码登录"""
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_login_phone").send_keys("18770059999")
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login_ok").click()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_pwd").send_keys("aa111111")
    #     self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
    #     time.sleep(4)
    #     try:
    #         self.assertTrue(self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_message").is_displayed())
    #     except Exception as error:
    #         print(error)
    #
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_personal_center").click()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_sign_out").click()

    # def test_longin_case2(self):
    #     """使用验证码登录"""
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
    #     #self.driver.find_element_by_id("com.shuniuyun.tjs:id/fixed_bottom_navigation_title").click()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login").click()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_login_phone").send_keys("18770059999")
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login_ok").click()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_code").click()#发送验证码
    #     time.sleep(3)
    #     tool = uiTool()#非静态方法使用需要实例化
    #     code = tool.do_sql_code("SELECT code FROM n_valid a ORDER BY a.add_time DESC LIMIT 1","num_sms")#获取登录验证码
    #     codelist = tool.get_codeList(int(code))
    #     #输入验证码模拟键盘输入
    #     for i in codelist:
    #         print (i)
    #         if i==0:
    #             self.driver.press_keycode(7)
    #         else:
    #             self.driver.press_keycode(i+7)
    #         time.sleep(1)
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_next").click()
    #     try:
    #         self.assertTrue(self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_message").is_displayed())
    #     except Exception as error:
    #         print(u'断言未通过：%s'%error)
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_personal_center").click()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_sign_out").click()

    @staticmethod
    def longIn(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_login_phone").send_keys("18770059999")
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login_ok").click()
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_pwd").send_keys("aa111111")
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        time.sleep(4)
        try:
            self.assertTrue(self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_message").is_displayed())
        except Exception as error:
            print(error)

    @staticmethod
    def get_toast(driver,text=None,timeout=30,poll_frequency=0.5):
        """
        driver - 传driver,
        text   - 页面上看到的文本内容
        timeout - 最大超时时间，默认30s
        poll_frequency  - 间隔查询时间，默认0.5s查询一次"""
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
        elm = WebDriverWait(driver, 5).until(EC.presence_of_element_located(toast_loc))
        return  elm


    def try_except(f):
        def handle_problems(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as err:
                print(err)
                exc_type, exc_instance, exc_traceback = sys.exc_info()
                formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
                message = '\n{0}\n{1}:\n{2}'.format(
                    formatted_traceback,
                    exc_type.__name__,
                    exc_instance
                )
                print(exc_type(message))

            finally:
                pass

        return handle_problems

    @staticmethod
    def get_contexts (driver,webview_name):
        """
        功能：hybrid 混合型APP 在native和webview之间切换
             切换当前driver为所填的contexts  “webview_name”
        driver  驱动
        webview_name  需要切换的contexts名称
         """
        webview = driver.contexts
        print("当前contexts：%s"%webview)
        for context in webview:
            if webview_name == context:
                driver.swith_to.contexts(context)
                break

    @try_except
    def test_buy_pro_feimuji_case3(self):
        """"购买非募集产品"""
        #后台发布测试产品
        # url = Android_data.url["CreatrUrl"]
        # body = Android_data.body["body"]
        # too = uiTool()
        # too.CreatProduct(url,body)
        # time.sleep(10)
        # #审核
        # examineUrl = Android_data2.examinUrl["examinUrl"]
        # examineData = Android_data2.examinPostDate["examinPostDate"]
        # print(examineData)
        # too.examine(examineUrl,examineData)
        # time.sleep(5)
        #
        appTests.longIn(self)#登录账号
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'理财')]").click()
        # par = self.driver.find_element_by_xpath("//android.widget.FrameLayout[@index = 0]")#获取第一条数据校验产品是否发布成功
        # text = par.find_element_by_id("com.shuniuyun.tjs:id/tv_item_title").get_attribute("text")
        text = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").get_attribute(
            "text")
        # try:
        #     self.assertEqual(text, "appp")
        # except Exception as err:
        #     print ("校验第一条产品是否是app",err)

        self.assertEqual(text, "appp")
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").click()
        # self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").get_attribute("text"),
        #                  "我要认购")
        # self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").click()  # 点击投资按钮跳转购买页面
        # # 校验起投金额是不是正确
        # self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").get_attribute("text"),
        #                  "10万元起投,100元的整数倍")
        # self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=1]").send_keys("99999")
        # self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
        # # 断言toast
        # toast_loc = ("xpath", ".//*[contains(@text,'10万元起投,100元的整数倍')]")
        # elm = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(toast_loc))
        # self.assertEqual(elm.text, '10万元起投,100元的整数倍')  # 购买金额小于剩余额度
        #
        # self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=1]").clear()
        # self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=1]").send_keys("5000000")
        # self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
        # self.assertEqual(appTests.get_toast(self.driver, "超过产品最大购买金额"))  # 购买金额大于剩余额度
        #
        # self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=1]").clear()
        # self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=1]").send_keys("500000")
        # self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
        # # 校验跳转是否成功
        # self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),
        #                  "投标")
        # self.driver.find_element_by_xpath("//android.view.View[@content-desc='出款金额：500000.00元']").is_displayed()
        #
        # self.driver.find_element_by_id("password").send_keys("aa111111")
        # self.driver.find_element_by_id("acceptBtn").click()
        # self.driver.find_element_by_id("title_content").is_displayed()  # 校验购买成功
        # self.driver.find_element_by_id("acceptBtn").click()

        #成标
        # establishUrl = Android_data3.establishUrl["establishUrl"]
        # establishData =Android_data3.establishPostDate["establishPostDate"]
        # too.examine(establishUrl, establishData)
        #
        # #删除产品
        #
        # too.Del("app")

        #成标后续可以接入还款的测试脚本
    def tearDown(self):
        self.driver.quit()








if __name__ == "__main__":
    unittest.main()
