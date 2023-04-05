
from .models import UserModel
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        # bio = request.POST.get('bio', '')
    if password != password2:
        return render(request, 'accounts/signup.html')
    else:
        UserModel.objects.create_user(username=username, password=password)
        return redirect ('/login')

def user_login(request):
    return render(request, 'accounts/login.html')


def user_logout(request):
    # 로그아웃 view
    pass