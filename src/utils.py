#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os.path
from config import data_write


class Util:
    def __init__(self):
        self.write_path = data_write
        self.sentence_map = {}
        self.sentence_labeling_map = {}
        self.load_path_data()

    def load_path_data(self):
        for name in os.listdir(self.write_path):
            idx = int(name.split('.')[0])
            f_name = os.path.join(self.write_path, name)
            token_arr, tag_arr = get_txt(f_name, return_token=True)
            sentence = ''.join(token_arr)
            self.sentence_map[idx] = sentence
            self.sentence_labeling_map[idx] = tag_arr

    def get_sentence(self, idx):
        if idx < 0 or idx > len(self.sentence_map) - 1:
            idx = 0
        sentence = self.sentence_map[idx]
        return sentence, self.get_labeling(idx)

    def get_labeling(self, idx):
        return self.sentence_labeling_map[idx]

    def set_labeling_arr(self, idx, lab_arr, senetnce=None):
        self.sentence_labeling_map[idx] = lab_arr
        if senetnce is not None:
            self.sentence_map[idx] = senetnce
        write(self.sentence_map[idx], lab_arr, self.get_path(idx))

    def get_path(self, idx):
        return os.path.join(self.write_path, str(idx) + '.txt')


def get_txt(path, return_token=False):
    with open(path, mode='r') as file:
        tag_arr = []
        token_arr = []
        for line in file.readlines():
            line = line.replace('\n', '')
            line_arr = line.split('\t')
            if len(line_arr) == 2:
                token = line_arr[0]
                tag = line_arr[1]
                tag_arr.append(tag)
                token_arr.append(token)
        if return_token:
            return token_arr, tag_arr
        return tag_arr


def write(sent: list, label_ing: list, path: str):
    with open(path, mode='w') as file:
        for i, lb in enumerate(label_ing):
            token = sent[i]
            tag = label_ing[i]
            file.write(token + '\t' + tag + '\n')
