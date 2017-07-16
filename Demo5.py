import requests
from bs4 import BeautifulSoup
import json
import time
from pymongo import MongoClient
from random import choice
import socket
from Crypto.Cipher import AES
import base64

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
    "https://106.91.35.241:8998",
    "https://183.66.81.178:8998",
    "https://117.57.58.90:8998",
    "https://61.191.41.130:80",
    "https://106.81.100.75:8998",
    "https://219.153.195.137:8998",
    "https://115.192.87.223:8118",
    "https://114.225.227.81:8118",
    "https://106.43.100.122:80",
    "https://221.175.232.183:8118",
    "https://221.238.72.196:8998",
    "https://124.67.210.252:80",
    "https://222.243.176.51:8998",
    "https://125.31.19.27:80",
    "https://117.166.178.46:8118",
    "https://211.147.240.86:808",
    "https://220.166.241.13:8118",
    "https://117.79.93.39:8808",
    "https://113.26.90.15:8998",
    "https://116.19.176.156:8118",
    "https://117.57.212.93:8998",
    "https://113.242.212.175:8998",
    "https://222.87.124.138:8998",
    "https://27.159.124.121:8118",
    "https://115.237.19.232:8998",
    "https://58.208.27.181:8118",
    "https://36.48.185.217:8998",
    "https://58.49.222.210:8998",
    "https://49.85.16.3:8998",
    "https://182.37.79.242:8118",
    "https://119.1.78.168:80",
    "https://125.117.48.8:8998",
    "https://115.231.219.202:3128",
    "https://113.248.43.228:8998",
    "https://115.216.174.156:8998",
    "https://58.210.202.234:808",
    "https://183.155.100.34:8998",
    "https://122.244.196.230:8998",
    "https://218.103.60.205:8080",
    "https://222.220.233.130:8998",
    "https://125.93.148.118:8118",
    "https://60.21.209.114:8080",
    "https://1.62.220.56:8118",
    "https://60.189.49.136:8998",
    "https://171.211.90.37:8998",
    "https://125.83.27.222:8998",
    "https://112.26.103.94:8118",
    "https://106.91.29.229:8998",
    "https://27.19.111.187:8998",
    "https://106.89.85.14:8998",
    "https://121.237.32.14:8998",
    "https://119.254.92.53:80",
    "https://49.4.178.24:9000",
    "https://121.57.139.36:8998",
    "https://111.61.35.76:8118",
    "https://114.38.241.17:8998",
    "https://125.117.95.38:8998",
    "https://116.255.192.209:808",
    "https://125.31.19.26:80",
    "https://211.151.48.60:8080",
    "https://121.236.57.85:8998",
    "https://42.235.162.165:8118",
    "https://113.64.12.154:8118",
    "https://119.249.200.90:8118",
    "https://183.156.116.145:8118",
    "https://183.154.222.75:8998",
    "https://182.87.214.166:8998",
    "https://113.250.110.154:8998",
    "https://202.194.61.149:8998",
    "https://14.109.103.36:8998",
    "https://106.81.133.79:8998",
    "https://114.231.193.128:8088",
    "https://61.166.75.48:8998",
    "https://60.183.15.103:8998",
    "https://106.56.204.9:8998",
    "https://183.157.48.230:8998",
    "https://36.107.239.38:8998",
    "https://117.65.34.120:8998",
    "https://183.217.70.223:8118",
    "https://113.248.29.162:8998",
    "https://49.65.150.61:8998",
    "https://123.138.89.130:9999",
    "https://101.71.224.46:8118",
    "https://122.244.20.145:8998",
    "https://183.167.22.52:8998",
    "https://182.240.152.137:8998",
    "https://183.63.14.107:808",
    "https://117.80.14.117:8998",
    "https://115.215.20.164:8998",
    "https://61.130.93.206:8998",
    "https://113.58.230.9:8118",
    "https://223.10.232.116:8998",
    "https://115.200.117.76:8998",
    "https://42.235.162.232:8118",
    "https://114.239.154.7:8998",
    "https://180.106.131.48:8118",
    "https://125.122.118.112:808",
    "https://113.244.152.119:8998",
    "https://117.87.186.195:8998",
    "https://218.66.253.144:8800",
    "https://124.227.68.194:8118",
    "https://221.175.226.31:8118",
    "https://218.64.93.207:808",
    "https://49.67.196.16:8998",
    "https://182.138.137.212:8118",
    "https://59.50.242.112:8998",
    "https://122.228.179.178:80",
    "https://114.232.161.23:8088",
    "https://182.87.212.172:8998",
    "https://125.93.149.232:8118",
    "https://42.84.79.38:8118",
    "https://117.68.100.24:8998",
    "https://117.64.143.53:8998",
    "https://182.101.11.42:8998",
    "https://121.229.104.162:8998",
    "https://114.55.155.120:80",
    "https://121.232.203.16:8998",
    "https://122.189.208.255:8118",
    "https://114.232.119.214:8088",
    "https://116.25.195.197:8118",
    "https://116.2.22.170:80"
]
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"
]




