from Demo6 import verif_ip
import requests
from pymongo import MongoClient

conn = MongoClient("localhost", 27017)
db = conn.mymongodb
table1 = db["SONG_INFO"]
table2 = db["SONG_INFO_NEW"]

data1 = table1.find()
# dataDis = table2.distinct()
allCommentsId = table1.distinct("songCommentId")

for commentId in allCommentsId:
    table1.update({"songCommentId": commentId}, {"$set": {"total": 1}})




