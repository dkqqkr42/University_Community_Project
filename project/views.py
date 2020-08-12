from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from article.models import User, Article
from django.http import JsonResponse # JSON 응답
from map.models import Point
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'index.html')

<<<<<<< HEAD
def signup(request):
    # 실제 데이터베이스에 데이터를 저장 (회원가입)
    if request.method == 'POST':
        # 회원정보 저장
        email = request.POST.get('email')
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user = User(email=email, name=name, pwd=pwd)
        user.save()
        return HttpResponseRedirect('/index/')

    # 회원가입을 위한 양식(HTML)전송
    return render(request, 'signup.html')

def id_overlap_check(request):
    username = request.GET.get('username')
    try:
        # 중복 검사 실패
        user = User.objects.get(username=username)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'overlap': overlap}
    return JsonResponse(context)   

def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(email=email, pwd=pwd)
            # 정보표시
            request.session['email'] = email
            return render(request, 'signin_success.html')
        except:
            return render(request, 'signin_fail.html')

    return render(request, 'signin.html')

def signout(request):
    del request.session['email'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return HttpResponseRedirect('/index/')
=======
def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')
>>>>>>> 4215dca3659a03611c601ff70e3df0f3fda99850
