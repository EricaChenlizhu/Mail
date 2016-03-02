from Functions.FunctionGeneral import *
from Functions.FunctionDatabase import *
from Functions.FunctionSendMail import *


#网址
home='http://www.careerdream.org'#主页
href='/index/?query=%E5%AE%9E%E4%B9%A0&cities=%E6%B7%B1%E5%9C%B3&page='
database_name='CareerDream'
code='utf8'
creat_table_if_not_exist(database_name)

#要检验的url产生的rule
def generate_url(home,href,i):
#    return home+href
    return home+href+str(i)
#信息检索rule
def find_rule(soup):
    return soup.find_all('div','conlist')
#停止提取信息条件
def end_open(find,i):
    '''
    if i>n:
        return True
'''
    return len(find)==0
#产生url_sub,head
def analyze_item(item):
    global home
    title=item.a.string
    company=item.find('a','com_name_sub')['title']
    mytime=item.strong.string.split()[1]
    url=home+item.a['href']
    head='[职业信息]'+company+' '+title+' '+mytime
    return {'url':url,'head':head}
#邮件正文，产生body（自定义）
def create_body(url,code='utf8'):
    soup=open_soup(url,code)
    find=soup.find_all('pre')

    Body='<a href="%s">%s</a>\n'%(url,url)
    i=0
    for item in find:
        i+=1
        body=str(item)
        if i==1:
            Body=Body+'<p class="ahead">工作职责</p>'+body+'\n'
        else:
            Body=Body+'<p class="ahead">岗位要求</p>'+body
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
            sent_log('logs')
    #写入数据库
            updata_database(database_name,url_sub,head,body,send_time)


file=open('logs\\log.txt','a')
file.write(home+'\n')
file.close()