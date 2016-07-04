import requests
from bs4 import BeautifulSoup
import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  

class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit() 

url = "https://www.hackerearth.com/challenges/"
#This does the magic.Loads everything
r = Render(url)  
#result is a QString.
result = r.frame.toHtml()   
formatted_result = str(result.toAscii())
page = BeautifulSoup(formatted_result,"lxml")

l = page.find_all("span","no-underline weight-600")


for x in range(len(l)):
	cname = l[x].get_text()
	
	print cname 
#print page

