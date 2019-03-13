# coding: utf-8
#from email import encoders, MIMEBase
from imp import reload
__author__ = 'Administrator'


import sys

reload(sys)
sys.setdefaultencoding('utf8')
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
import os
import smtplib
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda file: os.path.getmtime(test_report + '\\' + file))  # 对所有的测试报告已创建时间进行排序（os.path.getmtime  创建时间）
    file_new = os.path.join(test_report, lists[-1])  # 组成新的目录 ‘test_report\lists’下放最后一个文件（最新文件）
    print(file_new)
    return file_new


def send_mail(file_new, to_addr_in):
    msg = MIMEMultipart()

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # from_addr = '17612159836@163.com'
    # passward = 'xusitao429'  #发邮件的邮箱授权密码
    # smtp_server = 'smtp.163.com'
    from_addr = '951298221@qq.com'
    passward = 'drrbykolimdubbdh'  # 发邮件的邮箱授权密码
    smtp_server = 'smtp.qq.com'
    to_addr = to_addr_in
    print (to_addr)
    # to_addrs = to_addr.split(',')
    att1 = MIMEText(mail_body, 'html', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="test_result.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    print (msg.attach(att1))
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = from_addr  # 显示的发件人
    msg['To'] = ";".join(to_addr_in)
    print (msg['To'])
    msg['Subject'] = Header('同金社接口自动化测试报告', 'utf-8')


    smtp = smtplib.SMTP()
    smtp.connect(smtp_server,25)
    smtp.set_debuglevel(1)
    smtp.login(from_addr, passward)
    smtp.sendmail(from_addr, to_addr_in, msg.as_string())
    smtp.has_extn('同金社接口自动化测试报告')
    smtp.quit()
    print(u'邮件已发出！注意查收。')


if __name__ == '__main__':
    testDir = 'D:\\TjsApi\\TestCase\\'  # 定义测试用例目录
    discover = unittest.defaultTestLoader.discover(testDir, pattern="test*.py")
    reportDir = "D:\\TjsApi\\TestReport\\"  # 定义报告存放路径
    nowTime = time.strftime("%Y-%m-%d %H-%M-%S")  # 按照一定的格式获取当前的时间
    fileName = reportDir + nowTime + 'test_result.html'
    fp = open(fileName, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"同金社接口测试报告", description=u"测试用例执行情况：")
    runner.run(discover)  # 运行用例生成报告
    fp.close()
    testReport = reportDir
    new_report = new_report(testReport)
    to_addr_in = ["2738405220@qq.com", "17612159836@163.com","951298221@qq.com"]
    send_mail(new_report, to_addr_in)
