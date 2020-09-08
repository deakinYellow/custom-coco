#!/usr/bin/env python
# coding=utf-8

## 将labelImages软件进行图像标志的xml文件转成coco格式的txt文件

import os
import argparse
import xml.etree.ElementTree as ET
from os import listdir
from os.path import join

#自己数据集有哪些类别写哪些类，按照顺序
classes = ["f_001_01","f_001_02","f_001_03","f_001_04","f_001_05","f_001_06" ]

def convert( size, box ):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

####写入位置标志
def convert_annotation( xml_file_path , txt_file_path  )  :
    print("===image_id", xml_file_path  )

    in_file = open( xml_file_path , encoding = 'utf-8')
    out_file = open( txt_file_path , 'w')

    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write( str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

"""
val_percent = 0.1#测试集占总数据集的比例，默认0.1，如果测试集和训练集已经划分开了，则修改相应代码
#data_path = 'data/excavator/'#在darknet文件夹的相对路径，见github的说明，根据自己需要修改，注意此处也可以用绝对路径

parser = argparse.ArgumentParser()
parser.add_argument("--data_path", default="")
flags = parser.parse_args()
print("data_path:", flags.data_path )

if not os.path.exists('labels/'):
    os.makedirs('labels/')

image_ids = [f for f in os.listdir('Annotations')]#存放XML数据的文件夹

train_file = open('train.txt', 'w')
val_file = open('val.txt', 'w')

for i, image_id in enumerate( image_ids ):
    ### 划分训练集和验证集
    print("image_id: ",  image_id )
    if image_id[-3:] == "xml":#有些时候jpg和xml文件是放在同一文件夹下的，所以要判断一下后缀
        if i < ( len(image_ids) * val_percent ):
            val_file.write('%s\n'%( flags.data_path + image_id[:-3] + 'jpg'))
        else:
            train_file.write('%s\n'%( flags.data_path + image_id[:-3] + 'jpg'))
    ### xml 转 txt
    convert_annotation(image_id[:-4])
train_file.close()
val_file.close()
"""


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--xml_files_path", type=str, default="xml/", help="path for xml files")
    parser.add_argument("--labels_files_path", type=str, default="labels/train/", help="path for coco labels files")

    params_opt = parser.parse_args()

    #if not os.path.exists('labels/'):
    #    os.makedirs('labels/')
    ###开始遍历存放xml 数据的文件夹

    for parent, dirs, file_names in os.walk( params_opt.xml_files_path  ,  followlinks=True ):
        for file_name in file_names:
            file_path = os.path.join(  parent,  file_name )
            print('full path : {}'.format(  file_path ) )
            ### xml 转 txt
            # 判断为 xml 文件才操作
            if( file_name[-3: ] == "xml" ):
                convert_annotation(  file_path,   params_opt.labels_files_path + file_name[:-4] + ".txt"  )

        print("一共写入{}个数据, 保存在目录{}".format( file_names.__len__()  ,  params_opt.labels_files_path  ) )

