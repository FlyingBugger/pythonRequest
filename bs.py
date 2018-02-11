import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

conn=MongoClient('127.0.0.1',27017)
db=conn.m
mycoll=db.requests
f=open(r'cookies.txt','r')
cookies={}
for line in f.read().split(';'):
	name,value=line.strip().split('=',1)
	cookies[name]=value
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
contents=requests.get('https://www.zhihu.com/topic',cookies=cookies,headers=header).content
soup=BeautifulSoup(contents,'html.parser')
targets=soup.find_all('a',{'class':'question_link'})
aText=r'<a>(.*?)</a>'
for div in targets:
	type(div)
	type(1)
       #print(div)
#	res=re.findall(r'<a>(.*?)</a>',div,re.S|re.M)
#	mycoll.insert({"name":res[0]}) 
#	‘’‘
