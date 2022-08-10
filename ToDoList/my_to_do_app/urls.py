# my_to_do_app > urls.py

from django.urls import path
from . import views # my_to_do_app > views.py

urlpatterns = [
    # http://127.0.0.1:8000 요청이 넘어오면 views.py 파일의 index 함수가 응답(호출해야함)
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/createTodo 요청이 넘어오면 views.py 파일의 createTodo 함수가 응답(호출해야함)
    path('createTodo/',views.createTodo, name='createTodo'),
]
