from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField("제목", max_length = 100)
    description = models.TextField("설명", blank = True)
    created = models.DateTimeField("생성 일시", auto_now_add = True)
    completed = models.BooleanField("완료 여부", default = False)
    important = models.BooleanField("중요 여부", default = False)


# 3. Todo 모델 생성

# - title : Todo의 제목(최대 길이 100, 문자열)
# - description : Todo에 대한 설명(길이 제한 없음, 빈값 허용)
# - created : Todo 생성 일자(시간+날짜, 생성 일자 자동 입력)
# - complete : Todo 완료 여부(기본값:False)
# - important : Todo 중요 여부(기본값:False)