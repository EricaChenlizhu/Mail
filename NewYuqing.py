from Functions.FunctionGeneral import *
from Functions.FuctionDatabase import *
from Functions.FunctionSendMail import *
#网址
home='http://www.lwxsw.org'#主页
href='/books/0/609/'
database_name='Yuqing'
code='gbk'
creat_table_if_not_exist(database_name)

#生成需要检索的url
def generate_url(home,href,i):
#    return home+href+str(i)
    return home+href
#信息检索rule
def find_rule(soup):
    find=soup.find_all('div','dccss')
    return find
#停止提取信息条件
def end_open(find,i):
#    return len(find)==0
    if i==2:
        return True
#产生url_sub,head
def analyze_item(item):
    global home,href
    try:
        href_sub=item.a['href']
    except:
        return 'error'
    else:
        find_url=home+href+href_sub
        title=item.a.string
        head='[小说]'+'愚情'+' '+title
        return {'url':find_url,'head':head}
#邮件正文，产生body（自定义）
def create_body(url,code='utf8'):
    soup=open_soup(url,code)
    Body=str(soup.find('div',attrs={"id": "content"}))

    return Body


#读取网页
i=0
while True:
    i+=1
    url=generate_url(home,href,i)
#提取信息
    soup=open_soup(url,code)
    find=find_rule(soup)
#停止提取信息
    if end_open(find,i):break
#分析信息
    for item in find:
        temp=analyze_item(item)
        if temp=='error':break
        url_sub=temp['url']
        head=temp['head']
#判断是否为新信息
        if not is_url_exist(database_name,url_sub):
            head=temp['head']
            body=create_body(url_sub,code)
    #发送邮件
            send_time=time.strftime('%y-%m-%d,%H:%M:%S',time.localtime())
            send_mail(head,body)
    #写入数据库
            updata_database(database_name,url_sub,head,body,send_time)

file=open('logs\\log.txt','a')
file.write(home+'\n')
file.close()