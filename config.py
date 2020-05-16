#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 9:44 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os
from src.load_json import get_json

root_path = os.path.dirname(__file__)
data_path = os.path.join(root_path, "static")
dpath = "write"

# json 配置
json_path = os.path.join(root_path, "info_config.json")
json_config = get_json(json_path)
tag_name = json_config['config']['tag_name']
tag_color_mapping = json_config['config']['tag_color_mapping']

data_write = os.path.join(data_path, dpath)
taginfo = [{"name": v[1], "tag": v[0], 'tagcolor': tag_color_mapping[v[0]]} for i, v in enumerate(tag_name)]
