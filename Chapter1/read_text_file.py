#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/25 23:30
# Author : chendaiwu biubiubiu.....
# File : read_text_file.py
# Sofaware : PyCharm

import sys

#input_file = sys.argv[1]        #"file_to_read.txt"
input_file = "/Users/chendaiwu/workspace/Python_Basis_DataAnalysis/data/file_to_read.txt"

print("Output #143: ")
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()

print("Output #144: ")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))

