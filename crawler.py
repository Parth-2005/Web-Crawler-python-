import requests
from trial import *
from bs4 import BeautifulSoup
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
url = "https://google.com"
for x in url:
    # making requests instance
    reqs = requests.get(x)
    # using the BeaitifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')

    # displaying the title
    print("Title of the website is : ")
    title1 = str(soup.find_all('title'))
    title2 = title1.replace("[&lt  title&gt  ","").replace("&lt  /title&gt  ]","")
    if '[&lt  title id="main-title"&gt  ' in title2:
        title = title2.replace('[&lt  title id="main-title"&gt  ','')
    else:
        title=title2
    links = soup.find_all('a')
    aa = soup.find_all('meta')
    dis1 = str([meta.attrs['content'] for meta in aa if 'name' in meta.attrs and meta.attrs['name'] == 'description'])
    keywords = str([item['content'] for item in soup.select('[name=Keywords][content], [name=keywords][content]')])


    dis2 = dis1.replace("[",'')
    dis = dis2.replace("]","")

    if url == "":
        url = "--"
    if title == "":
        title = "--"
    if dis == "":
        dis = "--description--"
    if keywords =="[]":
        keywords = str(title)
    # else:
    #     keywords = keywords0.replace("'",'').replace(",",'][')        keywords.replace('"',"").replace(" ","")
    print(title)
    print(x)
    # print(keywords)
    print(dis)
    mydb = myclient['webbrowser']
    mycol = mydb["websites1"]
    mydict = {'title':title,'url':x,'description':dis, 'keywords':keywords}

    x = mycol.insert_one(mydict)

    print(x)