client = MongoClient("127.0.0.1", 27017)
db = client.mymongodb
table = db["SONG_INFO"]

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
    print(textarea)
    for x in json.loads(textarea):
        data = {
            "songId": x["id"],
            "songName": x["name"],
            "singer": x["artists"][0]["name"],
            "songCommentId": x["commentThreadId"]
        }
        print(data)
        saveMongoDB(data)

    # songA = soup.select(".f-hide > li > a")
    # for songData in songA:
    #     print(songData.get('href')+" "+songData.get_text())

def saveMongoDB(data):
    if table.insert(data):
        print("数据插入成功:"+str(data))
        return True
    return False

# 解密
def AES_encrypt(text,key,iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text.encode())
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

def getParams(page):
    iv = "0102030405060708"
    first_key = "0CoJUm6Qyw8W8jud"
    second_key = 16 * 'F'
    if (page == 1):  # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        h_encText = AES_encrypt(first_param, first_key.encode(), iv.encode())
    else:
        offset = str((page - 1) * 20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'false')
        h_encText = AES_encrypt(first_param, first_key.encode(), iv.encode())
    h_encText = AES_encrypt(h_encText.decode(), second_key.encode(), iv.encode())
    return h_encText.decode()

def getEncSeckey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey

def getSongComments(params,encSecKey,headers,commentId,proxies):
    song_url = "http://music.163.com/weapi/v1/resource/comments/%s?csrf_token=" % commentId
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    try:
        req = requests.post(url=song_url, data=data, headers=headers, proxies=proxies)
        num = 0
        if req.status_code == 200:
            r = json.loads(req.text)
            num = r["total"]
        return num
    except requests.HTTPError as e:
        print(e.reason)
    except requests.URLError as e:
        print(e.reason)
    except socket.error as e:
        print("socket error："+e.strerror)


