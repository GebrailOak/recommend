#-*- coding: utf-8 -*-
# @Time    : 2019/5/18 22:34
# @Author  : Z
# @Email   : S
# @File    : recommend1.py
import binascii
import os

path_0 = r"D:\python\recommend\data"

path_1 = r"D:\python\recommend"

filelist = os.listdir(path_0)

for files in filelist:

    dir_path = os.path.join(path_0, files)
    # 分离文件名和文件类型
    file_name = os.path.splitext(files)[0]  # 文件名
    file_type = os.path.splitext(files)[1]  # 文件类型

    print(dir_path)
    file_test = open(dir_path, 'r')
    # 将.dat文件转为.csv文件
    new_dir = os.path.join(path_1, str(file_name) + '.csv')

    print(new_dir)

    file_test2 = open(new_dir, 'w')

    for lines in file_test.readlines():
        str_data = ",".join(lines.split('\t'))
        # str_data_new= binascii.b2a_hex(str_data)
        file_test2.write(str_data)
    file_test.close()
    file_test2.close()

