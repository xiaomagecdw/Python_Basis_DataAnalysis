#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/31 00:29
# Author : chendaiwu biubiubiu.....
# File : write_csv_file.py
# Sofaware : PyCharm

#写入CSV文件
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = "/Users/chendaiwu/workspace/Python_Basis_DataAnalysis/data/write_text_file.txt"
filewrite = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index - 1):
        filewrite.write(str(my_numbers[index_value])+',')
    else:
        filewrite.write(str(my_numbers[index_value])+'\n')
filewrite.close()
print("Output #147: Output appended to file")