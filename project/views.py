from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from signin.models import User
from django.http import JsonResponse # JSON 응답
from django.forms.models import model_to_dict

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
            return render(request, '/index/')
        except:
            return render(request, 'signin_fail.html')

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
        if(dist <= 150): # 10km 이내의 장소만 응답결과로 저장
            map_list.append(d)
    # dict가 아닌 자료는 항상 safe=False 옵션 사용
    return JsonResponse(map_list, safe=False)
def signup(request):
<<<<<<< HEAD
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
  
=======
    return render(request, 'signup.html')
>>>>>>> 45c26b7f7d7126df42c7f96e592be1c7a662390d
