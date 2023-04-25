import json
import requests
from lxml import etree

path = './conf/url.json'
content = open(path, 'r', encoding='utf-8')
str = content.read()
data = json.loads(str)

list = data[0: 1]

def search(url):
    html = requests.get(url.replace('{{key}}', "大主宰").replace("{{page}}", "1"))
    res = etree.HTML(html.text)
    print(res)
    # print(url.replace("{{key}}", "大主宰"))


for v1 in list:
    if 'searchUrl' in v1:
        # print(v1['searchUrl'])
        search(v1['searchUrl'])

