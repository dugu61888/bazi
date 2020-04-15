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


class Wuxing:
    def __init__(self, bazi: str):
        self.bazi = bazi
        self.__mu = 0
        self.__huo = 0
        self.__tu = 0
        self.__jin = 0
        self.__shui = 0
        self.dict = self.__calculate(bazi)

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


if __name__ == '__main__':
    a = Wuxing("甲午-甲戌-庚申-辛巳")
    print(a.dict)
    print(Service.getRiZhu("甲午-甲戌-庚申-辛巳"))
    print(a.calculat_shishen("甲午-甲戌-庚申-辛巳"))
    print(a.calculat_shishen("戊辰-庚申-丙申-辛卯"))
