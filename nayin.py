from astral.sun import sun

import ganzhi
import sxtwl
import json
import metaphysic
import datetime
import re
import astral
import pytz

nayin = ["海中金", "炉中火", "大林木", "路旁土", "剑锋金", "山头火", "涧下水", "城头土", "白蜡金", "杨柳木", "泉中水", "屋上土", "霹雳火", "松柏木", "长流水",
         "沙中金", "山下火", "平地木", "壁上土", "金箔金", "佛灯火", "天河水", "大驿土", "钗钏金", "桑柘木", "大溪水", "沙中土", "天上火", "石榴木", "大海水"]
tiangans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhis = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
        "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九",
       "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

# 节气名称组 每个节气每个月2个，立春从2月份开始全。第一个为节，第二中气
name_Arr = ["立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
            "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
            "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
            "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"]


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
    file = open("jieqi.txt", 'r', encoding='utf-8')
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



if __name__ == '__main__':
    # print(find_nayin("戊午"))
    build_Dayun(1989, 8, 16, 21, 56, 0)
    location_XiChong = astral.LocationInfo('Shijiazhuang', 'China', 'Asia/Shanghai',34.16,108.91)
    print(location_XiChong.timezone)
    s = sun(location_XiChong.observer, date=datetime.date(1987, 6, 18))
    print(s.get("noon"))