from django.db import models
from users.models import User

class Post(models.Model):
    heading_post = models.CharField(max_length=255 )
    content_post = models.TextField()
    image_post = models.ImageField(
        upload_to='image_post',
        blank=True
    )
    date_created_post = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(User , on_delete=models.CASCADE, )
    like = models.IntegerField( default= 0)


class Comment(models.Model):
    account = models.ForeignKey(User , on_delete=models.CASCADE, )
    post = models.ForeignKey(Post , on_delete=models.CASCADE, )
    content_comment = models.TextField()
    date_created_comment = models.DateTimeField(auto_now_add=True)