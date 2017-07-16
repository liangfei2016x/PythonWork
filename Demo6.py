import urllib.request
import time
from lxml import etree
import socket
# 国内高匿代理的链接
def get_url(url):
    url_list = []
    for i in range(2, 11):
        url_new = url + str(i)
        url_list.append(url_new)
    return url_list
# 获取网页内容
def get_content(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    content = res.read()
    return content.decode('utf-8')
# 提取网页信息 / ip 端口
def get_info(content):
    datas_ip = etree.HTML(content).xpath('//*[@id="middle_wrapper"]/div/table/tr/td[1]/text()')
    datas_port = etree.HTML(content).xpath('//*[@id="middle_wrapper"]/div/table/tr/td[2]/text()')
    data_agree = etree.HTML(content).xpath('//*[@id="middle_wrapper"]/div/table/tr/td[5]/text()')
    with open("data.txt", "a") as fd:
        for (x, y, z) in zip(data_agree, datas_ip, datas_port):
            out = u"" + x.lower()
            out += u"," + x.lower()
            out += u"://" + y
            out += u":" + z
            fd.write(out + u"\n")     # 所有ip和端口号写入data文件

def verif_ip(agree,port):    # 验证ip有效性
    user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    proxy = {agree:port}
    print(proxy)

    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    test_url = "http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
    req = urllib.request.Request(url=test_url, headers=headers)
    time.sleep(3)
    try:
        res = urllib.request.urlopen(req)
        time.sleep(2)
        content = res.read()
        if content:
            print('that is ok')
            with open("data3.txt", "a") as fd:       # 有效ip保存到data2文件夹
                fd.write(port+u"\n")
        else:
            print('its not ok')
    except urllib.request.HTTPError as e:
        print(e.reason)
    except urllib.request.URLError as e:
        print(e.reason)
    except socket.error as e:
        print("socket error："+e.strerror)


if __name__ == '__main__':
    # url = 'http://www.mimiip.com/gngao/'
    # url_list = get_url(url)
    # for i in url_list:
    #     print(i)
    #     content = get_content(i)
    #     time.sleep(3)
    #     get_info(content)

    with open("data.txt", "r") as fd:
        datas = fd.readlines()
        for data in datas:
            verif_ip(data.split(u",")[0], data.split(u",")[1])


# //*[@id="middle_wrapper"]/div/table/tbody/tr/td[1]
# //*[@id="middle_wrapper"]/div/table/tbody/tr/td[2]
# //*[@id="middle_wrapper"]/div/table/tbody/tr/td[5]