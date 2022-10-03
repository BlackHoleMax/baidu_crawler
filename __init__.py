import requests
import re
import os
import time


def climb_image(photo_type, photo_num):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    name = photo_type
    num = 0
    num_1 = 0
    num_2 = 0
    x = photo_num
    list_1 = []
    for i in range(int(x)):
        name_1 = os.getcwd()
        name_2 = os.path.join(name_1, 'Pictures')
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + name + '&pn=' + str(i * 30)
        res = requests.get(url, headers=headers)
        htlm_1 = res.content.decode()
        a = re.findall('"objURL":"(.*?)",', htlm_1)
        if not os.path.exists(name_2):
            os.makedirs(name_2)
        for b in a:
            try:
                b_1 = re.findall('https:(.*?)&', b)
                b_2 = ''.join(b_1)
                if b_2 not in list_1:
                    num = num + 1
                    img = requests.get(b)
                    f = open(os.path.join(name_1, 'Pictures', name + str(num) + '.jpg'), 'ab')
                    f.write(img.content)
                    f.close()
                    list_1.append(b_2)
                elif b_2 in list_1:
                    num_1 = num_1 + 1
                    continue
            except Exception as e:
                num_2 = num_2 + 1
                continue
    time.sleep(30)



