from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from post.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('post/' , TemplateView.as_view(template_name = 'post.html') , name = 'post'),
    path('users/', include('users.urls')),
]