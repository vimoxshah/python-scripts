import requests
from bs4 import BeautifulSoup
import json
import os

def append_record(record):
    with open('my_file', 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)

output_file = open("output.txt", "a")
page = requests.get("http://www.cricbuzz.com/cricket-match/live-scores")
#print page.content
page = BeautifulSoup(page.content,"lxml")

tour_title_main = page.find_all("div","cb-col cb-col-100 cb-lv-main")
for x in range(len(tour_title_main)):
	t_tour=tour_title_main[x].contents
	if(len(t_tour)==2):
		tour_title=t_tour[0].get_text()
		temp=t_tour[1].contents
		match_title=temp[0].a.get_text()
		d= temp[0].find_all("div","text-gray")
		day=d[0].get_text()
		place = d[1].get_text()

		try:
			score=temp[1].div.get_text()
			
		except Exception, e:
			score="Score Not Available"
			
		try:
			result_c = temp[1].find("div","cb-lv-scrs-col cb-font-12 cb-text-complete").get_text()	
			x={'Tour':tour_title, 'Match':match_title, 'Championship':day,'Place':place,'score':score,'Result':result_c}
			append_record(x)
				#print tour_title +"\n"+match_title +"\n"+day +"\n"+place+ "\n"+score+"\n"+result_c
		except Exception, e:
			try:
				result_l= temp[1].find("div","cb-lv-scrs-col cb-font-12 cb-text-live").get_text()
				y={'Tour':tour_title, 'Match':match_title, 'Championship':day, 'Place':place,'score':score,'Result':result_l}
				append_record(y)
					#print tour_title +"\n"+match_title +"\n"+day +"\n"+place+ "\n"+score+"\n"+result_l
			except Exception, e:
				z={'Tour':tour_title, 'Match':match_title, 'Championship':day, 'Place':place,'score':score,'Result':"Not Started"}
				append_record(z)
			
			
		
	else:
		tour_title=t_tour[0].get_text()
		temp=t_tour[0].contents
		match_title=temp[0].a.get_text()
		d= temp[0].find_all("div","text-gray")
		day=d[0].get_text()
		place = d[1].get_text()
		
		try:
			score=temp[1].div.get_text()
			
		except Exception, e:
			score="Score Not Available"
			

		try:
			result_c = temp[1].find("div","cb-lv-scrs-col cb-font-12 cb-text-complete").get_text()	
			x={'Match':match_title, 'Championship':day, 'Place':place,'score':score,'Result':result_c}
			append_record(x)
				#print tour_title +"\n"+match_title +"\n"+day +"\n"+place+ "\n"+score+"\n"+result_c
		except Exception, e:
			try:
				result_l= temp[1].find("div","cb-lv-scrs-col cb-font-12 cb-text-live").get_text()
				y={'Match':match_title, 'Championship':day, 'Place':place,'score':score,'Result':result_l}
				append_record(y)
					#print tour_title +"\n"+match_title +"\n"+day +"\n"+place+ "\n"+score+"\n"+result_l
			except Exception, e:
				z={'Match':match_title, 'Championship':day, 'Place':place,'score':score,'Result':"Not Started"}
				append_record(z)			
			





