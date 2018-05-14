#-*- coding:utf-8 -*-
import os
#使用递归方法对文件进行遍历
def recursionsearch(FilePath):
    #获取当前路径下所有文件
    files=os.listdir(FilePath)
    #使用for循环进项遍历文件夹里所有文件对象
    for file in files:
        #进行路径拼接
        NewfilePath=os.path.join(FilePath,file)
        #通过文件对象路径判断文件对象
        if os.path.isdir(NewfilePath):
            #若为文件夹继续调用方法本身
            recursionsearch(NewfilePath)
        else:
            print('|------{0}'.format(NewfilePath))

            pass
#程序入口
if __name__=='__main__':
    FilePath=input('输入需要检索磁盘位置：>')
    recursionsearch(FilePath)
    print('检索结束....')