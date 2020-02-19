#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 9:57 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : utils.py
# @Software: PyCharm


import os.path


# self.sets_labeling = [''] * len(sentence_arr)
# sets = ['习近平感谢伊丽莎白二世女王和约翰逊对中方抗击新冠肺炎疫情的慰问。', '习近平指出，英方为我们抗击疫情提供了物资支持，这体现了中英两国和两国人民的友好情谊。']

class Util:
    # sets_labeling = [''] * len(sets)
    def __init__(self, sentence_arr):
        self.write_path = 'data/write/'
        self.sentence_arr = sentence_arr
        self.all_num = len(sentence_arr)
        self.sentence_labeling_arr = [[]] * self.all_num
        self.load_labeling()

    def _get_sentence(self, idx):
        sentence = self.sentence_arr[idx]
        senetnce = str(sentence.replace(' ', ''))
        return senetnce

    def get_sentence(self, idx):
        sentence = self.sentence_arr[idx]
        senetnce = str(sentence.replace(' ', ''))
        return senetnce, ' '.join(self.sentence_labeling_arr[idx])

    def load_labeling(self):
        self.sentence_labeling_arr = [[]] * self.all_num
        for i in range(self.all_num):
            self.sentence_labeling_arr[i] = self.get_labeling(i)

    def get_labeling(self, idx):
        if not os.path.isfile(self.get_path(idx)):
            lab_arr = len(self._get_sentence(idx)) * ['O']
            self._set_labeling_arr(idx, lab_arr)
            return lab_arr
        else:
            return get_txt(self.get_path(idx))

    def _set_labeling_arr(self, idx, arr):
        self.sentence_labeling_arr[idx] = arr
        write(self.sentence_arr[idx], self.sentence_labeling_arr[idx], self.get_path(idx))

    def get_path(self, idx):
        return self.write_path + str(idx) + '.txt'


def get_txt(path):
    with open(path, mode='r') as file:
        tag_arr = []
        for line in file.readlines():
            line = line.replace('\n', '')
            line_arr = line.split('\t')
            if len(line_arr) == 2:
                token = line_arr[0]
                tag = line_arr[1]
                tag_arr.append(tag)
        return tag_arr


def write(sent, label_ing, path):
    with open(path, mode='w') as file:
        for i, lb in enumerate(label_ing):
            token = sent[i]
            tag = label_ing[i]
            file.write(token + '\t' + tag + '\n')
