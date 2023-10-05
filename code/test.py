# -*- coding: utf-8 -*-
# @Author  : Lulu Lyu
# @Time    : 2023/9/28 16:09
# @E-mail  :lllyuwork@163.com 

import pprint
# import numpy as np
# import pandas as pd
#
# print('=========')
#
# matri = [[2, 3], [4, 5], [6, 7], [4, 7], [5, 1]]
# print(type(matri))
# list = [element for submar in matri for element in submar]
#
# # list = matri.tolist()
# print(list)
# print('=========')
# df = pd.DataFrame(columns=np.arange(len(list)))
# df.loc[len(df)] = list
# # pprint(df)
# print(df)
# indices = {}
# for index, item in enumerate(list):
#     if item in indices:
#         indices[item].append(index)
#     else:
#         indices[item] = [index]
# print(type(indices))
#
# for key,value in indices.items():
#     print(key,value)
#
# se = pd.Series(list)
# propotionDict = dict(se.value_counts(normalize=True))
# print(propotionDict)

import numpy as np
import random

stra = ['1', 'dd', 'sss', 'fff']
s = np.random.choice(stra)
print('np', type(s))

t = random.choice(stra)
print('random', type(t))
print(t)
# arr = list(range(100))
# print(arr)
# chooseTwo = random.sample(arr, 2)
# a=chooseTwo[0]
# b=chooseTwo[1]
# print(type(a))
# print(b)
