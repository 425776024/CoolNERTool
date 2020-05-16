#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 19:25
# @Author  : xinfa.jiang
# @Site    : 
# @File    : DataAugmentation_utils.py
# @Software: PyCharm
import os
from collections import defaultdict
import random
from src.config import data_augument_tag_list, ignore_tag_list

'''
给NER数据做数据增强！
'''


def get_random(start, end):
    assert start <= end - 1
    return random.randint(start, end - 1)


class DataAugmentation:
    def __init__(self, dir_name):
        self.ignore_tag_list = ignore_tag_list
        self.data_augument_tag_list = data_augument_tag_list
        self.tag_map = self.get_all_tag_map(dir_name)

    def get_random_ner(self, tag: str):
        assert tag in self.tag_map
        max_size = len(self.tag_map[tag])
        assert max_size > 1
        select_idx = get_random(0, max_size)
        new_sene = self.tag_map[tag][select_idx]
        return new_sene

    def get_all_tag_map(self, dir_name: str):
        '''
        得到目录下全部标注文件的，各种实体，ignore_tag_list 里面的不要
        :param dir_name:
        :return:
        '''
        tag_map = defaultdict(list)
        for name in os.listdir(dir_name):
            file_path = os.path.join(dir_name, name)
            data_iter = self.get_file_data_iter(file_path)
            for char_tag in data_iter:
                t_tag, t_ner_sentence = char_tag[0], char_tag[1]
                if t_tag in self.ignore_tag_list:
                    continue
                tag_map[t_tag].append(t_ner_sentence)
        return tag_map

    def get_file_data_iter(self, file_path: str):
        '''
        NER的BIO标注文本 xxx.txt的file_path，要对它做增强
        :param file_path: 路径path
        :return:
        '''
        with open(file_path, 'r', encoding='utf-8') as r_f:
            pre_tag = ''
            ner_sentence = ''
            for line in r_f:
                t_char, t_label = line.replace('\n', '').split('\t')
                tp_tag = 'O'
                if 'O' != t_label:
                    tp_tag = t_label.split('-')[1]
                if pre_tag == '':
                    pre_tag = tp_tag
                    ner_sentence += t_char
                elif pre_tag == tp_tag:
                    ner_sentence += t_char
                else:
                    yield [pre_tag, ner_sentence]
                    pre_tag = tp_tag
                    ner_sentence = t_char
            if ner_sentence != '':
                yield [pre_tag, ner_sentence]

    def data_augment_one(self, org_data):

        new_data = []
        for di in org_data:
            t_tag, t_ner_sentence = di[0], di[1]
            if t_tag in self.data_augument_tag_list and t_tag in self.tag_map:
                rdm_select_ner = self.get_random_ner(t_tag)
                new_data.append([t_tag, rdm_select_ner])
            else:
                new_data.append([t_tag, t_ner_sentence])
        return new_data

    def data_augment(self, org_data, size=3):
        '''
        对原始数据做增强
        :param org_data:
        :param size: 增强/最多/数量
        :return:
        '''

        new_data = []
        org_sent = ''.join([di[1] for di in org_data])
        for i in range(size):
            o_new_data = self.data_augment_one(org_data)
            new_sent = ''.join([di[1] for di in o_new_data])
            if org_sent != new_sent:
                new_data.append(o_new_data)
        return new_data

    def paser_ner(self, ner_data):
        # 数据还原成NER数组，字数组，标签数组
        sentence_arr = []
        label_arr = []
        for i in range(len(ner_data)):
            for j in range(len(ner_data[i][1])):
                label_arr.append(ner_data[i][0])
                sentence_arr.append(ner_data[i][1][j])
        return sentence_arr, label_arr

    def augment(self, file_name, size=3) -> tuple:
        '''
        对文件做增强，输出文件路径，返回size个增强好的数据对 [sentence_arr, label_arr]
        :param file_name:
        :param size:
        :return:
        '''
        org_data = list(self.get_file_data_iter(file_name))
        new_datas = self.data_augment(org_data, size)
        data_sentence_arr = []
        data_label_arr = []
        for ndi in new_datas:
            sentence_arr, label_arr = self.paser_ner(ndi)
            data_sentence_arr.append(sentence_arr)
            data_label_arr.append(label_arr)
        return data_sentence_arr, data_label_arr
