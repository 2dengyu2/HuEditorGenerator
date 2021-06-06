#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import readJSON

data = readJSON.读JSON文件("d.json")
名人名言 = data["famous"]  # 主要取自老胡经典的话
前面垫话 = data["before"]  # 在老胡名言前面弄点话
后面垫话 = data['after']  # 在老胡名言后面弄点话
废话 = data['bosh']  # 老胡文章主要废话

重复度 = 2

# 名人名言概率(百分比)
quotes_percent = 10
# 换行概率(百分比)
new_paragraph_percent = 10


def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素


下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)


def 来点名人名言():
    global 下一句名人名言
    _text = next(下一句名人名言)
    _text = _text.replace("a", random.choice(前面垫话))
    _text = _text.replace("b", random.choice(后面垫话))
    return _text


def 另起一段():
    _text = "。"
    _text += "\r\n"
    _text += " "
    return _text


if __name__ == "__main__":
    _new_paragraph_percent = quotes_percent + new_paragraph_percent
    _quotes_percent = quotes_percent
    title = input("请输入文章主题: ")
    for idx in range(len(title)):
        text = str()
        while len(text) < 100:
            分支 = random.randint(0, 100)
            if 分支 < _new_paragraph_percent:
                text += 另起一段()
            elif 分支 < _quotes_percent:
                text += 来点名人名言()
            else:
                text += next(下一句废话)
        text = text.replace("x", title).replace("。。", "。").replace("，。", "。")
        print(text)
