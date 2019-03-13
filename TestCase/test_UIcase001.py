# coding=utf-8

from selenium import webdriver
import re
import unittest, time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class myTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.tjs.com/login")
        self.driver.find_element_by_name("phone").send_keys("18770059999")
        self.driver.find_element_by_name("password").send_keys("aa111111")
        self.driver.find_element_by_xpath('.//form/button[@class="btn btn-blue full login-c"]').click()
    def tearDown(self):
        pass
        # self.driver.quit()

class test_1_gerenzhongxing(myTest):
    '''充值测试'''
    @staticmethod
    def RE(self,arg):
        self.r = ","
        self.a = re.sub(self.r,'',arg)
        return self.a

    def test_1_chongzhichenggong(self):
        '''测试用例1：正常充值'''
        global var2
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_xpath('.//div[2]/a[@class="logo"]').click()
        title = driver.title
        self.assertEqual(title, "同金社")
        time.sleep(2)
        driver.find_element_by_xpath('.//div[2]/div[@class="menu"]/a[6]').click()#点击个人中心
        var = int(float(self.test_1_chongzhichenggong.RE(self,driver.find_element_by_xpath('.//li[3]/p[@class="f18"]').text)))#获取充值前的可用余额用来做充值后的断言
        self.assertTrue(driver.find_element_by_xpath('.//div[1]/i[@class="mobile"]').is_displayed())
        self.assertTrue(driver.find_element_by_xpath('.//div[2]/i[@class="trade-pwd"]').is_displayed())
        driver.find_element_by_xpath('.//button[@class="btn btn-blue"]').click()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_xpath('.//p[@class="f16 mb30"]').is_displayed())
        driver.find_element_by_xpath('.//input[@class="input-ctrl"]').send_keys(100000)
        time.sleep(2)
        self.assertEqual(driver.find_element_by_id("mun_cn").text, '壹拾万元整')
        driver.find_element_by_id('recharge_btn').click()

        time.sleep(8)
        self.assertTrue(driver.find_element_by_xpath('.//span[@class="msg"]').text,"充值成功，资金一般5分钟内到账，最迟24小时内到账，到时请至“个人中心-资金明细”查看流水记录")#断言充值成功的提示
        driver.find_element_by_xpath('.//div[2]/div[@class="menu"]/a[6]').click()  # 点击返回个人中心
        time.sleep(2)
        var2 = int(float(self.test_1_chongzhichenggong.RE(self,driver.find_element_by_xpath('.//li[3]/p[@class="f18"]').text)))#获取充值后的可用余额用来做充值后的断言

        time.sleep(2)
        driver.find_element_by_xpath('.//a[@class="funds"]').click()#查看资金明细
        var3 = int(float(self.test_1_chongzhichenggong.RE(self,driver.find_element_by_xpath('.//div[@class="table container"]/table/tbody/tr[1]/td[2]').text)))#获取资金明细中的金额用来做可用余额充值的断言
        self.assertTrue(var2-var,var3)#断言可用余额增加的是否正确
        self.assertTrue(driver.find_element_by_xpath('.//div[@class="table container"]/table/tbody/tr[1]/td[2]').text,"100000")#校验资金记录中充值金额显示是否正确
        self.assertTrue(driver.find_element_by_xpath('.//tr[1]/td[4]/span[@class="green"]').text,"成功")#校验充值金额状态

    # def test_2_chizhishibai(self):
    #     driver = self.driver
    #     time.sleep(2)
    #     driver.find_element_by_xpath('.//div[2]/a[@class="logo"]').click()
    #     title = driver.title
    #     self.assertEqual(title, "同金社")
    #     time.sleep(2)
    #     driver.find_element_by_xpath('.//div[2]/div[@class="menu"]/a[6]').click()#点击个人中心
    #     self.assertTrue(driver.find_element_by_xpath('.//div[1]/i[@class="mobile"]').is_displayed())#校验跳转页面
    #     self.assertTrue(driver.find_element_by_xpath('.//div[2]/i[@class="trade-pwd"]').is_displayed())#校验跳转页面
    #     driver.find_element_by_xpath('.//button[@class="btn btn-blue"]').click()
    #     time.sleep(2)
    #     self.assertTrue(driver.find_element_by_xpath('.//p[@class="f16 mb30"]').is_displayed())
    #     for i in [0.01,100000000000,-1]:#测试充值边界值
    #         if i == 0:
    #             driver.find_element_by_xpath('.//input[@class="input-ctrl"]').clear()
    #             driver.find_element_by_xpath('.//input[@class="input-ctrl"]').send_keys(i)
    #             time.sleep(2)
    #             self.assertEqual(driver.find_element_by_id("mun_cn").text, '填写充值金额')
    #         elif i == 100000000000:
    #             driver.find_element_by_xpath('.//div[@class="form"]/div[3]/div[@class="addon"]').click()
    #             driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/input').clear()
    #             driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/input').send_keys(str(i))
    #             time.sleep(2)
    #             self.assertEqual(driver.find_element_by_id("mun_cn").text, '充值金额过大，请检查您的输入值')
    #         elif i == -1:
    #             driver.find_element_by_xpath('.//div[@class="form"]/div[3]/div[@class="addon"]').click()
    #             driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/input').clear()
    #             driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/input').send_keys(str(i))
    #             driver.find_element_by_id('recharge_btn').click()
    #             time.sleep(2)
    #             self.assertEqual(driver.find_element_by_xpath('.//div/div[@class="box error"]').text, '充值金额不能少于0.01，请修改充值金额。')
    #             driver.find_element_by_xpath('.//a[@class="btn btn-blue"]').click()

    def test_3_tixianchenggong(self):
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_xpath('.//div[2]/a[@class="logo"]').click()
        title = driver.title
        self.assertEqual(title, "同金社")
        time.sleep(2)
        driver.find_element_by_xpath('.//div[2]/div[@class="menu"]/a[6]').click()#点击个人中心
        self.assertTrue(driver.find_element_by_xpath('.//div[1]/i[@class="mobile"]').is_displayed())#校验跳转页面
        self.assertTrue(driver.find_element_by_xpath('.//div[2]/i[@class="trade-pwd"]').is_displayed())#校验跳转页面
        var6 = int(float(self.test_1_chongzhichenggong.RE(driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/ul/li[3]/p[1]').text)))
        driver.find_element_by_xpath('.//button[@class="btn btn-border-blue"]').click()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_xpath('.//*[@id="payment_form"]/div[2]/div[1]').is_displayed())#校验跳转的提现页面是否正确
        driver.find_element_by_xpath(".//*[@id='payment_form']/div[2]/div[2]/input").send_keys('10000')
        driver.find_element_by_id('to_withdraw_btn').click()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div").is_displayed())#校验跳转页面
        driver.find_element_by_id('password').send_keys("aa111111")
        driver.find_element_by_id('acceptBtn').click()
        time.sleep(2)
        self.assertTrue(driver.find_element_by_xpath('.//div[@class="wrap bgc-white mt20 mb20 ovh"]/div/span').is_displayed())#校验提现成功提示必现
        driver.find_element_by_xpath('html/body/div[1]/div[2]/div/a[6]').click()
        time.sleep(2)
        var4 = int(float(self.test_1_chongzhichenggong.RE(driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/ul/li[3]/p[1]').text)))#获取提现后的可用余额
        driver.find_element_by_xpath('.//div[@class="wrap uc-wrapper"]/div[1]/dl/dd[3]/a').click()
        var5 = int(float(self.test_1_chongzhichenggong.RE(driver.find_element_by_xpath('html/body/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]').text)))#获取提现后的资金记录
        self.assertEqual(driver.find_element_by_xpath('html/body/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]').text,'-10000.00')
        self.assertEqual(var4 - var6,var5)#断言可用余额扣除是否正确

#
# class test_2_gerenzhongxin:
#     pass



if __name__ == "__main__":
    unittest.main()
