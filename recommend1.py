#-*- coding: utf-8 -*-
# @Time    : 2019/5/19 20:44
# @Author  : Z
# @Email   : S
# @File    : recommend1.py
import pandas as pd
import binascii

data= pd.read_csv("item_ratings.csv")
# binascii.b2a_hex()
print(data.head())
