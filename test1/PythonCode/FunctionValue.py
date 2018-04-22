#-*- coding:utf-8 -*-
'''
    
    ===========================
    使用利用高阶函数实现线型代数一元二次方程求解函数
    @author: SnowSuo
    @date: 2018-04-17
'''
#步骤一：导入模块
import math
'''
    @name：fun
    @argv：float，float float
    @return：
    @date：2018-04-17
'''
#步骤一：定义一个函数
def fun(a,b,c,f):
    #创建一个列表用于存放方程解
    listX=[]
    if a==0:
        print("二次方程a不能为零！")
        return''
    #判断b2-4ac>0
    elif (b**2)-(4*a*c)>0:
        x1=(-b+f(b*b-4*a*c))/(2*a)
        x2=(-b-f(b*b-4*a*c))/(2*a)
        #将求解结果追加到列表中
        listX.append(x1)
        listX.append(x2)
        return listX
    else:
        return '此题无解'
#脚本程序入口
if __name__ =='__main__':
    #调用函数
    a=int(input('输入方程参数a：>-'))
    b=int(input('输入方程参数b：>-'))
    c=int(input('输入方程参数c：>-'))
    #对函数进行传参
    X=fun(a,b,c,math.sqrt)
    print(X)

