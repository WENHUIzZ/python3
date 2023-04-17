# 下面编写 发送邮件正文的Python 脚本 send.py
# 两个函数, 第一个基础功能发送邮件, 只包含正文, 第二个发送带有附件的邮件, 并抄送对应邮件地址


import codecs
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第三方 SMTP 服务

host_smtp = "smtp.163.com"  # SMTP服务器
username = "xxx@163.com"  # 发信人的邮箱地址
password = "*************"  # 163授权密码，非个人登录密码, 这样保护个人邮箱密码不暴露

from_mail = 'xxx@163.com'  # 发件人的邮箱
to_mail_list = ['xxx1@163.com', 'xxx2@163.com']  # 接收邮件地址list

content = '数据邮件日报'
title = '产品核心指标日报'  # 邮件主题
file_name = '/home/data/data.csv'  # 邮件附件的文件路径


# 含正文但不含附件的邮件发送函数

def sendEmail():
    message = MIMEText(content, 'java', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(from_mail)
    message['To'] = ",".join(to_mail_list)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(host_smtp, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(username, password)  # 登录验证
        smtpObj.sendmail(from_mail, to_mail_list, message.as_string())  # 发送
        print("邮件成功发送!")

    except smtplib.SMTPException as e:
        print(e)


# 含正文同时含附件的邮件发送函数

def sendEmailWithFile():
    msg = MIMEMultipart()
    att = MIMEText(codecs.open(file_name, 'rb', 'utf-8').read().encode("gb2312", 'ignore'), 'base64',
                   'gb2312')  # 增加附件，用gb2312编码，使得用Windows打开中文不乱码
    att['content-type'] = 'application/octet-stream'
    att['content-disposition'] = 'attachment;filename="data_report.csv"'
    msg.attach(att)
    mail_body = MIMEText(content, 'java', 'utf-8')  # 邮件正文格式设置: 内容, 格式, 编码
    msg.attach(mail_body)
    msg['From'] = "{}".format(from_mail)
    msg['To'] = ",".join(to_mail_list)
    msg['Cc'] = 'xxxx@163.com'  # 不支持多重抄送
    msg['subject'] = title + u'日报：发送于' + str(datetime.date.today())

    try:
        smtpObj = smtplib.SMTP_SSL(host_smtp, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(username, password)  # 登录验证
        smtpObj.sendmail(from_mail, to_mail_list, msg.as_string())  # 发送
        print("邮件(包含附件)已成功发送!")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    # 发送含正文但不含附件的邮件
    sendEmail()
    # 发送含正文同时含附件的邮件
    sendEmailWithFile()
