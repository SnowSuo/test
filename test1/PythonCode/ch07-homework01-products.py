#-*- coding:utf-8 -*-
'''
    ch07-zuoye01.py
    ===========================
    商品信息添加
    
    @copuright: Chinasoft International·ETC
    @author: suoyonggang
    @date: 2018-04-16

'''
import time
import sys
#步骤一：声明一个商品列表，用来存放商品
#步骤二：声明一个商品信息字典，存放商品详细信息
produts=[]
#步骤三：定义一个函数用来添加商品信息
#商品属性：商品编号pid，商品名称pname，商品价格pprice，商品销量psale
'''
    @name:addproduct
    @argv:str,str,float,int
    @return:none
    @date:2018-04-16
'''
def addproduct(pid,pname,pprice,psale):
    produt={}
    #将每个商品属性添加到字典中
    produt['pid']=pid
    produt['pname']=pname
    produt['pprice']=pprice
    produt['psale']=psale
    #将商品添加到商品列表中
    produts.append(produt)
    return True

#步骤四：定义一个函数将商品数据输出
'''
    @name:showproduct
    @argv:
    @return:none
    @date:2018-04-16
'''
def showproduct():
    print('............所有商品信息{0}..............'.format(len(produts)))
    
    #使用for循环遍历列表中元素
    for p in produts:
        #商品信息输出
        print('商品编号: %s'%(p['pid']))
        print('商品名称: %s'%(p['pname']))
        print('商品价格: %d'%(p['pprice']))
        print('商品销量: %d'%(p['psale']))
        print('#'*30)
    pass
pass
#程序脚本输入
if __name__ =='__main__':
    #调用addproduct函数添加商品信息
    #添加商品
    while True:
        pid=time.strftime('%Y%m%d%H%M%S', time.localtime())
        pname=input('输入商品名称：>-')
        pprice=int(input('输入商品价格：>-'))
        psale=int(input('输入商品销量：>-'))
        flag=addproduct(pid,pname,pprice,psale)
        if flag:
            print('商品{0}添加成功'.format(pid))
            print('#'*30)
        else:
            print('添加失败！')
        pass
        choice=input('是否继续添加商品(y/n)')
        if choice.lower()=='y':
            continue
        else:
            #调用商品输出函数，显示商品信息
            showproduct()
            sys.exit()

    
