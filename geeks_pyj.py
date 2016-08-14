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
TO = ['']
SUBJECT = "Programming Knowledge"

url ="http://www.geeksforgeeks.org/python/"

req = requests.get(url)

page= BeautifulSoup(req.content,"html.parser")

li = page.find_all("li")

rnum = random.randint(72,128)

ptitle = li[rnum].get_text()
plink = li[rnum].contents[0].get("href")

p="Python :"+"\t"+ptitle +"\t"+plink

jurl ="http://www.geeksforgeeks.org/java/"

req1 = requests.get(jurl)

page= BeautifulSoup(req1.content,"html.parser")

li1 = page.find_all("li")

rnum1 = random.randint(74,192)

jtitle = li1[rnum1].get_text()
jlink = li1[rnum1].contents[0].get("href")

j= "Java :"+"\t"+jtitle+"\t"+jlink

curl ="http://www.geeksforgeeks.org/c/"

req2 = requests.get(curl)

page= BeautifulSoup(req2.content,"html.parser")

li1 = page.find_all("li")

rnum1 = random.randint(74,311)

ctitle = li1[rnum1].get_text()
clink = li1[rnum1].contents[0].get("href")

c= "C :"+"\t"+ctitle+"\t"+clink

cpurl ="http://www.geeksforgeeks.org/c-plus-plus/"

req2 = requests.get(cpurl)

page= BeautifulSoup(req2.content,"html.parser")

li1 = page.find_all("li")

rnum1 = random.randint(74,249)

cptitle = li1[rnum1].get_text()
cplink = li1[rnum1].contents[0].get("href")

cp= "C++ :"+"\t"+cptitle+"\t"+cplink


send=p+"\n"+"\n"+j+"\n"+"\n"+c+"\n"+"\n"+cp

TEXT ="Hi,"+"\n"+  "You have to know this, Enjoy!!" +"\n" + "\n" +send.encode('utf-8') +"\n" +"\n" +"Have a Great Day!:)"+ "\n"+"\n" + "Thanks."
msg = MIMEText(TEXT)
msg['Subject']= SUBJECT
msg['From']=FROM
msg['To']=", ".join(TO)

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
                   