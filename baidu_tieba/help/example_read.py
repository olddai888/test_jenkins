from base.read_json import read_json


def get_data_publish_success():
    datas = read_json('tb.json')

    # 定义空列表
    list_data1 = []
    # 循环遍历字典，并将获取到的值写入列表中
    for i in datas.values():
        list_data1.append((i['username'], i['password'], i['title'], i['text']))

    # 返回列表
    return list_data1


print(get_data_publish_success())
