#coding=utf-8
'''
此模块用来装页面的元素定位的文本

'''''

class  Page_elem(object):
    #1.登录账号元素
    userName = ["id", "userAccount"]
    #2.登录密码元素
    passwd = ["id", "loginPwd"]
    #3.登录按钮元素
    loginbtn = ["id", "loginBtn"]
    #4.点击用户中心
    user_center = ["class","icon-user"]
    #5.点击用户管理
    user_manage = ["xpath","//*[@id='menu-user']/dd/ul/li[1]/a"]
    #6.进入iframe框
    iframe = ["name",'/cms/manage/user-list.html']
    #7.添加用户
    add_user = ["xpath", '/html/body/div/div[2]/span[1]/a[2]']
p=Page_elem()


















