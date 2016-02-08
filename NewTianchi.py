from FunctionGeneral import *
from FuctionDatabase import *
from FunctionSendMail import *

#网址
home='https://tianchi.aliyun.com'#主页
href='/competition/index.htm?pageIndex='
database_name='Tianchi'
code='utf8'
creat_table_if_not_exist(database_name)

#生成需要检索的url
def generate_url(home,href,i):
    return home+href+str(i)
#    return home+href
#信息检索rule
def find_rule(soup):
    find=soup.find_all('div','list-main')
    return find
#停止提取信息条件
def end_open(find,i):
#    return len(find)==0
    if i==2:
        return True
#产生url_sub,head
def analyze_item(item):
    global home
    temp=item.find('div','main-cont')
    title=temp.find('span','span-1').p['title']
    find_url=home+temp.find('span','span-1').a['href']
    time=temp.find('span','span-4').string
    head='[天池]'+title+' '+time
    return {'url':find_url,'head':head}
#邮件正文，产生body（自定义）
def create_body(url,code='utf8'):
    soup=open_soup(url,code)
    find=soup.find('li','current')
    href=find.a['href']

    url=home+href
    soup=open_soup(url,code)
    find=soup.find_all('div',"detail-right")
    Body='<a href="%s">%s</a>\n'%(url,url)+str(find)

    return Body


#读取网页
i=0
while True:
    i+=1
    url=generate_url(home,href,i)
#提取信息
    soup=open_soup(url)
    find=find_rule(soup)
#停止提取信息
    if end_open(find,i):break
#分析信息
    for item in find:
        temp=analyze_item(item)
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

file=open('Log.txt','a')
file.write(home+'\n')
file.close()