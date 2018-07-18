# -*- coding: utf-8 -*-
import requests
import time
import random
import os
#定义全局变量
#前台登陆的session
global forntSession
#后台管理登陆的session
global bakSess
#时间
global timestampHeader
def all_login():
    if member_login()=="fail":
        print 'member_login error'
        return -1
    if account_login()=="fail":
        print  'account_login error'
        return -1

    return 1


def member_login():
    #引用需要修改的全局变量
    global forntSession

    url = "http://s2-api.smarket.net.cn/member/login"

    payload = "{\"tenantId\":\"1116\",\"schemaId\":\"2808\",\"memberFormId\":\"6362\",\"memberSchemaId\":\"2808\",\"unique\":\"13393213135\",\"token\":\"\",\"password\":\"4297F44B13955235245B2497399D7A93\",\"checkCode\":\"\",\"loginType\":\"mobile\",\"url\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6362&configId=251717&memberSchemaId=2808\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/loginsuccess.html?memberFormId=6362&configId=251717&memberSchemaId=2808\",\"referenceTitle\":\"\",\"sessionId\":\"6c0257bde285d60356ae4a070101d6f3\"},\"globalUserId\":\"0903c078acc06f3713f73de9cc562e23\"}"
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "db317e03-b56c-4150-abd3-cff16ca8836c"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    info = response.text
    infostr = "successful"
    if info.find(infostr, 0) == -1:
        forntSession = ''
        return u"fail"
    else:
        forntSession = response.json()['body']['content']['sess']
        base_dir = os.path.join(os.path.dirname(__file__), 'tokenfornt.md')
        with open(base_dir, 'w') as f:
            f.write(forntSession)
        return u"successful"

# 登陆管理后台
def account_login():
    global bakSess
    url = "http://s2-api.smarket.net.cn/account/login"

    payload = "{\r\n    \"email\": \"13393213134\",\r\n    \"password\": \"4297F44B13955235245B2497399D7A93\",\r\n    \"clientType\": \"1\",\r\n    \"clientBrand\": \"Netscape\",\r\n    \"clientVersion\": \"5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36\",\r\n    \"platform\": \"sinobase\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"

    #print payload
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "ac86fe94-0c2f-47c2-a539-35cecd3c6050"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    info = response.text
    infostr = "successful"

    if info.find(infostr, 0) == -1:
        return u"fail"
    else:
        bakSess = response.json()['body']['content']['session']
        base_dir=os.path.join(os.path.dirname(__file__), 'token.md')
        with open(base_dir, 'w') as f:
            f.write(bakSess)
        return u"successful"
#20180703添加公共处理函数
import json
def post_req(url,payload,headers,querystring=""):
    print "payload:",payload
    response = requests.request("POST", url, data=payload, headers=headers,params=querystring)

    info = response.text
    print "status:",response.status_code
    print "info:",info

    #json字符串解析
    repValue = json.loads(info)
    #返回解析中需要字段的内容
    print "result:",repValue["body"]["result"]
    print "desc:",repValue["body"]["desc"]

    #print repValue["body"]["content"]
    return repValue["body"]["result"],repValue["body"]["desc"]
def get_req(url,payload,headers):
    print payload
    response = requests.request("GET", url, data=payload, headers=headers)
    print "status:",response.status_code
    info = response.text
    print info

    #json字符串解析
    repValue = json.loads(info)
    #返回解析中需要字段的内容
    print repValue["body"]["result"]
    print repValue["body"]["desc"]
    return repValue["body"]["result"],repValue["body"]["desc"]
def get_reqpng(url,payload,headers):
    print payload
    response = requests.request("GET", url, data=payload, headers=headers)
    print "status:",response.status_code
    info = response.status_code
    return info
def post_reqzip(url,payload,headers):
    print payload
    response = requests.request("POST", url, data=payload, headers=headers)

    info = response.status_code
    print "info:",info
    return info
if __name__ == "__main__":
    #member_login()
    #account_login()
    if all_login()==1:
        print "successful"

    else:
        print "get login session error"
#20180704获取时间
def get_date():
    #global timestampHeader
    return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
def get_mail():
    print "date:",get_date()
    # return get_date()[:13]+"@tiantang3123.com"
    return get_date()+get_random_str()+"@qq.com"
def get_random_str():
    return str(random.randint(1000, 9999))
def get_new_phone_no():
    return "1339321"+get_random_str()
def get_newmail():
    print "date:",get_date()
    s=get_random_str()+get_date()
    return s[:13]+"@qq.com"

def get_tiantangmail():
    print "date:", get_date()
    s = get_random_str() + get_date()
    return s[:13] + "@tiantang3123.com"
    # return get_date()+get_random_str()+"@qq.com"