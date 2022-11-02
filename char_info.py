import requests
import json
# https://api-static.mihoyo.com/common/blackboard/ys_obc/v1/home/content/list?app_sn=ys_obc&channel_id=25
# insert a new line on branch develop
# get resource from website
url = 'https://api-static.mihoyo.com/common/blackboard/ys_obc/v1/home/content/list?app_sn=ys_obc&channel_id=25'
fake_header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

char_info = {}
char_info['element'] = ''

res = json.loads(requests.get(url,headers = fake_header).content)
# recycly get each charter information
for char in res["data"]["list"][0]["list"]:
    # get charter name from resource data
    char_info["char_name"] = char["title"]

    # clean resource data
    data_list = json.loads(json.loads(char["ext"])['c_25']['filter']['text'])
    brg_str = ''
    for data_char in data_list:
        # solve travler has three elements problem
        if data_char.startswith("元素/"):
            brg_str += data_char.replace('元素/','')
            char_info['element'] = brg_str
        if data_char.startswith("地区/"):
                char_info['area'] = data_char.replace('地区/','')
        if data_char.startswith("星级/"):
                char_info['star'] = data_char.replace('星级/','')
        if data_char.startswith("武器/"):
                char_info['weap_type'] = data_char.replace('武器/', '')
    print(char_info)
