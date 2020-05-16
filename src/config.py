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
root_path = os.path.join(root_path, "../")
data_path = os.path.join(root_path, "static")

# json 配置
json_path = os.path.join(root_path, "config.json")
json_config = get_json(json_path)
tag_name = json_config['config']['tag_name']
tag_color_mapping = json_config['config']['tag_color_mapping']

# 读写目录
dpath = json_config['config']['write_data_path']
data_write = os.path.join(data_path, dpath)

# 会被忽略统计/收集的tag
ignore_tag_list = ['O']
# 会被增强的tag
data_augument_tag_list = ['Effect', 'Cause']
augument = json_config['config']['augument']
augument_size = json_config['config']['augument_size']
augument_dpath = json_config['config']['augument_data_path']
augument_data_write = os.path.join(data_path, augument_dpath)

taginfo = [{"name": v[1], "tag": v[0], 'tagcolor': tag_color_mapping[v[0]]} for i, v in enumerate(tag_name)]
