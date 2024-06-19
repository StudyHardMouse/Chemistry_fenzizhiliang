import requests
import bs4
import re
from itertools import groupby

pa = requests.get('https://baike.baidu.com/item/%E7%9B%B8%E5%AF%B9%E5%8E%9F%E5%AD%90%E8%B4%A8%E9%87%8F%E8%A1%A8/9731404')
soup = bs4.BeautifulSoup(pa.text, features="html.parser")
soup.prettify()

while True:
    try:
        list1 = []
        # creating table
        solar_table = soup.find_all('span')
        for a in solar_table:
            list1.append(a.text)


        def mk(x):
            pattern = r"(?=[A-Z])"
            su = re.split(pattern, x)
            
            return su

        x = str(input('请输入化学式'))
        su = mk(x)
        del su[0] 
        #print(su)
        lk = []
        for sd in su:
            target = sd
            try:
                result = list1.index(target)
                #print("目标元素在列表中的索引为：", result)
                #print(list1[result + 1])
                lk.append(int(list1[result + 1]))
                #print(lk)
            except ValueError:
                rest = [''.join(g) for _, g in groupby(target, str.isalpha)]
                aslk = int(rest[1])
                del rest[1]
                rest.append(aslk)
                #lk.append(rest[0])
                fghd = list1.index(rest[0])
                lk.append((int(list1[fghd + 1])) * int(aslk))
                
                
        print('相对分子质量是：', sum(lk))
    except:
        print('错误')


'''
CaCO3
['Ca', 'C', 'O3']


['O', 3]
'''
