# -*- coding: utf-8 -*-
import sys,os
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import requests
import time
from pages.api import apicommon
import random
"""
王亮开发组
"""
#global sess
#global loginSess
#global bakSess
global timestamp
global mail
global rannum
rannum = str(random.randint(1000, 9999))
timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
mail = '%s@tiantang3123.com' % (timestamp)
class ApiRequestsTwo():
    '''
    #登录
    def member_login(self):
        global sess

        url = "http://s2-api.smarket.net.cn/member/login"

        payload = "{\"tenantId\":\"1116\",\"schemaId\":\"2808\",\"memberFormId\":\"6362\",\"memberSchemaId\":\"2808\",\"unique\":\"13393213135\",\"token\":\"\",\"password\":\"4297F44B13955235245B2497399D7A93\",\"checkCode\":\"\",\"loginType\":\"mobile\",\"url\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6362&configId=251717&memberSchemaId=2808\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/loginsuccess.html?memberFormId=6362&configId=251717&memberSchemaId=2808\",\"referenceTitle\":\"\",\"sessionId\":\"6c0257bde285d60356ae4a070101d6f3\"},\"globalUserId\":\"0903c078acc06f3713f73de9cc562e23\"}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "db317e03-b56c-4150-abd3-cff16ca8836c"
        }

        return apicommon.post_req(url, payload, headers)

        sess =response.json()['body']['content']['sess']
        loginSess =response.json()['body']['content']['sess']
        # print loginSess

        # print(response.text)
        # print (response.status_code)

        print(response.text)
        info = response.text
        infostr = "successful"
        if info.find(infostr, 0) == -1:
            return u"fail"
            print u"失败"
            # print(info.find(infostr, 0))
        else:
            return u"successful"
            print u"成功"
            # print(info.find(infostr, 0))

    #根据已登录的session获取用户信息
    def member_geneGet(self):

        global loginSess
        loginSess = sess
        # print loginSess
        url = "http://s2-api.smarket.net.cn/member/geneGet"

        # payload = "{\r\n\"sess\": \"{{loginSess}}\"\r\n  \r\n}"
        payload = '{\r\n\"sess\": \"' + loginSess + '"''\r\n  \r\n}'
        print payload
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "848c4af2-9b4b-4c7a-8ad4-204c7f345a13"
        }

        return apicommon.post_req(url, payload, headers)

        # print(response.text)

        info = response.text
        infostr = "successful"
        if info.find(infostr, 0) == -1:
            return u"fail"
            print u"失败"
            # print(info.find(infostr, 0))
        else:
            return u"successful"
            print u"成功"
            # print(info.find(infostr, 0))
    '''
    #获取实例的行为记录数量
    def interaction_getCountByType(self):
        url = "http://s2-api.smarket.net.cn/interaction/getCountByType"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"instanceIds\": [\r\n   \r\n    40045\r\n  ],\r\n  \"moduleType\": 3,\r\n  \"type\": \"survey_browse\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}\r\n\r\n"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "e78d5d0f-29cc-4b35-8691-4fe3d28eff59"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return apicommon.post_req(url, payload, headers)



    #登陆管理后台
    def account_login(self):

        global session
        url = "http://s2-api.smarket.net.cn/account/login"

        payload = "{\r\n    \"email\": \"13393213134\",\r\n    \"password\": \"4297F44B13955235245B2497399D7A93\",\r\n    \"clientType\": \"1\",\r\n    \"clientBrand\": \"Netscape\",\r\n    \"clientVersion\": \"5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36\",\r\n    \"platform\": \"sinobase\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"

        print payload
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ac86fe94-0c2f-47c2-a539-35cecd3c6050"
        }

        return apicommon.post_req(url, payload, headers)


    # #报错 #ch重复
    # def de_contact_getLastSeminarsBySess(self):#报错
    #
    #
    #     url = "http://s2-api.smarket.net.cn/de/contact/getLastSeminarsBySess"
    #
    #     payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"contactId\": 705164,\r\n  \"sortName\": \"startTime\",\r\n  \"sortOrder\": \"desc\",\r\n  \"start\": 0,\r\n  \"num\": 20,\r\n  \"withTag\": 0,\r\n  \"sess\": \"" + apicommon.bakSess + "\"\r\n}"
    #     headers = {
    #         'Cache-Control': "no-cache",
    #         'Postman-Token': "733dbc86-9529-491a-8075-b79122f24ecc"
    #     }
    #
    #     return apicommon.post_req(url, payload, headers)


    #获取会场详细信息
    def webinar_open_getWebinarInfo(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getWebinarInfo"

        payload = "{\r\n    \"instanceId\": 38369,\r\n    \"tenantId\": 1116,\r\n    \"includeCustomField\": 0,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "5d5bb52c-270e-409a-ad57-4d4944bd4aa8"
        }

        return apicommon.post_req(url, payload, headers)



    # # 获取直播会议列表  #重复
    # def webinar_open_getWebinarList_012(self):
    #     url = "http://s2-api.smarket.net.cn/webinar/open/getWebinarList"
    #
    #     payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"startTime\": \"\",\r\n    \"status\": 3,\r\n    \"keyword\": \"\",\r\n    \"orderBy\": \"createTime\",\r\n    \"videoType\": \"1\",\r\n    \"start\": 0,\r\n    \"num\": 12,\r\n    \"includeGuest\": \"true\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
    #     headers = {
    #         'Cache-Control': "no-cache",
    #         'Postman-Token': "6c19b05f-1848-4dca-8ed7-483cdac0ddf4"
    #     }
    #
    #     return apicommon.post_req(url, payload, headers)



    #前台用户修改密码  报错
    def member_changePwd(self):

        url = "http://s2-api.smarket.net.cn/member/changePwd"

        payload = " {\r\n    \"oldPwd\": \"4297F44B13955235245B2497399D7A93\",\r\n    \"newPwd\": \"4297F44B13955235245B2497399D7A93\",\r\n    \"schemaId\": 2808,\r\n     \"sess\": \""+apicommon.forntSession+"\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "4533de22-a629-46f9-9cdf-20ba17992a15"
        }

        return apicommon.post_req(url, payload, headers)


    #获取字典值列表
    def dic_params_getList(self):
        url = "http://s2-api.smarket.net.cn/dic/params/getList"

        payload = "{     \"tenantId\": 119,     \"dicId\": \"2492\"   }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "7c2c46b0-4f24-48d7-9e2a-bdf25e4791d0"
        }

        return apicommon.post_req(url, payload, headers)



    #获取一个全局用户Id（cookieId）
    def anonymous_getId(self):
        url = "http://s2-api.smarket.net.cn/anonymous/getId"

        payload = "{\r\n  \"clientType\": \"iOS\",\r\n  \"clientBrand\": \"Mobile Safari\",\r\n  \"clientVersion\": \"5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36\",\r\n  \"clientIP\": \"192.168.0.1\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "0817c7ea-7588-4b39-907b-92e77e1fef89"
        }

        return apicommon.post_req(url, payload, headers)



    #记录一个互动
    def interaction_record(self):
        url = "http://s2-api.smarket.net.cn/member/interaction/record"

        payload = "{\r\n        \"tenantId\":198,\r\n        \"moduleId\": 0,\r\n        \"instanceId\": 0,\r\n        \"contactId\": 0,\r\n        \"cookieId\": \"817c4822639dfe314fada85204644011\",\r\n        \"openId\": \"\",\r\n        \"loginId\": 0,\r\n        \"memberId\": 0,\r\n        \"actionKey\": \"form_browse\",\r\n        \"objId\": 11880,\r\n        \"objTitle\": \"测试表单\", \r\n        \"signUserId\": 0,\r\n        \"ip\": \"\",\r\n        \"objectModuleId\": 0,\r\n        \"objectInstanceId\": 34248,\r\n        \"browseInfo\": \"string\",\r\n        \"weChatId\": 0,\r\n        \"sess\":\"\"\r\n    }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "8e977830-7acb-419f-ac2a-41ad4b24200d"
        }

        return apicommon.post_req(url, payload, headers)



    #获取表单信息
    def member_form_get(self):
        url = "http://s2-api.smarket.net.cn/member/form/get"

        payload = "{\r\n  \"memberFormId\":6329,\r\n  \"sess\": \"" + apicommon.bakSess + "\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "859e9627-9669-4cf7-aeb0-ee2dd5bc0aec"
        }

        return apicommon.post_req(url, payload, headers)


    #更新注册用户信息  #2000000000000000
    def member_geneUpdate(self):
        url = "http://s2-oldapi.smarket.net.cn/member/geneUpdate"

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[size]\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[dst]\"\r\n\r\n01-0401-00000001\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[orn]\"\r\n\r\n02-0001-00000001\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[type]\"\r\n\r\n2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[sess]\"\r\n\r\n666d591b7b19c6c72cf1785c51a3a3b6\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[cmd]\"\r\n\r\nmember.update\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[seq]\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[ver]\"\r\n\r\n1000\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[body][memberId]\"\r\n\r\n1079888\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[body][formData][0][fieldName]\"\r\n\r\nprovince\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[body][formData][0][value][]\"\r\n\r\n北京\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[body][formData][0][value][]\"\r\n\r\n北京\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"command[body][tenantId]\"\r\n\r\n1116\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            'Postman-Token': "2192ef14-d6fa-4cef-bda6-e13070708b2f"
        }

        return apicommon.post_req(url, payload, headers)


    #验证前台sess
    def anonymous_checkSess(self):
        url = "http://s2-api.smarket.net.cn/anonymous/checkSess"

        payload = "{\r\n    \"sess\": \"" + apicommon.bakSess + "\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "0f7f346a-d0a2-4512-9cc5-6e23d03a2779"
        }

        return apicommon.post_req(url, payload, headers)


    #根据已登录的session获取用户信息
    def member_geneGet(self):
        url = "http://s2-api.smarket.net.cn/member/geneGet"

        payload = "{\r\n\"sess\": \"" + apicommon.forntSession + "\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "3137a01b-97e0-4c77-9b98-7342bd111670"
        }

        return apicommon.post_req(url, payload, headers)

    #检测用户唯一，检测字段值唯一
    def member_checkUnique(self):
        url = "http://s2-api.smarket.net.cn/member/checkUnique"

        payload = "{\r\n    \"memberSchemaId\": \"1116\",\r\n    \"unique\": \"13393213135\",\r\n    \"fieldName\": \"mobil\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "df143fd9-0534-4952-9148-d53115d408f4"
        }

        return apicommon.post_req(url, payload, headers)


    #获取实例详情信息
    def account_channel_get(self):
        url = "http://s2-api.smarket.net.cn/account/channel/get"

        payload = "{\r\n  \"id\": \"38367\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1dc6f17f-1bc4-4355-b569-cf24e09fc251"
        }

        return apicommon.post_req(url, payload, headers)

    #查询符合条件的表单
    def member_form_search(self):
        url = "http://s2-api.smarket.net.cn/member/form/search"

        payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"schemaId\": \"\",\r\n  \"formId\": \"\",\r\n  \"trackId\": \"\",\r\n  \"keyword\": \"\",\r\n  \"start\": \"0\",\r\n  \"num\": \"12\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6548662b-6149-484e-b226-ea58d874ccae"
        }

        return apicommon.post_req(url, payload, headers)

    #根据已登录的session获取用户信息
    def member_get(self):
        url = "http://s2-api.smarket.net.cn/member/get"
        #20180704 sees不是变量
        #payload = "{ \"tenantId\": \"1116\",\"sess\":\"cf31297169105dc546da49831460bb3b\",\"memberId\": [\"1079888\"],\"memberIdList\": [\"1079888\"]}\r\n    \r\n"
        payload = { "tenantId": "1116","sess":apicommon.forntSession,"memberId": ["1079888"],"memberIdList": ["1079888"]}
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "5ff22966-17e4-47b3-bb4d-906f3b075915"
        }

        return apicommon.post_req(url, payload, headers)

    #使用openId登录，如果未登录会返回绑定使用的authCode
    def member_loginByOpenId(self):
        url = "http://s2-api.smarket.net.cn/member/loginByOpenId"

        payload = " {\r\n    \"schemaId\": 4997,\r\n    \"wechatId\": \"38503\",\r\n    \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n    \"clientType\": \"\",\r\n    \"clientBrand\": \"\",\r\n    \"clientVersion\": \"\",\r\n    \"platform\": \"\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "44ee07aa-a460-4a80-a3f4-6f959b1810fe"
        }

        return apicommon.post_req(url, payload, headers)

    #注册用户
    def member_geneRegister(self):
        global timestamp
        global mail
        global rannum
        rannum = str(random.randint(1000, 9999))
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        timetest=timestamp[:13]
        mail = '%s@qq.com' % (timetest)
        print "mail:",mail
        base_dir = os.path.join(os.path.dirname(__file__), 'tokenfornt.md')
        with open(base_dir, 'r') as f:
            Sesson = f.read()
        print "sesson:", Sesson
        url = "http://s2-api.smarket.net.cn/member/geneRegister"
        #20180704
        #payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"schemaId\": \"2808\",\r\n  \"memberFormId\": \"6388\",\r\n  \"url\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl=\",\r\n  \"referenceUrl\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\r\n  \"token\": \"\",\r\n  \"verify\": \"\",\r\n  \"formData\": [{\r\n    \"fieldName\": \"name\",\r\n    \"value\": \"13393213121\"\r\n  }, {\r\n    \"fieldName\": \"email\",\r\n    \"value\": \""+mail+"\"\r\n  }, {\r\n    \"fieldName\": \"password\",\r\n    \"value\": \"4297F44B13955235245B2497399D7A93\"\r\n  }],\r\n  \"browseInfo\": {\r\n    \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\",\r\n    \"browser\": \"Chrome\",\r\n    \"version\": \"66.0.3359.139\",\r\n    \"os\": \"Windows\",\r\n    \"equipment\": \"电脑端\",\r\n    \"resolution\": \"1536X864\",\r\n    \"referenceUrl\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\r\n    \"referenceTitle\": \"\",\r\n      \"sess\": \""+apicommon.forntSession+"\"\r\n  },\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\"\r\n}"
        # payload = {
        #   "tenantId": "1116",
        #   "schemaId": "2808",
        #   "memberFormId": "6388",
        #   "url": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl=",
        #   "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305",
        #   "token": "",
        #   "verify": "",
        #   "formData": [{
        #     "fieldName": "name",
        #     "value": "13393213121"
        #   }, {
        #     "fieldName": "email",
        #     "value": apicommon.get_mail()
        #   }, {
        #     "fieldName": "password",
        #     "value": "4297F44B13955235245B2497399D7A93"
        #   }],
        #   "browseInfo": {
        #     "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        #     "browser": "Chrome",
        #     "version": "66.0.3359.139",
        #     "os": "Windows",
        #     "equipment": "电脑端",
        #     "resolution": "1536X864",
        #     "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305",
        #     "referenceTitle": "",
        #     "sess": apicommon.forntSession
        #   },
        #   "globalUserId": apicommon.get_date()+apicommon.get_random_str()
        # }
        payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"schemaId\": \"2808\",\r\n  \"memberFormId\": \"6388\",\r\n  \"url\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl=\",\r\n  \"referenceUrl\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\r\n  \"token\": \"\",\r\n  \"verify\": \"\",\r\n  \"formData\": [{\r\n    \"fieldName\": \"name\",\r\n    \"value\": \"13393213121\"\r\n  }, {\r\n    \"fieldName\": \"email\",\r\n    \"value\": \""+apicommon.get_newmail()+"\"\r\n  }, {\r\n    \"fieldName\": \"password\",\r\n    \"value\": \"4297F44B13955235245B2497399D7A93\"\r\n  }],\r\n  \"browseInfo\": {\r\n    \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\",\r\n    \"browser\": \"Chrome\",\r\n    \"version\": \"66.0.3359.139\",\r\n    \"os\": \"Windows\",\r\n    \"equipment\": \"电脑端\",\r\n    \"resolution\": \"1536X864\",\r\n    \"referenceUrl\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\r\n    \"referenceTitle\": \"\",\r\n      \"sess\": \""+Sesson+"\"\r\n  },\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f2cc7a6d-c77a-405e-84c2-e3829b3a5be8"
        }
        # response = requests.request("POST", url, data=payload, headers=headers)
        return apicommon.post_req(url, payload, headers)

    #获取租户下一个用户的某类型的互动记录
    def interaction_getDetailList(self):
        url = "http://s2-api.smarket.net.cn/interaction/getDetailList"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"instanceId\": 40837,\r\n  \"moduleType\": 3,\r\n  \"memberId\": 875941,\r\n  \"type\": \"post_create\",\r\n  \"start\": 0,\r\n  \"num\": -1,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a0a88607-6837-4dff-966e-e7fbd53dd5cc"
        }

        return apicommon.post_req(url, payload, headers)


    #该接口为后台接口，后期即将移除，请不要继续使用，获取用户在实例中的（浏览/分享/资料）计数
    def interaction_getStatCountList(self):
        url = "http://s2-api.smarket.net.cn/interaction/getStatCountList"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"instanceId\": 40837,\r\n  \"moduleType\": 3,\r\n  \"memberId\": 875941,\r\n  \"type\": \"project_browse\",\r\n  \"statType\": \"url\",\r\n  \"start\": 0,\r\n  \"num\": -1,\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6c604cca-3bd3-47a3-97c2-13a51485540d"
        }

        return apicommon.post_req(url, payload, headers)

    #获取表单模板信息
    def member_form_getTemplate(self):
        url = "http://s2-api.smarket.net.cn/member/form/getTemplate"

        payload = "{\r\n  \"memberFormId\": 6388,\r\n  \"trackId\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "de5dd4a3-2537-4ee8-ba7c-0b9fbd2a8c92"
        }

        return apicommon.post_req(url, payload, headers)

    #向用户邮箱发送验证码
    def member_sendVerificationCodeToMail(self):
        #20180704 使用公共函数生成随机邮箱
        #global timestamp
        #global mail
        #global rannum
        #rannum = str(random.randint(1000, 9999))
        #timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        #mail = '%s@qq.com' % (timestamp)
        url = "http://s2-api.smarket.net.cn/member/sendVerificationCodeToMail"

        #payload = "{\r\n  \"memberFormId\": 6388,\r\n  \"unique\": \"3929077@q12q.com\"\r\n}"
        payload = {
          "memberFormId": 6388,
          "unique": apicommon.get_mail()
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6b308ec7-f0cc-4f54-9a77-ec337bc00a7f"
        }

        # response = requests.request("POST", url, data=payload, headers=headers)
        return apicommon.post_req(url, payload, headers)

    #获取字典树形结构
    def dic_params_getTree(self):
        url = "http://s2-api.smarket.net.cn/dic/params/getTree"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"dicId\": \"484362\",\r\n  \"format\": \"object\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1fa11902-e62f-4c85-93d7-ba1c66704e6a"
        }

        return apicommon.post_req(url, payload, headers)

    #注册表单浏览
    def member_form_view(self):
        url = "http://s2-api.smarket.net.cn/member/form/view"

        payload = "{\r\n  \"memberFormId\": \"6329\",\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"url\": \"\",\r\n  \"referenceUrl\": \"\",\r\n  \"trackId\": \"0\",\r\n  \"openId\": \"\",\r\n  \"sess\": \""+apicommon.forntSession+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2747b77e-584e-4707-be3f-1cff081bbe42"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某个会员信息
    def member_getById(self):
        url = "http://s2-api.smarket.net.cn/member/getById"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"memberId\": [\r\n    803868\r\n  ],\r\n\"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "32e1cce3-c5b7-4e4f-bbee-bba8e4c4c6d2"
        }

        return apicommon.post_req(url, payload, headers)

    #获取验证信息
    def account_getAuth(self):
        url = "http://s2-api.smarket.net.cn/account/getAuth"

        payload = "{\r\n  \"nodeId\": 40920,\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"instanceId\": 40920,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "fb02b90f-afd9-4389-8c72-81c6186d7567"
        }

        return apicommon.post_req(url, payload, headers)

    #注册
    def member_register(self):
        #20180704
        #global timestamp
        #global mail
        #global rannum
        #rannum = str(random.randint(1000, 9999))
        #timestamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        #mail = '%s@qq.com'% (timestamp)
        #phone ='1339321 %s '%(rannum)
        #print timestamp
        #print mail

        url = "https://s2-api.smarket.net.cn/member/register"
        print "email:",apicommon.get_random_str()
        #payload = "{\"tenantId\":\"1116\",\"schemaId\":\"2808\",\"memberFormId\":\"6388\",\"url\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl=\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\"token\":\"\",\"verify\":\"\",\"formData\":[{\"fieldName\":\"name\",\"value\":\"邢英丽\"},{\"fieldName\":\"email\",\"value\":\"1530696604809@tiantang3123.com\"},{\"fieldName\":\"password\",\"value\":\"4297F44B13955235245B2497399D7A93\"}],\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\"referenceTitle\":\"\",\"sessionId\":\"ec69f3edd1c9908cb8cfeb1e4528488e\"},\"globalUserId\":\"76ef040b-49ad-49db-8f4d-afe9636baca5\"}"
        # payload ={"tenantId":"1116","schemaId":"2808","memberFormId":"6388","url":"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl=",
        #           "referenceUrl":"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305",
        #           "token":"","verify":"","formData":[{"fieldName":"name","value":"邢英丽"},
        #                                              {"fieldName":"email","value":apicommon.get_mail()},
        #                                              {"fieldName":"password","value":"4297F44B13955235245B2497399D7A93"}],
        #           "browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"电脑端","resolution":"1366X768","referenceUrl":"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305","referenceTitle":"","sessionId":"ec69f3edd1c9908cb8cfeb1e4528488e"},"globalUserId":"76991fd6-62ff-46ef-aec6-e4df7d5627ab"}
        payload = "{\"tenantId\":\"1116\",\"schemaId\":\"2808\",\"memberFormId\":\"6388\",\"url\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl=\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\"token\":\"\",\"verify\":\"\",\"formData\":[{\"fieldName\":\"name\",\"value\":\"邢英丽\"},{\"fieldName\":\"email\",\"value\":\""+apicommon.get_tiantangmail()+"\"},{\"fieldName\":\"password\",\"value\":\"4297F44B13955235245B2497399D7A93\"}],\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305\",\"referenceTitle\":\"\",\"sessionId\":\"ec69f3edd1c9908cb8cfeb1e4528488e\"},\"globalUserId\":\"11e3f2c4-a839-4ba5-b70d-831a8a3ac189\"}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "d06acbfd-9163-4796-9965-1a1b72159629"
        }

        # response = requests.request("POST", url, data=payload, headers=headers)
        return apicommon.post_req(url, payload, headers)

    #通过openId获取注册信息
    def member_identification_information_GetByOpenId(self):

        url = "http://s2-api.smarket.net.cn/member/identification/information/GetByOpenId"

        payload = " {\r\n    \"openId\": \"otYzet6sfobnSyeIdqLBUDk4szQk\",\r\n    \"tenantId\": \"1043\",\r\n    \"unionId\": \"\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "e59f5a64-0bcc-4b3b-b46c-0686a0039c4a"
        }

        return apicommon.post_req(url, payload, headers)

    #获取身份标识字段列表
    def member_schema_field_sorting_GetList(self):
        url = "http://s2-api.smarket.net.cn/member/schema/field/sorting/GetList"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"schemaId\": \"1116\",\r\n    \"loginIds\": [\r\n      1088668,\r\n      1088667\r\n    ],\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "0b33d875-89a9-4b7d-ae7c-931863aa6b0e"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，通过实例获取验证信息
    def account_getAuthByInstance(self):
        url = "http://s2-api.smarket.net.cn/account/getAuthByInstance"

        payload = "{\r\n  \"instanceId\": 40837,\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "04b5ed1e-b136-419b-864b-f7bec6c4d058"
        }

        return apicommon.post_req(url, payload, headers)

    #查询收藏的信息列表
    def collect_search(self):
        url = "http://s2-api.smarket.net.cn/collect/search"

        payload = "{\r\n  \"start\": 1,\r\n  \"num\": 1,\r\n  \"sort\": 1,\r\n  \"r\": {\r\n    \"application\": \"luckDraw\",\r\n    \"cookieId\": \"cookieId\",\r\n    \"openId\": \"openId\",\r\n    \"type\": \"\",\r\n    \"objectId\": \"20\"\r\n  },\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e496b517-dc3d-46f8-89e0-4245d3eac23c"
        }

        return apicommon.post_req(url, payload, headers)

    #身份认证体系发送手机修改密码验证码(member_sendCheckCode)新加的接口增加前端的控制（有效期和重发时间）
    def member_sendCheckCode(self):
        url = "http://s2-api.smarket.net.cn/member/sendCheckCode"
        #20180704 自动添加新的号码，避免60s限制
        payload = "{\r\n  \"unique\": \"13393213135\",\r\n  \"memberSchemaId\": 30,\r\n  \"validTime\": 60,\r\n  \"intervalTime\": 6,\r\n  \"action\": \"login\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}\r\n"
        payload ={
          "unique": apicommon.get_new_phone_no(),
          "memberSchemaId": 30,
          "validTime": 60,
          "intervalTime": 6,
          "action": "login",
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
}

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "9d70992f-9d24-4272-ad76-a0986c9426db"
        }

        return apicommon.post_req(url, payload, headers)

    #会员修改，只修改给定的字段.需要登录
    def member_updateByField(self):
        url = "http://s2-api.smarket.net.cn/member/updateByField"

        payload = "{\r\n  \"formData\": [\r\n    {\r\n      \"fieldId\": 1,\r\n      \"text\":\"jobNumber:001\"\r\n    },\r\n    {\r\n      \"fieldId\": 2,\r\n      \"text\":\"enterprise:sinobase\"\r\n    }\r\n  ],\r\n  \"sess\":\""+apicommon.forntSession+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "1f2ab3b0-a0a8-45fb-a864-214806f83c67"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return apicommon.post_req(url, payload, headers)

    # #获取实例的行为记录数量  重复复
    # def interaction_getCountByType(self):
    #     url = "http://s2-api.smarket.net.cn/interaction/getCountByType"
    #
    #     payload = "{\r\n  \"tenantId\": 1116,\r\n  \"instanceIds\": [\r\n   \r\n    40045\r\n  ],\r\n  \"moduleType\": 3,\r\n  \"type\": \"survey_browse\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}\r\n\r\n"
    #     headers = {
    #         'Cache-Control': "no-cache",
    #         'Postman-Token': "24fee977-bcb5-42af-ae9d-3d91fa683ff8"
    #     }
    #
    #     return apicommon.post_req(url, payload, headers)

    #获取一个图片验证码
    def member_getImageCode(self):
        url = "http://s2-oldapi.smarket.net.cn/member/getImageCode"

        payload = {"height": "20", "width": "20", "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8", "len": "10"}

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "c514b010-c1ab-4046-bbd9-c8308df25ac6"
        }

        return apicommon.get_reqpng(url, payload, headers)

    #验证session,并获取相应的信息
    def account_verifySession(self):

        url = "http://s2-oldapi.smarket.net.cn/account/verifySession"

        payload = {"referer": "", "sess": apicommon.forntSession}

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "80463536-5196-4719-9163-85bf4cd8bf3d"
        }

        return apicommon.get_req(url, payload, headers)

