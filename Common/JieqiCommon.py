import json
import datetime
import re


def build_jieqi():
    file = open("/Users/zhaomin/Documents/ownproject/baziback/Common/jieqi.txt", 'r', encoding='utf-8')
    dic = dict()
    for line in file.readlines():
        dic.update(json.loads(line))
    file.close()
    return dic

def build_jieqi_list(english_year):
    dict = build_jieqi()
    cur_year_of_jieqi = [dict.get(str(english_year))[i] for i in range(0, 24, 2)]
    cur_year_of_jieqi = map(lambda x: re.sub(re.compile('年|月'), '-', x.replace('日', '')), cur_year_of_jieqi)
    cur_year_of_jieqi = map(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), cur_year_of_jieqi)
    cur_year_of_jieqi = sorted(cur_year_of_jieqi)
    return cur_year_of_jieqi