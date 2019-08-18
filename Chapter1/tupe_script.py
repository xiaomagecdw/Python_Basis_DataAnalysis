#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/19 00:09
# Author : chendaiwu biubiubiu.....
# File : tupe_script.py
# Sofaware : PyCharm

#创建元组
#使用圆括号创建元组
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))

#元组解包
#使用赋值操作符左侧的变量对元组进行解包
one, two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one, two, three))
var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1, var2))

#在变量之间变化彼此的值
var1, var2 = var2, var1
print("Output #99: {} {}".format(var1, var2))


