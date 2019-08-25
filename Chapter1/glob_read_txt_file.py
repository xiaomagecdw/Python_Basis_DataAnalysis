#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Time : 2019/8/25 23:51
# Author : chendaiwu biubiubiu.....
# File : glob_read_txt_file.py
# Sofaware : PyCharm

import glob
import os

print("Output #145: ")
inputPath = "/Users/chendaiwu/workspace/Python_Basis_DataAnalysis/data/"
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='')as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
