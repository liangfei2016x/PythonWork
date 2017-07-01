#encoding='utf-8'
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from os import path


def readTxt(data):
    with open(data,'r',encoding='utf-8') as f:
        line=f.read()
        return line

def showImg(txt):
    font = r'C:\Windows\Fonts\simfang.ttf' #设置中文
    wc = WordCloud(font_path=font).generate(txt)
    plt.imshow(wc,interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
       t = readTxt(os.getcwd()+'/test.txt')
       showImg(t)
