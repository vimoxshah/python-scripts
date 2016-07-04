# -*- coding: utf-8 -*-
# encoding=utf8 
import sys
import requests
from bs4 import BeautifulSoup
import random
import smtplib
from tabulate import tabulate
from email.mime.text import MIMEText
import webbrowser
import re

gmail_user = ''
gmail_pwd = ''
FROM = ''
TO=[]
SUBJECT = "Interview Questions"



url = "https://careercup.com/categories"
i=0
ftitle=""
slink=""
while (i<5):


	req= requests.get(url)

	page=BeautifulSoup(req.content,"html.parser")

	div = page.find_all("div", style="width: 45%; float: left;")

	rnum = random.randint(0,430)



	title = div[rnum].contents[1].get_text()
	flink = div[rnum].contents[1].get("href")
	clink = "https://careercup.com"+flink

	req1 = requests.get(clink)

	npage= BeautifulSoup(req1.content,"html.parser")

	ndiv = npage.find_all("span","entry")

	rq = random.randint(0,len(ndiv)-1)
	qlink = ndiv[rq].contents[1].get("href")

	link = "https://careercup.com"+qlink

	ftitle= title+"\t"+link+"\n"+"\n"+ftitle

	
	i+=1

FTEXT="Hi,"+"\n"+"Today's Interview Questions."+"\n"+"\n"+ftitle+"Hope you like this. "+"\n"+"\n"+"Have a Great Day :)"+"\n"+"Thanks."
msg = MIMEText(FTEXT)
msg['Subject']= SUBJECT
msg['From']=FROM
msg['To']=", ".join(TO)

 

# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(gmail_user, gmail_pwd)
mailserver.sendmail(FROM, TO, msg.as_string())
mailserver.quit()
#print "Successfully sent email"

