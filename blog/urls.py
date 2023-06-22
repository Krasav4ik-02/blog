from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from post.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('posts/' , Create_post.as_view() , name = 'posts'),
    path('users/', include('users.urls')),
    path('post_view/', post_view, name = 'post_view')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)