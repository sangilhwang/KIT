from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    
    else:
        return redirect("users:login")
    
def post_add(request):
    return render(request, "posts/post_add.html")