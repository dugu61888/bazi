#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Service.WuXingService as Service
from Service.WuXingFenshu import Wuxing

yixiangDict={'木':['强木','漂木','焚木','折木','断木','弱木'],
             '火':['强火','弱火','炽火','熄火','灭火','弱火'],
             '土':['强土','焦土','变土','流土','倾土','弱土'],
             '金':['强金','埋金','沉金','缺金','熔金','弱金'],
             '水':['强水','浊水','缩水','灼水','淤水','弱水']
             }

wuxing = ("木", "火", "土", "金", "水")

wuXingDescribtionDict={
    '强木':'当令或繁盛为强。喜土分力，金雕琢，火泄秀；忌水生木，木加重',
    '弱木':'失令或稀少为弱。喜水生木，木比助；忌土分力，金克害，火泄气',
    '漂木':'水多木漂。喜土制水，忌金助水',
    '焚木':'火多木焚。喜水克火，土泄火；忌木生助，火炽烈',
    '折木':'土重木折，喜水生木，取木制土，忌土加重',
    '断木':'金多木断，喜火制金存木，水泄金生木；忌土助金，金坚锐',
    '强火':'当令或繁盛为强。喜土分力，金雕琢，火泄秀；忌水生木，木加重',
    '弱火':'失令或稀少为弱。喜水生木，木比助；忌土分力，金克害，火泄气',
    '炽火':'水多木漂。喜土制水，忌金助水',
    '晦火':'火多木焚。喜水克火，土泄火；忌木生助，火炽烈',
    '熄火':'土重木折，喜水生木，取木制土，忌土加重',
    '灭火':'金多木断，喜火制金存木，水泄金生木；忌土助金，金坚锐',
    '强土':'当令或繁盛为强。喜水分力，木疏通，金泄秀；忌火生土，土加重',
    '弱土':'失令或稀少为弱。喜火生土，土比助；忌水分力，木克制，金泄气',
    '焦土':'火多土焦。喜水制火，水少取金，忌木助火',
    '变土':'金多土变。喜火制金，水泄金；忌土助金，金坚实',
    '流土':'水多土流。喜火生木，取土为上，忌水加重',
    '倾土':'木多土倾。喜金制木存土，火泄木生土；忌水助木，木繁盛',
    '强金':'当令或繁盛为强。喜木分力，火煅炼，水泄秀；忌土生金，金加重',
    '弱金':'失令或稀少为弱。喜土生金，金比助；忌木分力，火克制，水泄气',
    '埋金':'土多金埋。喜木制土，忌火助土',
    '沉金':'水多金沉。喜土克水，木泄水；忌金助水泛',
    '缺金':'木坚金缺。喜土生金，忌木加重',
    '熔金':'火多金熔。喜水制火存金，土泄火生金；水土少取金比助，忌木助火炽',
    '强水':'当令或繁盛为强。喜火分力，土堤防，木泄秀；忌金生水，水加重',
    '弱水':'失令或稀少为弱。喜金生水，水比助；忌火分力，土克制，木泄气',
    '浊水 ':'金多水浊。喜火制金，火少取木，忌土助金',
    '缩水':'木多水缩。喜火泄木，金制木；忌水生助木繁盛',
    '灼水':'火炎水灼。喜金生水，取水为上，忌火加重',
    '淤水':'土多水淤。喜木克土存水，金泄土生水；忌火助土，土坚实',
}

