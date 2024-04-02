from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length = 20)
    price = models.IntegerField(default = 0)
    calories = models.IntegerField(default = 0)
    
# 목록 페이지에서 대표로 표시될 약칭을 지정해준다
    def __str__(self):
        return self.name