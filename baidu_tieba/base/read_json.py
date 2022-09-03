# 导包
import json


# 创建获取json数据方法
def read_json(filename):
    # 定义文件路径
    filepath = '../data/' + filename
    # 打开并读取文件
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# print(read_json('tb.json'))
