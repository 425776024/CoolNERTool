#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 9:34 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : star_web.py
# @Software: PyCharm

from flask import Flask
from flask import render_template, request, redirect, url_for

from src.config import button_dict, title, get_sentence
from src.utils import Util

app = Flask(__name__)

util = Util(get_sentence())


@app.route('/')
def index():
    return redirect("/labeling/0")


@app.route('/labeling/<int:idx>')
def labeling(idx):
    senetnce, label_sen = util.get_sentence(idx)
    return _page('index.html', cur=idx, all_num=util.all_num, text=senetnce, label_sen=label_sen)


@app.route('/submit_labling', methods=("GET", "POST"))
def submit_labling():
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        sub_info = request.values.to_dict()
        lab_text = sub_info['lab_text']

        token_size = sub_info['token_size']
        token_size = int(token_size)

        cur_idx = sub_info['cur_idx']
        cur_idx = int(cur_idx)
        lab_token_arr = lab_text.split(' ')
        lab_token_arr = lab_token_arr[:token_size]
        util._set_labeling_arr(cur_idx, lab_token_arr)
        return redirect('/labeling/' + str(cur_idx))


def _page(page='index.html', **kwargs):
    return render_template(page, title=title, button_dict=button_dict, **kwargs)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='127.0.0.1', port=8080, debug=True)
