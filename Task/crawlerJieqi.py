import requests
from bs4 import BeautifulSoup
import re
headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
import json


def crawl_data():
    file = open("jieqi.txt", 'w+', encoding='utf-8')

    for i in range(1900, 2100, 1):
        dic = dict()
        print(i)
        start_url = 'https://jieqi.911cha.com/{}.html'.format(i)
        r = requests.get(start_url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        ret = re.compile('[(19)|(20)]{2}[0-9]{2}年[1-9][0-2]{0,1}月[1-9][0-9]{0,1}日\s\d{2}:\d{2}:\d{2}')
        dic = {i: soup.find_all(string=ret)}
        file.write(json.dumps(dic))
        file.write('\n')
    file.close()
    return "finish"



if __name__ == '__main__':
    pass
