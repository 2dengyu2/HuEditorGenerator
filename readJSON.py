# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2019-11-01 16:52:34
# @Last Modified by:   Admin
# @Last Modified time: 2019-11-01 18:18:14

import json
import re

pattern = re.compile(r'.json$')


def read(file_name=''):
    if pattern.search(file_name):
        with open(file_name, mode='r', encoding="utf-8") as file:
            return json.loads(file.read())
    else:
        raise IOError(f'期望读取.json结尾的文件名，而不是{file_name}')
