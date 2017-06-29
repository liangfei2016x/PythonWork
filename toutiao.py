import requests
import json
import os
import time
from multiprocessing import Pool
from hashlib import md5

def get_html(offset):
    url = "http://www.toutiao.com/search_content/"
    payload = {
        "offset": offset,
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": 20,
        "cur_tab": 1
    }
    r = requests.get(url, params=payload)
    print(r.url)
    if r.status_code == 200:
        return r.text
    else:
        return None
#生成器
def get_img_url(text):
    data = json.loads(text)
    for i in data.get("data"):
        for j in i.get("image_list"):
            yield j.get("url")

def save_img(imgUrl):
    filed_path = "{0}\{1}\{2}.jpg".format(os.getcwd(),"tupian",md5(str(imgUrl).encode("utf-8")).hexdigest())
    trueImg = requests.get(imgUrl).content
    if not os.path.exists(filed_path):
        with open(filed_path,"wb") as f:
            f.write(trueImg)
            f.close()



if __name__ == '__main__':
    start = time.time()
    groups = [x*20 for x in range(0,20)]
    texts = list(map(get_html, groups))
    for text in texts:
        item = get_img_url(text)
        for x in item:
            save_img(x)
    end = time.time()
    print(str(end-start)+"毫秒")


