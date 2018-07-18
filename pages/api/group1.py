# -*- coding: utf-8 -*-
import requests,os
from pages.api import apicommon
import sys
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
"""
刘国静开发组
"""

class ApiRequestsOne():

    #根据已登录的前台session获取用户信息
    def member_geneGet_003(self):



        url = "http://s2-api.smarket.net.cn/member/geneGet"

        payload = "{\"sess\": \"" + apicommon.forntSession + "\"  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a41e7503-e0a7-4768-b07c-93363f52aa6d"
        }

        return apicommon.post_req(url, payload, headers)

    # 获取分会场详细信息
    def seminar_subSeminar_frontGet(self):
        url = "http://s2-api.smarket.net.cn/seminar/subSeminar/frontGet"

        payload = "{\r\n    \"subSeminarId\": \"4875\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "6c58c171-71bc-4f08-a1d2-a27cf5ff4d6b"
        }

        return apicommon.post_req(url, payload, headers)

    #获取参与过的会议
    def de_contact_getLastSeminarsBySess(self):
        url = "http://s2-api.smarket.net.cn/de/contact/getLastSeminarsBySess"

        payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"contactId\": 705164,\r\n  \"sortName\": \"startTime\",\r\n  \"sortOrder\": \"desc\",\r\n  \"start\": 0,\r\n  \"num\": 20,\r\n  \"withTag\": 0,\r\n  \"sess\": \"" + apicommon.bakSess + "\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "154383ab-3ce5-45b9-aebc-86a31cf8b212"
        }

        return apicommon.post_req(url, payload, headers)

    #获取字段列表
    def field_getList(self):
        url = "http://s2-api.smarket.net.cn/field/getList"

        payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"fieldType\": \"seminar\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "b797ced8-a2a3-4ec2-a363-599c08719734"
        }

        return apicommon.post_req(url, payload, headers)

    #获取短地址
    def shortUrl_getList(self):
        url = "http://s2-api.smarket.net.cn/shortUrl/getList"

        payload = "{\r\n  \"withCreate\": 0,\r\n  \"realUrlList\": [\r\n    \"http://www.baidu.com/\"\r\n  ]\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "d78391fe-8cc1-46cc-b619-e5acb9e1ced1"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，获取联系人字段
    def app_seminar_contact_field_getCustomFields(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/contact/field/getCustomFields"

        payload = " {\r\n    \"seminarId\": 4793\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1a41a79a-52f4-41c0-8cf6-1341982cf233"
        }

        return apicommon.post_req(url, payload, headers)

    #根据参会二维码获取会议联系人
    def app_seminar_contact_getByUniqueField(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/contact/getByUniqueField"

        payload = "{\r\n    \"seminarId\":\"4793\",\r\n    \"fieldName\" : \"mc_qrCode\",\r\n    \"fieldValue\" : \"2168071847\",\r\n    \"sess\": \"" + apicommon.bakSess + "\"\r\n  }\r\n"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "02dd31b8-d601-4de0-a809-dbdea8c15b27"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，获取会议联系人
    def app_seminar_contact_getList(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/contact/getList"

        payload = "{\r\n    \"seminarId\": \"4793\",\r\n    \"lastModify\": \"2015-10-22T12:00:00\",\r\n    \"start\": 0,\r\n    \"num\": 100,\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "135d68e9-695f-405e-bd88-a3239950f79e"
        }

        return apicommon.post_req(url, payload, headers)

    # 获取会议详情
    def seminar_frontGet(self):
        url = "http://s2-api.smarket.net.cn/seminar/frontGet"

        payload = "{\r\n        \"seminarId\": 4868\r\n    }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "3934c9d8-2565-45ce-be07-d87bcc078933"
        }

        return apicommon.post_req(url, payload, headers)

    # 获取嘉宾列表
    def seminar_guest_getGroupList(self):
            url = "http://s2-api.smarket.net.cn/seminar/guest/getGroupList"

            payload = "{\r\n    \"tenantId\": 968,\r\n    \"seminarId\": 3307\r\n  }"
            headers = {
                'Cache-Control': "no-cache",
                'Postman-Token': "fa6bb6b7-dd74-404f-bde6-f0d20cda0080"
            }

            return apicommon.post_req(url, payload, headers)

    #获取会议日程按天分组
    def seminar_agenda_getGroupList(self):
        url = "http://s2-api.smarket.net.cn/seminar/agenda/getGroupList"

        payload = "{\r\n  \"seminarId\": \"4813\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "077a7e04-35dc-4118-8809-3bd509a1bc86"
        }

        return apicommon.post_req(url, payload, headers)

    #获取会议日程信息
    def seminar_agenda_get(self):
        url = "http://s2-api.smarket.net.cn/seminar/agenda/get"

        payload = "\r\n{\r\n    \"seminarId\":\"4813\",\r\n    \"agendaId\":\"4026\"\r\n}\r\n"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "9bf2f56f-a301-4937-b624-38a5123a5b96"
        }

        return apicommon.post_req(url, payload, headers)

    #会议报名接口 #时间戳报错
    def seminar_contact_register(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/registerNew"
        #20180704
        #payload = " {\r\n    \"formId\":\"13282\",\"linkId\":\"26810\",\"instanceId\":\"38367\",\"globalUserId\":\"\",\"url\":\"https://f.smarket.net.cn/s/template/34758dc860857df9a0b4f2b94a015051/html/customForm.html?customFormId=13282&instanceId=38367&linkId=26810&configId=246953\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=38367\",\"ver\":\"v2.0.1\",\"verificationCode\":\"971355\",\"formData\":[{\"fieldName\":\"name\",\"value\":\"高明\"},{\"fieldName\":\"email\",\"value\":\"{{timestampHeader}}@qq.com\"},{\"fieldName\":\"avatar\",\"value\":{\"fileName\":\"\",\"mapId\":\"\"}},{\"fieldName\":\"province\",\"value\":[\"北京\",\"北京\"],\"otherValue\":\"\"},{\"fieldName\":\"jobNumber\",\"value\":\"\"},{\"fieldName\":\"enterprise\",\"value\":\"\"},{\"fieldName\":\"department\",\"value\":[],\"otherValue\":\"\"},{\"fieldName\":\"position\",\"value\":[],\"otherValue\":\"\"},{\"fieldName\":\"gender\",\"value\":[],\"otherValue\":\"\"},{\"fieldName\":\"industry\",\"value\":[],\"otherValue\":\"\"}],\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        payload =  {
            "formId":"13282","linkId":"26810","instanceId":"38367","globalUserId":"","url":"https://f.smarket.net.cn/s/template/34758dc860857df9a0b4f2b94a015051/html/customForm.html?customFormId=13282&instanceId=38367&linkId=26810&configId=246953","referenceUrl":"https://f.smarket.net.cn/s/template/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=38367","ver":"v2.0.1","verificationCode":"971355","formData":[{"fieldName":"name","value":"高明"},{"fieldName":"email","value":apicommon.get_mail()},{"fieldName":"avatar","value":{"fileName":"","mapId":""}},{"fieldName":"province","value":["北京","北京"],"otherValue":""},{"fieldName":"jobNumber","value":""},{"fieldName":"enterprise","value":""},{"fieldName":"department","value":[],"otherValue":""},{"fieldName":"position","value":[],"otherValue":""},{"fieldName":"gender","value":[],"otherValue":""},{"fieldName":"industry","value":[],"otherValue":""}],
            "_cache_with_cached": "1",
            "_cache_refresh": "1",
            "_cache_timeout": "60"
        }
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "1db1d290-75bd-4dd8-930b-8e7c2520fa34"
        }

        return apicommon.post_req(url, payload, headers)

     #获取会议日程信息

    #获取表单详细信息
    def seminar_topicTemplate_seminar_get(self):
        url = "http://s2-api.smarket.net.cn/seminar/topicTemplate/seminar/getFormInfo"

        payload = "{\r\n    \"instanceId\": 38367,\r\n    \"formId\": 5005,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "5bef8218-2acf-4a1a-b0d8-f09a150873f7"
        }

        return apicommon.post_req(url, payload, headers)

    #获取会议列表
    def seminar_getList(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/getList"

        payload = " {\r\n        \"tenantId\": \"1116\",\r\n        \"key\": \"\",\r\n        \"sceneName\": \"\",\r\n        \"status\": \"\",\r\n        \"sortName\": \"createTime\",\r\n        \"conditions\": [\r\n          \r\n        ],\r\n       \r\n        \"start\": 0,\r\n        \"num\": 10\r\n    }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "32de7d21-144f-45bd-bc9d-83e8efb30396"
        }

        return apicommon.post_req(url, payload, headers)

    # #获取会议详情
    # def seminar_frontGet(self):  #重复
    #
    #     url = "http://s2-api.smarket.net.cn/seminar/frontGet"
    #
    #     payload = "{\r\n    \"seminarId\": \"4793\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
    #     headers = {
    #         'Cache-Control': "no-cache",
    #         'Postman-Token': "b9697113-6c0f-4307-8d70-2fc262ded1c0"
    #     }
    #
    #     return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，获取压缩过的会议联系人
    def app_seminar_contact_getListCompressed(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/contact/getListCompressed"
        print "apicommon.bakSess:",apicommon.bakSess
        payload = "{\r\n    \"seminarId\":\"4793\",\r\n    \"lastModify\": \"2017-10-22T12:00:00\",\r\n    \"start\": 0,\r\n    \"num\": 10,\r\n     \"sess\": \"" + apicommon.bakSess + "\"\r\n  }"
        print "payload:",payload
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "04d7388a-7cd6-4aa4-ae24-bbad47113ea6"
        }

        return apicommon.post_reqzip(url, payload, headers)


    #获取会议下签到点缩略信息
    def app_seminar_contact_prints_getSigningPointInfo(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/contact/prints/getSigningPointInfo"

        payload = "{\r\n    \"seminarId\": \"4793\",\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "e6389f9c-81a7-48eb-af68-c462d931fc7a"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，获取会议列表
    def app_seminar_getList(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/getList"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"start\": 0,\r\n    \"num\": 10,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "c439cf7b-17ca-4768-b9ef-68620d1afae6"
        }

        return apicommon.post_req(url, payload, headers)

    #获取签到历史记录,压缩版
    def app_seminar_signingPoint_checkIn_getListCompressed(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/signingPoint/checkIn/getListCompressed"

        payload = "{\r\n    \"seminarId\": \"4793\",\r\n    \"lastModify\": \"2015-10-22T12:00:00\",\r\n    \"start\": 0,\r\n    \"num\": 100,\r\n    \"sess\": \"" + apicommon.bakSess + "\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "c37fbe85-8726-4eb2-b9a2-d0c6045bcbe7"
        }

        return apicommon.post_reqzip(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，获取签到点通道下人员
    def app_seminar_signingPoint_contact_getList(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/signingPoint/contact/getList"

        payload = "{\r\n    \"seminarId\": \"4989\",\r\n    \"signingPointId\": \"6345\",\r\n    \"passageId\": \"6528\",\r\n    \"key\": \"13393213135\",\r\n    \"start\": 0,\r\n    \"num\": 20,\r\n     \"sess\": \"" + apicommon.bakSess + "\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "5c268ea5-c4b1-45b5-869d-459724e3fc0e"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，获取会议下的所有签到点信息
    def app_seminar_signingPoint_getGroupList(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/signingPoint/getGroupList"

        payload = " {\r\n    \"seminarId\": \"4793\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ceb68a0a-fca8-46a9-9ade-28f74158743f"
        }

        return apicommon.post_req(url, payload, headers)

    #获取大屏签到墙信息
    def seminar_bigScreen_forBigScreenWall_getCheckInData(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/forBigScreenWall/getCheckInData"

        payload = "{\r\n    \"id\": \"2748\",\r\n    \"signingPointId\": \"6323\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "d6b75aa9-c2c4-4f8f-951f-35044a02398d"
        }

        return apicommon.post_req(url, payload, headers)

    #获取大屏手机端签到信息
    def seminar_bigScreen_forBigScreenWall_getWapCheckInfo(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/forBigScreenWall/getWapCheckInfo"

        payload = "{\r\n    \"bigScreenId\": \"2748\",\r\n    \"contactId\": \"707517\",\r\n    \"uniqueValue\": \"13393213132\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2c11a020-0e7b-415a-99c6-e1bac584c44e"
        }

        return apicommon.post_req(url, payload, headers)

    #获取大屏详细信息
    def seminar_bigScreen_get(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/get"

        payload = "{\r\n    \"id\": \"2748\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e090aad1-1b6d-4203-bc84-cde41ea16971"
        }

        return apicommon.post_req(url, payload, headers)

    #获取大屏列表
    def seminar_bigScreen_getListByGroup(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/getListByGroup"

        payload = "{\r\n    \"groupId\": \"0\",\r\n    \"seminarId\": \"4793\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a62aca2c-0a11-4d87-8c88-9ba36371bb0d"
        }

        return apicommon.post_req(url, payload, headers)

    #获取投票大屏预设信息
    def seminar_bigScreen_getPollPreset(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/getPollPreset"

        payload = " {\r\n    \"tenantId\": \"1116\",\r\n    \"seminarId\": \"4793\",\r\n    \"screenId\": \"2753\",\r\n    \"pollId\": \"2312\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "63dfc111-bea6-4d93-8d4a-be9be49d9a98"
        }

        return apicommon.post_req(url, payload, headers)

    #参会人签到
    def seminar_contact_front_checkIn(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/front/checkIn"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"seminarId\": \"4793\",\r\n    \"signingPointId\": \"6351\",\r\n    \"passageId\": \"6534\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "366a7827-e16a-457d-9d81-9440e2234e49"
        }

        return apicommon.post_req(url, payload, headers)
    #获取会议嘉宾列表
    def seminar_guest_getList(self):
        url = "http://s2-api.smarket.net.cn/seminar/guest/getList"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"seminarId\": 4793\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6715e00a-0655-4a7e-a166-7876c0b792ac"
        }

        return apicommon.post_req(url, payload, headers)

    #获取报名表单列表
    def seminar_register_getList(self):
        url = "http://s2-api.smarket.net.cn/seminar/register/getList"

        payload = "{\r\n    \"seminarId\": \"4793\"\r\n   \r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "466926b4-8625-4858-be9b-276f69fbbd09"
        }

        return apicommon.post_req(url, payload, headers)

    #获取会议签到点签到统计信息
    def seminar_signingPoint_getNumberSignInPassage(self):
        url = "http://s2-api.smarket.net.cn/seminar/signingPoint/getNumberSignInPassage"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"seminarId\": 4793,\r\n    \"instanceId\": 38367,\r\n    \"groupId\": 0,\r\n    \"signingPointId\": 6323,\r\n    \"passageId\": 6506,\r\n    \"sess\": \"" + apicommon.bakSess + "\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "759c44c0-07f4-4a68-ac98-ef08abe1de01"
        }

        return apicommon.post_req(url, payload, headers)

    #获取分会场列表
    def seminar_subSeminar_getListByType(self):
        url = "http://s2-api.smarket.net.cn/seminar/subSeminar/getListByType"

        payload = "{\r\n    \"seminarId\": \"4793\",\r\n    \"type\": \"disabled\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2ea21b8c-1809-482a-9baf-dbd8b367fe5d"
        }

        return apicommon.post_req(url, payload, headers)

    #获取表单详细信息
    def seminar_topicTemplate_seminar_getFormInfo(self):
        url = "http://s2-api.smarket.net.cn/seminar/topicTemplate/seminar/getFormInfo"

        payload = " {\r\n    \"instanceId\": 38532,\r\n    \"formId\": 5025\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "8b471f38-b2aa-4412-a963-1fcb99c89d64"
        }

        return apicommon.post_req(url, payload, headers)

    #获取会议信息，包括所有的分会场
    def seminar_topicTemplate_seminar_getWithAllSub(self):
        url = "http://s2-api.smarket.net.cn/seminar/topicTemplate/seminar/getWithAllSub"

        payload = "{\r\n    \"instanceId\": 38532\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1adec629-be5e-472d-8477-3770e2553c2f"
        }

        return apicommon.post_req(url, payload, headers)

    #提交问卷
    def questionary_action(self):
        url = "http://s2-api.smarket.net.cn/questionary/action"
        #20180704 整体改为数组 globalUserid改为当前时间 null改为None fasle改为False
        #payload = "{\"globalUserId\":\"2061b2be-f424-4276-978d-0eb094f14350\",\"city\":\"\",\"country\":\"\",\"gender\":\"\",\"groupId\":\"\",\"groupid\":\"\",\"headImgUrl\":\"\",\"headimgurl\":\"\",\"language\":\"\",\"nickname\":\"\",\"openId\":\"\",\"openid\":\"\",\"authCode\":\"\",\"province\":\"\",\"remark\":\"\",\"sex\":\"\",\"subscribe\":\"\",\"subscribeTime\":\"\",\"subscribe_time\":\"\",\"name\":\"\",\"memberId\":null,\"unique\":\"\",\"uniqueType\":\"\",\"session\":\"\",\"needWechat\":false,\"questionaryId\":\"6223\",\"referenceUrl\":\"\",\"options\":[{\"fieldName\":\"name\",\"value\":\"邢英丽\"},{\"fieldName\":\"mobile\",\"value\":\"15201232181\"},{\"itemId\":\"1\",\"answer\":\"测试\"}],\"url\":\"https://f.smarket.net.cn/s/template/e2ba9d7e12c7e74fa9ccb58318acc60d/view/PcQuestionnaire.html?questionaryId=6223&configId=251338\",\"preview\":0,\"sess\":\"\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"\",\"referenceTitle\":\"\",\"sessionId\":\"3c4ea604b0097df4ee1e6525dfbb2127\"}}"
        payload = {
                "globalUserId":apicommon.get_date()+apicommon.get_random_str(),"city":"","country":"","gender":"","groupId":"","groupid":"","headImgUrl":"","headimgurl":"","language":"","nickname":"","openId":"","openid":"","authCode":"","province":"","remark":"","sex":"","subscribe":"","subscribeTime":"","subscribe_time":"","name":"","memberId":None,"unique":"","uniqueType":"","session":"","needWechat":False,"questionaryId":"6223","referenceUrl":"","options":[{"fieldName":"name","value":"邢英丽"},{"fieldName":"mobile","value":"15201232181"},{"itemId":"1","answer":"测试"}],"url":"https://f.smarket.net.cn/s/template/e2ba9d7e12c7e74fa9ccb58318acc60d/view/PcQuestionnaire.html?questionaryId=6223&configId=251338","preview":0,"sess":"","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"电脑端","resolution":"1366X768","referenceUrl":"","referenceTitle":"","sessionId":"3c4ea604b0097df4ee1e6525dfbb2127"}
            }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "dfc19476-cd34-4c33-be24-8c85f32fdcb0"
        }

        return apicommon.post_req(url, payload, headers)

    #用户答题
    def questionary_exam_action(self):
        url = "http://s2-api.smarket.net.cn/questionary/exam/action"
        #20180704同上
        #payload = "{\"globalUserId\":\"dcf20776-312d-4465-9261-02195496d7f4\",\"city\":\"\",\"country\":\"\",\"gender\":\"\",\"groupId\":\"\",\"groupid\":\"\",\"headImgUrl\":\"\",\"headimgurl\":\"\",\"language\":\"\",\"nickname\":\"\",\"openId\":\"\",\"openid\":\"\",\"authCode\":\"\",\"province\":\"\",\"remark\":\"\",\"sex\":\"\",\"subscribe\":\"\",\"subscribeTime\":\"\",\"subscribe_time\":\"\",\"name\":\"\",\"memberId\":null,\"unique\":\"\",\"uniqueType\":\"\",\"session\":\"\",\"needWechat\":false,\"questionaryId\":\"6224\",\"referenceUrl\":\"\",\"options\":[{\"fieldName\":\"name\",\"value\":\"高明\"},{\"fieldName\":\"mobile\",\"value\":\"13393213135\"},{\"id\":\"168960\",\"selected\":[1]},{\"id\":\"168961\",\"selected\":[2]}],\"url\":\"https://f.smarket.net.cn/s/template/dd13c38de8fadfd8c5714e225f798a21/view/answer.html?questionaryId=6224&configId=251344\",\"preview\":0,\"sess\":\"\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"\",\"referenceTitle\":\"\",\"sessionId\":\"6c0257bde285d60356ae4a070101d6f3\"}}"
        payload ={"globalUserId":apicommon.get_date(),"city":"","country":"","gender":"","groupId":"","groupid":"","headImgUrl":"","headimgurl":"","language":"","nickname":"","openId":"","openid":"","authCode":"","province":"","remark":"","sex":"","subscribe":"","subscribeTime":"","subscribe_time":"","name":"","memberId":None,"unique":"","uniqueType":"","session":"","needWechat":False,"questionaryId":"6224","referenceUrl":"","options":[{"fieldName":"name","value":"高明"},{"fieldName":"mobile","value":"13393213135"},{"id":"168960","selected":[1]},{"id":"168961","selected":[2]}],"url":"https://f.smarket.net.cn/s/template/dd13c38de8fadfd8c5714e225f798a21/view/answer.html?questionaryId=6224&configId=251344","preview":0,"sess":"","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"电脑端","resolution":"1366X768","referenceUrl":"","referenceTitle":"","sessionId":"6c0257bde285d60356ae4a070101d6f3"}}
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "19c0fae7-3d75-49f2-9b59-c6fbdb4b554e"
        }

        return apicommon.post_req(url, payload, headers)
    #获取问卷信息
    def questionary_get(self):
        url = "http://s2-api.smarket.net.cn/questionary/get"

        payload = "{\r\n    \"questionaryId\": 6225\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "d0235c3b-55d0-49cd-b10c-d61100f21866"
        }

        return apicommon.post_req(url, payload, headers)

    #获取问卷的列表
    def questionary_getList(self):
        url = "http://s2-api.smarket.net.cn/questionary/getList"

        payload = " {\r\n    \"tenantId\": 1116,\r\n    \"moduleType\": \"\",\r\n    \"instanceId\":\" \",\r\n    \"attachId\": \"\",\r\n    \"name\": \"\",\r\n    \"status\": -1,\r\n    \"start\": 0,\r\n    \"num\": 12,\r\n    \"type\": 0\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1489852c-4f10-456f-a786-62f03b882f15"
        }

        return apicommon.post_req(url, payload, headers)

    #浏览问卷
    def questionary_HasParticipation(self):
        url = "http://s2-api.smarket.net.cn/questionary/HasParticipation"

        payload = "{\r\n    \"questionaryId\": 6225,\r\n    \"globalUserId\": \"0903c078acc06f3713f73de9cc562e23\",\r\n    \"openId\": \"\",\r\n    \"referenceUrl\": \"\",\r\n    \"url\": \"\",\r\n    \"instanceId\": \"\",\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "7cc6fe99-d169-4ebe-afe8-805a96cb2a25"
        }

        return apicommon.post_req(url, payload, headers)

    #获取投票
    def poll_get(self):
        url = "http://s2-api.smarket.net.cn/poll/get"

        payload = "{\r\n    \"pollId\": 2299,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a51252b7-6e91-45ba-8f30-9effb8d0a021"
        }

        return apicommon.post_req(url, payload, headers)

    #获取自定义表单详情
    def customForm_get(self):
        url = "http://s2-api.smarket.net.cn/customForm/get"

        payload = "{\r\n    \"customFormId\": \"13323\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "98e039c9-94c7-4824-9fc9-007d4162106d"
        }

        return apicommon.post_req(url, payload, headers)

    #获取会议列表，无sess调用
    def seminar_frontGetList(self):
        url = "http://s2-api.smarket.net.cn/seminar/frontGetList"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"key\": \"我\",\r\n    \"sceneName\": \"business\",\r\n    \"status\": \"proposed\",\r\n    \"sortName\": \"createTime\",\r\n    \"sortOrder\": \"asc\",\r\n    \"conditions\": null,\r\n    \"start\": 0,\r\n    \"num\": 10,\r\n    \"expandInfo\": [\r\n      \"agenda\",\r\n      \"guest\",\r\n      \"subSeminar\"\r\n    ],\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "71e2858b-3776-49f0-9f02-63bc93b6bb5c"
        }

        return apicommon.post_req(url, payload, headers)

    #浏览问卷
    def questionary_view(self):
        url = "http://s2-api.smarket.net.cn/questionary/view"

        payload = "{\r\n  \"questionaryId\": 6224,\r\n  \"globalUserId\": \"69ae2018dd08ac3690ef702e817e1fda\",\r\n  \"openId\": \"\",\r\n  \"referenceUrl\": \"\",\r\n  \"url\": \"\",\r\n  \"instanceId\": \"\",\r\n  \"sess\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9e80ff24-ee31-4167-833a-a662d74258a7"
        }

        return apicommon.post_req(url, payload, headers)

    #根据openID获取会中联系人信息
    def seminar_contact_getContactToWechat(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/getContactToWechat"

        payload = "{\r\n  \"seminarId\": 4997,\r\n  \"wechatId\": 38503,\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "b47b22b6-c5b2-43b9-b415-9d0e13ad7ff4"
        }

        return apicommon.post_req(url, payload, headers)

    #获取参会人员信息
    def seminar_contact_front_getCommonContactInfo(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/front/getCommonContactInfo"

        payload = "\r\n{\r\n  \"seminarId\": 4793,\r\n  \"unique\": \"1528275710000@qq.com\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "7fa9e845-a018-430b-a993-202390ee2fb1"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，更新大屏消息
    def seminar_bigScreen_updateMessage(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/updateMessage"
        #20180704 字符串改为其他形式
        #payload = "{\r\n  \"seminarId\": 4793,\r\n  \"id\": \"2797\",\r\n  \"name\": \"留言\",\r\n  \"scale\": \"narrow\",\r\n  \"topicId\": \"1430\",\r\n  \"groupId\": \"148\",\r\n  \"configId\": \"252065\",\r\n  \"messageConfigId\": \"252064\",\r\n  \"loop\": \"on\",\r\n  \"interval\": \"3\",\r\n  \"status\": \"on\",\r\n  \"url\": \"\",\r\n    \"sess\": \""+apicommon.bakSess+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        payload = {
          "seminarId": 4793,
          "id": "2797",
          "name": "留言",
          "scale": "narrow",
          "topicId": "1430",
          "groupId": "148",
          "configId": "252065",
          "messageConfigId": "252064",
          "loop": "on",
          "interval": "3",
          "status": "on",
          "url": "",
            "sess": apicommon.bakSess,
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "955212e3-f838-4b34-a27c-3eb295a21013"
        }

        return apicommon.post_req(url, payload, headers)

    #获取联系人信息
    def seminar_topicTemplate_contact_get(self):
        url = "http://s2-api.smarket.net.cn/seminar/topicTemplate/contact/get"

        payload = "{\r\n  \"instanceId\": 38367,\r\n  \"uniqueValue\": \"1528339524000@qq.com\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2d3559cb-192a-47ee-a3d4-514ee4deac82"
        }

        return apicommon.post_req(url, payload, headers)

    #会议是否可以报名 如果有报名返回线下会报名信息，如果没有报名但是有注册返回注册信息，如果没有注册没有报名返回null
    def seminar_register_canRegister(self):
        url = "http://s2-api.smarket.net.cn/seminar/register/canRegister"

        payload = "{\r\n  \"instanceId\": 38367,\r\n   \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "7e12bec1-c064-438f-ac67-ade97c9f9ef5"
        }

        return apicommon.post_req(url, payload, headers)

    #获取de联系人信息
    def de_contact_front_get(self):
        url = "http://s2-api.smarket.net.cn/de/contact/front/get"

        payload = "{\r\n    \"tId\": \"1116\",\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9403cf02-c89b-4cd4-a177-40e20d2f0914"
        }

        return apicommon.post_req(url, payload, headers)

    #记录表单的浏览记录
    def customForm_view(self):
        url = "http://s2-api.smarket.net.cn/customForm/view"

        payload = "{\r\n  \"customFormId\": 13323,\r\n  \"globalUserId\": \"\",\r\n  \"linkId\": 1,\r\n  \"openId\": 1,\r\n  \"memberId\": 1,\r\n  \"referenceUrl\": \"\",\r\n  \"url\": \"\",\r\n  \"trackingCode\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2701c561-0001-450f-8da7-0e8721c6ed47"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某人的答题记录
    def questionary_exam_user_getSingleResult(self):
        url = "http://s2-api.smarket.net.cn/questionary/exam/user/getSingleResult"

        payload = "{\r\n    \"questionaryId\": \"2545\",\r\n    \"examResultId\": 86,\r\n    \"tenantId\": 1116,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ba12a66f-3a33-40c2-bf49-ebe95a3214dd"
        }


        return apicommon.post_req(url, payload, headers)

    #生成试卷
    def questionary_exam_user_GenerateExam(self):
        url = "http://s2-api.smarket.net.cn/questionary/exam/user/GenerateExam"

        payload = " {\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"questionaryId\": \"6225\",\r\n    \"openId\": \"\",\r\n    \"globalUserId\":\"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n    \"isSave\": 1,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "c47ac77c-d5e0-4786-982a-ecc14385bf65"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某会议下签到点的签到数
    def seminar_signingPoint_checkIn_getCheckInCount(self):
        url = "http://s2-api.smarket.net.cn/seminar/signingPoint/checkIn/getCheckInCount"

        payload = "{\r\n  \"seminarId\": \"4989\",\r\n  \"signPoints\": [\r\n   6345\r\n  ],\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "15132c2b-8387-4518-a1a5-8e646cf92ffc"
        }

        return apicommon.post_req(url, payload, headers)

    #通过微信OpenId获取某会议下的联系人
    def seminar_topicTemplate_contact_getByOpenId(self):
        url = "http://s2-api.smarket.net.cn/seminar/topicTemplate/contact/getByOpenId"

        payload = "{\r\n  \"seminarId\": 4997,\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "01c81ae5-ced0-48aa-b604-9da4993704f0"
        }

        return apicommon.post_req(url, payload, headers)

    #通过自定义表单id获取报名表单信息
    def seminar_register_getSubList(self):
        url = "http://s2-api.smarket.net.cn/seminar/register/getSubList"

        payload = "{\r\n  \"customFormId\": \"13759\",\r\n  \"instanceId\": \"39920\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "b9e5f9c5-24c5-4c7b-9841-3d64a8123144"
        }

        return apicommon.post_req(url, payload, headers)

    #绑定微信和参会人员
    def seminar_contact_setContactToWechat(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/setContactToWechat"

        payload = "{\r\n  \"seminarId\": 4989,\r\n  \"contactId\": 772250,\r\n  \"wechatId\": 38503,\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "02eac5f9-e23d-4842-811b-6ffec2bf9752"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，更新留言大屏信息
    def seminar_bigScreen_updateLottery(self):

        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/updateLottery"

        headers = {
            'Content-Type': "application/json",
        }
        payload = {
            "seminarId": 4989,
            "id": "2806",
            "name": "大屏帖子",
            "scale": "narrow",
            "topicId": "1439",
            "groupId": "0",
            "configId": "1",
            "messageConfigId": "1",
            "loop": "on",
            "interval": "3",
            "status": "on",
            "url": "",
            "sess": apicommon.bakSess,
            "_cache_with_cached": "1",
            "_cache_refresh": "1",
            "_cache_timeout": "60"
        }
        return apicommon.post_req(url, payload, headers)
    #检查表单的不重复字段是否重复
    def customForm_checkRepeatable(self):
        url = "http://s2-api.smarket.net.cn/customForm/checkRepeatable"

        payload = "{\r\n    \"customFormId\": 13323,\r\n    \"fieldId\": \"1\",\r\n    \"fieldValue\": \"1\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9d3f4375-4fcf-44a7-97ba-a7f1b7bbfabe"
        }

        return apicommon.post_req(url, payload, headers)

    #此接口即将过期不在维护，可使用 member_geneGet 代替
    def seminar_contact_front_getRegContact(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/front/getRegContact"

        payload = "{\r\n        \"tenantId\": 1116,\r\n        \"sess\": \""+apicommon.forntSession+"\"\r\n    }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ba1b490f-75ab-418f-98d8-a33dbe60f9d4"
        }

        return apicommon.post_req(url, payload, headers)

    #标准报名
    def seminar_contact_front_regSeminar(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/front/regSeminar"
        #20180704
        #payload = "{\r\n  \"items\": [\r\n    {\r\n      \"fieldId\": \"2\",\r\n      \"key\": \"name\",\r\n      \"text\": \"上帝\"\r\n    },\r\n    {\r\n      \"fieldId\": \"3\",\r\n      \"key\": \"email\",\r\n    \"text\": \"1530674108132@tiantang31231.com\"\r\n    }\r\n  ],\r\n   \"sess\": \""+apicommon.forntSession+"\",\r\n  \"instanceId\": 40762,\r\n  \"seminarId\": \"5105\",\r\n  \"customFormId\": 14046,\r\n  \"channel\": \"\",\r\n  \"subSeminars\": [\r\n    1\r\n  ],\r\n  \"openId\": \"\",\r\n  \"wechatId\": \"38503\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        payload = {
          "items": [
            {
              "fieldId": "2",
              "key": "name",
              "text": "上帝"
            },
            {
              "fieldId": "3",
              "key": "email",
            "text": apicommon.get_mail()
            }
          ],
           "sess": apicommon.forntSession,
          "instanceId": 40762,
          "seminarId": "5105",
          "customFormId": 14046,
          "channel": "",
          "subSeminars": [
            1
          ],
          "openId": "",
          "wechatId": "38503",
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "90a0e75b-4cce-4f8c-a72d-ba4a78eb88a4"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某个OpenId的答表单的记录
    def customForm_user_getResultByOpenId(self):
        url = "http://s2-api.smarket.net.cn/customForm/user/getResultByOpenId"

        payload = "{\r\n  \"openId\": \"otqO01HFNgV_Z06fEQgxiH6FAaM0-4\",\r\n  \"customFormId\": 13323,\r\n  \"start\": 0,\r\n  \"num\": 10,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f3534466-8027-48f1-a292-911608eade61"
        }

        return apicommon.post_req(url, payload, headers)

    #自定义表单提交
    def customForm_action(self):
        url = "http://s2-api.smarket.net.cn/customForm/action"

        payload = "{\r\n  \"customFormId\": \"13323\",\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"referenceUrl\": \"\",\r\n  \"linkId\": \"26892\",\r\n  \"openId\": \"\",\r\n  \"nickName\": \"\",\r\n  \"name\": \"\",\r\n  \"memberId\": \"\",\r\n  \"headImage\": \"\",\r\n  \"city\": \"\",\r\n  \"province\": \"\",\r\n  \"country\": \"\",\r\n  \"items\": [\r\n      {\r\n      \"fieldName\": \"name\",\r\n      \"value\": \"高明\"\r\n    },\r\n    {\r\n      \"fieldName\": \"mobile\",\r\n      \"value\": \"18633873521\"\r\n    },\r\n    {\r\n      \"fieldName\": \"avatar\",\r\n      \"value\": {\r\n        \"fileName\": \"username\",\r\n        \"mapId\": \"9a644a7fea95749f75f8cafffd055055\"\r\n      }\r\n    }\r\n  ],\r\n  \"checkCode\": \"\",\r\n  \"createTime\": \"\",\r\n  \"sess\": \"\",\r\n  \"ver\": \"v2.0.1\",\r\n  \"enteredId\": \"\",\r\n  \"instanceId\": \"\",\r\n  \"url\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e60d0ece-425a-46dd-8a1a-62dc07cf098a"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，获取表单列表
    def customForm_getListByIds(self):

        url = "http://s2-api.smarket.net.cn/customForm/getListByIds"

        payload = "\r\n{\r\n  \"tenantId\": 1116,\r\n  \"customFormIds\": [\r\n    \"5190\"\r\n  ],\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "55f264d4-856f-494d-9920-d5c268b88c30"
        }

        return apicommon.post_req(url, payload, headers)

    #获取渠道追踪代码列表
    def seminar_trackingCode_getList(self):
        url = "http://s2-api.smarket.net.cn/seminar/trackingCode/getList"

        payload = "{\r\n  \"seminarId\": \"4973\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e2ee4792-7cd1-43bd-95d6-7184b1b3f3bb"
        }

        return apicommon.post_req(url, payload, headers)

    #获取每个投票选项的结果数量
    def poll_stat_getResult(self):
        url = "http://s2-api.smarket.net.cn/poll/stat/getResult"

        payload = "{\r\n  \"pollId\": \"2399\",\r\n  \"itemId\": \"5\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "4b98c17d-36b0-4275-bd7e-be5109a8244a"
        }

        return apicommon.post_req(url, payload, headers)

    #获取会议详情
    def seminar_get(self):

        url = "http://s2-api.smarket.net.cn/seminar/get"

        payload = "{\r\n  \"seminarId\": \"4793\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "86bfb1cd-2e01-4230-8501-02331edd7ae0"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，获取nfc绑定关系列表
    def app_seminar_contact_nfc_getList(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/contact/nfc/getList"

        payload = "{\r\n  \"seminarId\": \"4997 \",\r\n  \"lastModify\": \"2018-12-26T18:00:00\",\r\n  \"start\": 0,\r\n  \"num\": 100,\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "5ec5beb5-2bef-4460-bec2-b710b655bdc4"
        }

        return apicommon.post_req(url, payload, headers)

    #报名前验证
    def customForm_checkRegistration(self):

        url = "http://s2-api.smarket.net.cn/customForm/checkRegistration"

        payload = "{\r\n  \"customFormId\": 13788,\r\n  \"moduleType\": \"3\",\r\n  \"cookieId\": \"\",\r\n  \"instanceId\": \"40045\",\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"ver\": \"v2.0.1\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1bd0acd6-af7e-4975-865a-1f4475f1a750"
        }

        return apicommon.post_req(url, payload, headers)

    #会议是否可以报名
    def seminar_register_canRegisterNew(self):
        url = "http://s2-api.smarket.net.cn/seminar/register/canRegisterNew"

        payload = "{\r\n  \"instanceId\": \"40045\",\r\n  \"formId\": \"13788\",\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"openId\": \"\",\r\n  \"needSignupUrl\": \"1\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e4c7a51d-655e-4a72-a22d-d97805ad9b6c"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，创建签到信息
    def app_seminar_signingPoint_checkIn_create(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/signingPoint/checkIn/create"
        #20180704问题同上
        #payload = "{\r\n  \"isValidateCheckIn\": 0,\r\n  \"items\": [\r\n    {\r\n      \"signingPointId\": 1,\r\n      \"contactId\": 1,\r\n      \"checkInType\": \"搜索\",\r\n      \"appId\": \"1\",\r\n      \"checkInTime\": \"2016-02-04T11:32:11\",\r\n      \"seminarId\": 1,\r\n      \"userId\": \"1\",\r\n      \"mediaType\": \"APP\",\r\n      \"passageId\": 1\r\n    },\r\n    {\r\n      \"signingPointId\": 1,\r\n      \"contactId\": 2,\r\n      \"checkInType\": \"二维码\",\r\n      \"appId\": \"1\",\r\n      \"checkInTime\": \"2016-02-04T11:23:11\",\r\n      \"seminarId\": 1,\r\n      \"userId\": \"1\",\r\n      \"mediaType\": \"H5\",\r\n      \"passageId\": 1\r\n    }\r\n  ],\r\n  \"sess\": \""+apicommon.bakSess+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        payload = {
          "isValidateCheckIn": 0,
          "items": [
            {
              "signingPointId": 1,
              "contactId": 1,
              "checkInType": "搜索",
              "appId": "1",
              "checkInTime": "2016-02-04T11:32:11",
              "seminarId": 1,
              "userId": "1",
              "mediaType": "APP",
              "passageId": 1
            },
            {
              "signingPointId": 1,
              "contactId": 2,
              "checkInType": "二维码",
              "appId": "1",
              "checkInTime": "2016-02-04T11:23:11",
              "seminarId": 1,
              "userId": "1",
              "mediaType": "H5",
              "passageId": 1
            }
          ],
          "sess": apicommon.bakSess,
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f02e34f4-88fc-4acc-892e-569860813435"
        }

        return apicommon.post_req(url, payload, headers)

    #报名前验证
    def questionary_tool_checkRegistration(self):
        url = "http://s2-api.smarket.net.cn/questionary/tool/checkRegistration"

        payload = "{\r\n  \"questionnaireId\": \"6390\",\r\n  \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"instanceId\": \"40045\",\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"sess\": \""+apicommon.forntSession+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}\r\n"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "20e88243-636b-463a-a3f6-46b8a66c968a"
        }

        return apicommon.post_req(url, payload, headers)

    #自定义表单发送手机修改密码验证码
    def customForm_sendCheckCode(self):
        url = "http://s2-api.smarket.net.cn/customForm/sendCheckCode"

        payload = "{\r\n  \"customFormId\": 13788,\r\n  \"mobile\": \"13393213135\",\r\n   \"globalUserId\": \"66e086fb9d9364161895e217dda7b5c8\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1c9df15e-043c-45bf-9e71-bc126476992a"
        }

        return apicommon.post_req(url, payload, headers)

    #会议报名接口
    def seminar_contact_registerNew(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/registerNew"

        payload = "{\r\n  \"instanceId\": \"40045\",\r\n  \"formId\": 4278,\r\n  \"channel\": \"\",\r\n  \"globalUserId\": \"\",\r\n  \"weChatId\": \"\",\r\n  \"openId\": \"\",\r\n  \"isPreview\": \"0\",\r\n  \"formData\": [\r\n    {\r\n      \"fieldName\": \"name\",\r\n      \"value\": \"高\"\r\n    },\r\n    {\r\n      \"fieldName\": \"email\",\r\n      \"value\": \"bantenio@gmail.com\"\r\n    }\r\n  ],\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2b89f908-c853-453f-a6c1-f7ef4aae1ac5"
        }

        return apicommon.post_req(url, payload, headers)

    #微信签到
    def seminar_bigScreen_forBigScreenWall_checkIn(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/forBigScreenWall/checkIn"
        #20180704
        #payload = "{  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",  \"nickName\": \"高明啊\",  \"headImgUrl\": \"\",  \"bigScreenId\": \"2863\",  \"contactId\": \"772896\",  \"sess\": \""+apicommon.bakSess+"\",  \"_cache_with_cached\":\"1\",  \"_cache_refresh\":\"1\",  \"_cache_timeout\":\"60\"}"
        payload = {
          "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
          "nickName": "高明啊",
          "headImgUrl": "",
          "bigScreenId": "2863",
          "contactId": "772896",
          "sess": apicommon.bakSess,
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "deefa2b1-2d94-414c-bced-f14cd135b632"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        return apicommon.post_req(url, payload, headers)

    #更新签到大屏信息
    def seminar_bigScreen_updateCheckIn(self):
        url = "http://s2-api.smarket.net.cn/seminar/bigScreen/updateCheckIn"

        payload = "{\r\n  \"seminarId\": 4997,\r\n  \"id\": 1,\r\n  \"name\": \"签到大屏(1)\",\r\n  \"scale\": \"narrow\",\r\n  \"groupId\": \"1\",\r\n  \"signingPointId\": \"1\",\r\n  \"signingPoint\": \"普通签到点\",\r\n  \"checkInByWeChat\": \"on\",\r\n  \"checkInStatus\": \"on\",\r\n  \"status\": \"on\",\r\n  \"onTheWallField\": \"regInfo\",\r\n  \"regOnSite\": \"on\",\r\n  \"regFormId\": \"1\",\r\n  \"regFormName\": \"asd\",\r\n  \"interval\": \"3\",\r\n  \"loop\": \"on\",\r\n  \"isControl\": \"1\",\r\n  \"url\": \"http://www.baidu.com\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "023deb09-dea8-48fd-8cc1-1475deb03128"
        }

        return apicommon.post_req(url, payload, headers)

    #此接口即将过期不在维护，可使用seminar_contact_front_editRegContact标准格式实现

        url = "http://s2-api.smarket.net.cn/seminar/contact/update"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"seminarId\": 4989,\r\n  \"contactId\": 775686,\r\n  \"fields\": {\r\n    \"mobile\": \"18032257279\",\r\n    \"name\": \"柳旦旦\",\r\n    \"email\": \"1064265199@qq.com\",\r\n    \"enterprise\": \"\",\r\n    \"department\": \"销售部\",\r\n    \"industry \": \"制造业\",\r\n    \"position\": \"\",\r\n    \"region\": {\r\n      \"country\": \"中国\",\r\n      \"countryId\": \"1\",\r\n      \"province\": \"北京\",\r\n      \"provinceId\": \"1\",\r\n      \"city\": \"北京\",\r\n      \"cityId\": \"0\"\r\n    }\r\n  },\r\n  \"subSeminars\": [\r\n   5143\r\n  ],\r\n  \"category\": \"\",\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "0c383d03-6e94-4b11-bdb1-ba7e92924f4d"
        }

        return apicommon.post_req(url, payload, headers)

    #浏览投票
    def poll_view(self):
        url = "http://s2-api.smarket.net.cn/poll/view"

        payload = "{\r\n  \"pollId\": 2319,\r\n  \"globalUserId\": \"\",\r\n  \"openId\": \"\",\r\n  \"referenceUrl\": \"\",\r\n  \"url\": \"\",\r\n  \"sess\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "7ef17193-93f9-497c-b6b5-e20de81181ec"
        }

        return apicommon.post_req(url, payload, headers)

    #提交投票
    def poll_action(self):
        url = "http://s2-api.smarket.net.cn/poll/action"

        payload = "{\"globalUserId\":\"6d7c6c1f-a8ee-48e8-89a7-dd9c50ebf63a\",\"city\":\"\",\"country\":\"\",\"gender\":\"\",\"groupId\":\"\",\"groupid\":\"\",\"headImgUrl\":\"\",\"headimgurl\":\"\",\"language\":\"\",\"nickname\":\"\",\"openId\":\"\",\"openid\":\"\",\"authCode\":\"\",\"province\":\"\",\"remark\":\"\",\"sex\":\"\",\"subscribe\":\"\",\"subscribeTime\":\"\",\"subscribe_time\":\"\",\"name\":\"\",\"memberId\":null,\"unique\":\"\",\"uniqueType\":\"\",\"session\":\"\",\"needWechat\":false,\"pollId\":\"2319\",\"referenceUrl\":\"\",\"options\":[{\"fieldName\":\"name\",\"value\":\"邢英丽\"},{\"fieldName\":\"mobile\",\"value\":\"15201232181\"}],\"url\":\"https://f.smarket.net.cn/s/template/2d8786076af18578c93bd945f0681953/view/vote.html?pollId=2319&configId=251376\",\"preview\":0,\"sess\":\"\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"\",\"referenceTitle\":\"\",\"sessionId\":\"ec69f3edd1c9908cb8cfeb1e4528488e\"}}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "f78fc904-e0e7-4642-8989-802d88b6208d"
        }

        return apicommon.post_req(url, payload, headers)

    #提交问卷
    def questionary_reAction(self):
        url = "http://s2-api.smarket.net.cn/questionary/reAction"

        payload = "{\r\n        \"questionaryId\": \"6225\",\r\n        \"globalUserId\": \"544fbf14b96536d1e966ac92e3e98a34\",\r\n        \"referenceUrl\": \"\",\r\n        \"headImgUrl\": \"\",\r\n        \"openId\": \"\",\r\n        \"nickname\": \"\",\r\n        \"gender\": \"\",\r\n        \"city\": \"\",\r\n        \"province\": \"\",\r\n        \"country\": \"\",\r\n        \"preview\": \"\",\r\n        \"instanceId\": \"\",\r\n        \"options\": [\r\n            {\r\n                \"itemId\": \"1\",\r\n                \"options\": [\r\n\r\n                ]\r\n            }\r\n        ]\r\n    }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "c30d7a09-c5c6-45ca-b3b1-5e5474f8eaa3"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某人试卷的试题记录
    def questionary_exam_user_getAnswers(self):
        url = "http://s2-api.smarket.net.cn/questionary/exam/user/getAnswers"

        payload = "{\r\n  \"questionaryId\": \"6225\",\r\n  \"openId\": \"\",\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"isSave\": 1,\r\n  \"isGenerated\": 1,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "51219d57-8bb2-49e6-8173-95eb46d2b1e5"
        }

        return apicommon.post_req(url, payload, headers)

    #用户重复回答试题保留最后一次结果
    def questionary_exam_repeatAction(self):
        url = "http://s2-api.smarket.net.cn/questionary/exam/repeatAction"
        #20180704
        #payload = "{\r\n  \"sess\": \""+apicommon.forntSession+"\",\r\n  \"questionaryId\": 1144,\r\n  \"openId\": \"xxxwsewex\",\r\n  \"globalUserId\": \"1488088356\",\r\n  \"referenceUrl\": \"来源\",\r\n  \"nickName\": \"naonao\",\r\n  \"headImgUrl\": \"http://testf.smarket.net.cn/t/template/1759447356/images/img-success.png\",\r\n  \"gender\": 1,\r\n  \"city\": \"武汉市\",\r\n  \"provice\": \"湖北省\",\r\n  \"country\": \"中国\",\r\n  \"options\": [\r\n    {\r\n      \"id\": 1,\r\n      \"selected\": [\r\n        1,\r\n        2\r\n      ]\r\n    }\r\n  ],\r\n  \"preview\": 0,\r\n  \"isRepeat\": 1,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        payload ={
          "sess": apicommon.forntSession,
          "questionaryId": 1144,
          "openId": "xxxwewex",
          "globalUserId": "1488088356",
          "referenceUrl": "来源",
          "nickName": "naonao",
          "headImgUrl": "http://testf.smarket.net.cn/t/template/1759447356/images/img-success.png",
          "gender": 1,
          "city": "武汉市",
          "provice": "湖北省",
          "country": "中国",
          "options": [
            {
              "id": 1,
              "selected": [
                1,
                2
              ]
            }
          ],
          "preview": 0,
          "isRepeat": 1,
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "d20d621c-9c0b-4393-a3a4-539072a883f4"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        return apicommon.post_req(url, payload, headers)

    #该接口为APP专用接口，项目不要使用，nfc批量绑定
    def app_seminar_contact_nfc_bind(self):
        url = "http://s2-api.smarket.net.cn/app/seminar/contact/nfc/bind"

        payload = "{\r\n  \"items\": [\r\n    {\r\n      \"seminarId\": \"5144\",\r\n      \"chipNo\": \"SDD32232332\",\r\n      \"contactId\": 1,\r\n      \"bindTime\": \"1491374562\"\r\n    },\r\n    {\r\n      \"seminarId\": \"5144\",\r\n      \"chipNo\": \"SDD32232333\",\r\n      \"contactId\": 2,\r\n      \"bindTime\": \"1491374562\"\r\n    }\r\n  ],\r\n  \"sess\": \"" + apicommon.bakSess + "\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "e1327c61-aac0-40e9-bb2d-dbd3744e33ed"
        }

        return apicommon.post_req(url, payload, headers)

    #此接口即将过期不在维护，可使用seminar_contact_front_editRegContact标准格式实现
    def seminar_contact_update(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/update"

        # apicommon.account_login()
        Sesson = apicommon.bakSess
        base_dir=os.path.join(os.path.dirname(__file__), 'token.md')
        with open(base_dir,'r') as f:
            Sesson=f.read()
        print "sesson:",Sesson
        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"seminarId\": 4989,\r\n  \"contactId\": 775686,\r\n  \"fields\": {\r\n    \"mobile\": \"18032257279\",\r\n    \"name\": \"柳旦旦\",\r\n    \"email\": \"1064265199@qq.com\",\r\n    \"enterprise\": \"\",\r\n    \"department\": \"销售部\",\r\n    \"industry \": \"制造业\",\r\n    \"position\": \"\",\r\n    \"region\": {\r\n      \"country\": \"中国\",\r\n      \"countryId\": \"1\",\r\n      \"province\": \"北京\",\r\n      \"provinceId\": \"1\",\r\n      \"city\": \"北京\",\r\n      \"cityId\": \"0\"\r\n    }\r\n  },\r\n  \"subSeminars\": [\r\n  5143 \r\n],\r\n  \"category\": \"\",\r\n  \"sess\": \""+Sesson+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "75f9e7a5-df61-4dec-8078-793acae6ba6d"
        }

        # response = requests.request("POST", url, data=payload, headers=headers)
        return apicommon.post_req(url, payload, headers)


