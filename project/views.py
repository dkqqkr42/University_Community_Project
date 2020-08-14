from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from signin.models import User, Article
from map.models import Point
from django.http import JsonResponse # JSON 응답
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import Paginator
import smtplib
from email.mime.text import MIMEText
# import requests
# from bs4 import BeautifulSoup


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
            # messages.info(request, '아이디나 비밀번호가 다릅니다.')
            return HttpResponse('<script>alert("아이디나 비밀번호가 다릅니다.");history.back()</script>')

    return render(request, 'signin.html')

def map(request):
    return render(request, 'map.html')              # map 생성

 
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
    type = request.GET.get('type')
    q = request.GET.get('q')
    if type == 'title':
        article_list = Article.objects.filter(title__contains=q).order_by('-id')
    # article_list = Article.objects.all().order_by('-id')
    else:
        if not q:
            q = ''
        article_list = Article.objects.filter(content__contains=q).order_by('-id')
    paginator = Paginator(article_list, 5)
    page = int(request.GET.get('p', 1))
    posts = paginator.get_page(page)
    return render(request, "board.html", {'article_list' : article_list, 'posts' : posts})

def write(request):
    if not request.session.session_key:
        return HttpResponse('<script>alert("권한이 없습니다.");history.back()</script>')
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
            return HttpResponse('<script>alert("글 작성이 완료되었습니다.");history.back()</script>')
        except:
            return HttpResponse('<script>alert("로그인 후 이용해주세요.");history.back()</script>')
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
            return HttpResponse('<script>alert("수정되었습니다.");history.back()</script>')
        except:
            return HttpResponse('<script>alert("수정할 수 없습니다.");history.back()</script>')
    context = {
        'article' : article
    }
    return render(request, 'update.html', context)

def delete(request, id):
    try:
        # select * from article where id = ?
        article = Article.objects.get(id=id)
        article.delete()
        return HttpResponse('<script>alert("삭제되었습니다.");history.back()</script>')
    except:
        return HttpResponse('<script>alert("삭제할 수 없습니다.");history.back()</script>')

def signout(request):
    del request.session['userID'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return HttpResponse('<script>alert("로그아웃 되었습니다.");history.back()</script>')
  
def map_data(request):
    list = Point.objects.all()
    data = []
    for li in list:
        li = model_to_dict(li)
        data.append(li)
    return JsonResponse(data, safe=False)


def help(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        email = 'chojaelong@gmail.com'
        # 발신자주소, 수신자주소, 메시지
        send_mail(email, title, comment)
        return HttpResponse('<script>alert("메일이 전송되었습니다 소중한 의견 감사합니다.");history.back()</script>')
    return render(request, 'help.html')

def send_mail(email, title, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # SMTP 설정
    smtp.login(email, 'lpzloitdranbjwro')  # 인증정보 설정
    msg = MIMEText(msg)
    msg['Subject'] = '[웹페이지 문의사항]' + title  # 제목
    msg['To'] = email  # 수신 이메일
    smtp.sendmail(email, email, msg.as_string())
    smtp.quit()

# def food(soup):
#     req = requests.get('http://www.andong.ac.kr/main/module/foodMenu/index.do?menu_idx=222')
#     html = req.text
#     soup = BeautifulSoup(html, 'html.parser')
#     my_titles = soup.select('h3 > a')
#     data = {}
#     for title in my_titles:
#         data[title.text] = title.get('href')
#     return render(soup, 'food.html', data)


# def food(request):
#     result = requests.get('http://www.andong.ac.kr/main/module/foodMenu/index.do?menu_idx=222')
#     result.encoding = 'utf-8'
#     result = result.text
#     s_table = 0
#     e_table = 0
#     star = ["","","","","","","","","","","","","","",]
#     i=0
#     while True:
#         s_table = result.find('<table',e_table)
#         s_table = result.find('>',s_table)        
#         if s_table == -1:
#             break
#         e_table = result.find('</table>',s_table)
#         star[i] += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
#         i+=1
#     r_ta = {
#         'contact' : star[0],
#         'contact1' : star[1],
#         'contact2' : star[2],
#         'contact3' : star[3],
#         'contact4' : star[4],
#         'contact5' : star[5],
#         'contact6' : star[6],
#     }
#     return render(request, 'food.html',r_ta)
