import requests
import json
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from Crypto.Cipher import AES
import base64



forth_param = "0CoJUm6Qyw8W8jud"
# 第二个参数
second_param = "010001"
# 第三个参数
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

def getParams(page):
    iv = "0102030405060708"
    first_key = forth_param
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

def AES_encrypt(text,key,iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text.encode())
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

def getJson(url,params,encSeckey):
    data = {
        "params": params,
        "encSecKey": encSeckey
    }
    response = requests.post(url,data=data)
    print(response)
    return response.text

def getCommentImg(songId):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=' % songId
    userData={
        "params":"Ji5BYFzwYIPq3xCG6/DYwFXN5chKK5CvvfHdi+Tkwu2ymBL69ixfpUggjK1sAKkNRt3yvGxGySpRMEyarXKa787GKaIqvY4V17dgjP/SUMgzUSsEM7ETCMtsHiHsQuAv/FQNbwe1iJ9tjr7PI1YvLfAjkE6eNxlJ2/x7FZpzNZaAUUROdUaTI0bmEvpiFs9F",
        "encSecKey":"1f0e120f1d79ade7ff4a3bb106027807b7c8066432723747ccdb91f199e29724f3cadeed19be2951caf4c56c56ccdbacfa006ce0ead589d1a0c7ec27cf417557761f042d5326452110922fcea808a737fc98e3b057844adfb6f0999457c5bd64460fbbf24e821cc1b222d4e5a4562744f2e73260145b2fad267702627bd81d6a"
    }
    r = requests.post(url, data=userData)
    comments = json.loads(r.text)["hotComments"]
    content = ""
    for comment in comments:
        content += comment["content"]
    font = r'C:\Windows\Fonts\simfang.ttf' #设置中文
    conList = jieba.cut(content)
    conList = " ".join(conList)
    wc = WordCloud( font_path=font)
    wc.generate(conList)
    plt.imshow(wc,interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    #songId = input("你想看那首歌的热评:")
    #getCommentImg(songId)
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_172325?csrf_token="
    params = getParams(2)
    encSecKey = getEncSeckey()
    data = getJson(url, params, encSecKey)
    print(data)