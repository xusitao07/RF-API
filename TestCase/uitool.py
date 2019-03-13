# coding=utf-8
import re,random
from PIL import Image
import pytesseract
import requests,json
import pymysql
class uiTool():

    def examine(self,examine_url,examine_date):

        session = requests.Session()
        host = "http://admin.tjs.com"

        login_url = "http://admin.tjs.com/login.html"
        login_post_data = {
        "phone": "18770027573",
        "password":"aa111111"
        }
        session.post(login_url, login_post_data)

        # mysql2 = UITool()
        # login_url2 = "http://admin.tjs.com/login/check_sms.html"
        # m_verify = mysql2.do_sql_code("select code from n_valid  order by add_time desc limit 1", "num_sms")
        # login_post_data2 = {
        #     "m_verify": m_verify
        # }
        # print login_post_data2["m_verify"]
        # ress = session.post(login_url2, login_post_data2)

        ress2 = session.post(examine_url, examine_date)
        print(ress2.content.decode('UTF-8'))

    def do_dql(self, sql):
        connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com',db='num_pro', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        sql = sql
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        print (results)
        for row in results:
            id = row["id"]
        connection.close()
        return id


    def do_sql_code(self,sql,DB):
        connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db=DB,charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()

        Sql = sql
        cursor.execute(Sql)
        connection.commit()
        results = cursor.fetchall()
        print (results)
        for row in results:
            code = row["code"]
            print (code)
        connection.close()
        return code

    def DelProduct(self):
        try:
            connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db='num_pro',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            sql = "DELETE FROM n_product WHERE NAME = 'autotesting'"
            print (sql)
            cursor.execute(sql)
            connection.commit()
        except:
            print ("Error: unable to fecth data")

    def Del(self,name):
        try:
            connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db='num_pro',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            sql = ("DELETE FROM n_product WHERE NAME = %s"%name)
            print (sql)
            cursor.execute(sql)
            connection.commit()
        except:
            print ("Error: fail")

    def Subtraction(self,arg1,arg2):
        var = arg1-arg2
        return var

    def len(self,arg):
        a = len(arg)

        return a

    def RE(self,arg):
        self.r = ","
        self.a = re.sub(self.r,'',arg)

        return self.a



    def GetVerificationCode(self,x,y,width,height):
        rangle = (int(x), int(y), int(x + int(width)), int(y + int(height))) #需要截取的位置坐标
        i=Image.open("D://test_image//img.png")   #打开截图
        frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save("D://test_image//frame4.png")
        img = Image.open("D://test_image//frame4.png")
        print (img.load())
        aa =pytesseract.image_to_string(img)
        print (u"识别的验证码为："+aa)
        return aa

    def number(self,): #随机生成注册号码

        try:
            list1 = ["187", "176", "159"]
            for a in range(1):
                var = (random.choice(list1) + "".join(str(random.choice(range(10))) for i in range(8)))#random.choice随机选择
                print (var)
            return var
        except:
            raise IndexError('fail')


    def CreatProduct(self,creatr_url,create_post_date):
        try:
            session = requests.Session()
            host = "http://admin.tjs.com"

            login_url = "http://admin.tjs.com/login.html"
            login_post_data = {
                "phone": "18770053344",
                "password": "aa111111"
            }
            session.post(login_url, login_post_data)
            # mysql = UITool()
            # login_url2 = "http://admin.tjs.com/login/check_sms.html"
            # m_verify = mysql.do_sql_code("select code from n_valid  order by add_time desc limit 1", "num_sms")
            # login_post_data2 = {
            #     "m_verify": m_verify
            # }
            # print login_post_data2["m_verify"]
            # ress = session.post(login_url2, login_post_data2)
            ress2 = session.post(creatr_url, create_post_date)
            print(ress2.content.decode('UTF-8'))
        except:
            raise IndexError()


    def should_be_in(self,actualValue_list,*expectValue_list):     #  成标方法
        try:
            if actualValue_list in expectValue_list:
                return True
            else:
                return False

        except:

            raise IndexError()
    def newDelProduct(self,DB,sql):
        try:
            connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db=DB,charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            sql = sql
            print (sql)
            cursor.execute(sql)
            connection.commit()
        except:
            print ("Error: unable to fecth data")

    def do_sql(self,sql,DB,pram):
        connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db=DB,charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()

        Sql = sql
        cursor.execute(Sql)
        connection.commit()
        results = cursor.fetchall()
        print (results)
        for row in results:
            code = row[pram]
            print (code)
        connection.close()
        return code

    def get_codeList(self, code):
        """ 将获取到的6位数验证码拆成6个元素放到codelist中"""
        codelist = []
        codelist.append(code / 100000)
        codelist.append(code % 100000 / 10000)
        codelist.append(code % 100000 % 10000 / 1000)
        codelist.append(code % 100000 % 10000 % 1000 / 100)
        codelist.append(code % 100000 % 10000 % 1000 % 100 / 10)
        codelist.append(code % 10)
        return codelist

    def enter_code (self,element1,element2,codeList):
        """将验证码列表（codeList）里的验证码依次输入验证码输入框,element1父节点的元素id,element2子节点的元素class"""
        element = self.driver.find_element_by_id(element1)
        elements = element.find_elements_by_class_name(element2)
        for i in range(5):
            elements[i].send_keys(codeList[i])






# if __name__ == '__main__':
#     st = "autotesting"   len(str(${keyall}))<8|len(str(${keyall}))>18   7<len(${keyall})| len(${keyall})<19
#     obj = Http
#     obj.DelProduct(st)

