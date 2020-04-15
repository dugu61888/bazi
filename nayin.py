from astral.sun import sun
import ganzhi
import json
import metaphysic
import datetime
import re
import astral
from Common.BaziCommon import *




def find_nayin(name: str):
    tian_index = tiangans.index(list(name)[0])
    dizhi_index = dizhis.index(list(name)[1])
    times = 0
    if tian_index - dizhi_index < 0:
        times = (tian_index + 12 - dizhi_index) // 2
    else:
        times = (tian_index - dizhi_index) // 2
    index = tian_index // 2

    index = index + 5 * times

    return nayin[index]


def build_jieqi():
    file = open("Common/jieqi.txt", 'r', encoding='utf-8')
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


def judge_neast_jieqi():
    pass


def build_Dayun(english_year, english_month, english_day, hour, minutes, sex: int):
    '''

    :param english_year:
    :param english_month:
    :param english_day:
    :param hour:
    :param minutes:
    :param sex:  1  是男，0 是女
    :return:
    '''
    lunar = ganzhi.day(english_year, english_month, english_day)
    bazi = metaphysic.getShenChenBaZi(english_year, english_month, english_day, hour)

    lunar_year = lunar[4]
    order = lunar_year % 2 ^ sex  # 判断是正序还是逆序

    birth_day = datetime.datetime(english_year, english_month, english_day, hour, minutes)

    cur_year_of_jieqi = build_jieqi_list(english_year)

    if english_month == 1 and not order:
        pre_year_jieqi = build_jieqi(english_year - 1)[-1]
        cur_year_of_jieqi.insert(0,pre_year_jieqi)

    if english_month ==12 and order:
        next_year_jieqi = build_jieqi(english_year+1)[0]
        cur_year_of_jieqi.append(next_year_jieqi)
    # 防止逆序查找的时候，没有比生日大的节气，故使用最后一个元素初始化
    cur_jieqi = cur_year_of_jieqi[len(cur_year_of_jieqi)-1]
    for i in range(0, len(cur_year_of_jieqi)):
        if cur_year_of_jieqi[i] > birth_day:
            cur_jieqi = (cur_year_of_jieqi[i] if order else cur_year_of_jieqi[i-1])
            break

    print(cur_jieqi)

    delta_diff = (cur_jieqi-birth_day if order else birth_day-cur_jieqi)

    shichen = delta_diff.seconds//60//120

    fenzhong = delta_diff.seconds//60 % 120

    qiyun_shichen = fenzhong

    qiyun_tian = shichen * 10

    qiyun_yue = delta_diff.days % 3

    qiyun_sui = delta_diff.days//3

    new_form = tuple(reversed(modify_qiyun_format(qiyun_shichen,qiyun_tian,qiyun_yue*4,qiyun_sui)))

    print(bazi)

    print(lunar)

    print(new_form)

    print("您出生后 %d年%d月%d日 %d时辰后 起运" % new_form)

    print(get_niunian_list(bazi,order))


def get_niunian_list(bazi:str,order:bool):
    yuezhu = bazi.split("-")[1]
    yuegan = list(yuezhu)[0]
    yuezhi = list(yuezhu)[1]

    return build_liunian_list(yuegan,yuezhi,order)


def build_liunian_list(tiangan:str,dizhi:str,order:bool):
    tianganss:list = tiangans+tiangans
    dizhiss:list = dizhis+dizhis
    if not order:
        tianganss.reverse()
        dizhiss.reverse()
    outcome = []
    begintian = tianganss.index(tiangan)
    begindi = dizhiss.index(dizhi)
    for i in range(1,11):
        outcome.append(tianganss[begintian+i]+''+dizhiss[begindi+i])

    return outcome


def modify_qiyun_format(shichen,tian,yue,sui):

    print(shichen,tian,yue,sui)
    tian += shichen//12

    shichen = shichen % 12

    yue += tian//30

    tian = tian % 30

    sui += yue//12

    yue = yue % 12

    return shichen,tian ,yue ,sui



