from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user
from post.forms import Posts , Comment

class Create_post(View):
    def get(self, request):
        form = Posts()
        return render(request, 'posts.html', context={'form': form})
    def post(self, request):
        bount_form = Posts(request.POST)

        if bount_form.is_valid():
            new_post = bount_form.save(commit=False)
            new_post.account = get_user(request)
            new_post.save()
            return render(request, 'home.html')
        return render(request, 'posts.html', context={'form': bount_form})