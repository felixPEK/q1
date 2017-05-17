#!/usr/bin/env python
# -*- coding:utf-8 -*-

def email_v2(mailaddr,text, subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    ret = True
    try:
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = formataddr(['bonze2000', 'bonze2000@163.com'])
        msg['To'] = formataddr(['faye.89c51', '4621237@qq.com'])
        msg['Subject'] = subject

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("bonze2000@163.com", "woyaomit2014")
        server.sendmail('bonze2000@163.com',[mailaddr,], msg.as_string())
        server.quit()
    except:
        ret = False

    return ret

rr = email_v2("felixpek@outlook.com", '正式开业！BTW this is a mail send using python', "澳门首家线上赌场！！！")

if rr:
    print("mail sent successfully")
else:
    print("mail didn't send")