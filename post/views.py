from django.shortcuts import render
from django.views import View
from post.forms import Post , Comment
class Post(View):
    template_name = 'post.html'

    def create_post(self, request):
        form = Post(request.POST)
        if form.is_valid():
            return render(request , self.template_name , context)