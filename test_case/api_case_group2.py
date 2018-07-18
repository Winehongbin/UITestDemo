# -*- coding: utf-8 -*-
"""
os模块就是对操作系统进行操作，比如取文件的路径。

sys模块提供了一系列有关Python运行环境的变量和函数,例如：
#生成报告是报错，编码错误。python2.7默认使用ascii，设置成utf-8，python2.7以后不用setdefaultencoding了
   reload(sys)
  sys.setdefaultencoding('utf8')
"""
import sys
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import os
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import time
import unittest
from common.report import report
from pages.common_pages.login_page import LoginPage
from pages.api.group2 import ApiRequestsTwo
from pages.api import apicommon
from common.mail import email_oper
from pages.api.group1 import ApiRequestsOne
from pages.api.group3 import ApiRequestsThree
from pages.api.group4 import ApiRequestsfoureFour
"""
王亮开发组
"""


class Api_Case_Group2(unittest.TestCase):
    """ 接口自动化二组测试用例 """
    def setUp(self):
        if apicommon.all_login() == 1:
            print "successful"
        else:
            print "get login session error"
    def test_001_interaction_getCountByType(self):
        """获取实例的行为记录数量"""

        object = ApiRequestsTwo()
        # object.interaction_getCountByType()
        actual_result,desc = object.interaction_getCountByType()
        
        self.assertEqual(actual_result, 0, desc)


    def test_003_member_geneGet(self):
        """根据已登录的session获取用户信息"""
        object = ApiRequestsTwo()
        # object.member_geneGet()
        actual_result,desc = object.member_geneGet()
        
        self.assertEqual(actual_result, 0, desc)

    def test_004_account_login(self):
        """登陆管理后台"""
        object = ApiRequestsTwo()
        # object.account_login()
        actual_result,desc = object.account_login()
        
        self.assertEqual(actual_result, 0, desc)

    def test_005_member_changePwd(self):
        """前台用户修改密码"""
        object = ApiRequestsTwo()
        # object.member_changePwd()
        actual_result,desc = object.member_changePwd()
        
        self.assertEqual(actual_result, 0, desc)

    def test_006_dic_params_getList(self):
        """获取字典值列表"""
        object = ApiRequestsTwo()
        # object.dic_params_getList()
        actual_result,desc = object.dic_params_getList()
        
        self.assertEqual(actual_result, 0, desc)

    def test_007_anonymous_getId(self):
        """获取一个全局用户Id（cookieId）"""
        object = ApiRequestsTwo()
        # object.anonymous_getId()
        actual_result,desc = object.anonymous_getId()
        
        self.assertEqual(actual_result, 0, desc)

    def test_008_interaction_record(self):
        """记录一个互动"""
        object = ApiRequestsTwo()
        # object.interaction_record()
        actual_result,desc = object.interaction_record()
        
        self.assertEqual(actual_result, 0, desc)

    def test_009_member_form_get(self):
        """获取表单信息"""
        object = ApiRequestsTwo()
        # object.member_form_get()
        actual_result,desc = object.member_form_get()
        
        self.assertEqual(actual_result, 0, desc)

    def test_010_member_geneUpdate(self):
        """更新注册用户信息"""
        object = ApiRequestsTwo()
        # object.member_geneUpdate()
        actual_result,desc = object.member_geneUpdate()
        
        self.assertEqual(actual_result, 0, desc)

    def test_011_anonymous_checkSess(self):
        """验证前台sess"""
        object = ApiRequestsTwo()
        # object.anonymous_checkSess()
        actual_result,desc = object.anonymous_checkSess()
        
        self.assertEqual(actual_result, 0, desc)

    def test_012_member_geneGet(self):
        """根据已登录的session获取用户信息"""
        object = ApiRequestsTwo()
        # object.member_geneGet()
        actual_result,desc = object.member_geneGet()
        
        self.assertEqual(actual_result, 0, desc)

    def test_013_member_checkUnique(self):
        """检测用户唯一，检测字段值唯一"""
        object = ApiRequestsTwo()
        # object.member_checkUnique()
        actual_result,desc = object.member_checkUnique()
        
        self.assertEqual(actual_result, 0, desc)

    def test_014_account_channel_get(self):
        """获取实例详情信息"""
        object = ApiRequestsTwo()
        # object.account_channel_get()
        actual_result,desc = object.account_channel_get()
        
        self.assertEqual(actual_result, 0, desc)

    def test_015_member_form_search(self):
        """查询符合条件的表单"""
        object = ApiRequestsTwo()
        # object.member_form_search()
        actual_result,desc = object.member_form_search()
        
        self.assertEqual(actual_result, 0, desc)

    def test_016_member_get(self):
        """根据已登录的session获取用户信息"""
        object = ApiRequestsTwo()
        # object.member_get()
        actual_result,desc = object.member_get()
        
        self.assertEqual(actual_result, 0, desc)

    def test_017_member_loginByOpenId(self):
        """使用openId登录，如果未登录会返回绑定使用的authCode"""
        object = ApiRequestsTwo()
        # object.member_loginByOpenId()
        actual_result,desc = object.member_loginByOpenId()
        
        self.assertEqual(actual_result, 0, desc)

    def test_018_member_geneRegister(self):
        """注册用户"""
        object = ApiRequestsTwo()
        # object.member_geneRegister()
        actual_result,desc = object.member_geneRegister()
        
        self.assertEqual(actual_result, 0, desc)

    def test_019_interaction_getDetailList(self):
        """获取租户下一个用户的某类型的互动记录"""
        object = ApiRequestsTwo()
        # object.interaction_getDetailList()
        actual_result,desc = object.interaction_getDetailList()
        
        self.assertEqual(actual_result, 0, desc)

    def test_020_interaction_getStatCountList(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，获取用户在实例中的（浏览/分享/资料）计数"""
        object = ApiRequestsTwo()
        # object.interaction_getStatCountList()
        actual_result,desc = object.interaction_getStatCountList()
        
        self.assertEqual(actual_result, 0, desc)

    def test_021_member_form_getTemplate(self):
        """获取表单模板信息"""
        object = ApiRequestsTwo()
        # object.member_form_getTemplate()
        actual_result,desc = object.member_form_getTemplate()
        
        self.assertEqual(actual_result, 0, desc)

    def test_022_member_sendVerificationCodeToMail(self):
        """向用户邮箱发送验证码"""
        object = ApiRequestsTwo()
        # object.member_sendVerificationCodeToMail()
        actual_result,desc = object.member_sendVerificationCodeToMail()
        
        self.assertEqual(actual_result, 0, desc)

    def test_023_dic_params_getTree(self):
        """获取字典树形结构"""
        object = ApiRequestsTwo()
        # object.dic_params_getTree()
        actual_result,desc = object.dic_params_getTree()
        
        self.assertEqual(actual_result, 0, desc)

    def test_024_member_form_view(self):
        """注册表单浏览"""
        object = ApiRequestsTwo()
        # object.member_form_view()
        actual_result,desc = object.member_form_view()
        
        self.assertEqual(actual_result, 0, desc)

    def test_025_member_getById(self):
        """获取某个会员信息"""
        object = ApiRequestsTwo()
        # object.member_getById()
        actual_result,desc = object.member_getById()
        
        self.assertEqual(actual_result, 0, desc)

    def test_026_account_getAuth(self):
        """获取验证信息"""
        object = ApiRequestsTwo()
        # object.account_getAuth()
        actual_result,desc = object.account_getAuth()
        
        self.assertEqual(actual_result, 0, desc)

    def test_027_member_register(self):
        """注册"""
        object = ApiRequestsTwo()

        actual_result,desc = object.member_register()
        
        self.assertEqual(actual_result, 0, desc)

    def test_028_member_identification_information_GetByOpenId(self):
        """通过openId获取注册信息"""
        object = ApiRequestsTwo()
        # object.member_identification_information_GetByOpenId()
        actual_result,desc = object.member_identification_information_GetByOpenId()
        
        self.assertEqual(actual_result, 0, desc)

    def test_029_member_schema_field_sorting_GetList(self):
        """获取身份标识字段列表"""
        object = ApiRequestsTwo()
        # object.member_schema_field_sorting_GetList()
        actual_result,desc = object.member_schema_field_sorting_GetList()
        
        self.assertEqual(actual_result, 0, desc)

    def test_30_account_getAuthByInstance(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，通过实例获取验证信息"""
        object = ApiRequestsTwo()
        # object.account_getAuthByInstance()
        actual_result,desc = object.account_getAuthByInstance()
        
        self.assertEqual(actual_result, 0, desc)

    def test_31_collect_search(self):
        """查询收藏的信息列表"""
        object = ApiRequestsTwo()
        # object.collect_search()
        actual_result,desc = object.collect_search()
        
        self.assertEqual(actual_result, 0, desc)

    def test_32_member_sendCheckCode(self):
        """身份认证体系发送手机修改密码验证码(member_sendCheckCode)新加的接口增加前端的控制（有效期和重发时间）"""
        object = ApiRequestsTwo()
        # object.member_sendCheckCode()
        actual_result,desc = object.member_sendCheckCode()
        
        self.assertEqual(actual_result, 0, desc)

    def test_33_member_updateByField(self):
        """会员修改，只修改给定的字段.需要登录"""
        object = ApiRequestsTwo()
        # object.member_updateByField()
        actual_result,desc = object.member_updateByField()
        
        self.assertEqual(actual_result, 0, desc)

    # def test_34_interaction_getCountByType(self):  重复
    #     """获取实例的行为记录数量"""
    #     object = ApiRequestsTwo()
    #     object.interaction_getCountByType()
    #     actual_result,desc = object.interaction_getCountByType()
        
        self.assertEqual(actual_result, 0, desc)

    def test_35_member_getImageCode(self):
        """获取一个图片验证码"""
        object = ApiRequestsTwo()
        # object.member_getImageCode()
        actual_result = object.member_getImageCode()
        
        self.assertEqual(actual_result,200)

    def test_35_account_verifySession(self):
        """验证session,并获取相应的信息"""
        object = ApiRequestsTwo()
        # object.account_verifySession()
        actual_result,desc = object.account_verifySession()
        
        self.assertEqual(actual_result, 0, desc)



if __name__ == "__main__":
    #全部用例按照数字顺序测试
    #unittest.main()
    StartTime = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Api_Case_Group2("test_35_account_verifySession"))



    #执行单元测试，生成报告
    AddSuite = report.AllReport()
    AddSuite.onlyneed_suite(suite)

    #发送邮件
    EndTime = time.time()
    PerformTime = EndTime - StartTime
    content ="test_createoffline"

    # SendEmail = email.SendEmailModel()
    SendEmail = email_oper.SendEmailModel()
    #SendEmail.postreport_only(PerformTime,content)

