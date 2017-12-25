from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .models import User, Store
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
from django.contrib import auth

def md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.get(username= username):
            request.session['username'] = username
            return HttpResponseRedirect('/')
        return HttpResponse(u'Error')
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        psd = request.POST['password']
        re_pass = request.POST['re_password']
        if psd != re_pass:
            return HttpResponse(u'两次密码填写不正确')
        password = md5(psd + 'the-Salt')
        User(username= username, password= password).save()
    return HttpResponseRedirect('/')


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
        return Response(session)
    except:
        return Response('null')


# Create your views here.
