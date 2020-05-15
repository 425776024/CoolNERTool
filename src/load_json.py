#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 14:11
# @Author  : xinfa.jiang
# @Site    : 
# @File    : load_json.py
# @Software: PyCharm

import json


def get_json(path_json: str):
    with open(path_json, encoding='utf-8') as f:
        return json.load(f)
