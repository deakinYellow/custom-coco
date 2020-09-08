# coding=utf-8

# 生成包含图片路径的txt文件
# 输入参数图像路径

import csv
import os, sys
import  shutil
import time
import datetime
import argparse

from glob import glob
from PIL import Image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--images_src_path", type=str, default="data/", help="path to src images")
    parser.add_argument("--saved_txt_name", type=str, default="images_path.txt", help="name for images paths txt file")
    #　保存参数操作对象
    params_opt = parser.parse_args()  
    print(params_opt)

    #生成TXT文件
    saved_txt_name = params_opt.saved_txt_name

    print("saved txt_file_name: {}".format( saved_txt_name   ) )

    fp = open( saved_txt_name , 'w')

    """
    for i in range( 10 ) :
        fp.write(str(i) + '.txt' )
        fp.write('\n')
    """
    #new_dir = "/media/deakin/b97f0b66-decd-496e-bfdc-0d01fc70d04d/DL/datasets/finger-recognition/datasets/SDU_CP/images/"
    #复制到新的目录
    #shutil.copy( file_path, new_dir + filename )

    #遍历目录下的所有文件，将图片路径写入txt文件
    for parent, dirs, file_names in os.walk( params_opt.images_src_path ,  followlinks=True ):
        # 遍历文件夹
        """
        print("#######dir list#######")
        for dir in dirs:
            print(dir)
        print("#######dir list#######")
        """
        #遍历所有文件
        for file_name in file_names:
            file_path = os.path.join( parent, file_name )
            #print('文件名: {}'.format(  file_name ) )
            print('full path : {}'.format(  file_path ) )
            # 将文件完整路径写入txt文件
            fp.write( file_path   )
            fp.write('\n')

    # 写入完成
    print("一共写入{}条数据, 保存在文件{}".format( file_names.__len__()  ,  saved_txt_name  ) )


