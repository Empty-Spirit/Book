import json
import requests
from lxml import etree

# path = './conf/url.json'
# content = open(path, 'r', encoding='utf-8')
# str = content.read()
# data = json.loads(str)

# list = data[0: 1]

html = requests.get('https://wap.faloo.com/booklist/1264593.html')
res = etree.HTML(html.text)
print(res)
# def search():
    # html = requests.get(url.replace('{{key}}', "大主宰").replace("{{page}}", "1"))
    # print(url.replace("{{key}}", "大主宰"))

# search()
# for v1 in list:
#     if 'searchUrl' in v1:
#         # print(v1['searchUrl'])
#         search(v1['searchUrl'])

