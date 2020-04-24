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