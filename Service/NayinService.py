#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Common.BaziCommon import *

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

