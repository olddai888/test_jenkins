import json


# 读取文件方法
def read_json(filename):
    # 文件路径
    filepath = '../data/' + filename
    # 读入json文件
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


# print(read_json('login.json'))
 