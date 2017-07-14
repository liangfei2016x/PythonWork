import requests
from bs4 import BeautifulSoup
import json
import time
from pymongo import MongoClient
from random import choice

url = "http://music.163.com"
proxy = [
    "https://106.120.175.76:55336",
    "https://222.181.26.44:8998",
    "https://222.181.61.1:8998",
    "https://106.88.115.194:8998",
    "https://113.251.83.191:8998",
    "https://14.109.112.79:8998",
    "https://14.106.87.116:8998",
    "https://125.82.226.175:8998",
    "https://14.109.98.69:8998",
    "https://113.250.106.72:8998",
    "https://106.91.44.173:8998",
    "https://106.88.6.133:8998",
    "https://14.109.96.119:8998",
    "https://106.91.47.231:8998",
    "https://218.70.208.117:8998",
    "https://106.91.28.220:8998",
    "https://183.66.18.110:8998",
    "https://119.85.28.113:8998",
    "https://106.83.54.36:8998",
    "https://14.108.120.166:8998",
    "https://219.151.207.222:8998",
    "https://1.24.150.234:808",
    "https://14.105.94.153:8118",
    "https://113.251.218.66:8998",
    "https://125.85.186.2:8998",
    "https://121.32.251.44:80",
    "https://121.32.251.43:80",
    "https://121.32.251.45:80",
]
headers = {
    "Cookie": "Province=020; City=0755;s_=1; UM_distinctid=15d119cbb09520-0e985fd25569ec-5393662-140000-15d119cbb0ab1d; vjuids=108eb9c4a.15d119cc02a.0.96704a5d00366; vjlast=1499239072.1499239072.30; _ntes_nnid=4f779cc48ebffb7d6cd4c2f417146702,1499239071791; _ntes_nuid=4f779cc48ebffb7d6cd4c2f417146702; vinfo_n_f_l_n3=7aed8a8a7222e5ad.1.0.1499239071800.0.1499239116879; usertrack=c+xxClleDZNjwJfsAxXPAg==; _ga=GA1.2.1914621278.1499336092; _gid=GA1.2.1491023381.1499733731; playerid=95556586; JSESSIONID-WYYY=cDJOUnmvyV5xciI4X4DnWjS3PK4d1WdWspmMwp3%2BqH1M3Bep2F104vYcF07pIIw3TvenevHvmjRVORGonqRbf2RZppErYB%2F1pnSqDO%5Clhos9wKD%5Cxsh8p3YITG2%5C0Vi%5Cs6Fcl2MefrNDFK4VdfOT9drNP36Fbiq%5C8iHrfspzZ%2B88gwKN%3A1499759703747; _iuqxldmzr_=32; __utma=94650624.317178145.1499321600.1499749373.1499756164.12; __utmb=94650624.6.10.1499756164; __utmc=94650624; __utmz=94650624.1499749373.11.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
# proxies = {
#   "https": "https://14.106.87.116:8998"
# }

# client = MongoClient("127.0.0.1", 27017)
# db = client.mymongodb
# table = db["SONG_INFO"]

def getListHtml(page,headers,proxies):
    offset = str(page*35)
    url = "http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset={}".format(offset)
    response = requests.get(url=url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        r = response.text
    else:
        print("访问被限制")
        pass
        r = ""
    return r

def getSongListUrl(html):
    soup = BeautifulSoup(html, "lxml")
    li = soup.select("#m-pl-container > li > p.dec > a")
    for aTag in li:
        ahref = aTag.get("href")
        yield ahref

def openSongList(listUrl,headers,proxies):
    reqUrl = url+listUrl
    resp = requests.get(url=reqUrl, headers=headers, proxies=proxies)
    if resp.status_code == 200:
        songlist = resp.text
    else:
        print("请求被限制")
        pass
        songlist = ""
    return songlist

def getSong(songListHtml):
    soup = BeautifulSoup(songListHtml, "lxml")
    textarea = soup.select("textarea")[0].get_text()
    for x in json.loads(textarea):
        data = {
            "songId": x["id"],
            "songName": x["name"],
            "singer": x["artists"][0]["name"],
            "songCommentId": x["commentThreadId"]
        }
        print(data)
        #saveMongoDB(data)

    # songA = soup.select(".f-hide > li > a")
    # for songData in songA:
    #     print(songData.get('href')+" "+songData.get_text())

# def saveMongoDB(data):
#     if table.insert(data):
#         print("数据插入成功:"+str(data))
#         return True
#     return False


if __name__ == '__main__':
    start = time.time()
    for i in range(1):
        print("*****第"+str(i+1)+"页*****")
        one_proxy = choice(proxy)
        proxies = {
            one_proxy.split(":")[0]: one_proxy
        }
        listHtml = getListHtml(i, headers, proxies)
        listUrls = getSongListUrl(listHtml)
        for listUrl in listUrls:
            print(listUrl)
        # print(list(listUrls))
        # for listUrl in listUrls:
        #     listHtml = openSongList(listUrl, headers, proxies)
        #     getSong(listHtml)
        # time.sleep(10+i)
    end = time.time()

    print("共运行 "+str(end-start)+" 秒")
    # a = getSongListUrl(listHtml)
    # listUrl = "/playlist?id=718630307"
    # html = openSongList(listUrl, headers)
    # print(html)
    # getSong(html)
    # m-pl-container > li
    # m-pl-container > li:nth-child(1) > p.dec > a
    # m-pl-container > li:nth-child(1) > p.dec > a
    # http://www.mimiip.com/gngao/

