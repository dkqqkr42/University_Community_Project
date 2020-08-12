from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse # JSON 응답
from map.models import Point
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
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