if __name__ == '__main__':
    start = time.time()
    #allCommentsId = table.distinct("songCommentId")
    group = {'$group': {'_id': "$singer", 'count': {'$sum': 1}}}
    sort = {'$sort': {'count': -1}}
    limit = {'$limit': 100}
    pipeline = [group, sort, limit]
    #data1 = table.aggregate(pipeline)
    data1 = [
        {'_id': '红花会', 'count': 160},
        {'_id': '朴树', 'count': 159},
        {'_id': 'Ariana Grande', 'count': 158},
        {'_id': '王力宏', 'count': 157},
        {'_id': 'Tyga', 'count': 157},
        {'_id': 'Two Steps From Hell', 'count': 155},
        {'_id': 'Coldplay', 'count': 154},
        {'_id': 'Kygo', 'count': 153},
        {'_id': '澤野弘之', 'count': 153},
        {'_id': 'The Weeknd', 'count': 152},
        {'_id': '汪苏泷', 'count': 151},
        {'_id': '杨丞琳', 'count': 148},
        {'_id': 'David Guetta', 'count': 148},
        {'_id': 'Berner', 'count': 147},
        {'_id': '徐梦圆', 'count': 144},
        {'_id': '久石譲', 'count': 144},
        {'_id': '加藤達也', 'count': 137},
        {'_id': 'Tiësto', 'count': 135},
        {'_id': 'Taylor Swift', 'count': 134},
        {'_id': '蔡健雅', 'count': 133},
        {'_id': 'R3hab', 'count': 130},
        {'_id': '蔡依林', 'count': 130},
        {'_id': '杨千嬅', 'count': 128},
        {'_id': 'DJ Snake', 'count': 128},
        {'_id': 'Jony J', 'count': 128},
        {'_id': '好妹妹乐队', 'count': 128},
        {'_id': '萧忆情Alex', 'count': 125},
        {'_id': '张敬轩', 'count': 123},
        {'_id': '邓丽君', 'count': 123},
        {'_id': 'IU', 'count': 122},
        {'_id': '谢春花', 'count': 122},
        {'_id': 'Vicetone', 'count': 122},
        {'_id': 'Flo Rida', 'count': 121},
        {'_id': '河图', 'count': 121},
        {'_id': '高梨康治', 'count': 120},
        {'_id': '宋冬野', 'count': 120},
        {'_id': 'Shawn Mendes', 'count': 120},
        {'_id': 'Hardwell', 'count': 120},
        {'_id': 'Katy Perry', 'count': 118},
        {'_id': '陈鸿宇', 'count': 117},
        {'_id': 'Fall Out Boy', 'count': 117},
        {'_id': 'Adele', 'count': 116},
        {'_id': 'TheFatRat', 'count': 114},
        {'_id': '谭咏麟', 'count': 112},
        {'_id': '张惠妹', 'count': 112},
        {'_id': '苏打绿', 'count': 112},
        {'_id': '陈绮贞', 'count': 111},
        {'_id': '许巍', 'count': 110},
        {'_id': '满舒克', 'count': 110},
        {'_id': '莫文蔚', 'count': 108},
        {'_id': 'Justin Timberlake', 'count': 107},
        {'_id': '不才', 'count': 106},
        {'_id': '小曲儿', 'count': 106},
        {'_id': 'Drake', 'count': 105},
        {'_id': 'OneRepublic', 'count': 105},
        {'_id': 'Tizzy T', 'count': 104},
        {'_id': '银临', 'count': 102},
        {'_id': 'G.E.M.邓紫棋', 'count': 102},
        {'_id': '李克勤', 'count': 102}
    ]
    for x in data1:
        print(x)
        data2 = table.find({"singer": x['_id']}).distinct("songCommentId")
        for commentId in data2:
            one_proxy = choice(proxy)
            proxies = {
                one_proxy.split(":")[0]: one_proxy
            }
            params = getParams(1)
            encSecKey = getEncSeckey()
            headers = {
                "User-Agent": choice(USER_AGENTS),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, sdch",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Connection": "keep-alive"
            }
            total = getSongComments(params, encSecKey, headers,commentId, proxies)
            print("更新:"+commentId+":"+str(total))
            table.update({"songCommentId": commentId}, {"$set": {"total": total}})



    # for i in range(37, 38):
    #     print("*****第"+str(i+1)+"页*****")
    #     one_proxy = choice(proxy)
    #     proxies = {
    #         one_proxy.split(":")[0]: one_proxy
    #     }
    #     listHtml = getListHtml(i, headers, proxies)
    #     listUrls = getSongListUrl(listHtml)
    #     print(list(listUrls))
    #
    #     for listUrl in listUrls:
    #         print(listUrl)
    #         two_proxy = choice(proxy)
    #         proxies = {
    #             two_proxy.split(":")[0]: two_proxy
    #         }
    #         listHtml = openSongList(listUrl, headers, proxies)
    #         getSong(listHtml)

    # two_proxy = choice(proxy)
    # proxies = {
    #     two_proxy.split(":")[0]: two_proxy
    #     }
    # listUrl = "/playlist?id=646969233"
    # listHtml = openSongList(listUrl, headers, proxies)
    # getSong(listHtml)

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

