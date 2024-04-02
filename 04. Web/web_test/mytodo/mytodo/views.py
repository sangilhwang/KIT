from django.shortcuts import render, redirect
from todo.models import Todo

# def todo(request):
#     todo = Todo.objects.filter(completed=False)

#     context = {
#         "todo" : todo
#     }

#     return render(request, "todo_list_test.html", context)

# def todo_detail(request, todo_id):
#     todo = Todo.objects.get(id=todo_id)

#     context = {
#         "todo" : todo
#     }
#     return render(request, "todo_detail_test.html", context)