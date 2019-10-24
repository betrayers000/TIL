from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Image(models.Model):
    image = ProcessedImageField(
            processors= [ResizeToFill(300,300)],
            format= 'JPEG',
            options= {'quality': 90},
            upload_to= 'media'
        )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    