def creat_table_if_not_exist(database_name):
    import sqlite3
    database=sqlite3.connect('%s.db'%database_name)
    cur=database.cursor()
    sql='create table content(url VARCHAR (100),head VARCHAR (100),body MESSAGE_TEXT ,time VARCHAR (30),PRIMARY KEY (url))'
    try:
        cur.execute(sql)
    except:
        pass
    else:
        database.commit()
    cur.close()
    database.close()

def is_url_exist(database_name,url):
    import sqlite3
    database=sqlite3.connect('%s.db'%database_name)
    cur=database.cursor()
    sql='select * from content where url=\'%s\''%url
    result=cur.execute(sql).fetchall()
    if len(result)==0:
        return False
    else:
        return True

def updata_database(database_name,url,head,body,send_time):
    import sqlite3
    database=sqlite3.connect('%s.db'%database_name)
    cur=database.cursor()
    sql='insert into content values(?,?,?,?)'
    cur.execute(sql,(url,head,body,send_time))
    database.commit()
    cur.close()
    database.close()


