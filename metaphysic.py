import datetime
import math
import ganzhi
import wuxingData
import dizhicanggan
from Common.BaziCommon import *


def calculateTime(tianganOfDay, time):  # tiangan%10 : 10
    tianganIndex = (2 * tianganOfDay - 1) % 10
    if time == 23 or time == 0 or time == 24:
        dizhi = dizhis[0]
        dizhiIndex = 0
    else:
        dizhiIndex = time / 2
        if dizhiIndex >= 0.5:
            dizhiIndex = math.ceil(dizhiIndex)
        else:
            dizhiIndex = round(dizhiIndex)
        dizhi = dizhis[dizhiIndex]
    return tiangans[(tianganIndex - 1 + dizhiIndex) % 10] + dizhi


def getShenChenBaZi(year, month, day, time):
    data = ganzhi.day(year, month, day)
    print("data is neeed" + str(data))
    tianganOfDay = data[2]
    tianganOfDaySymbol = tiangans.index(tianganOfDay) + 1
    ganzhiOfTime = calculateTime(tianganOfDaySymbol, time)
    return data[0] + '-' + ganzhiOfTime


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


def main():
    # birthYear = input("please input your birth year: ")
    # birthMonth = input("please input your birth month: ")
    # birthDay = input("please input your birth day: ")
    # birthTime = input("please input your birth time: ")
    # shenchenbazi = getShenChenBaZi(1990, 12, 21, 17)
    shenchenbazi = getShenChenBaZi(1989, 10, 13, 9)
    # shenchenbazi = getShenChenBaZi(
    #     int(birthYear), int(birthMonth), int(birthDay), int(birthTime))
    print("你的生辰八字是: %s" % (shenchenbazi))
    wuxing = getWuXing(shenchenbazi)
    print("您的生辰八字五行指数为  金：%d,木：%d,水：%d,火：%d,土:%d" % (wuxing))
    wushi = dizhicanggan.wuxinshishen(shenchenbazi)

    print("您的天干五行是 " + str(wushi[0]))

    print("您的地支五行是 " + str(wushi[1]))

    minScore = 0
    minIndexes = []
    for index, value in enumerate(wuxing):
        if value == minScore:
            minIndexes.append(index)
    lackingWuxings = []
    for minIndex in minIndexes:
        lackingWuxings.append(wuxingNames[minIndex])
    wuxingCharacters = []
    print(lackingWuxings)
    for lackingWuxing in lackingWuxings:
        lackingWuxingCharacters = wuxingData.wuxingDic.get(lackingWuxing)
        if lackingWuxingCharacters:
            wuxingCharacters.extend(wuxingData.wuxingDic.get(lackingWuxing))
    return wuxingCharacters


if __name__ == '__main__':
    main()
