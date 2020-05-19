# [CoolNERTool](https://github.com/425776024/CoolNERTool)

Chrome浏览器端端NER实体标注工具，基于Vue + python的fastAPI
- 1.可多人协作共同标注（内网）
- 2.支持模型预标注：读取/写入文件完全一致
- 3.```static/write ```下的是NER数据文件（给出案例），可自己修改
- 4.可以拿模型预测的BIO数据作为输入
- 5.可在线编辑标注文字
- 6.```可以对NER数据做简单的数据增强```（配置config.json中的true/false，会以3.中的NER数据文件目录为基础数据）


## 配置 config
编辑 `/config.json`内含有详细案例，和描述
```json
{
  "descrip_config": {
    "tag_name": "标签，标签展示名称",
    "tag_color_mapping": "tag的展示颜色",
    "augument": "【是否】开启NER数据增强",
    "augument_size": "每条数据最多增强多少条",
    "write_data_path": "用于【标注的数据】的路径",
    "augument_data_path": "用于给标注的数据，【做增强的输出路径】（确保此时标注路径下文件有标注了，不是全O）"
  },
  "config": {
    "tag_name": [
      ["O","0清除"],
      ["Cause","Cause原因"],
      ["Effect","Effect结果"],
      ["CauseEffect","CauseEffect既是原因又是结果"],
      ["T","因果触发词"]
    ],
    "tag_color_mapping": {
      "O": "black",
      "Cause": "#FF0000",
      "Effect": "#0000FF",
      "CauseEffect": "#ffa500",
      "T": "#0ff10f"
    },
    "augument" : true,
    "augument_size" : 3,
    "write_data_path" : "write",
    "augument_data_path" : "augument_write"
  }
}
```
## 运行 run
```shell
pip install requirements.txt
```
```shell
python run.py
```
## 主界面
![](img/home.png)

## 标注界面
- 1.选择上排按钮，点击选择标签
- 2.对中排文字，选择NER实体，点击【选择头一个字和尾一个字】，实体会对应高亮
- 3.无需手动保存，时时自动同步到 配置的输出目录下
![](img/help_img.png)



## 使用说明
运行后查看首页的[使用帮助]链接