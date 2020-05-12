#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Common.BaziCommon import *


def shensha(bazi: str):
    pass


def split_ganzhi(ganzhi: str):
    gan = list(ganzhi)[0]
    zhi = list(ganzhi)[1]
    return gan, zhi


def judge_in_list(ganzhi: str, needList: list):
    if ganzhi in needList:
        return True
    else:
        return False


def judge_lushen(ganzhi: str):
    lu = {'甲寅', '乙卯', '丙巳', '丁午', '戊巳', '己午', '庚申', '辛酉', '壬亥', '癸子'}
    return judge_in_list(ganzhi, lu)


def judge_tianyi(ganzhi: str):
    gan, zhi = split_ganzhi(ganzhi)
    if gan in ('甲戊庚') and zhi in ('丑未') or gan in ('乙己') and zhi in ('申子') or gan in ('丙丁') and \
            zhi in ('酉亥') or gan in ('辛') and zhi in ('寅午') or gan in ('壬癸') and zhi in ('卯巳'):
        return True
    return False


# 又特殊情况 需要特殊处理
def judge_tiande(ganzhi: str, ):
    # 特殊是亥午 和酉寅
    tiande = {'丁寅', '申卯', '壬辰', '巳辛', '亥午', '甲未', '癸申', '丙戌', '乙亥', '巳子', '庚丑', '酉寅'}
    return judge_in_list(ganzhi, tiande)


def judge_yuede(ganzhi: str):
    yuede = {'丙寅', '甲卯', '壬辰', '辛巳', '庚巳', '丙午', '甲未', '壬申', '庚酉', '丙戌', '甲亥', '壬子', '庚丑'}
    return judge_in_list(ganzhi, yuede)


def judge_wenchang(ganzhi: str):
    wenchang = {'甲巳', '乙午', '丙申', '丁酉', '戊申', '己酉', '庚亥', '辛子', '壬寅', '癸卯'}
    return judge_in_list(ganzhi, wenchang)


def judge_taiji(ganzhi: str):
    list(ganzhi)
    taiji = {'甲午', '乙午', '甲子', '乙子', \
             '丙酉', '丁酉', '丙卯', '丁卯', \
             '庚寅', '庚亥', '辛寅', '辛亥', \
             '壬巳', '壬申', '癸巳', '癸申'
             }
    if judge_in_list(ganzhi, taiji):
        return True
    elif list(ganzhi)[0] in '戊己' and list(ganzhi)[1] in '辰戌丑未':
        return True
    else:
        return False


def judge_kuigang(ganzhi: str):
    kuigang = {'壬辰', '庚戌', '庚辰', '戊戌'}
    return judge_in_list(ganzhi, kuigang)


def judge_jinyu(ganzhi: str):
    jinyu = {'甲辰', '乙巳', '戊未', '丙未', '己申', '丁申', '庚戌', '辛亥', '壬丑', '癸寅'}
    return judge_in_list(ganzhi, jinyu)


def judge_guoyin(ganzhi: str):
    guoyin = {'甲戌', '乙亥', '丙丑', '丁寅', '戊丑', '己寅', '庚辰', '辛巳', '壬未', '癸申'}
    return judge_in_list(ganzhi, guoyin)


# 没看懂
def judege_xuetang(ganzhi: str):
    pass


def judge_jiangxing(ganzhi: str):
    jiangxing = {'申子', '子子', '辰子', '午寅', '午午', '午戌', '酉巳', '酉酉', '酉丑', '卯亥', '卯卯', '卯未'}
    return judge_in_list(ganzhi, jiangxing)


def judge_huagai(ganzhi: str):
    huagai = {'辰申', '辰辰', '辰子', '戌戌', '戌寅', '戌午', '丑丑', '丑巳', '丑酉', '未未', '未亥', '未卯'}
    return judge_in_list(ganzhi, huagai)


def judge_yima(ganzhi: str):
    yima = {'寅辰', '寅申', '寅子', '申寅', '申午', '申戌', '巳亥', '巳未', '巳卯', '亥丑', '亥巳', '亥酉'}
    return judge_in_list(ganzhi, yima)


def judge_yangren(ganzhi: str):
    yangren = {'甲卯', '乙辰', '丙午', '丁未', '戊午', '己未', '庚酉', '辛戌', '壬子', '癸丑'}
    return judge_in_list(ganzhi, yangren)


def judge_tianshe(bazi: str):
    bazilist = bazi.split("-")
    yue = list(bazi[1])[1]
    ri = bazilist[2]
    if yue in '寅卯辰' and ri == '戊寅' or yue in '巳午未' and ri == '甲午' or yue in '申酉戌' and ri in ('戊申') \
            or yue in '亥子丑' and ri == '甲子':
        return True
    else:
        return False


