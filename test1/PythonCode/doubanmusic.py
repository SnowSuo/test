import re
import requests
import os ,json,csv,xlwt
'正则表达式应用，及re.sub（）替换方法使用'
#创建全局列表用于存放获取数据
data=[]
for i in range(10):
    url='https://music.douban.com/top250?start={}'.format(i*25)
    content=requests.get(url).text
    #创建一个compile对象，供匹配时循环使用
    patern=re.compile('<div.*?pl2.*?href="(.*?)".*?>(.*?)</a>.*?pl.*?>(.*?)</p>.*?rating_nums.*?>(.*?)</span>.*?</td>',re.S|re.M)
    results=re.findall(patern,content)
    #results=patern.findall(content)（或用此处调用方法）
    for result in results:
        url,songs,author,rate=result
        music={}
        music['歌曲地址']=url
        music['歌曲名称']=re.sub('\s','',re.sub('<span.*?>|</span>','',songs))#数据清洗，去掉空格及span标签
        music['歌曲作者']=(re.sub('</a>|<p.*?>','',author)).strip()#去掉头尾换行符，及替换掉a和p标签
        music['歌曲评分']=rate
        #封装至列表对象中
        data.append(music)
print(len(data))
#将数据写入json文件中，持久化存储
#设置json文件的存储路径
dataDir=os.path.join(os.getcwd(),'MusicData')
if not os.path.exists(dataDir):
    os.mkdir(dataDir)
#将数据写入json文件

# with open(dataDir+os.sep+'music.json','a',encoding='utf-8')as jsonfile:#方法一换行输出，以追加方式
#     #使用json中dump快速序列化并写入指定文件
#     for item in data:
#         datas=json.dumps(item,ensure_ascii=False)+'\n'
#         jsonfile.write(datas)
#     print('json文件写入完毕') 


    #方法二：''
with open(dataDir+os.sep+'music1.json','w',encoding='utf-8')as jsonfile:
    #使用json中dump快速序列化并写入指定文件
    json.dump(data,jsonfile,ensure_ascii=False)
    print('json文件写入完毕')


'将数据写入csv文件'
with open(dataDir+os.sep+'music.csv','w',encoding='utf-8',newline='')as csvfile:
    #使用json中dump快速序列化并写入指定文件
    fieldnames=['歌曲地址','歌曲名称','歌曲作者','歌曲评分']
    #keys=[key for key in data[0]]#获取标题
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    print('csv文件写入完毕')
#csv数据读取，注意item为元祖数据类型，使用dict（item）变为字典数据
# with open(dataDir+os.sep+'music.csv','r',encoding='utf-8')as csvfile:
#     #使用json中dump快速序列化并写入指定文件
#     reader=csv.DictReader(csvfile)
#     lstReader=[dict(item) for item in reader]
#     print(lstReader)


'将文件写入xls'
with open(dataDir+os.sep+'music1.json', 'r',encoding='utf-8') as jsonfile:
        # 步骤2：使用json.load()函数获取json文件数据并反序列化列表对象
        data = json.load(jsonfile)
        print(' json文件读取完毕.')
    # 写入excel文件
 # 步骤1：获取工作簿对象workbook
workbook = xlwt.Workbook(encoding='utf-8')
    # 步骤2：获取单页对象sheet
sheet = workbook.add_sheet('豆瓣音乐信息')
    # 步骤3：写入标题行
headers = [k for k in data[0]]
for colIndex in range(len(headers)):
    sheet.write(0, colIndex, headers[colIndex])
    # 步骤4：写入数据内容
contents = [[v for v in item.values()] for item in data]
for rowIndex in range(1, len(contents)+1):
    for colIndex in range(len(headers)):
        sheet.write(rowIndex, colIndex, contents[rowIndex-1][colIndex])
    # 步骤5：工作簿保存
workbook.save(dataDir+os.sep+'music.xls')
print(' excel文件写入完毕.')
    


 

