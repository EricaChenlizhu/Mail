from PersonalInformation import *
import smtplib
from email.mime.text import MIMEText
import time

#定义邮件发送过程

def send_mail(head,body,code='utf-8'):
#gmail
    if type=='gmail':
    # The below code never changes, though obviously those variables need values.
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        body = body # 邮件正文
        msg = MIMEText(body, 'html') # 正文格式为html，txt
        msg['subject'] = head # 设置邮件标题
        msg['from'] = GMAIL_USERNAME # 设置发送人
        msg['to'] = To  # 设置接收人
        msg["Accept-Language"]="zh-CN"
        msg["Accept-Charset"]="ISO-8859-1,%s"%code
        session.sendmail(GMAIL_USERNAME, To, msg.as_string(),)
#163.com
    else:
        host = 'smtp.163.com'  # 设置发件服务器地址
        port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式

        body = body # 邮件正文
        msg = MIMEText(body, 'html') # 正文格式为html，txt
        msg['subject'] = head # 设置邮件标题
        msg['from'] = sender # 设置发送人
        msg['to'] = To  # 设置接收人

        s = smtplib.SMTP(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)  # 登陆邮箱
        s.sendmail(sender, To, msg.as_string())  # 发送邮件

#write sendLog
def sent_log(address):
    try:
        file=open('%s\\logSend.txt'%address,'a')
    except:
        file=open('%s\\logSend.txt'%address,'r')
    file.write(time.strftime('%y-%m-%d,%H:%M:%S',time.localtime())+'\n')
    file.close()


if __name__ == '__main__':
    head='test'

    from urllib import request
    url='http://www.liaoxuefeng.com/feed'
    conn=request.urlopen(url)
    page=conn.read().decode()
    body=page
    send_mail(head,body)