wuXingXiJiDict={
    '强木':dict(喜='土、金、火',忌='水、木'),
    '弱木':dict(喜='木、水',忌='金、土、火'),
    '漂木':dict(喜='土、火',忌='金、水'),
    '焚木':dict(喜='水、土',忌='火、金'),
    '折木':dict(喜='水、木',忌='土、金'),
    '断木':dict(喜='火、水、木',忌='土、金'),
    '强火':dict(喜='金、水、土',忌='木、火'),
    '弱火':dict(喜='火、木',忌='水、金、土'),
    '炽火':dict(喜='金、土',忌='水、木'),
    '晦火':dict(喜='金、木',忌='土、水'),
    '熄火':dict(喜='火、木',忌='金、土'),
    '灭火':dict(喜='土、木、火',忌='水、金'),
    '强土':dict(喜='水、木、金',忌='火、土'),
    '弱土':dict(喜='土、火',忌='木、水、金'),
    '焦土':dict(喜='水、金',忌='木、火'),
    '变土':dict(喜='火、水',忌='金、木'),
    '流土':dict(喜='火、木',忌='金、水'),
    '倾土':dict(喜='金、火、土',忌='水、木'),
    '强金':dict(喜='木、火、水',忌='土、金'),
    '弱金':dict(喜='金、土',忌='火、木、水'),
    '埋金':dict(喜='木、水',忌='火、土'),
    '沉金':dict(喜='土、木',忌='水、火'),
    '缺金':dict(喜='土、金',忌='木、水'),
    '熔金':dict(喜='水、土、金',忌='火、木'),
    '强水':dict(喜='火、土、木',忌='金、水'),
    '弱水':dict(喜='水、金',忌='土、火、木'),
    '浊水':dict(喜='火、木',忌='土、金'),
    '缩水':dict(喜='火、金',忌='木、土'),
    '灼水':dict(喜='金、水',忌='火、木'),
    '淤水':dict(喜='木、金、水',忌='火、土'),
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



class YiXiang:
    def __init__(self, bazi: str):
        self.__rizhu = Service.getRiZhu(bazi)
        self.__rizhutype = wuxingDicForTiangan.get(self.__rizhu)
        self.__yin = wuxing[Service.getYin(self.__rizhutype)]
        self.__dict = Wuxing(bazi).dict
        self.__total = Wuxing(bazi).total

    def __judgeType(self):
        rilist = yixiangDict.get(self.__rizhutype)
        rifen = self.__dict.get(self.__rizhutype)
        yinfen = self.__dict.get(self.__yin)
        rizhanbi = rifen/self.__total
        yinzhanbi = yinfen/self.__total
        plus1 = wuxing.index(self.__rizhutype) + 1 if wuxing.index(self.__rizhutype) + 1 <len(wuxing) else \
            wuxing.index(self.__rizhutype) + 1-len(wuxing)
        plus1zhanbi = self.__dict.get(wuxing[plus1])/self.__total
        plus2 = wuxing.index(self.__rizhutype) + 2 if wuxing.index(self.__rizhutype) + 2 < len(wuxing) else wuxing.index(
            self.__rizhutype) + 2 - len(wuxing)
        plus2zhanbi = self.__dict.get(wuxing[plus2]) / self.__total
        plus3 = wuxing.index(self.__rizhutype) + 3 if wuxing.index(self.__rizhutype) + 3 < len(wuxing) else wuxing.index(
            self.__rizhutype) + 3 - len(wuxing)
        plus3zhanbi = self.__dict.get(wuxing[plus3]) / self.__total
        if rizhanbi+yinzhanbi > 0.5 and rizhanbi >0.2:
            return rilist[0]
        elif rizhanbi+yinzhanbi > 0.5 and rizhanbi <= 0.2:
            return rilist[1]
        elif rizhanbi+yinzhanbi <= 0.5 and plus1zhanbi >= 0.4:
            return rilist[2]
        elif rizhanbi+yinzhanbi <= 0.5 and plus2zhanbi >= 0.4:
            return rilist[3]
        elif rizhanbi+yinzhanbi <= 0.5 and plus3zhanbi >= 0.4:
            return rilist[4]
        elif rizhanbi+yinzhanbi <= 0.5:
            return rilist[5]
        else:
            return None

    def getXiJiYiXing(self):
        wuxingType = self.__judgeType()
        des = wuXingDescribtionDict.get(wuxingType)
        xiji = wuXingXiJiDict.get(wuxingType)
        outcome = dict()
        outcome.update(name=wuxingType, description=des)
        outcome.update(xiji)
        return outcome

if __name__ == '__main__':
    a = YiXiang("己卯-乙亥-癸未-壬戌")
    outcome = a.getXiJiYiXing()
    print(outcome)