if __name__ == "__main__":
    apicommon.all_login()

    o = ApiRequestsOne()

    # o.member_geneGet_003()
    # o.seminar_subSeminar_frontGet()
    # o.de_contact_getLastSeminarsBySess()
    # o.field_getList()
    # o.shortUrl_getList()
    # o.app_seminar_contact_field_getCustomFields()
    # o.app_seminar_contact_getByUniqueField()
    # o.app_seminar_contact_getList()
    # o.seminar_frontGet()
    # o.app_seminar_contact_getListCompressed()
    # o.app_seminar_contact_prints_getSigningPointInfo()
    # o.app_seminar_getList()
    #o.app_seminar_signingPoint_checkIn_getListCompressed()
    # o.app_seminar_signingPoint_contact_getList()
    # o.app_seminar_signingPoint_getGroupList()
    # o.seminar_bigScreen_forBigScreenWall_getCheckInData()
    # o.seminar_bigScreen_forBigScreenWall_getWapCheckInfo()
    # o.seminar_bigScreen_get()
    # o.seminar_bigScreen_getListByGroup()
    # o.seminar_bigScreen_getPollPreset()
    # o.seminar_contact_front_checkIn()
    # o.seminar_guest_getList()
    # o.seminar_register_getList()
    # o.seminar_signingPoint_getNumberSignInPassage()
    # o.seminar_subSeminar_getListByType()
    # o.seminar_topicTemplate_seminar_getFormInfo()
    # o.seminar_topicTemplate_seminar_getWithAllSub()
    # o.questionary_action()
    o.questionary_exam_action()
    # o.questionary_get()
    # o.questionary_getList()
    # o.questionary_HasParticipation()
    # o.poll_get()
    # o.customForm_get()
    # o.seminar_frontGetList()
    # o.questionary_view()
    # o.seminar_contact_getContactToWechat()
    # o.seminar_contact_front_getCommonContactInfo()
    #o.seminar_bigScreen_updateMessage()
    # o.seminar_topicTemplate_contact_get()
    # o.seminar_register_canRegister()
    # o.de_contact_front_get()
    # o.customForm_view()
    # o.questionary_exam_user_getSingleResult()
    # o.questionary_exam_user_GenerateExam()
    # o.seminar_signingPoint_checkIn_getCheckInCount()
    # o.seminar_topicTemplate_contact_getByOpenId()
    # o.seminar_register_getSubList()
    # o.seminar_contact_setContactToWechat()
    # o.seminar_bigScreen_updateLottery()
    # o.customForm_checkRepeatable()
    # o.seminar_contact_front_getRegContact()
    #o.seminar_contact_front_regSeminar()
    # o.customForm_user_getResultByOpenId()
    # o.customForm_action()
    # o.customForm_getListByIds()
    # o.seminar_trackingCode_getList()
    # o.poll_stat_getResult()
    # o.seminar_get()
    # o.app_seminar_contact_nfc_getList()
    # o.customForm_checkRegistration()
    # o.seminar_register_canRegisterNew()
    #o.app_seminar_signingPoint_checkIn_create()
    # o.questionary_tool_checkRegistration()
    # o.customForm_sendCheckCode()
    #o.seminar_contact_registerNew()
    #o.seminar_contact_register()
    #o.seminar_bigScreen_forBigScreenWall_checkIn()
    # o.seminar_contact_update()
    # o.seminar_bigScreen_updateCheckIn()
    # o.poll_view()
    # o.poll_action()
    # o.questionary_reAction()
    # o.questionary_exam_user_getAnswers()
    # o.questionary_exam_repeatAction()
    # o.app_seminar_contact_nfc_bind()
    #






