import requests
import json


# 角色
class Charter:
    def __init__(self, b_name='', b_element='', b_weapon_type='', b_star=''):  # 初始化方法
        self.name = b_name   # Charter类的属性
        self.element = b_element
        self.weapon_type = b_weapon_type
        self.star = b_star

    def append_element(self, e):   # 加入新元素
        self.element += e

    def __str__(self):   #
        return "[{} - {} - {} - {}]".format(self.name, self.element, self.weapon_type, self.star)


# 列表， Charter对象
def clear_charter_data(url, header):
    res = json.loads(requests.get(url, headers=header).content)
    characters = []
    for char in res['data']['list'][0]['list']:
        data_list = json.loads(json.loads(char["ext"])['c_25']['filter']['text'])
        c = Charter()
        c.name = char["title"]
        for data_char in data_list:
            # solve travler has three elements problem
            if data_char.startswith("元素/"):
                c.append_element(data_char.replace('元素/', ''))
            #if data_char.startswith("地区/"):
            #    c.area = data_char.replace('地区/', '')
            if data_char.startswith("星级/"):
                c.star = data_char.replace('星级/', '')
            if data_char.startswith("武器/"):
                c.weapon_type = data_char.replace('武器/', '')

        characters.append(c)
    return characters


# 打开文件
target_url = 'https://api-static.mihoyo.com/common/blackboard/ys_obc/v1/home/content/list?app_sn=ys_obc&channel_id=25'
fake_header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

s = []
for i in clear_charter_data(target_url, fake_header):
    s.append(str(i))

print(s)