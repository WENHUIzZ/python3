import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:

    def __init__(self):
        """
        配置发件人信息
        :param mail_host: 设置服务器
        :param mail_user: 用户名
        :param mail_pw: 密码
        """

        self.mail_host = ""
        self.mail_user = ""
        self.mail_pw = ""

    def sendEmail(self, recipient, subject, content, attachment):

        msg = MIMEMultipart()
        msg['From'] = Header(self.mail_user, 'utf-8')
        msg['To'] = Header(recipient, 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')

        # 邮件正文
        part = MIMEText(content)
        msg.attach(part)

        # 文本文档/图片/PDF/音频
        part = MIMEApplication(open(attachment, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=attachment)
        msg.attach(part)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pw)
            smtpObj.sendmail(self.mail_user, recipient, msg.as_string())
            print("---邮件发送成功---")

        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


if __name__ == '__main__':
    """
    输入： 收件人地址，邮件标题，邮件内容, 附件名
    """
    SendEmail().sendEmail("", subject="TEST", content="测试邮件正文", attachment="测试图片.jpg")
