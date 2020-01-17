import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail(object):
    def __init__(self, receivers, content):
        # 第三方 SMTP 服务
        self.mail_host = "smtp.qq.com"  # 设置服务器:这个是qq邮箱服务器，直接复制就可以
        self.mail_pass = "xswsxmcscqkjbegi"  # 刚才我们获取的授权码
        self.sender = '1039459472@qq.com'  # 你的邮箱地址
        self.receivers = receivers  # 收件人的邮箱地址，可设置为你的QQ邮箱或者其他邮箱，可多个
        self.content = content
        self.send()

    def send(self):
        message = MIMEText(self.content, 'plain', 'utf-8')
        message['From'] = Header("管理员", 'utf-8')  # 第一个参赛是发件人的称呼
        message['To'] = Header("同学", 'utf-8')  # 第一个参赛是收件人的称呼
        subject = '最新澳门线上赌场上线啦！'  # 发送的主题，可自由填写
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')


if __name__ == '__main__':
    email_content = "我是邮件内容 "
    to_email = ['1039459472@qq.com', ]  # 发送方的邮件
    mail = Mail(receivers=to_email, content=email_content)
