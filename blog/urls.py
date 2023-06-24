from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from post import views
from post.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_view , name='post_view'),
    path('posts/' , Create_post.as_view() , name = 'posts'),
    path('users/', include('users.urls')),
    path('post_view/', post_view, name = 'post_view'),
    path('comment/add/<int:post_id>/', views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)