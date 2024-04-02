from django.shortcuts import render
from todo.models import Todo

# Create your views here.
def todo(request):
    todos = Todo.objects.filter(completed=False)

    context = {
        "todos" : todos
    }

    return render(request, "todo_list_test.html", context)

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    context = {
        "todo" : todo
    }
    return render(request, "todo_detail_test.html", context)