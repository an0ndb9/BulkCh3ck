#!/usr/bin/python2

import requests
import re
import os,sys
import unicodedata
import string
from threading import Thread


sys.tracebacklimit = 0

#Cool banner <3

print(""" 

  ____        _ _     _____ _     ____       _    
 |  _ \      | | |   / ____| |   |___ \     | |   
 | |_) |_   _| | | _| |    | |__   __) | ___| | __
 |  _ <| | | | | |/ / |    | '_ \ |__ < / __| |/ /
 | |_) | |_| | |   <| |____| | | |___) | (__|   < 
 |____/ \__,_|_|_|\_\\_____|_| |_|____/ \___|_|\__|
                                                


""" + '  \033[1;32m[*]\033[0m Usage: ./BulkCh3ck.py <Filename>\n')

#Banner Ends !

cookies = {
    '__gads': 'ID=9067097a1da93abb-225b52027fc7004d:T=1619078020:RT=1619078020:R:S=ALNI_Malm36no5ofQ_rfnxu0uYq9dH4RAg', 
    '_omappvp': 'oIYeymPvOFVTR9UHVPU1E2KsohGjHTss549r3yRuY68xsBe8orYlnxoHTY72fJhDnlXNqWUNoAkES4WzbRdWKgeJ3BlJKFFG', 
    '_ga': 'GA1.2.1073461880.1601217239', 
    'cookiebanner-accepted': '1',
    '_gid': 'GA1.2.1218030005.1619185640',
}

headers = {
    'Origin': 'https://www.ipvoid.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Chrome/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://www.ipvoid.com/',
    'Connection': 'keep-alive',
}


def check(i):

        data = [('ip', i),]
        g=requests.post('https://www.ipvoid.com/ip-blacklist-check/', headers=headers, cookies=cookies, data=data)
        string1 = unicodedata.normalize('NFKD', g.text).encode('ascii','ignore')
        r = string1.translate(string.maketrans("\n\t\r", "   "))
        print('  \033[1;32m[+]\033[0m')+ str(i)+ str(re.findall(r'BLACKLISTED \d+\/\d+',str(r)))
        
with open(sys.argv[1]) as f:
    lines = f.readlines()

from multiprocessing import Pool

if __name__ == '__main__':

    p = Pool(10)
    p.map(check, lines)