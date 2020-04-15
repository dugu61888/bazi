#!/usr/bin/env python
# -*- coding: utf-8 -*-


dizhi = dict(子='癸', 丑='己癸辛', 寅='甲丙戊', 卯='乙',
             辰='戊乙癸', 巳='丙戊庚', 午='丁己', 未='己丁乙', 申='庚壬戊', 酉='辛', 戌='戊辛丁', 亥='壬甲')

wuxingDicForTiangan = dict(甲="阳木", 乙="阴木", 丙="阳火", 丁="阴火", 戊="阳土", 己="阴土", 庚="阳金", 辛="阴金", 壬="阳水", 癸="阴水")

wuxing = ("木", "火", "土", "金", "水")  


def findCanggan(per: str):
    """
    将地支中的藏干找到
    :param per: 输入的数据 辛丑-戊戌-癸未-壬戌
    :return: 返回 辛-己癸辛#戊-戊辛丁#癸-己丁乙#壬-戊辛丁
    """
    templist = []
    perlist = per.split("-")
    for temp in perlist:
        print((dizhi[list(temp)[1]]) + "-" + list(temp)[0])
        templist.append(list(temp)[0] + "-" + dizhi[list(temp)[1]])
    outcome = '#'.join(templist)
    return outcome


def findtiangan(temp: str):
    return wuxingDicForTiangan[temp]


def wuxinshishen(per: str):
    canggan = findCanggan(per)
    canganlist = canggan.split("#")
    rizhu = canganlist[2].split("-")[0]
    tianlist = []
    canlist = []
    for zhu in canganlist:
        templist = zhu.split("-")
        if len(templist) > 1:
            tianlist.append(shishen(rizhu, templist[0]))
            for di in list(templist[1]):
                canlist.append(shishen(rizhu, di))
    tianlist.remove(tianlist[2])
    return tianlist, canlist,canggan


def shishen(rizhu: str, zhu: str):

    rizhuvalue = wuxingDicForTiangan.get(rizhu)
    zhuvalue = wuxingDicForTiangan.get(zhu)
    isTong = None
    if rizhuvalue is not None and zhuvalue is not None:
        isTong = list(rizhuvalue)[0] == list(zhuvalue)[0]
        rizhutemp =list(rizhuvalue)[1]
        zhutemp =list(zhuvalue)[1]
        rizhuint = None
        zhuint = None
        for i, value in enumerate(wuxing):
            if rizhutemp == value:
                rizhuint = i
            if zhutemp == value:
                zhuint = i
        value = None
        if rizhuint is not None and zhu is not None:
            if rizhuint - zhuint < -2:
               value = rizhuint - zhuint + 5
            elif rizhuint - zhuint > 2:
                value = rizhuint - zhuint - 5
            else:
                value = rizhuint - zhuint
        return jundeShishen(value, isTong)
    else:
        return None

def jundeShishen(value: int, isTong: bool):
    outcome = ""
    if value == 0:
        if isTong is True:
            outcome = "比肩"
        else:
            outcome = "劫财"
    if value == 1:
        if isTong is True:
            outcome = "偏印"
        else:
            outcome = "正印"
    if value == 2:
        if isTong is True:
            outcome = "七杀"
        else:
            outcome = "正官"
    if value == -1:
        if isTong is True:
            outcome = "食神"
        else:
            outcome = "伤官"
    if value == -2:
        if isTong is True:
            outcome = "偏财"
        else:
            outcome = "正财"
    return outcome


if __name__ == '__main__':
    t = findCanggan("辛丑-戊戌-癸未-壬戌")
    print(t)
    # print(shishen('丙', '壬'))
    print(wuxinshishen("辛丑-戊戌-癸未-壬戌"))
