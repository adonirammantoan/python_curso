#!/usr/bin/python3
# forma 1
#import pymongo
# forma 2
from pymongo import MongoClient
from pprint import pprint

try:
    # usar com a forma 1
    #con = pymongo.MongoClient()
    # usar com a forma 2
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print("erro ao conectar no mongo db")
#db.conta.update({'_id':1}, {"$set":{"titular": "user python"}})

# for registro in db.conta.find():
#    print(registro)

pprint([x for x in db.conta.find()])
