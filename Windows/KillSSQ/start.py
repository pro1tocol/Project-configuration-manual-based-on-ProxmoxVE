# Using csv module (Version Python 3.7) 
import time
import csv 
import prettytable  
import random
import itertools
from itertools import chain
from itertools import product
from itertools import combinations

print('\n程序将在10秒后启动, 请放大视窗...')
time.sleep(10) 

csv_file = './killssq.csv' 
reader = csv.reader(open(csv_file, encoding='utf-8'), delimiter=',') 
    # 忽略第一行
next(reader, None)
data_list = list(reader) 

data_rows = len(data_list) 
col_index = 0

vals_red = [] 
vals_blue = [] 
for i in range(data_rows):
    data_2 = data_list[i][0] 

    # RED 模板
    for j in range(6):
        # 使用了int() 方法
        if data_2:
            vals_red.append(int(data_2.strip("").split(',')[j]))	

    # BLUE 模板
    # 使用了int() 方法
    if data_2:
        vals_blue.append(int(data_2.strip("").split(',')[6]))

# 计算 RED 模块出现次数
count_red = {}
for k in vals_red:
    if k in count_red:
        count_red[k] += 1
    else:
        count_red[k] = 1

# 计算 BLUE 模块出现次数
count_blue = {}
for l in vals_blue:
    if l in count_blue:
        count_blue[l] += 1
    else:
        count_blue[l] = 1

#以表格方式从小到大排序打印。
#"RED" 模块
print('\n#!红球出现次数: ') 
tb_red = prettytable.PrettyTable() 
data_red_sort = sorted([[int(k),v] for k,v in count_red.items()],key = lambda x: int(x[0]))

# 将列表转为字典
data_dict = dict((value[0], value[1]) for value in data_red_sort)
for key in data_dict.keys():
    tb_red.add_column(str(key), [data_dict[key]])

print(tb_red) 

# 计算 RED 模块总次数
total_red = 0
for num in count_red.values():
    total_red = total_red + num

# 计算 RED 模块平均值
red_avg  = total_red / 33
red_avg = int(round(red_avg, 0))

# 打印 more_than_avg 列表，其中包含大于（平均值+9）的整数
values_more_than_avg = []
for key,value in data_dict.items():
    if value > red_avg + 9:
        values_more_than_avg.append(key)

# 打印 equal_than_avg 列表，其中包含大于（平均值-9）且小于（平均值+9）的整数
values_equal_than_avg = []
for key,value in data_dict.items():
    if value > red_avg - 9 and value < red_avg + 9:
        values_equal_than_avg.append(key)

# 打印 less_than_avg 列表，其中包含小于（平均值-9）的整数
values_less_than_avg = []
for key,value in data_dict.items():
    if value < red_avg - 9:
        values_less_than_avg.append(key)

print('\n当前红球总次数: ' + str(total_red))
print('\n当前红球平均值是: {}'.format(red_avg))
print('\n高于平均值的红球: ', ','.join(str(x) for x in values_more_than_avg)) 
print('\n接近平均值的红球: ', ','.join(str(x) for x in values_equal_than_avg)) 
print('\n低于平均值的红球: ', ','.join(str(x) for x in values_less_than_avg))
print("\n-------------------------------------------------------------------------------------------------")

print('\n正在统计蓝球数据, 请等待....')
time.sleep(5) 

# "BLUE" 模块
print('\n#!蓝球出现次数: ') 
tb_blue = prettytable.PrettyTable() 
data_blue_sort = sorted([[int(k),v] for k,v in count_blue.items()],key = lambda x: int(x[0]))

# 将列表转为字典
data_dict_blue = dict((value[0], value[1]) for value in data_blue_sort) 
for key in data_dict_blue.keys():
    tb_blue.add_column(str(key), [data_dict_blue[key]])

print(tb_blue)

# 计算 "BLUE" 模块总次数
total_blue = 0
for num in count_blue.values():
    total_blue = total_blue + num

# 计算 "BLUE" 模块平均值
blue_avg  = total_blue / 16
blue_avg = int(round(blue_avg, 0))

# 打印 more_than_avg_blue 列表，其中包含大于（平均值+3）的整数
values_more_than_avg_blue = []
for key,value in data_dict_blue.items():
    if value > blue_avg + 3:
        values_more_than_avg_blue.append(key)

# 打印 equal_than_avg_blue 列表，其中包含大于（平均值-3）且小于（平均值+3）的整数
values_equal_than_avg_blue = []
for key,value in data_dict_blue.items():
    if value > blue_avg - 3 and value < blue_avg + 3:
        values_equal_than_avg_blue.append(key)

# 打印 less_than_avg_blue 列表，其中包含小于（平均值-3）的整数
values_less_than_avg_blue = []
for key,value in data_dict_blue.items():
    if value < blue_avg - 9:
        values_less_than_avg_blue.append(key)


print('\n当前蓝球总次数: ' + str(total_blue))
print('\n当前蓝球平均值是: {}'.format(blue_avg))
print('\n高于平均值的蓝球: ', ','.join(str(x) for x in values_more_than_avg_blue))
print('\n接近平均值的蓝球: ', ','.join(str(x) for x in values_equal_than_avg_blue)) 
print('\n低于平均值的蓝球: ', ','.join(str(x) for x in values_less_than_avg_blue))
print("\n-------------------------------------------------------------------------------------------------")

print('\n正在生成随机数组, 请等待....')
time.sleep(5) 

# RED 模块随机抽取
# 从values_equal_than_avg中随机抽取3个整数
equal_sample = random.sample(values_equal_than_avg, 3)
# 从values_less_than_avg中随机抽取4个整数
less_sample = random.sample(values_less_than_avg, 4)

# Merge and sort numbers
merged_red_list = sorted(equal_sample + less_sample)
print('\n红球数组', *merged_red_list, sep=",")
#----------------------

time.sleep(2)

# BLUE 模块随机抽取
# 从values_equal_than_avg_blue中随机抽取1个整数
equal_sample_blue = random.sample(values_equal_than_avg_blue, 1)
# 从values_less_than_avg_blue中随机抽取1个整数
less_sample_blue = random.sample(values_less_than_avg_blue, 2)

# Merge and sort numbers
merged_blue_list = sorted(less_sample_blue + equal_sample_blue)
print('\n蓝球数组', *merged_blue_list, sep=",")
print("\n-------------------------------------------------------------------------------------------------")

print('\n正在校验随机数组, 请等待....')
time.sleep(5) 

# 将以上抽取的整数连拼成一个字符串
killnumb_data = merged_red_list + merged_blue_list
print('\n整合输出: ', ', '.join(map(str, killnumb_data)))
with open('./killnumb.csv', 'a') as f:
        writer = csv.writer(f)		
        writer.writerow([killnumb_data])

print('\n默认红球(7位)蓝球(3位)')

# 生成六位加一位的新数组
print('\n正在分解为(6+1)数组: ')
time.sleep(10) 

merged_left = itertools.chain(merged_red_list)
merged_right = itertools.chain(merged_blue_list)

combs_left = []
for comb in combinations(merged_left, 6): 
    combs_left.append(comb)

combs_right = []
for comb2 in combinations(merged_right, 1):
    combs_right.append(comb2)
          
#Printing logic  
for left in combs_left:
    for right in combs_right:
        victory = left + right
        time.sleep(0.5)
        print('\n', victory)

        #write the combination to a file
        with open('./allow.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([victory])
print('\n数据已保存')
print('\n请查看当前目录下的killnumb.csv/allow.csv文件 ')