#coding='utf-8'
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import os
import jieba
from scipy.misc import imread
import numpy as np
from PIL import Image


def readTxt(data):
    with open(data,'r',encoding='utf-8') as f:
        line=f.read()
        return line

def chinese(text):
    #text="故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的"
    segs = jieba.cut(text)
    return  " ".join(segs)
    # for seg in segs:
    #     print(seg)

def showImg(txt):
    font = r'C:\Windows\Fonts\simfang.ttf' #设置中文
    imgPath = imread(os.getcwd()+'/ali.jpg')
    #imgPath = np.array(Image.open(os.getcwd()+'/ali.jpg'))
    wc = WordCloud(background_color="white", font_path=font, mask=imgPath, max_font_size=150)
    wc.generate(txt)
    #recolor 把填充的字体设置为图片本身的颜色 wc.recolor(color_func=ImageColorGenerator(imgPath)
    plt.imshow(wc,interpolation='bilinear')
    plt.axis("off")
    plt.show()
    #保存图片
    wc.to_file(os.getcwd()+"/newAli.jpg")


if __name__ == '__main__':
       t = readTxt(os.getcwd()+'/test.txt')
       ykzzldx = chinese(t)
       showImg(ykzzldx)

