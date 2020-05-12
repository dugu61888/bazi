#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Common.BaziCommon import *


def getRiZhu(bazi):
    bazilist = str(bazi).split("-")
    if len(bazilist) > 2:
        return list(bazilist[2])[0]
    else:
        return None


def getYin(str: str):
    index = wuxing.index(str)
    return index - 1 if index is not None else None


def getTianlist(bazi):
    bazilist = str(bazi).split("-")
    outcome = []
    if len(bazilist) <= 0:
        return None
    for temp in bazilist:
        outcome.append(list(temp)[0])
    return outcome


def findCanggan(per: str):
    """
    将地支中的藏干找到
    :param per: 输入的数据 辛丑-戊戌-癸未-壬戌
    :return: 返回 辛-己癸辛#戊-戊辛丁#癸-己丁乙#壬-戊辛丁
    """
    templist = []
    perlist = per.split("-")
    for temp in perlist:
        templist.append(list(temp)[0] + "-" + dizhi[list(temp)[1]])
    outcome = '#'.join(templist)
    return outcome


def getWuXing(bazi):
    bazilist = str(bazi).split("-")
    wuxingList = []
    countForJin = 0
    countForMu = 0
    countForShui = 0
    countForHuo = 0
    countForTu = 0
    for bazi in bazilist:
        wuxingList.append(wuxingDicForTiangan[bazi[0]])
        wuxingList.append(wuxingDicForDizhi[bazi[1]])
    for wuxing in wuxingList:
        if wuxing == "金":
            countForJin = countForJin + 1
        elif wuxing == "木":
            countForMu = countForMu + 1
        elif wuxing == "水":
            countForShui = countForShui + 1
        elif wuxing == "火":
            countForHuo = countForHuo + 1
        else:
            countForTu = countForTu + 1
    scoreForJin = countForJin
    scoreForMu = countForMu
    scoreForShui = countForShui
    scoreForHuo = countForHuo
    scoreForTu = countForTu
    return scoreForJin, scoreForMu, scoreForShui, scoreForHuo, scoreForTu


def findtiangan(temp: str):
    return wuxingDicForTiangan[temp]


def wuxinshishen(bazi: str):
    canggan = findCanggan(bazi)
    canganlist = canggan.split("#")
    rizhu = canganlist[2].split("-")[0]
    tianlist = []
    canlist = []
    tiandict = {}
    didict = {}
    # for zhu in canganlist:
    for i in range(0, 4):
        templist = canganlist[i].split("-")
        if len(templist) > 1:
            shikey = shishen(rizhu, templist[0])
            tianlist.append(shikey)
            for di in list(templist[1]):
                shikey = shishen(rizhu, di)
                canlist.append(shikey)
    tianlist.remove(tianlist[2])
    return tianlist, canlist, canggan,


def shishen(rizhu: str, zhu: str):
    rizhuvalue = wuxingDicForTiangan1.get(rizhu)
    zhuvalue = wuxingDicForTiangan1.get(zhu)
    isTong = None
    if rizhuvalue is not None and zhuvalue is not None:
        isTong = list(rizhuvalue)[0] == list(zhuvalue)[0]
        rizhutemp = list(rizhuvalue)[1]
        zhutemp = list(zhuvalue)[1]
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
    t=findCanggan('己卯-乙亥-癸未-壬戌')
    print(t)