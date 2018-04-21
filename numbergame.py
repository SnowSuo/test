#-*-coding UTF-8 -*-
'''
        guess number game.py
        ============================
        猜数字游戏，有三次机会可供猜取
        @author: SnowSuo
        @date: 2018-04-16

'''
#导入随机数函数模块
import random #调用随机函数
#游戏入口布局
print('----------一起玩个猜数字游戏-------------')
#数字进行整型
temp=int(input('请输入一个数字:>-') )
times=2
#定义数字区间为1-10
a=random.randint(1,10) 
if a<temp:
        print('数字有点大')        
else:
        print('数字有点小')
 #当输入的数字不等于要猜的数字，并且猜数的次数大于0
while temp!=a and times>0:     
        temp=int(input('猜错了，重新输入一个数字吧：>- '))
        times=times-1
        if temp==a:
                print('这么NB,这样都被你猜中了。')
        else:
                if temp>a:
                        print('数字大了你还有'+str(times)+'次机会')
                else:
                        print('数字小了，请重新输入')
        if times<=0:
                print('次数用完')
print('游戏结束') 
 
