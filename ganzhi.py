#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from Common.BaziCommon import *

def day(english_year,english_month,english_day):
    #旧历的计算
    chinese_years_days = helper_days_list()
    english_days = datetime.date(english_year,english_month,english_day) - datetime.date(1901,1,1)
    english_days = english_days.days  #获取输入日期的天数
    if english_days <50:
        d49 = day_49(english_year,english_month,english_day)
        return d49
    chinese_year_list = helper_year_data_find(english_days,chinese_years_days) #获得年位置 [(31439, 86), 1987, 140]
    print(chinese_year_list)
    change_dict = { '00':29, '01':30, '10':29,'11':30,}
    a = bin(CHINESE_1990_2100[chinese_year_list[1]])
    b = [a[i:i+2] for i in range(0, len(a),2)][2:] #二进制列表
    c = [change_dict[x] if x in change_dict else x for x in b]#十进制列表

    d = [ sum(c[0:i]) for i in range(len(c))] #月份的天数
    chinese_month_list = helper_month_data_find(chinese_year_list[3] ,d) #获得月位置 [118, 4, 5, 23]
    chinese_month_list_2 = chinese_month_list[2]
    b_len= len(b)
    if b_len == 13:
        r = [ (i,b.index(i))  for i in b if i=='10' or i=='11'][0]
        chinese_month_list_2 = chinese_month_list_2-1  if chinese_month_list_2 > r[1]  else chinese_month_list_2

    #天干地支的计算
    chinese_years_days_60 = helper_days_60_list()
    chinese_year_list = helper_year_60_data_find(english_days,chinese_years_days_60) #获得年干支位置[1130, 3, 1904, 60]
    year_60_list = CHINESE_60 + CHINESE_60 +CHINESE_60 + CHINESE_60 + CHINESE_60
    year_60_list = year_60_list [37:37+200] #生成年干支列表
    #print CHINESE_10_1[int(year_60_list[chinese_year_list[1]][0:2])]

    e = bin(CHANGE_1990_2100_24[chinese_year_list[1]])#解析24气节的数据
    e = e[3:]
    f = [ e[i:i+2] for i in range(0, len(e),2)]#去除保留数值
    g = [ f[i] for i in range(2,len(f),2)]
    a1= { '00':'2', '01':'3', '10':'4','11':'5',}
    a2= { '00':'4', '01':'5', '10':'6','11':'7',}
    a3= { '00':'9', '01':'6', '10':'7','11':'8',}
    g_list = [a1[g[0]],a2[g[1]],a2[g[2]],a2[g[3]],a2[g[4]],a3[g[5]],a3[g[6]],a3[g[7]],a3[g[8]],a3[g[9]],a3[g[10]],]#转换为１０进制的列表

    e2 = bin(CHANGE_1990_2100_24[chinese_year_list[1]+1])#获取向前一年的u"小寒",u"大寒"
    e2 = e2[3:]
    f2 = [ e2[i:i+2] for i in range(0, len(e2),2)]
    g2 = [ f2[i] for i in range(0,len(f2),2)]
    g_list = g_list + [a2[g2[0]]] #生成完整的10进制列表
    
    g_list_new = []
    for v in range(11):
        v_day  = datetime.date(chinese_year_list[2],2+v,int(g_list[v])) - datetime.date(chinese_year_list[2],2,int(g_list[0])) 
        g_list_new.append(v_day.days )
    v_day_2  = datetime.date(chinese_year_list[2]+1,1,int(g_list[11])) - datetime.date(chinese_year_list[2],2,int(g_list[0]))
    g_list_new.append(v_day_2.days) #生成月干支天数，数据列表
    chinese_month_days_60  = helper_month_60_data_find(chinese_year_list[3],g_list_new)#获得月干支位置[60, 2, 3, 1]
    
    year_value_key = int(year_60_list[chinese_year_list[1]][0:2]) #年干
    year_value =  year_value_key if year_value_key <= 4 else year_value_key-5 #通过年干支定位月干支列表
    v1 = CHINESE_10_1 + CHINESE_10_1 + CHINESE_10_1
    month_value = 2 +(year_value*2)#获取开始位置的公式
    v2 = v1[month_value:month_value+12] #生成月干
    v3 = CHINESE_12_1[2:] + CHINESE_12_1[0:2]#生成月支，因为一月为u"寅"
    #print v2[chinese_month_days_60[1]] + v3[chinese_month_days_60[1]]
    
    v4 = datetime.date(english_year,english_month,english_day) - datetime.date(1901,2,15) #日干支
    v5 = v4.days%60
    #print CHINESE_10_1[int(CHINESE_60[v5][0:2])] +CHINESE_12_1[int(CHINESE_60[v5][2:4])]
    f1 = str(english_year) + '-' +str(english_month) + '-' +str(english_day)
    f2 = str(chinese_year_list[2]) + '-' + str(chinese_month_list_2) + '-' + str(chinese_month_list[3])
    f3 = CHINESE_10_1[int(year_60_list[chinese_year_list[1]][0:2])]+CHINESE_12_1[int(year_60_list[chinese_year_list[1]][2:4])] + '-' + v2[chinese_month_days_60[1]]+v3[chinese_month_days_60[1]]  + '-' + CHINESE_10_1[int(CHINESE_60[v5][0:2])]+CHINESE_12_1[int(CHINESE_60[v5][2:4])]
    f4 = CHINESE_12_2[int(year_60_list[chinese_year_list[1]][2:4])] #生肖
    f5 = CHINESE_10_1[int(CHINESE_60[v5][0:2])] #日的天干
    print (u'输入:[' +f1+ u']; 输出:[' +f2+ u']; 天干地支:[' +f3+ u']; 生肖:[' +f4 +']')

    
    
    return [f3,f4,f5,f2,english_year]






