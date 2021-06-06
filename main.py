#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import readJSON
import sys
import getopt

data = readJSON.read('data.json')
quote_list = data['famous']  # 主要取自老胡经典的话
before_quote_list = data['before']  # 在老胡名言前面弄点话
after_quote_list = data['after']  # 在老胡名言后面弄点话
bullshit_list = data['bosh']  # 老胡文章主要废话

repeatability = 2

# 名人名言概率(百分比)
quotes_percent = 10
# 换行概率(百分比)
new_paragraph_percent = 10
# 缩进符
indent: str = '\t'


def pick(dictionary):
    """
    从字典中选取一段
    :param dictionary: 字典
    """
    global repeatability
    pool = list(dictionary) * repeatability
    while True:
        random.shuffle(pool)
        for item in pool:
            yield item


bullshit = pick(bullshit_list)
quote = pick(quote_list)


def get_quote():
    """
    生成一句追加了前后垫话的名人名言
    :return: 名人名言
    """
    global quote
    _text = next(quote)
    _text = _text.replace('a', random.choice(before_quote_list))
    _text = _text.replace('b', random.choice(after_quote_list))
    return _text


def get_newline():
    """
    换行，另起一段
    :return: 换行符并首行缩进
    """
    _text = '。'
    _text += '\r\n'
    _text += indent
    return _text


def generate(argv):
    """
    生成文本
    :param argv: 参数表
    :return: 生成的文本
    """
    title = '此事'
    repeat_time = 10
    global quotes_percent
    global new_paragraph_percent
    global indent
    hint = 'HuEditorGenerator\n\t -t <title:标题>\n\t -n <repeat_time:重复次数>默认10\n\t ' \
           '-q <quotes_percent:名人名言概率(百分比)>默认10\n\t -p <new_paragraph_percent:换行概率(百分比)>默认10\n\t ' \
           '-i <indent_type:换行后的缩进符类型[0:制表符, 1:空两格, 2:空四格]>默认0'
    try:
        opts, args = getopt.getopt(argv, "ht:n:q:p:i:",
                                   ["title=", "repeat_time=", "quotes_percent=", "new_paragraph_percent=",
                                    "indent_type="])
    except getopt.GetoptError:
        print(hint)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(hint)
            sys.exit()
        elif opt in ("-t", "--title"):
            title = arg
        elif opt in ("-n", "--repeat_time"):
            repeat_time = int(arg)
        elif opt in ("-q", "--quotes_percent"):
            quotes_percent = int(arg)
        elif opt in ("-p", "--new_paragraph_percent"):
            new_paragraph_percent = int(arg)
        elif opt in ("-i", "--indent_type"):
            if opt == '0':
                indent = '\t'
            elif opt == '1':
                indent = '  '
            elif opt == '2':
                indent = '    '
            else:
                raise getopt.GetoptError(f'indent_type可选值为[0:制表符, 1:空两格, 2:空四格]，输入值为：{opt}')
            title = arg

    _new_paragraph_percent = quotes_percent + new_paragraph_percent
    _quotes_percent = quotes_percent
    _article = indent
    for idx in range(repeat_time):
        _paragraph = ''
        _disabled_newline = True
        while len(_paragraph) < 100:
            rand = random.randint(0, 100)
            if not _disabled_newline and rand < _new_paragraph_percent:
                # 至少执行一次再换行
                _text = get_newline()
                _disabled_newline = True
            elif rand < _quotes_percent:
                _text = get_quote()
                _disabled_newline = False
            else:
                _text = next(bullshit)
                _disabled_newline = False
            _paragraph += _text
        _paragraph = _paragraph.replace('x', title).replace('。。', '。').replace('，。', '。')
        _article += _paragraph
    return _article


if __name__ == '__main__':
    s_article = generate(sys.argv[1:])
    print(s_article)
