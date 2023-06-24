from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import get_user
from post.forms import Posts , Comments
from post.models import Post, Comment


class Create_post(View):
    def get(self, request):
        form = Posts()
        return render(request, 'posts.html', context={'form': form})
    def post(self, request):
        bount_form = Posts(request.POST, request.FILES)

        if bount_form.is_valid():
            new_post = bount_form.save(commit=False)
            new_post.account = get_user(request)
            new_post.save()
            return render(request, 'base.html')
        return render(request, 'posts.html', context={'form': bount_form})

def post_view(request):
    posts = Post.objects.order_by('-date_created_post')
    return render(request, 'post_view.html', {'posts': posts})


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = Comments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.account = get_user(request)
            comment.post = post
            comment.save()
            return redirect('post_view')
    else:
        form = Comments()

    return render(request, 'add_comment.html', {'form': form, 'post_id': post_id})