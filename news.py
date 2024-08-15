import requests
import json,time
# create greet decorator
def greet(xyz):
    def first(*args,**kwargs):
        print(50*'*')
        xyz(*args,**kwargs)
        print(50*'*')
    return first
# use greet decorator
@greet
def title_discription(abc):
    print(abc['title'])
    print(abc['description'])

# it take querry for api as q in url
x=input('enter which type news you want :- ')

# dste for api
m=int(time.strftime('%m'))-1
date=time.strftime(f'%Y-{m}-%d')

# fetch news api
a=requests.get(f'https://newsapi.org/v2/everything?q={x}&from={date}&sortBy=publishedAt&apiKey=12ab853afc184767a2ced22221022ecf')
# print(a.text)

# json module is for giving data serialization and deserialization
news=json.loads(a.text)
# for taking news in i 
# for i in news['articles']:
#     # for news article and description
#     title_discription(i)
title_discription(news['articles'][0])