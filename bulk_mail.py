#!/usr/bin/python
#coding:utf-8

import smtplib 
import argparse 
from email.mime.text import MIMEText  
from email.header import Header
      
host = 'gstsh.com'  
SENDER= 'gstsh@gstsh.com'  
CONTENT=u"你好，测试!"
SUBJECT="python email test"
      
def send_mail(msg,mailto,subject):
	msg=MIMEText('<html><h1>%s</h1></html>'%msg,'html','utf-8')
	msg['Subject']=Header(subject,'utf-8')
	msg['From']=SENDER
	smtp=smtplib.SMTP()
	print(u"连接服务器....")
	smtp.connect(host)
	print(u"连接服务器成功，准备发送消息...")
	msg['TO']=mailto
	print(u"正在发送给%s"%mailto)
	smtp.sendmail(SENDER,mailto,msg.as_string())
	print(u"发送给%s成功"%mailto)
	#smtp.sendmail(sender,mailto,msg.as_string())
	smtp.quit()

def parse_args():
	parser=argparse.ArgumentParser(description=u'邮件群发系统参数使用说明')
	parser.add_argument('-m',dest='mode',action='store',choices=['n','p'],default='p',help=u"群发模式，n为普通模式，即一般的群发，p为专业模式， 让每一个收到邮件的人都以为是你只给他／她发了邮件")
	parser.add_argument('-f',dest='filename',action='store',required=True,help=u'存储邮箱地址的文件')
	parser.add_argument('-t',dest='threads_name',action='store',type=int,default=20,help=u'开启多线程，后接线程数目,默认为20，最大不超过50')
	args=parser.parse_args()
	
	filename=args.filename
	f=open(filename,'r')
	addrs=f.read()
	f.close()
	
	addrs=addrs.split('\n')[:-1]
	print addrs
	if args.mode=='n':
		send_mail(CONTENT,addrs,SUBJECT)
	elif args.mode=='p':
		for addr in addrs:
			send_mail(CONTENT,addr,SUBJECT)
	
		


if __name__=="__main__":
	args=parse_args()
	print dir(args)

        
