# -*- coding: UTF-8 -*-
import redis
import smtplib
from email.mime.text import MIMEText

mailto_list=['qinbiash.net']
mail_host="smtp.163.com"  #设置服务器smtpserver = 'smtp.163.com'
mail_user="15255"    #用户名
mail_pass="2215255"   #口令
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me="代理池"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='UTF-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

r = redis.Redis(host="10.251.46.109", port=7000,db=0)
iplist= r.hkeys("proxyPool_slave")
print iplist
orilist = []
for line in open("mac.txt"):  
    orilist.append(line[:-1])
print orilist
print len(orilist)
print len(set(orilist))
print len(iplist)
if (len(iplist) < 77 ):
	send_mail(mailto_list,"代理池报警","请登录机器127查看")

for i in iplist:
	num = orilist.count(i)
	if (num < 1):
		print "warning,ip not in mac.txt"+i

for ori in orilist:
	orinum = iplist.count(ori)
	if (orinum < 1):
		print "warning,ip not running"+ori
	else:
		print "ok,okokokokok,ok"
