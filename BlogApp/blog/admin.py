from django.contrib import admin
from blog.models import Blog, BlogComments

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogComments)