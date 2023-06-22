from django import forms
from post.models import Post , Comment
from users.models import User

class Posts(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'heading_post',
            'content_post',
            'image_post',
            'like',
            'account',
        ]





class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content_comment'
        ]