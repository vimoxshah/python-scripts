import requests
from bs4 import BeautifulSoup
import random
import smtplib
from tabulate import tabulate
from email.mime.text import MIMEText


gmail_user = ''
gmail_pwd = ''
FROM = ''
TO=['']
SUBJECT = "Today's Task"


url1="http://geeksquiz.com/category/articles/puzzle/"
url2="http://geeksquiz.com/category/articles/puzzle/page/2/"
url3="http://geeksquiz.com/category/articles/puzzle/page/3/"
url4="http://geeksquiz.com/category/articles/puzzle/page/4/"
url5="http://geeksquiz.com/category/articles/puzzle/page/5/"

urls = [url1,url2,url3,url4,url5]

url=random.choice(urls)

req= requests.get(url)

page = BeautifulSoup(req.content,"html.parser")

econ = page.find_all("h2","entry-title")

rnum = random.randint(0,len(econ)-1)

ptilte=econ[rnum].contents[1].get_text()
target=econ[rnum].contents[1].get("href")

table = [[ptilte,target]]
send=tabulate(table,tablefmt="rst")

fmsg="Please provide your feedback here:"
fback="https://goo.gl/1n8wXL"
table1 = [[fmsg,fback]]
fbacktext=tabulate(table1,tablefmt="plain").encode('utf-8')

TEXT ="Hi,"+"\n"+  "Here is Your Today's Task, Enjoy!!" +"\n" + "\n" +send.encode('utf-8') +"\n" +"\n"+ fbacktext+ "\n"+"\n"+"Have a Great Day!:)"+ "\n"+"\n" + "Thanks."


msg = MIMEText(TEXT)
msg['Subject']= "Today's Puzzle"
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
#print "Successfully sent email"


