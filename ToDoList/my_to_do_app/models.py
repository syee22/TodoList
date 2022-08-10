# models 클래싀 db와 관련된 최상위 클래스
# 앱에 필요한 db의 모델 구성: 클래스로 구성
# 앱에 필요한 db 모델을 구성하기 위해서는 models.Model을 상속받아야 함
from django.db import models

# Create your models here.
class Todo(models.Model):
    # table을 구성
    # 테이블의 컬럼(필드)을 속성 설정
    # 앱이름클래스명 연결해서 테이블명을 만든
    # my_to_do_app_todo 테이블이 생성됨
    # 생성된 테이블 정보 확인: dbshell에서 PRAGMA table_info(my_to_do_app_todo);
    # DB 테이블 안에 저장된 행(레코드) 확인: dbshell에서 select * from my_to_do_app_todo;
    content = models.CharField(max_length=255) # CharField: 문자열(character field)
