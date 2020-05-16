#!/usr/bin/env python
# -*- coding: utf-8 -*-


import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
from config import dpath, taginfo, tag_color_mapping
from src.utils import Util

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

util = Util()


class Item(BaseModel):
    idx: int
    senetnce: str = None
    label_sen_arr: List[str] = None


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("hello.html", {"request": request, "message": '欢迎使用'})


@app.get('/help')
async def help(request: Request):
    return templates.TemplateResponse("help.html", {"request": request, "message": '使用帮助'})


@app.get('/editfile/{idx}')
async def config(request: Request, idx: int = 0):
    senetnce, label_sen_arr = util.get_sentence(idx)
    data = {'idx': idx,
            "message": '编辑',
            "senetnce": senetnce,
            "updatelablingurl": "updatelabling"
            }

    return templates.TemplateResponse("edit.html", {"data": data, "request": request})


def get_lab_color(label_sen_arr):
    label_sen_arr = [c.split('-')[1] if '-' in c else c for c in label_sen_arr]
    label_color = [tag_color_mapping[c] for c in label_sen_arr]
    return label_color


def get_senetnce_tag_list(label_sen_arr, senetnce_arr):
    idx_list = list(range(len(label_sen_arr)))
    label_color = get_lab_color(label_sen_arr)
    senetnce_tag_list = list(zip(senetnce_arr, label_sen_arr, label_color, idx_list))
    return senetnce_tag_list


@app.get('/getlabeling/{idx}')
async def labeling(request: Request, idx: int = 0):
    senetnce, label_sen_arr = util.get_sentence(idx)
    senetnce_arr = list(senetnce)

    senetnce_tag_list = get_senetnce_tag_list(label_sen_arr, senetnce_arr)

    data = {
        'idx': idx,
        'all_num': len(util.sentence_map),
        'senetnce_tag_list': senetnce_tag_list,
        'dpath': dpath,
        'taginfo': taginfo,
        'tag_color_mapping': tag_color_mapping,
        'labelingurl': 'getlabeling',
        'updatelablingurl': 'updatelabling'
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


@app.put('/updatelabling')
async def submit_labling(item: Item):
    idx = item.idx
    senetnce = None
    if item.label_sen_arr is None and item.senetnce is not None:
        # 更新句子
        senetnce = item.senetnce
        label_sen_arr = ['O'] * len(senetnce)
    else:
        label_sen_arr = item.label_sen_arr

    util.set_labeling_arr(idx, label_sen_arr, senetnce)
    return {
        'status': 'success',
        'labelingurl': 'getlabeling',
        'idx': idx
    }


# 启动命令：
# uvicorn main:app --reload
# or __main__
if __name__ == '__main__':
    templates.env.variable_start_string = '{['
    templates.env.variable_end_string = ']}'
    uvicorn.run(app=app, host="127.0.0.1", port=8080)
