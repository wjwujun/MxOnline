from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic.base import View
from  django.contrib.auth.hashers import make_password

from  .form   import   LoginForm,RegisterForm,ForgetForm,ModifyPwdForm
from  .models import UserProfile
from users.models import EmailVerifyRecord

from utils.email_send import send_rigister_email

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})
    def post(self,request):
            login_form=LoginForm(request.POST)
            if login_form.is_valid():
                user_name = request.POST.get('username', '')
                pass_word = request.POST.get('password', '')
                user = authenticate(username=user_name, password=pass_word)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return render(request, 'index.html')
                    else:
                        return render(request, 'login.html', {'msg': "用户未激活"})
                else:
                    return render(request, 'login.html', {'msg':"用户名或者密码错误"})
            else:
                return render(request, 'login.html', {'login_form':login_form})

class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form':register_form,'msg':"用户名已存在"})
            pass_word = request.POST.get('password', '')
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.password=make_password(pass_word)
            user_profile.save()

            send_rigister_email(user_name,'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form':register_form})

class ActiveView(View):
    def get(self,request,active_code):
        all_records=EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email=record.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = RegisterForm()
        return render(request, 'forgetpwd.html', {'forget_form':forget_form})
    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email=request.POST.get('email', '')
            send_rigister_email(email, 'forget')
            return render(request, 'success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})



class ResetView(View):
    def get(self,request,active_code):
        all_records=EmailVerifyRecord.objects.filter(code=active_code)
        print(active_code)
        if all_records:
            for record in all_records:
                email=record.email
                return render(request, 'password_reset.html',{'email':email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')

class ModifyPwdView(View):
    def post(self,request):
        modify_form=ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1=request.POST.get('password1','')
            pwd2=request.POST.get('password2','')
            email=request.POST.get('email','')
            print(pwd1,pwd2,email)

            if pwd1!=pwd2:
                return render(request,'password_reset.html',{'email':email,'msg':"两次密码不一致"})

            user=UserProfile.objects.filter(email=email)
            user.password=make_password(pwd2)
            user.update()
            return render(request,'login.html')
        else:
            email=request.POST.get('email','')
            return render(request,"password_reset.html",{'email':email,'modify_form':modify_form})







