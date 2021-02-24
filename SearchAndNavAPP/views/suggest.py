import requests
import json
import bs4
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

proxies = {
    'http':'http://183.167.217.152'
}

def getHTMLText(url):   #通用 获取网页信息
    try:
        r = requests.get(url, headers=headers)   #设置代理 设置时间
        r.raise_for_status()
    except:
        print("搜索失败")
        return ""
    return r.text


def getSearch(key):
    data = []
    url = "https://www.dogedoge.com/sugg/" + key
    text = getHTMLText(url)
    soup = BeautifulSoup(text, "html.parser")
    for i in soup:
        if isinstance(i,bs4.element.Tag):
            data.append(i.text.strip())
    return data


def getMovie(key):
    data=""
    url = "http://service-channel.mtime.com/Search.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Services&Ajax_CallBackMethod=GetSuggestObjs&Ajax_CallBackArgument0="+key
    text=getHTMLText(url)
    text= text.strip()
    text=text[27:-1]

    if text != "":
        data = json.loads(text);  # 将 JSON 对象转换为 Python 字典
        if (data['value']!=None):
            data=data.get('value',"")
            data=data.get('objs',"")
    return data


def getBook(key):
    data=""
    url = "https://book.douban.com/j/subject_suggest?q=" + key
    text=getHTMLText(url)
    if text != "":
        data = json.loads(text);  # 将 JSON 对象转换为 Python 字典
    return data
