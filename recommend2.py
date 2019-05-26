#-*- coding: utf-8 -*-
# @Time    : 2019/5/19 21:27
# @Author  : Z
# @Email   : S
# @File    : recommend2.py
#基于物品的协同过滤算法
import math
class ItemBaseCF:
    #初始化数据
    def __init__(self,train_file,test_file):
        self.train_file = train_file
        self.test_file = test_file
        #读取数据
        self.readData()
    #读取数据的方法
    def readData(self):
        #训练集
        self.train = dict()
        for line in open(self.train_file):
            user,item,_,score = line.strip().split(",")
            self.train.setdefault(user,{})
            self.train[user][item] = int(score)
        #测试集
        self.test = dict()
        for line in open(self.test_file):
            user,item,_,score = line.strip().split(",")
            self.test.setdefault(user,{})
            self.test[user][item] = int(score)

#球物品相似度
def similaruity(self):
    #建立物品和物品的同现矩阵
    C = dict()#物品和物品的同现矩阵
    N = dict()#物品被多少个不同的用户购买
    for user,item in self.train.items():
        for i in item.keys():
            N.setdefault(i,0)
            N[i]+=1
            #物品-物品的共现矩阵数据加1
            C.setdefault(i,{})
            for j in item.keys():
                if i == j : continue
                C[i].setdefault(j,0)
                C[i][j] +=1
        #计算物品-物品的相似度
        self.W = dict()
        #遍历物品-物品同现矩阵的所有项
        for i ,related_items in C.item():
            #存放物品间的相似度
            self.W.setdefault(i,{})
            #遍历其他物品的及同现矩阵的值，即分子部分
            for j,cij in related_items():
                #余弦相似度计算
                self.W[i][j] = cij/(math.sqrt(N[i]*N[j]))
                #返回物品相似度
            return self.W



