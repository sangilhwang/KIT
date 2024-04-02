from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("타이틀", max_length=30)
    content = models.TextField("내용", blank=True)
    created_at = models.DateTimeField("작성일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정일시", auto_now=True)

    def __str__(self):
        return f"[{self.id}]{self.title}"
    
    def get_absolute_url(self):
        return f"/blog/{self.pk}/"