from django import forms
from posts.models import Post, Comment, PostImage

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",
            "content",            
        ]
        widgets = {"content": forms.Textarea(attrs={"placeholder": "댓글달기..."})}
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "content",
        ]
        widgets = {"content": forms.Textarea(attrs={"placeholder": "본문 입력..."})}
