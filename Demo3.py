import requests
import json
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
    songId = input("你想看那首歌的热评:")
    getCommentImg(songId)