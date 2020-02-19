#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 9:44 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : config.py
# @Software: PyCharm

title = 'NER 命名实体标注工具 1.0'

button_dict = {0: 'O无',
               1: 'P人',
               2: 'ORG组织',
               3: 'LOC地点',
               4: 'COM公司'
               }


color_map={"O":"black",
            "B-P":"blue","I-P":"blue",
            "B-ORG":"green","I-ORG":"green",
            "B-LOC":"DarkTurquoise","I-LOC":"DarkTurquoise",
            "B-COM":"red","I-COM":"red"
            }

def get_sentence():
    sets = ['习近平感谢伊丽莎白二世女王和约翰逊对中方抗击新冠肺炎疫情的慰问。', '习近平指出，英方为我们抗击疫情提供了物资支持，这体现了中英两国和两国人民的友好情谊。']
    return sets