def helper_days_list():
    """
    构建从1900年至今农历每年有多少天的列表
    :return:
    """
    chinese_years_data =49
    chinese_years_list = [49]
    change_dict = { '00':29, '01':30, '10':29,'11':30}

    for i in CHINESE_1990_2100:
        a = bin(i)
        b = [a[i:i+2] for i in range(0, len(a),2)][2:] #转为二进制的列表 后面的切片，list切片
        c = sum([ int(change_dict[x]) if x in change_dict else int(x) for x in b]) #转为十进制的列表
        chinese_years_data = chinese_years_data + c #得出年初的天数
        chinese_years_list.append(chinese_years_data) #添加进列表
    return chinese_years_list #返回列表

def helper_days_60_list():
    chinese_years_data = 1901
    chinese_years_list = []
    change_dict = { '00':'2', '01':'3', '10':'4','11':'5',}
    
    for t in range(len(CHANGE_1990_2100_24)):
        a = bin(CHANGE_1990_2100_24[t])
        a = a[3:]
        b = [ a[i:i+2] for i in range(0, len(a),2)][2]#转为二进制的列表
        c = int(change_dict[b]) #立春的天数
        english_days = datetime.date(chinese_years_data+t,2,c) - datetime.date(1901,1,1) 
        chinese_years_list.append(english_days.days) #添加进列表
        
    return chinese_years_list #返回列表

def helper_month_60_data_find(value,li):
    chinese_month_data_find = [ (i,li.index(i))  for i in li if i <= value ][-1]
    return [chinese_month_data_find[0],chinese_month_data_find[1],1+ chinese_month_data_find[1],value-chinese_month_data_find[0]+1]
        
def helper_year_60_data_find(value,li):
    chinese_year_data_find = [ (i,li.index(i))  for i in li if i <= value ][-1]
    return [chinese_year_data_find [0],chinese_year_data_find [1],1901+chinese_year_data_find [1],value-chinese_year_data_find[0]]



def helper_month_data_find(value,li):
    chinese_month_data_find = [ (i,li.index(i))  for i in li if i <= value ][-1]
    return [chinese_month_data_find[0],chinese_month_data_find[1],1+ chinese_month_data_find[1],value-chinese_month_data_find[0]+1]

def helper_year_data_find(value,li):
    chinese_year_data_find = [(i, li.index(i)) for i in li if i <= value][-1]
    return [chinese_year_data_find[0], chinese_year_data_find[1], 1901+chinese_year_data_find[1], value-chinese_year_data_find[0]]


def change(chinese_year,chinese_month,chinese_day): 
    CHANGE_MONTHS = { '00':29, '01':30, '10':29,'11':30,}
    chinese_years_days = helper_days_list() #旧历年，初一的天数
    english_year_days = chinese_years_days[chinese_year-1901]
    
    english_month_days = CHINESE_1990_2100[chinese_year-1901]
    a = bin(english_month_days)
    b = [ a[i:i+2] for i in range(0, len(a),2)][2:]
    b_len= len(b)
    if b_len == 13:
        r = [ (i,b.index(i))  for i in b if i=='10' or i=='11'] #判断那个月是闰月
        c = [ CHANGE_MONTHS[x] if x in CHANGE_MONTHS else x for x in b]
        d = [ sum(c[0:i]) for i in range(len(c))]
        if chinese_month<r[0][1]:
            e = d[chinese_month-1]
            english_days = datetime.date(1901,1,1)  + datetime.timedelta (english_year_days + e + chinese_day-1)
            li = english_days.strftime('%Y-%m-%d').split('-')
            print (li)
            return [li]
        elif chinese_month>r[0][1]:
            e = d[chinese_month]
            english_days = datetime.date(1901,1,1)  + datetime.timedelta (english_year_days + e + chinese_day-1)
            li = english_days.strftime('%Y-%m-%d').split('-')
            print (li)
            return [li]
        else:
            e1 = d[chinese_month-1]
            english_days_1 = datetime.date(1901,1,1)  + datetime.timedelta (english_year_days + e1 + chinese_day-1)
            li1 = english_days_1.strftime('%Y-%m-%d').split('-')
            e2 = d[chinese_month]
            english_days_2 = datetime.date(1901,1,1)  + datetime.timedelta (english_year_days + e2 + chinese_day-1)
            li2 = english_days_2.strftime('%Y-%m-%d').split('-')
            print ([li1, li2])
            return [li1, li2]
    else:
        c = [ CHANGE_MONTHS[x] if x in CHANGE_MONTHS else x for x in b]
        d = [ sum(c[0:i]) for i in range(len(c))][chinese_month-1]
        english_days = datetime.date(1901,1,1)  + datetime.timedelta (english_year_days + d + chinese_day-1)
        li = english_days.strftime('%Y-%m-%d').split('-')
        print ([li])
        return [li]

