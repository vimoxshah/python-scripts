from bs4 import BeautifulSoup
import requests
import datetime
from datetime import date,timedelta
from tabulate import tabulate
	
now = datetime.datetime.now().date()
#month = now.month
month='{:02d}'.format(now.month)
ndate=timedelta(days=8)+now

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


url = requests.get("https://www.hackerrank.com/calendar/feed.rss")

page = BeautifulSoup(url.text,"lxml")

item = page.find_all("item")

li=""
for x in range(len(item)):
	title=item[x].title.text
	sTime=item[x].starttime.text
	url=item[x].url.text
	#smonth=sTime[5:7]
	sdate=(sTime[0:10])
	eTime=item[x].endtime.text
	
	
	m=0
	
	for y in daterange(now, ndate):

		if(str(y)==str(sdate)):
			m+=1
			#data={"Title":title ,"Start Time":sTime ,"End Time":eTime ,"URL":url}
   			k= title +"\n"+sTime+"\t"+"-"+" "+eTime +"\n"+url+"\n"
   			li=li+"\n"+k
   			
	
print li   			
   			
   	

	
