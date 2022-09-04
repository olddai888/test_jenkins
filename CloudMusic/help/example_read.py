# 读取数据
from base.read_json import read_json


def get_data():
    # 使用变量保存数据
    datas = read_json('login.json')
    # 定义空列表
    list_data1 = []
    # 循环遍历数据
    for i in datas.values():
        # 添加数据到列表
        list_data1.append((i['email'], i['password'], i['name']))
    # 返回列表
    return list_data1


print(get_data())


# from base.read_json import read_json
#
#
# def get_data_publish_success():
#     datas = read_json('login.json')
#
#     # 定义空列表
#     list_data1 = []
#     # 循环遍历字典，并将获取到的值写入列表中
#     for i in datas.values():
#         list_data1.append((i['email'], i['password'], i['name']))
#
#     # 返回列表
#     return list_data1
#
#
# print(get_data_publish_success())
