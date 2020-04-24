#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 9:44 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os

title = 'NER 命名实体标注工具 1.0'

root_path = os.path.dirname(__file__)
data_path = os.path.join(root_path, 'static')
dpath = 'write'

data_write = os.path.join(data_path, dpath)
