#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/31 00:39
# Author : chendaiwu biubiubiu.....
# File : Exercises_Script.py
# Sofaware : PyCharm

#1
print("Output #习题第一题：")
list1 = ['apply', 'banana', 'orange']
list2 = ['teacher', 'student', 'classroom']
list3 = ['dog', 'tag', 'cat']
list = list1 + list2 + list3
max_index = len(list)
for i in range(len(list)):
    if i < max_index:
        print("Output #1: {0}:{1}".format(i, list[i]))

print("------------------")

print("Output #习题第二题：")
#2
list1 = ["apply", "teacher", "day"]
list2 = ["one", "two", "three", "four", "five"]
dict1 = {}
for index_value in range(len(list1)):
    if index_value not in dict1:
        dict1[list1[index_value]] = list2[index_value]
for key, value in dict1.items():
    print("Output #2: {0}:{1}".format(key, value))


print("------------------")

print("Output #习题第三题：")
#3
list3 = [['teacher', 'student', 'classroom'], ['apply', 'banana', 'orange'], ['dog', 'tag', 'cat']]
output = ''
for lists in list3:
    max_index = len(lists)
    for i in range(len(lists)):
        if i < (max_index - 1):
            output += str(lists[i])+','
        else:
            output += str(lists[i])+'\n'
print("Output #3: {}".format(output))




