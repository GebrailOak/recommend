#-*- coding: utf-8 -*-
# @Time    : 2018/4/2 15:15
# @Author  : Z
# @Email   : S
# @File    : 10.1CTR.py
#1.导入数据并进行简单的数据探索
import os
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
data_path = os.path.join(".", "train_small.csv")
import pandas as pd
ctr_data1 = pd.read_csv(data_path)
print(ctr_data1.shape)
# print ctr_data.head()
# print ctr_data.describe()
print (ctr_data1.columns)
print ("="*100)
training_Set=ctr_data1.drop(['id','site_id', 'app_id', 'device_id', 'device_ip', 'site_domain',
                  'site_category', 'app_domain', 'app_category', 'device_model'], axis=1)
ctr_data=training_Set.values
#2.对数据进行处理和分析
from sklearn.model_selection import train_test_split
X=ctr_data[:,1:]
print (X.shape)
y=ctr_data[:,0]
print (y.shape)
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.22,random_state=33)
print (X_train.shape)
print (y_train.shape)
# #3.引入机器学习算法
grd = GradientBoostingClassifier(n_estimators=10)
from sklearn.preprocessing import OneHotEncoder
# grd_enc = OneHotEncoder(categories='auto')
#独热编码
grd_enc = OneHotEncoder()
lr=LogisticRegression(C=0.1, penalty= 'l2',solver="lbfgs",max_iter=1000)
grd.fit(X_train, y_train)
grd_enc.fit(grd.apply(X_train)[:,:,0])

# lr=LogisticRegression()
#           0       0.83      1.00      0.91     18240
#           1       0.00      0.00      0.00      3760
#
# avg / total       0.69      0.83      0.75     22000
lr.fit(grd_enc.transform(grd.apply(X_train)[:,:,0]), y_train)
# lr.fit(X_train,y_train)
# #4.模型预测
# y_pred=lr.predict(X_test)
y_pred = lr.predict_proba(grd_enc.transform(grd.apply(X_test)[:, :, 0]))[:, 1]
print (y_pred)
# #5.模型校验
print( "train set score",lr.score(grd_enc.transform(grd.apply(X_train)[:,:,0]),y_train))
print ("test set score" ,lr.score(grd_enc.transform(grd.apply(X_test)[:,:,0]),y_test))
# from sklearn.metrics import confusion_matrix
# print( confusion_matrix(y_test,y_pred))
# from sklearn.metrics import classification_report
# print( classification_report(y_test,y_pred))
# #6.保存模型
from sklearn.externals import joblib
# joblib.dump(lr,filename="Ctr_Predict.pkl")
# #8.按照要求写入对应的csv文件
import numpy as np
import pandas as pd
ctr_data2=pd.read_csv("test.csv")
ctr_data3=ctr_data2.drop(['click','site_id', 'app_id', 'device_id', 'device_ip', 'site_domain',
                  'site_category', 'app_domain', 'app_category', 'device_model'], axis=1)
print( ctr_data3)
ids=ctr_data3.values[0:,0]
print("ids is:",ids)
y_pred_test=lr.predict(ctr_data3)
# print("crt3",ctr_data3.values[0:,1:])
# # print ids
submit=np.concatenate((ids.reshape(len(ids),1),y_pred_test.reshape(len(y_pred_test),1)),axis=1)
df=pd.DataFrame(submit)
df.to_csv("submit.csv", header=['id', 'click'], index=False)