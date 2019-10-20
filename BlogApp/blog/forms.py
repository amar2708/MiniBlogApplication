from django import forms
from .models import Blog, BlogComments


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', ]


class AddComment(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ['comment', ]
