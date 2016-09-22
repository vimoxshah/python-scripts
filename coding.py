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
import datetime
from datetime import date,timedelta

reload(sys)
sys.setdefaultencoding("utf-8")
gmail_user = ''
gmail_pwd = ''
FROM = ''
TO=['']
SUBJECT = "Programming Challenge"


nt="https://a2oj.com/category?ID=41"
dp="https://a2oj.com/category?ID=33"
ce="https://www.codechef.com/problems/easy"
cm="https://www.codechef.com/problems/medium/"
ch="https://www.codechef.com/problems/hard/"
lt = "https://leetcode.com/problemset/algorithms/"
dfs="https://a2oj.com/category?ID=13"

gmt="https://a2oj.com/category?ID=21"
nflow="https://a2oj.com/category?ID=12"
prob="https://a2oj.com/category?ID=100"
stree="https://a2oj.com/category?ID=25"
acmd="https://a2oj.com/category?ID=230"
hld="https://a2oj.com/category?ID=72"


quotes=["Java Is C++ Without The Guns, Knives, And Clubs","Keyboard Not Found. Press < F1 > To RESUME. ","There Are Only 10 Types Of People In The World: Those Who Understand Binary, And Those Who Don't.","There Are Only 10 Types Of People In This World. Those Who Know Ternary, Those Who Don't And Those Who Confuse It With Binary.","A Language That Doesn't Have Everything Is Actually Easier To Program In Than Some That Do","Adding Manpower To A Late Software Project Makes It Later","Always Program As If The Person Who Will Be Maintaining Your Program Is A Violent Psychopath That Knows Where You Live.","Any Sufficiently Advanced Bug Is Indistinguishable From A Feature.","Base Eight Is Just Like Base Ten Really, If You're Missing Two Fingers.","Before Software Can Be Reusable It First Has To Be Usable.","Beware Of Bugs In The Above Code; I Have Only Proved It Correct, Not Tried It.""Bug, N: An Elusive Creature Living In A Program That Makes It Incorrect. The Activity Of Debugging, Or Removing Bugs From A Program, Ends When People Get Tired Of Doing It, Not When The Bugs Are Removed.","C Is Quirky, Flawed, And An Enormous Success.","Coding Styles Are Like A*****Es, Everyone Has One And No One Likes Anyone Elses.","Debugging Is Twice As Hard As Writing The Code In The First Place. Therefore, If You Write The Code As Cleverly As Possible, You Are, By Definition, Not Smart Enough To Debug It.","Documentation Is Like Sex: When It Is Good, It Is Very, Very Good; And When It Is Bad, It Is Better Than Nothing.","Don't Get Suckered In By The Comments— They Can Be Terribly Misleading. Debug Only Code.","He Who Hasn't Hacked Assembly Language As A Youth Has No Heart. He Who Does As An Adult Has No Brain.","I Mean, If 10 Years From Now, When You Are Doing Something Quick And Dirty, You Suddenly Visualize That I Am Looking Over Your Shoulders And Say To Yourself: 'Dijkstra Would Not Have Liked This', Well That Would Be Enough Immortality For Me.","If Debugging Is The Process Of Removing Bugs, Then Programming Must Be The Process Of Putting Them In.","If The Code And The Comments Disagree, Then Both Are Probably Wrong.","Managing Senior Programmers Is Like Herding Cats.","Memory Is Like An Orgasm. It's A Lot Better If You Don't Have To Fake It.","Once You're Done Writing The Code, Never Open It Again Unless You Want To See How Uncomprehensible And Utterly Ridiculous It Really Is.","Part Of The Inhumanity Of The Computer Is That, Once It Is Competently Programmed And Working Smoothly, It Is Completely Honest.","Programming Is Like Sex: One Mistake And You Have To Support It For The Rest Of Your Life.","Software Engineering Is That Part Of Computer Science Which Is Too Difficult For The Computer Scientist.","The Evolution Of Languages: FORTRAN Is A Non-Typed Language. C Is A Weakly Typed Language. Ada Is A Strongly Typed Language. C++ Is A Strongly Hyped Language.","The Generation Of Random Numbers Is Too Important To Be Left To Chance.","The Most Likely Way For The World To Be Destroyed, Most Experts Agree, Is By Accident. That's Where We Come In; We're Computer Professionals. We Cause Accidents.","The Ultimate Metric That I Would Like To Propose For User Friendliness Is Quite Simple: If This System Was A Person, How Long Would It Take Before You Punched It In The Nose?","The trouble with programmers is that you can never tell what a programmer is doing until it’s too late. ","The best performance improvement is the transition from the nonworking state to the working state.","In order to understand recursion, one must first understand recursion.","There are only two kinds of programming languages: those people always bitch about and those nobody uses. ","It’s a curious thing about our industry: not only do we not learn from our mistakes, we also don’t learn from our successes. ","Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the universe trying to produce bigger and better idiots. So far, the universe is winning. ","Software undergoes beta testing shortly before it’s released. Beta is Latin for “still doesn’t work. ","Walking on water and developing software from a specification are easy if both are frozen. ","Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. ","A good programmer is someone who always looks both ways before crossing a one-way street","It’s not a bug – it’s an undocumented feature.","Ready, fire, aim: the fast approach to software development. Ready, aim, aim, aim, aim: the slow approach to software development","There are two ways to write error-free programs; only the third one works. ","If builders built buildings the way programmers wrote programs, then the first woodpecker that came along wound destroy civilization.","I think Microsoft named .Net so it wouldn’t show up in a Unix directory listing. ","The best method for accelerating a computer is the one that boosts it by 9.8 m/s2. ","Without requirements or design, programming is the art of adding bugs to an empty text file","The best thing about a boolean is even if you are wrong, you are only off by a bit. "]
quote=random.choice(quotes)


