# [CoolNERTool](https://github.com/425776024/CoolNERTool)

自行设计的实体标注工具(A NER Labeling Tool , base on web flask)：

- 鼠标滑动选择文本，按键0-4给选中文本标记
- ```static/write ```下的是NER数据文件，可自己修改
- 支持模型预标注：读取/写入文件完全一直
- 可以拿模型预测的BIO数据作为输入

![](img/image.png)

## 运行 run
```shell
pip install Flask==1.1.1
```
```shell
python start_web.py
```

## 配置 config
`编辑 config.py`

## 自定义标注
- 1.修改static/index.js 里面的
```python
color_map={"O":"black",
            "B-P":"#0000FF","I-P":"#00CCFF",
            "B-ORG":"#00FF33","I-ORG":"#009933",
            "B-LOC":"#660099","I-LOC":"#666699"
            }

key_code = {
    48:['O','O'],
    49:['B-P','I-P'],
    50:['B-ORG','I-ORG'],
    51:['B-LOC','I-LOC']
}
```
- 2.修改templates/index.html中的
```html
<a class="sty_button">0（O 清除）</a>
<a class="sty_button">1（P 人物）</a>
<a class="sty_button">2（ORG 组织）</a>
<a class="sty_button">3（LOC 地址）</a>
```