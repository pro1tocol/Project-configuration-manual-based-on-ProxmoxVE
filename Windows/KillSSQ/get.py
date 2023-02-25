# Using csv module (Version Python 3.7)
import pandas as pd
import csv
import re

def get_page_data(page):
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % str(page)
    tb = pd.read_html(url)[0]
    return tb.drop([len(tb)-1])

with open(r'./killssq.csv', 'w', encoding='utf-8-sig', newline='') as f:
    csv.writer(f).writerow(['中奖号码'])

for i in range(0,150):  # 目前149页数据第
    page = i
    df = get_page_data(page)
    columns_to_drop = [0, 1, 3, 4, 5]
    df.drop(df.columns[columns_to_drop], axis=1, inplace=True)
    print(f'正在抓取第{page * len(df)}条记录')
    
    # 针对一列中每个元素处理: 去掉首部的 0，并在每个整数之后加上','
    for index, row in df.iterrows():
        lottery_data = [i for i in re.split(' +', row['中奖号码'].replace([' ' '-'], '').values[0])]
        lottery_data = [i.lstrip("0") + ',' for i in lottery_data]
        df.loc[index, "中奖号码"] = ''.join(lottery_data)

    df.to_csv(r'./killssq.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
    if (page == 149):
        print('总共'+str(page)+'页抓取完成') 