def judge_taohua(zhi1: str, zhi2: str):
    if zhi1 in '申子辰' and zhi2 == '酉' or zhi1 in '寅午戌' and zhi2 == '卯' or zhi1 in '巳酉丑' and zhi2 == '午' \
            or zhi1 in '亥卯未' and zhi2 == '子':
        return True
    else:
        return False


# 日支查
def judge_hongyan(ganzhi: str):
    hongyan = {'甲午', '乙午', '丙寅', '丁未', '戊辰', '己辰', '庚戌', '辛酉', '壬子', '癸申'}
    return judge_in_list(ganzhi, hongyan)


def judge_guluan(ganzhi: str):
    guluan = {'甲寅', '乙巳', '丙午', '丁巳', '戊午', '戊申', '辛亥', '壬子'}
    return judge_in_list(ganzhi, guluan)


# 以年支或日支为主
def judge_wangshen(zhi1: str, zhi2: str):
    if zhi1 in '寅午戌' and zhi2 == '巳' or zhi1 in '亥卯未' and zhi2 == '寅' or zhi1 in '巳酉丑' and zhi2 == '申' or zhi1 in '申子辰' and zhi2 == '亥':
        return True
    else:
        return False


def judge_jiesha(zhi1: str, zhi2: str):
    if zhi1 in '申子辰' and zhi2 == '巳' or zhi1 in '亥卯未' and zhi2 == '申' or \
            zhi1 in '寅午戌' and zhi2 == '亥' or zhi1 in '巳酉丑' and zhi2 == '寅':
        return True
    else:
        return False


def judge_zhaisha(zhi1: str, zhi2: str):
    if zhi1 in '申子辰' and zhi2 == '午' or zhi1 in '亥卯未' and zhi2 == '酉' or \
            zhi1 in '寅午戌' and zhi2 == '子' or zhi1 in '巳酉丑' and zhi2 == '卯':
        return True
    else:
        return False


def judge_gucheng(zhi1: str, zhi2: str):
    if zhi1 in '亥子丑' and zhi2 == '寅' or zhi1 in '寅卯辰' and zhi2 == '巳' or \
            zhi1 in '巳午未' and zhi2 == '申' or zhi1 in '申酉戌' and zhi2 == '亥':
        return True
    else:
        return False


def judge_guasu(zhi1: str, zhi2: str):
    if zhi1 in '亥子丑' and zhi2 == '戌' or zhi1 in '寅卯辰' and zhi2 == '丑' or \
            zhi1 in '巳午未' and zhi2 == '辰' or zhi1 in '申酉戌' and zhi2 == '未':
        return True
    else:
        return False


def judge_yinchayangcuo(rizhu: str):
    yinchayangcuo = {'丙子', '丁丑', '戊寅', '辛卯', '壬辰', '癸巳', '丙午', '丁未', '戊申', '辛酉', '壬戌', '癸亥'}
    return judge_in_list(rizhu, yinchayangcuo)


def judge_siwei(yuezhi: str, rizhu: str):
    if yuezhi in '寅卯辰' and rizhu in ('庚申', '辛酉') or yuezhi in '巳午未' and rizhu in ('壬子', '癸亥') or \
            yuezhi in '申酉戌' and rizhu in ('甲寅', '乙卯') or yuezhi in '亥子丑' and rizhu in ('丙午', '丁巳'):
        return True
    else:
        return False


def judge_bazhuan(rizhu: str):
    bazhuan = {'甲寅', '乙卯', '丁未', '戊戌', '己未', '庚申', '辛酉', '癸丑'}
    return judge_in_list(rizhu, bazhuan)


def judege_jiuchou(rizhu: str):
    jiuchou = {'丁酉', '戊子', '戊午', '己卯', '己酉', '辛卯', '辛酉', '壬子', '壬午'}
    return judge_in_list(rizhu, jiuchou)


def judge_kongwang(rizhu: str, zhi: str):
    tian_index = tiangans.index(list(rizhu)[0])
    dizhi_index = dizhis.index(list(rizhu)[1])
    times = 0
    ## 查看需要几个圈
    if tian_index - dizhi_index < 0:
        times = (tian_index + 12 - dizhi_index) // 2
    else:
        times = (tian_index - dizhi_index) // 2

    if times == 0 and zhi in '戌亥' or times == 1 and zhi in '申酉' or times == 2 and zhi in '午未' or \
            times == 3 and zhi in '辰巳' or times == 4 and zhi in '寅卯' or times == 5 and zhi in '子丑':
        return True
    else:
        return False
