from pymongo import MongoClient
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import json
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

conn = MongoClient("localhost", 27017)
db = conn.mymongodb
table1 = db["SONG_INFO"]
table2 = db["SONG_INFO_NEW"]


# data1 = table1.find({"total":{"$gt":0}},{"_id":0}).sort("total",pymongo.DESCENDING)
# for data in data1:
#     print(data)
project = {'$project': {'commentId': 1, 'singer': 1}}
group = {'$group': {'_id': "$singer",'total_comment':{'$sum':'$total'}}}
sort = {'$sort': {'total_comment': -1}}
limit = {'$limit': 100}
pipeline = [group, sort, limit]
data1 = table1.aggregate(pipeline)

list = list(data1)
with open("comment_sum1.json","w",encoding='utf-8') as f:
    json.dump(list, f, ensure_ascii=False)
# print(list(data1))
# count_list = []
# name_list = []
# for x in data1:
#     count_list.append(x["count"])
#     name_list.append(x["_id"])
# count_list.reverse()
# name_list.reverse()
# ts = pd.Series(count_list, name_list)
# font = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
# ts.plot(kind='barh')
# # plt.xlabel(u"中文", fontproperties=font)
# plt.show()

    # data2 = table1.find({"singer": x['_id']}).distinct("songCommentId")
    # for y in data2:
    #     print(y)
# dataDis = table2.distinct()

# for x in data1:
#     data2 = table2.distinct("songCommentId")
#     if x["songCommentId"] not in data2:
#         table2.insert(x)
#         print(x)





