
from .models import UserModel
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

    if password != password2:
        return render(request, 'accounts/signup.html', {'error': '패스워드를 다시 입력해 주세요.'})
    elif username == '' or password == '':
        return render(request, 'accounts/signup.html', {'error': '이름과 비밀번호는 필수입니다.'})
    else:
        exist_user = get_user_model().objects.filter(username=username)
        if exist_user:
            return render(request, 'accounts/signup.html', {'error': '이미 등록된 이름입니다.'})

        UserModel.objects.create_user(username=username, password=password)
        return redirect('/login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': '이름 혹은 패스워드를 확인해주세요.'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/login.html')


@login_required()
def user_logout(request):
    auth.logout(request)
    return redirect('/')


# 실제 코드 흐름 > url주소를 지정하면 > view함수 > templates

# view함수 - 먼저 네이밍만 한다. > html에서 메소드와 액션을 추가
# > form을 생각하며 어떤 값들을 html에서 넘겨주는가?를 생각하면서 view함수를 작성
# >
