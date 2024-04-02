from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-pk") # primary key 의 내림차순으로 정렬해서 데이터를 호출한다

    context = {
        "posts" : posts,
    }

    return render(request, "blog/blog_list.html", context)

def single_post_page(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        "post" : post,
    }

    return render(request, "blog/single_post_page.html", context)