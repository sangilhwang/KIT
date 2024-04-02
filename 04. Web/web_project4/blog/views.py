from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.
def index(request):
    return render(request, "index.html")

def post_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()

    context = {
        "posts" : posts,
        "comments" : comments,
    }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id 값인 Post 객체
    print(post)

    context = {
        "post" : post,
    }

    if request.method == "POST":

        comment = Comment.objects.create(
            post_id = post_id,
            content = request.POST["comment"],
        )

        return redirect(f"/post/{post.id}/")

    return render(request, "post_detail.html", context)

def post_add(request):
    
    if request.method == "POST": # method가 POST인 경우
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail =  request.FILES.get("thumbnail", None) # 이미지 파일

        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail = thumbnail # 이미지 파일 게시글 객체 생성시에 전달
        )

        return redirect(f"/post/{post.id}/")

    return render(request, "post_add.html")