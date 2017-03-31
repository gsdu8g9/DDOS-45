from bs4 import BeautifulSoup
import urllib2
import zlib
import sys
import re

header={}
count=0
ip_list=[]

def getHeader(filename):
    fp=open(filename,'r')
    for eachline in fp:
        if(len(eachline)>1):
            name,value=eachline[:-1].split('=',1)
            header[name]=value
    fp.close()

def getIpAddr(url):
    global count
    req=urllib2.Request(url,headers=header)
    page=urllib2.urlopen(req)
    info=page.info()
    if info["Content-Encoding"]=="gzip":
        output=zlib.decompress(page.read(),16+zlib.MAX_WBITS)
    else:
        output=page.read()
    bs=BeautifulSoup(output,'lxml')
    ip_list.extend(bs.find_all(attrs={'data-title':'IP'}))
    for ip in ip_list:
        print ip
        count+=1



def loop(url):
    getIpAddr(url)



def startDdos():
    pass



if __name__=='__main__':
    getHeader(sys.argv[1])
    loop(sys.argv[2])
