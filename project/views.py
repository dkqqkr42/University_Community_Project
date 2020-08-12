from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from signin.models import User, Article
from map.models import Point
from django.http import JsonResponse # JSON 응답
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        userID = request.POST.get('userID')
        userPassword = request.POST.get('userPassword')
        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(userID=userID, userPassword=userPassword)
            # 정보표시
            request.session['userID'] = userID
            return render(request, 'index.html')
        except:
            messages.info(request, '아이디나 비밀번호가 다릅니다.')
            return HttpResponseRedirect('/signin/')

    return render(request, 'signin.html')

def map(request):
    return render(request, 'map.html')              # map 생성

def map_data(request):
    data = Point.objects.all()
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    map_list = []
    for d in data:
        d = model_to_dict(d) # QuerySet -> Dict
        dist = distance(float(lat), float(lng), d['lat'], d['lng'])
        map_list.append(d)
    # dict가 아닌 자료는 항상 safe=False 옵션 사용
    return JsonResponse(map_list, safe=False)
    
def signup(request):
    if request.method == 'POST':
        userID = request.POST.get("userID")
        userPassword = request.POST.get("userPassword")
        userName = request.POST.get("userName")
        userEmail = request.POST.get("userEmail")
        userGender = request.POST.get("userGender")
        user = User(userID=userID, userPassword=userPassword, userName=userName, userEmail=userEmail, userGender=userGender)
        user.save()
        return HttpResponseRedirect('/index/')

    # if User.objects.filter(userID=userID).exists():
    #     return HttpResponse('이미 사용중입니다.')

    return render(request, 'signup.html')

def board(request):
    # select * from article order by id desc
    article_list = Article.objects.order_by('-id')
    context = {'article_list' : article_list}
    page = int(request.GET.get('p', 1)) #없으면 1로 지정
    paginator = Paginator(article_list, 5) #한 페이지 당 몇개 씩 보여줄 지 지정 
    return render(request, 'board.html', context)

def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        try:
            userID = request.session['userID']
            # select * from user where email = ?
            user = User.objects.get(userID=userID)

            # insert into article (title, content, user_id) values (?, ?, ?)
            article = Article(title=title, content=content, user=user)
            article.save()
            return render(request, 'write_success.html')
        except:
            return render(request, 'write_fail.html')
    return render(request, 'write.html')


def detail(request, id):

    # select * from article where id = ?
    article = Article.objects.get(id=id)
    context = {
    'article' : article
    }
    return render(request, 'detail.html', context)

def update(request, id):

    # select * from article where id = ?
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            article.title = title
            article.content = content
            article.save()
            return render(request, 'update_success.html')
        except:
            return render(request, 'update_fail.html')
    context = {
        'article' : article
    }
    return render(request, 'update.html', context)

def delete(request, id):
    try:
        # select * from article where id = ?
        article = Article.objects.get(id=id)
        article.delete()
        return render(request, 'delete_success.html')
    except:
        return render(request, 'delete_fail.html')

def signout(request):
    del request.session['userID'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return HttpResponseRedirect('/index/')
  
def map_data(request):
    list = Point.objects.all()
    data = []
    for li in list:
        li = model_to_dict(li)
        data.append(li)
    return JsonResponse(data, safe=False)