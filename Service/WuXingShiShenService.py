#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# from Common.BaziCommon import *
# import Service.WuXingService as Service
#
#
#
# def findtiangan(temp: str):
#     return wuxingDicForTiangan[temp]
#
#
# def wuxinshishen(bazi: str):
#     canggan = Service.findCanggan(bazi)
#     canganlist = canggan.split("#")
#     rizhu = canganlist[2].split("-")[0]
#     tianlist = []
#     canlist = []
#     tiandict = {}
#     didict = {}
#     # for zhu in canganlist:
#     for i in range(0, 4):
#         templist = canganlist[i].split("-")
#         if len(templist) > 1:
#             shikey = shishen(rizhu, templist[0])
#             tianlist.append(shikey)
#             for di in list(templist[1]):
#                 shikey = shishen(rizhu, di)
#                 canlist.append(shikey)
#     tianlist.remove(tianlist[2])
#     return tianlist, canlist, canggan,
#
#
# def shishen(rizhu: str, zhu: str):
#     rizhuvalue = wuxingDicForTiangan1.get(rizhu)
#     zhuvalue = wuxingDicForTiangan1.get(zhu)
#     isTong = None
#     if rizhuvalue is not None and zhuvalue is not None:
#         isTong = list(rizhuvalue)[0] == list(zhuvalue)[0]
#         rizhutemp = list(rizhuvalue)[1]
#         zhutemp = list(zhuvalue)[1]
#         rizhuint = None
#         zhuint = None
#         for i, value in enumerate(wuxing):
#             if rizhutemp == value:
#                 rizhuint = i
#             if zhutemp == value:
#                 zhuint = i
#         value = None
#         if rizhuint is not None and zhu is not None:
#             if rizhuint - zhuint < -2:
#                 value = rizhuint - zhuint + 5
#             elif rizhuint - zhuint > 2:
#                 value = rizhuint - zhuint - 5
#             else:
#                 value = rizhuint - zhuint
#         return jundeShishen(value, isTong)
#     else:
#         return None
#
#
# def jundeShishen(value: int, isTong: bool):
#     outcome = ""
#     if value == 0:
#         if isTong is True:
#             outcome = "比肩"
#         else:
#             outcome = "劫财"
#     if value == 1:
#         if isTong is True:
#             outcome = "偏印"
#         else:
#             outcome = "正印"
#     if value == 2:
#         if isTong is True:
#             outcome = "七杀"
#         else:
#             outcome = "正官"
#     if value == -1:
#         if isTong is True:
#             outcome = "食神"
#         else:
#             outcome = "伤官"
#     if value == -2:
#         if isTong is True:
#             outcome = "偏财"
#         else:
#             outcome = "正财"
#     return outcome
#
#
# if __name__ == '__main__':
#     t = findCanggan("辛丑-戊戌-癸未-壬戌")
#     print(t)
#     # print(shishen('丙', '壬'))
#     print(wuxinshishen("辛丑-戊戌-癸未-壬戌"))
#
