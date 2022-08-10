# my_to_do_app > views.py
# url 요청이 들어오면 응답하는 처리 함수 구성
from django.shortcuts import render

# request가 들어오면 HttpResponse를 임의로 만들어 강제 응답할 때 사용
from django.http import HttpResponse
from .models import *
# Create your views here.
# request 변수는 클라이언트가 요청 시 전송한 모든 data를 받는 변수(사용자 입력 값도 포함)

# def index(request):
    # http://127.0.0.1:8000 요청에 대응하는 응답 객체를 반환
    # return HttpResponse("my_to_do_app 첫번째 페이지를 응답합니다.")

def index(request):
    # http://127.0.0.1:8000 요청에 대응하는 HTML 페이지를 반환
    return render(request,'my_to_do_app/index.html')

# def createTodo(request):
#     # 임의의 문자열로 응답
#     return HttpResponse("createTodo 작성합시다. 메모하기 버튼을 눌렀습니다.")

def createTodo(request):
    # 사용자의 메모 입력칸에 입력하여 전송된 내용을 응답(출력)
    # input 태그의 name 속성의 값(변수)에 담아 전달됨
    # input 태그의 설정: name = "todoContent", method = "Post"
    # 변수 todoContent에 있는 값을 POST 형식으로 추출해야 함
    # 클라이언트가 보낸 정보는 request 안에 다 들어있음
    user_input_str = request.POST['todoContent']
    # DB 저장하기 위한 모델 객체 생성
    new_todo = Todo(content=user_input_str)
    # DB 테이블 내 컬럼 content에 저장
    new_todo.save()
    return HttpResponse("DB에 저장했습니다." + user_input_str)

