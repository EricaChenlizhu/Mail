from Functions.FunctionGeneral import *
from Functions.FunctionDatabase import *
from Functions.FunctionSendMail import *
#网址
home='http://customer.cs.ecitic.com'
href='/login/positionAction.do?method=listPositionByPageFromIndex&type=08&url=/login/positionAction&extendUrl=type=08;url=/login/positionAction'
database_name='zhongXing'
code='utf-8'
creat_table_if_not_exist(database_name)

#邮件正文，产生body（自定义）
def create_body(url,code):
    soup=open_soup(url,code)
    Body=str(soup.find('div',"mainConter"))
    return Body

#读取网页
if __name__ == '__main__':
    url=home+href
#提取信息
    soup=open_soup(url,code)
    finds=soup.find_all('tr')
#分析信息
    for item in finds:
        if finds.index(item)==0:continue
        url_sub=home+item.find('a','jobname')['href']
#判断是否为新信息
        if not is_url_exist(database_name,url_sub):
            head='[中信]'+item.find_all('td')[0].string+'|'+item.find_all('td')[1].string
            body=create_body(url_sub,code)
    #发送邮件
            send_time=time.strftime('%y-%m-%d,%H:%M:%S',time.localtime())
            send_mail(head,body)
    #写入数据库
            updata_database(database_name,url_sub,head,body,send_time)

file=open('log.txt','a')
file.write(home+'\n')
file.close()