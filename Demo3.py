# encoding='utf-8'
import requests
import json
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from Crypto.Cipher import AES
import base64
import os

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

# 解密
def AES_encrypt(text,key,iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text.encode())
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

# 获取json格式数据
def getJson(url,params,encSeckey):
    headers = {
        "Cookie":"Province=020; City=0755;s_=1; UM_distinctid=15d119cbb09520-0e985fd25569ec-5393662-140000-15d119cbb0ab1d; vjuids=108eb9c4a.15d119cc02a.0.96704a5d00366; vjlast=1499239072.1499239072.30; _ntes_nnid=4f779cc48ebffb7d6cd4c2f417146702,1499239071791; _ntes_nuid=4f779cc48ebffb7d6cd4c2f417146702; vinfo_n_f_l_n3=7aed8a8a7222e5ad.1.0.1499239071800.0.1499239116879; usertrack=c+xxClleDZNjwJfsAxXPAg==; _ga=GA1.2.1914621278.1499336092; _gid=GA1.2.1491023381.1499733731; playerid=95556586; JSESSIONID-WYYY=cDJOUnmvyV5xciI4X4DnWjS3PK4d1WdWspmMwp3%2BqH1M3Bep2F104vYcF07pIIw3TvenevHvmjRVORGonqRbf2RZppErYB%2F1pnSqDO%5Clhos9wKD%5Cxsh8p3YITG2%5C0Vi%5Cs6Fcl2MefrNDFK4VdfOT9drNP36Fbiq%5C8iHrfspzZ%2B88gwKN%3A1499759703747; _iuqxldmzr_=32; __utma=94650624.317178145.1499321600.1499749373.1499756164.12; __utmb=94650624.6.10.1499756164; __utmc=94650624; __utmz=94650624.1499749373.11.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    data = {
        "params": params,
        "encSecKey": encSeckey
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        r = response.text
    else:
        print("访问被限制")
        pass
    return r

def saveFile(name,text):
    filePath = os.path.join(os.getcwd(), name+".txt")
    with open(filePath, "a", encoding="utf-8") as f:
        f.write(text)
        f.close()

def getComments(songId,songName):
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=" % songId
    params = getParams(1)
    encSecKey = getEncSeckey()
    data = getJson(url, params, encSecKey)
    data = json.loads(data)
    # 总页数
    totalPage = data["total"]//20 + (1 if data["total"] % 20 > 0 else 1)
    for i in range(totalPage):
        print("第"+str(i+1)+"页")
        params = getParams(i+1)
        pageData = getJson(url, params, encSecKey)
        pageData = json.loads(pageData)
        txt = ""
        for comment in pageData["comments"]:
            nikeName = comment["user"]["nickname"]
            content = comment["content"]
            txt += nikeName+":"+content+"\n"
        saveFile(songName, txt)


def getCommentImg(filePath):
    with open(filePath, "r", encoding="utf-8") as f:
        content = f.read()
    font = r'C:\Windows\Fonts\simfang.ttf' #设置中文
    conList = jieba.cut(content)
    conList = " ".join(conList)
    wc = WordCloud(font_path=font)
    wc.generate(conList)
    plt.imshow(wc,interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    songId = input("你想看那首歌的热评,请输入歌曲ID:")
    songName = input("歌曲名字:")
    getComments(songId, songName)
    filePath = os.path.join(os.getcwd(), songName+".txt")
    getCommentImg(filePath)

