#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/20 00:54
# Author : chendaiwu biubiubiu.....
# File : control_flow.py
# Sofaware : PyCharm

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