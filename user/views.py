import random
from django.contrib.auth import authenticate, login, logout
from wumai.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, reverse
from user.forms import UserRegisterForm, UserForgetForm, UserLoginForm
from user.models import UserProfile, EmailVerify


# Create your views here.
def user_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'register.html', {'user_register_form': user_register_form})
    else:
        user = UserRegisterForm(request.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            email = user.cleaned_data['email']
            password = user.cleaned_data['password']
            u = UserProfile.objects.filter(Q(username=username) | Q(email=email))
            if u:
                return render(request, 'register.html', {'msg': '此用户名或邮箱已被注册'})
            else:
                user_profile = UserProfile()
                user_profile.email = email
                user_profile.username = username
                user_profile.set_password(password)
                user_profile.is_active = 0
                user_profile.save()
                send_email(email, 'register')
                return HttpResponse('注册成功，去激活吧！ <a href="http://123.56.23.97">回到首页</a>')
        else:
            return render(request, 'register.html', {'user_register_form': user})


def user_active(request, code):
    if code:
        emailobj = EmailVerify.objects.filter(code=code)
        if emailobj:
            email = emailobj[0].email
            user = UserProfile.objects.filter(email=email)
            if user:
                user[0].is_active = 1
                user[0].save()
                return render(request, 'index.html')
            else:
                return HttpResponse('邮箱激活失败！')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active == 1:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    return HttpResponse('账号还未激活！')
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误'})
        else:
            return render(request, 'login.html', {'user_form': user_form})


def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect(reverse('index'))


def user_forget(request):
    if request.method == 'GET':
        user_forget_form = UserForgetForm()
        return render(request, 'forget.html', {'user_forget_form': user_forget_form})
    else:
        user_form = UserForgetForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            user = UserProfile.objects.filter(email=email)
            if user:
                send_email(email, 'update')
                return HttpResponse('快去邮箱点击链接吧！')
            else:
                return render(request, 'forget.html', {'msg': '无此邮箱'})
        else:
            return render(request, 'forget.html', {'user_form': user_form})


def get_random(length):
    str0 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(length):
        ran = random.randint(0, len(str0) - 1)
        code += str0[ran]
    return code


def send_email(email, send_type):
    code = get_random(8)
    email_verify = EmailVerify()
    email_verify.email = email
    email_verify.code = code
    email_verify.send_type = send_type
    email_verify.save()
    if send_type == 'register':
        subject = '欢迎注册中国雾霾网'
        content = 'http://123.56.23.97/user/active/' + code
        send_mail(subject, content, EMAIL_HOST_USER, [email, ], html_message=content)
    if send_type == 'update':
        subject = '正在修改密码'
        content = 'http://123.56.23.97/user/password_reset/' + code
        send_mail(subject, content, EMAIL_HOST_USER, [email, ], html_message=content)

