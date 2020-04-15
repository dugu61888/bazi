#!/usr/bin/env python
# -*- coding: utf-8 -*-

wuxing = ("木", "火", "土", "金", "水")

wuxingDicForTiangan = {
    "甲": "木",
    "乙": "木",
    "丙": "火",
    "丁": "火",
    "戊": "土",
    "己": "土",
    "庚": "金",
    "辛": "金",
    "壬": "水",
    "癸": "水"
}
wuxingDicForDizhi = {
    "亥": "水",
    "子": "水",
    "丑": "土",
    "寅": "木",
    "卯": "木",
    "辰": "土",
    "巳": "火",
    "午": "火",
    "未": "土",
    "申": "金",
    "酉": "金",
    "戌": "土",
}

tiangans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhis = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

yuncheng = ['长生', '沐浴', '冠带', '临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养']


def build_ChangSheng_dic(rizhu: str):
    (_1, _2) = find_shuxing(rizhu)
    index_first = dizhis.index(_1)
    outcome=[]
    if _2:
        outcome = dizhis[index_first::-1] + dizhis[11:index_first:-1]
    else:
        outcome=dizhis[index_first:12] + dizhis[0:index_first]
    return outcome


def find_zhangshang_list(bazi:str):
    '''
    :param bazi:  己巳-甲戌-丙午-癸巳
    :return:  [1,2,3,4]
    '''
    bazilist =  bazi.split("-")
    rizhustr = bazilist[2]
    rizhu = list(rizhustr)[0]
    diganlist = [list(key)[1] for key in bazilist]
    changshenglist = build_ChangSheng_dic(rizhu)
    outcome = [yuncheng[changshenglist.index(index)] for index in diganlist]
    return outcome

def find_shuxing(rizhu: str):
    tiangan_index = tiangans.index(rizhu)  # 判断奇偶数 阴阳性
    wuxingshuxing = wuxingDicForTiangan.get(rizhu)  # 五行属性
    wuxin_index = wuxing.index(wuxingshuxing)
    t = ()
    if wuxingshuxing == '火':
        t = (wuxing[wuxin_index - 1], wuxing[wuxin_index + 2])
    elif wuxingshuxing in ('土', '金'):
        t = (wuxing[wuxin_index - 2], wuxing[wuxin_index + 1])
    else:
        t = (wuxing[wuxin_index - 1], wuxing[wuxin_index + 1 if wuxin_index + 1 < 5 else wuxin_index + 1-5])
    first_shuxing = ''
    if (tiangan_index % 2 == 0):
        # 顺排 并且 地支生天干找到开始的元素
        first_shuxing = judge_first_element(t[0],True)
    else:
        first_shuxing = judge_first_element(t[1],False)
    return first_shuxing,tiangan_index%2

def judge_first_element(element: str, isOrder: bool):
    outcome = ''
    for key, value in wuxingDicForDizhi.items():
        if value == element and isOrder:
            outcome = key
            break
        elif value == element and not isOrder:
            isOrder = True
            continue
    return outcome


if __name__ == '__main__':
    for key in tiangans:
        k = build_ChangSheng_dic(key)
        print(k)
    outcome = find_zhangshang_list('壬申-癸丑-丙申-癸巳')
    print(outcome)
