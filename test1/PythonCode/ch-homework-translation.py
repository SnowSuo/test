#-*-  coding:utf-8 -*-
'''
    =============================
    1.确定URL：http://www.zaixian-fanyi.com/
    2.用户选择菜单 （1）英译汉  （2）汉译英 （3）退出 
    3.请求网址内容并解析 使用浏览器抓包 或 抓包工具抓包，找到json地址。
    4.选择功能后可以 根据输入的单词翻译成对应的语言

    @copyright：Chinasoft international .ETC
    @author：suoyonggang
    @date：2018-05-05

'''
import os
import urllib.request
import sys
import urllib
#定义汉译英选项函数
def zhTOen(url):
    #获取网页内容数据并显示
    response=urllib.request.urlopen(url)
    content=response.read().decode('utf-8')
    print('翻译结果为：'+content)
#定义英译汉选项函数
def enTOzh(url):
    #获取网页内容数据并显示
    response=urllib.request.urlopen(url)
    content=response.read().decode('utf-8')
    print('翻译结果为：'+content)
if __name__=='__main__':
    while True:
        #清屏
        print('=============用户菜单选择================')
        print('1.汉译英')
        print('2.英译汉')
        print('3.退出')
        print('#'*30)
        choice=int(input('用户选择翻译类型选项：'))
        if choice not in range(1,4):
            input('请输入（1-3）选项')
            continue
            pass
        if choice==1:
            #确定网络资源地址
            url1='http://ms.zaixianfanyi.com/v2/Ajax.svc/Translate?appId=TBy4D7rq7Wlyk66tc1C3uasNr0w0tCFPhLmhEgflVUHU*&from=zh-CHS&to=en&text='
            #输入需要翻译的汉子
            words=input('输入需要翻译的汉字：>>>')
            #网址中不能含有中文，需要先编码
            words=urllib.parse.quote(words)
            url=url1+words+'&oncomplete='
           #print(url)
            zhTOen(url)
            
        elif choice==2:
            #确定网络资源地址
            url2='http://ms.zaixianfanyi.com/v2/Ajax.svc/Translate?appId=TBy4D7rq7Wlyk66tc1C3uasNr0w0tCFPhLmhEgflVUHU*&from=en&to=zh-CHS&text='
            #输入需要翻译的单词
            words=input('输入需要翻译的单词：>>>')
            url=url2+words+'&oncomplete='
            enTOzh(url)
        else:
            #接收用户退出选项
            choice=input('你确定要退出系统吗（y/n)\n')
            if choice.lower() == 'y':
                #退出系统
                sys.exit(0)
            else:
                continue
                pass
        pass

    pass