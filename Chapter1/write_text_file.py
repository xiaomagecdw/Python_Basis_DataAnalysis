#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/31 00:14
# Author : chendaiwu biubiubiu.....
# File : write_text_file.py
# Sofaware : PyCharm

#写入文件
#写入一个文本文件
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = "/Users/chendaiwu/workspace/Python_Basis_DataAnalysis/data/write_text_file.txt"
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output #146: Output written to file")