def day_49(english_year,english_month,english_day):
    english_days = datetime.date(english_year,english_month,english_day) - datetime.date(1901,1,1) 
    english_days = english_days.days  #获取输入日期的天数
    chinese_year = '1900'
    chinese_month = '12' if english_days>18 else '11' 
    chinese_day = english_days+11 if chinese_month=='11' else english_days-18
    #print chinese_year +'-' + chinese_month +'-' + str(chinese_day)
    
    chinese_year_60 = '0600' if english_days<34 else '0701'  #庚子 '辛丑'
    chinese_month_60 = u'戊子' if english_days<6 else (u'乙丑' if english_days<34 else u'庚寅' )
    
    v4 = datetime.date(english_year,english_month,english_day) - datetime.date(1900,12,17) #日干支
    v5 = v4.days%60
    
    f1 = str(english_year) + '-' +str(english_month) + '-' +str(english_day)
    f2 =  chinese_year +'-' + chinese_month +'-' + str(chinese_day)
    a = CHINESE_10_1[int(chinese_year_60[0:2])]+CHINESE_12_1[int(chinese_year_60[2:4])]
    c = CHINESE_10_1[int(CHINESE_60[v5][0:2])]+CHINESE_12_1[int(CHINESE_60[v5][2:4])]
    
    f3 = a  + '-' + chinese_month_60 + '-' + c
    f4 = f4 = CHINESE_12_2[int(CHINESE_60[v5][2:4])]
    print (u'输入:[' +f1+ u']; 输出:[' +f2+ u']; 天干地支:[' +f3+ u']; 生肖:[' +f4 +']')
    
    return [f1,f2,f3,f4]

def helper_verify_year(english_year):
    errors = 0
    english_year_error = 0
    if english_year <1901:
        errors = errors + 1
        english_year_error = 1
    elif english_year >2100:
        errors = errors + 1
        english_year_error = 2
    return [english_year_error,errors]

def helper_verify_month(english_month):
    errors = 0
    english_year_error = 0
    if english_month <1:
        errors = errors + 1
        english_year_error =3
    elif english_month >12:
        errors = errors + 1
        english_year_error = 4
    return [english_year_error,errors]

def helper_verify_day(english_year,english_month,english_day):
    a  = (datetime.date(english_year,english_month+1,1) - datetime.date(english_year,english_month,1)).days
    errors = 0
    english_day_error = 0
    if english_day <1:
        errors = errors + 1
        english_day_error =5
    elif english_day >a:
        errors = errors + 1
        english_day_error = 6
    return [english_day_error,errors]

def helper_verify_day_60(chinese_year,chinese_month,chinese_day):
    errors = 0
    chinese_day_error = 0
    
    CHANGE_MONTHS = { '00':29, '01':30, '10':29,'11':30,}
    english_month_days = CHINESE_1990_2100[chinese_year-1901]
    #print english_month_days 
    a = bin(english_month_days)
    b = [ a[i:i+2] for i in range(0, len(a),2)][2:]
    #print b
    b_len= len(b)
    if b_len == 13:
        r = [ (i,b.index(i))  for i in b if i=='10' or i=='11'] #判断那个月是闰月
        c = [ CHANGE_MONTHS[x] if x in CHANGE_MONTHS else x for x in b]
        #d = [ sum(c[0:i]) for i in range(len(c))]
        e = None
        if chinese_month<r[0][1]:
            e = c[chinese_month-1]
        elif chinese_month>r[0][1]:
            e = c[chinese_month]
        else:
            e1 = c[chinese_month-1]
            e2 = c[chinese_month]
            e = max([e1,e2])
            
        #print e
        if chinese_day <1:
            errors = errors + 1
            chinese_day_error =5
        elif chinese_day >e:
            errors = errors + 1
            chinese_day_error = 6
        return [chinese_day_error,errors]
            
    else:
        c = [ CHANGE_MONTHS[x] if x in CHANGE_MONTHS else x for x in b]
        e = c[chinese_month-1]
        if chinese_day <1:
            errors = errors + 1
            chinese_day_error =5
        elif chinese_day >e:
            errors = errors + 1
            chinese_day_error = 6
        return [chinese_day_error,errors]
        

def main():
    a = day(1987,6,18)  # 闰年
    # c = day(1991, 12, 15)
    # b = change(1903,3,4)
    # d = helper_verify_day_60(1984,10,11)


if __name__ == '__main__':
    main()
