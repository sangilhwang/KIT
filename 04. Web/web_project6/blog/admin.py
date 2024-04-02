from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "content",
        "created_at",
        "updated_at"
        ]