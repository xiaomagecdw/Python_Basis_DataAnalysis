#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/20 00:54
# Author : chendaiwu biubiubiu.....
# File : control_flow.py
# Sofaware : PyCharm

import numpy as np
#if-else
#if-else语句
x = 5
if x > 4 or x != 9:
    print("Output #123: {}".format(x))
else:
    print("Output #124: x is not greater than 4")

#if-elif-else语句
if x > 6:
    print("Output #125: x is greater than six")
elif x > 4 and x == 5:
    print("Output #125: {}".format(x))
else:
    print("Output #125: x is not greater than 4")

#for循环
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', 'Holly', 'Isabel', 'Jenny']
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}

print("Output #126:")
for month in y:
    print("{!s}".format(month))

print("Output #127: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}: {1:s}".format(i, z[i]))

print("Output #128: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))

print("Output #129:")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))


#简化for循环:列表、集合、字典生成式
#使用列表生成式选择特定的行
my_data = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #130 (list comprehension): {}".format(rows_to_keep))

#使用集合生成式在列表中选择出一组唯一的元组
my_data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9)]
set_of_tules1 = {x for x in my_data}
print("Output #131 (set comprehension): {}".format(set_of_tules1))
set_of_tules2 = set(my_data)
print("Output #132 (set function): {}".format(set_of_tules2))

#使用字典生成式选择特定的健-值对
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if value >= 9}
print("Output #133 (dictionary comprehension): {}".format(my_results))

#while
#while循环
print("Output #134:")
x = 0
while x < 11:
    print("{!s}".format(x))
    x += 1

#函数
#计算一些列熟知的均值
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 else float('nan')
my_list = [2, 2, 4, 4, 6, 6, 8, 9]
print("Output #135 (mean): {!s}".format(getMean(my_list)))
print("Output #135 (mean): {!s}".format(np.mean(my_list)))

#异常
#try-except
#计算一系列数值的均值
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)
my_list2 = []
try:
    print("Output #138: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("Output #138 (Error): {}".format(float('nan')))
    print("Output #138 (Error): {}".format(detail))

#try-except-else-finally
#完整形式
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("Output #139 (Error): " + str(float('nan')))
    print("Output #140 (Error): ", detail)
else:
    print("Output #141 (The mean is): ", result)
finally:
    print("Output #142 (Finally): The finally block is executed every time")

















