#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Service.WuXingService as Service

tianganfenshu = 60
from functools import reduce

dizhifenshu = {
    "子": {"水": 100},
    "丑": {"土": 60, "水": 20, "金": 20},
    "寅": {"木": 60, "火": 30, "土": 10},
    "卯": {"木": 100},
    "辰": {"土": 60, "木": 20, "水": 20},
    "巳": {"火": 60, "土": 30, "金": 10},
    "午": {"火": 70, "土": 30},
    "未": {"土": 60, "火": 20, "木": 20},
    "申": {"金": 60, "水": 30, "土": 10},
    "酉": {"金": 100},
    "戌": {"土": 60, "金": 20, "火": 20},
    "亥": {"水": 70, "木": 30}
}

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

wuxingDicForTiangan1 = dict(甲="阳木", 乙="阴木", 丙="阳火", 丁="阴火", 戊="阳土", 己="阴土", 庚="阳金", 辛="阴金", 壬="阳水", 癸="阴水")
dizhican = dict(子='癸', 丑='己癸辛', 寅='甲丙戊', 卯='乙',
                辰='戊乙癸', 巳='丙戊庚', 午='丁己', 未='己丁乙', 申='庚壬戊', 酉='辛', 戌='戊辛丁', 亥='壬甲')

zhulist = ["年干", "年支", "月干", "月支", "日主", "日支", "时干", "时支"]

wuxing = ("木", "火", "土", "金", "水")

baZiYinYangDict = {4: '八字纯阳：刚健至极，好动，不利婚姻',
                   3: '八字偏阳：活跃、刚劲',
                   2: '八字均衡：刚柔并济、动静皆宜',
                   1: '八字偏阴：安静、柔韧',
                   0: '含蓄柔顺，好静，逢冲则多动荡'
                   }

class Wuxing:
    def __init__(self, bazi: str):
        self.bazi = bazi
        self.__mu = 0
        self.__huo = 0
        self.__tu = 0
        self.__jin = 0
        self.__shui = 0
        self.dict = self.__calculate(bazi)
        self.total = self.__getTotalScore()

    def __calculate(self, baiz: str):
        balist = baiz.split("-")
        tiandict = {}
        didict = {}
        for i in range(0, 4):
            zhu = list(balist[i])
            tiankey = wuxingDicForTiangan.get(zhu[0])
            fenshu = tianganfenshu if i in (0, 3) else tianganfenshu * 2
            self.__set_value(tiankey, fenshu,
                             tiandict)
            dikeys = dizhifenshu.get(zhu[1])
            for k, v in dikeys.items():
                v = v if i in (0, 2, 3) else v * 2
                self.__set_value(k, v, didict)
        # 若天干在地支无比肩，则分数折半
        for k, v in tiandict.items():
            if didict.get(k) is None or didict.get(k) == 0:
                tiandict[k] = v / 2
        print(tiandict)
        print(didict)
        merger = self.__sum_dict(tiandict, didict)
        return merger

    def __getTotalScore(self):
        sum = 0
        for v in self.dict.values():
            sum += v;
        return sum

    def __sum_dict(self, a, b):
        temp = dict()
        # python3,dict_keys类似set； | 并集
        for key in a.keys() | b.keys():
            temp[key] = sum([d.get(key, 0) for d in (a, b)])
        return temp

    def __set_value(self, key, value, map: dict):
        if map.get(key) is None:
            map.setdefault(key, value)
        else:
            map[key] = map.get(key, 0) + value

    def calculat_shishen(self, bazi: str):
        rizhu = Service.getRiZhu(bazi)
        bazilist = bazi.split("-")
        outcome = dict();
        for i in range(0, 4):
            gan = list(bazilist[i])[0]
            shishen = Service.shishen(rizhu, gan)
            fenshu = tianganfenshu if i in (0, 3) else tianganfenshu * 2
            gandict = dict(十神=shishen, 分数=fenshu, 五行=wuxingDicForTiangan.get(gan))
            outcome[zhulist[i * 2]] = gandict
            zhi = list(bazilist[i])[1]
            cangan = dizhican.get(zhi)
            canganlist = list(cangan)
            zhishishenlist = []
            for item in canganlist:
                shishen = Service.shishen(rizhu, item)
                fenshudict = dizhifenshu.get(zhi)
                key = wuxingDicForTiangan.get(item)
                fenshu = fenshudict.get(key) if i in (0, 2, 3) else fenshudict.get(key) * 2
                zhidict = dict(十神=shishen, 分数=fenshu, 五行=wuxingDicForTiangan.get(item))
                zhishishenlist.append(zhidict)
            outcome[zhulist[i * 2 + 1]] = zhishishenlist
            # 修正分数
        for i in range(0, len(zhulist), 2):
            item = outcome.get(zhulist[i])
            exist = False
            for k in range(1, len(zhulist), 2):
                item2 = outcome.get(zhulist[k])
                for v in item2:
                    if v.get("五行") == item.get("五行"):
                        exist = True
                        break
                if exist:
                    break
            if not exist:
                item['分数'] = item.get('分数') / 2
        return outcome

    def rizhu_shuaiwang(self, bazi: str):
        rizhu = Service.getRiZhu(bazi)
        rizhutype = wuxingDicForTiangan.get(rizhu)
        yinIndex = wuxing.index(rizhutype) - 1
        yintype = wuxing[yinIndex]
        rizhanbi = self.__wuxingZhanbi(rizhutype)
        yinzhanbi = self.__wuxingZhanbi(yintype)
        totalzhbi = rizhanbi + yinzhanbi
        shuaiwang = ""
        if 0 < totalzhbi <= 0.1:
            shuaiwang = "日主极弱"
        elif 0.1 < totalzhbi <= 0.45:
            shuaiwang = "日主偏弱"
        elif 0.45 < totalzhbi <= 0.55:
            shuaiwang = "日主中和"
        elif 0.55 < totalzhbi <= 0.75:
            shuaiwang = "日主偏强"
        elif 0.75 < totalzhbi <= 1:
            shuaiwang = "日主极强"
        return shuaiwang


    def __wuxingZhanbi(self, wuxingType: str):
        fenshu = self.dict.get(wuxingType, 0)
        return fenshu / self.__total




    def baziYinYang(self):
        num = self.baziTianGanYangNum()
        return baZiYinYangDict.get(num, None)

    def baziTianGanYangNum(self):
        tianlist = Service.getTianlist(self.bazi)
        yangnum = 0
        for tian in tianlist:
            wuxingtype = wuxingDicForTiangan1.get(tian)
            if list(wuxingtype)[0] == '阳':
                yangnum += 1
        return yangnum





if __name__ == '__main__':
    a = Wuxing("己卯-乙亥-癸未-壬戌")
    print(a.baziYinYang())
