#打开网页，产生soup
def open_soup(url,code='utf8'):
    from urllib import request
    from bs4 import BeautifulSoup as BS
    conn=request.urlopen(url)
    page=conn.read().decode(code)
    soup=BS(page,'html.parser')
    return soup