topics=[ce,dp,cm,nt,lt,dfs,gmt,nflow,prob,stree,acmd,hld]
i=0
send=""

while (i<5):
		
	rtopic = random.choice(topics)

	title=""
	link=""
	

	if(rtopic==nt):
		req= requests.get(nt)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,214)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")

		#print title +"\t"+ link

	elif(rtopic==dfs):
		req= requests.get(dfs)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,471)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")

		#print title +"\t"+ link	

	elif(rtopic==dp):
		req= requests.get(dp)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,1021)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")

		#print title +"\t"+ link

	elif(rtopic==ce):

		req= requests.get(ce)

		page=BeautifulSoup(req.content,"html.parser")
		tble = page.find_all("div","problemname")

		rnum = random.randint(0,len(tble)-1)

		ftitle = tble[rnum].get_text()
		title=re.sub('\n','',ftitle)
		flink = tble[rnum].contents[1].get("href")
		link="https://www.codechef.com"+flink
		#print title +"\t"+ link

	elif(rtopic==ch):

		req= requests.get(ch)

		page=BeautifulSoup(req.content,"html.parser")
		tble = page.find_all("div","problemname")

		rnum = random.randint(0,len(tble)-3)

		ftitle = tble[rnum].get_text()
		title=re.sub('\n','',ftitle)
		flink = tble[rnum].contents[1].get("href")
		link="https://www.codechef.com"+flink
		#print title +"\t"+ link	


	elif(rtopic==cm):

		req= requests.get(cm)

		page=BeautifulSoup(req.content,"html.parser")
		tble = page.find_all("div","problemname")

		rnum = random.randint(0,len(tble)-1)

		ftitle = tble[rnum].get_text()
		title=re.sub('\n','',ftitle)
		flink = tble[rnum].contents[1].get("href")
		link="https://www.codechef.com"+flink
		#print title +"\t"+ link	

	elif(rtopic==lt):
		
		req = requests.get(lt)

		page = BeautifulSoup(req.content,"html.parser")

		al = page.find_all("a")	

		rnum = random.randint(32,367)

		title = al[rnum].get_text()
		flink = al[rnum].get("href")
		link="https://leetcode.com"+flink
		#print title +"\t"+link	

	elif(rtopic==gmt):
		req= requests.get(gmt)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,197)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")


	elif(rtopic==nflow):
		req= requests.get(nflow)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,112)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")


	elif(rtopic==prob):
		req= requests.get(prob)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,100)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")	


	elif(rtopic==stree):
		req= requests.get(stree)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,97)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")	


	elif(rtopic==acmd):
		req= requests.get(acmd)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,16)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")	


	elif(rtopic==hld):
		req= requests.get(hld)

		page=BeautifulSoup(req.content,"html.parser")

		tble = page.find_all("a",target="_blank")

		rnum = random.randint(2,23)

		title = tble[rnum].get_text()
		link = tble[rnum].get("href")


	table = [[title,link]]
	send=tabulate(table,tablefmt="rst")+"\n"+"\n"+send
	i+=1

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

fs=""
for x in range(len(item)):
	title=item[x].title.text
	sTime=item[x].starttime.text
	url=item[x].url.text
	#smonth=sTime[5:7]
	sdate=(sTime[0:10])
	eTime=item[x].endtime.text
	

	for y in daterange(now, ndate):
		if(str(y)==str(sdate)):
			
   			k= title +"\n"+sTime+"\t"+"-"+"\t"+eTime +"\n"+url+"\n"
   			fs=fs+"\n"+k
   		 	

fmsg="Please provide your feedback here:"
fback="https://goo.gl/1n8wXL"
table1 = [[fmsg,fback]]
fbacktext=tabulate(table1,tablefmt="plain").encode('utf-8')


TEXT ="Hi,"+"\n"+ "\n"+quote.encode('utf-8')+"\n"+"\n"+"Here is Your Today's Coding Challenge, I think you can Crack it !!" +"\n" + "\n" +send.encode('utf-8') 
FTEXT=TEXT+"\n"+"Do you want Interview questions from tech giant companies like Google,Facebook,Amazon etc. then Please share your ideas or suggestions in Feedback form."+fbacktext+"\n"+"\n"+"\n"+"Happy Coding!" +"\n" +"Have a Great Day!:)"+ "\n"+"\n" + "Thanks."


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

