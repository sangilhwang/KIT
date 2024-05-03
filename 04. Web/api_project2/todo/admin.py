from django.contrib import admin
from todo.models import Todo

# Register your models here.
class TodoInline(admin.TabularInline):
    model = Todo
    extra = 1

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created",
        "completed",
        "important",
    ]