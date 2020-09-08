#!/usr/bin/env python
# coding=utf-8

import os

###生成文件名txt
train_file=open('data/train_VOC/ImageSets/Main/train.txt','w')
#test_file=open('data/test_VOC/ImageSets/Main/test.txt','w')

for _,_,train_files in os.walk('data/train_VOC/JPEGImages'):
    continue

for _,_,test_files in os.walk('data/test_VOC/JPEGImages'):
    continue

for file in train_files:
    train_file.write(file.split('.')[0]+'\n')

#for file in test_files:
#   test_file.write(file.split('.')[0]+'\n')

