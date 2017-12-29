from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .models import User, Store
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
from django.contrib import auth


# 邮件发送
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
import smtplib


# 邮件发送模块
def send_email(to):
    from_addr = '1657586283@qq.com'
    password = 'mbibvoszlbkjciai'
    smtp_server = 'smtp.qq.com'
    to = to
    msg = MIMEText('点击<a href="http://localhost:8080/is_active">www.yendnx.club</a>完成注册', 'html', 'utf-8')
    msg['From'] = 'yendnx.club'
    msg['To'] = '注册用户'
    msg['Subject'] = Header('确认邮件', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to], msg.as_string())
    server.quit()

# 算法加盐模块
def md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# 登陆用户
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_list = User.objects.get(username= username)
        psw = md5(password + 'the-Salt')
        if psw == user_list.password:
            request.session['username'] = username
            return HttpResponseRedirect('/')
        return HttpResponse(u'Error')
    return HttpResponseRedirect('/')


# 注册用户
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        psd = request.POST['password']
        re_pass = request.POST['re_password']
        if psd != re_pass:
            return HttpResponse(u'两次密码填写不正确')
        password = md5(psd + 'the-Salt')
        User(username= username, password= password, email=email, is_avtive=False).save()
        send_email(email)
        # 注册用户时方便邮箱验证所以设置session
        request.session['username'] = username
    return HttpResponseRedirect('/complete')


# 邮箱验证
def is_active(request):
    # 获取session值
    value = request.session['username']
    print(value)
    User.objects.filter(username=value).update(is_avtive=True)
    return HttpResponseRedirect('/')


#退出登陆
def signout(request):
    auth.logout(request)
    try:
        del request.session['username']
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')


def index(request):
    if request.method == 'GET':
        data = Store.objects.all()
        print(data)
        return render(request, 'index.html', {'list': data})


@api_view(['GET'])
def session(request):
    try:
        session = request.session['username']
        # 向前台发送数据
        return Response(session)
    except:
        return Response('null')


class Sess(object):
    def sess(self, request):
        Value = request.session['username']
        return Value


se = Sess()


def car(request):
    if request.method == 'POST':
        store_name = request.POST['store_name']
        image = request.POST['image']
        unit = request.POST['unit']
        print([store_name])
        return HttpResponse(u'OK')


# Create your views here.
