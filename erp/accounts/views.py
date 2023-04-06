
from .models import UserModel
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


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
        return redirect('/login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session['user'] = me.username
            return redirect('/')
        else:
            return redirect('/login')
    elif request.method == 'GET':
        return render(request, 'erp/product_list.html')


def user_logout(request):
    # 로그아웃 view
    pass


# 실제 코드 흐름 > url주소를 지정하면 > view함수 > templates

# view함수 - 먼저 네이밍만 한다. > html에서 메소드와 액션을 추가
# > form을 생각하며 어떤 값들을 html에서 넘겨주는가?를 생각하면서 view함수를 작성
# >