if __name__ == "__main__":
    apicommon.all_login()
    o = ApiRequestsTwo()
    # o.interaction_getCountByType()
    # o.account_login()
    # o.de_contact_getLastSeminarsBySess()
    # o.webinar_open_getWebinarInfo()
    # o.webinar_open_getWebinarList_012()
    # o.member_changePwd()
    #o.dic_params_getList()
    # o.anonymous_getId()
    # o.interaction_record()
    # o.member_form_get()
    # o.member_geneUpdate()
    # o.anonymous_checkSess()
    # o.member_geneGet()
    # o.member_checkUnique()
    # o.account_channel_get()
    # o.member_form_search()
    #o.member_get()
    # o.member_loginByOpenId()
    # o.member_geneRegister()
    # o.interaction_getDetailList()
    # o.interaction_getStatCountList()
    # o.member_form_getTemplate()
    # o.member_sendVerificationCodeToMail()
    # o.dic_params_getTree()
    # o.member_form_view()
    # o.member_getById()
    # o.account_getAuth()
    o.member_register()  #字段重复：邮箱
    # o.member_identification_information_GetByOpenId()
    # o.member_schema_field_sorting_GetList()
    # o.account_getAuthByInstance()
    # o.collect_search()
    #o.member_sendCheckCode()
    # o.member_updateByField()
    # o.interaction_getCountByType()
    # o.member_getImageCode()
    # o.account_verifySession()











