#coding=gbk

import os
import urllib2
import time


IP = "192.168.0."
GATEWAY = "192.168.0.1"
IP = "10.0.2."
GATEWAY = "10.0.2.2"

for n in range(10, 256):

    ip = IP + str(n)
    print "Trying", ip,
    
    try:
        cmd = "netsh interface ip set address 本地连接 static %s 255.255.255.0 %s 1" % (ip, GATEWAY)
        os.system(cmd)
        time.sleep(1)
        s = urllib2.urlopen("http://27.115.111.138:9090/accounts/login/?next=/", timeout=3).read()
        if "easypath" in s.lower():
            print ip, " - Success!!!"
        else:
            print ip, " - Unavailable."
    except:
        print ip, " - Time out."
        
