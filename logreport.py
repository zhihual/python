#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

# ways to log report. email/file/exe
# first choice is email


import smtplib  
from email.mime.text import MIMEText  
mailto_list=["7275337@qq.com"] 
mail_host="smtp.sina.com"  #设置服务器 smtp.sina.com
mail_user="dikehua"    #用户名
mail_pass="7275337"   #口令 
mail_postfix="sina.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="mimi"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
		#s.set_debuglevel(1)
        s.connect(mail_host,587)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception as e:  
        print(str(e))
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"hellow world","stock info"):  
        print('发送成功')  
    else:  
        print('发送失败')  