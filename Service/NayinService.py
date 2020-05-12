#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Common.BaziCommon import *

def find_nayin(name: str):
    tian_index = tiangans.index(list(name)[0])
    dizhi_index = dizhis.index(list(name)[1])
    times = 0
    ## 查看需要几个圈
    if tian_index - dizhi_index < 0:
        times = (tian_index + 12 - dizhi_index) // 2
    else:
        times = (tian_index - dizhi_index) // 2

    #连续两个全都是一样的命
    index = tian_index // 2

    # 连续是5个纳音，所以一圈就是5
    index = index + 5 * times

    return nayin[index]


if __name__ == '__main__':
    print(find_nayin('丙午'))