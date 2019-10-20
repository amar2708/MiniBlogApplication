from django.db import models
from django.contrib.auth.models import User
import uuid


class Blog(models.Model):
    blog_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


class BlogComments(models.Model):
    comment_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)
