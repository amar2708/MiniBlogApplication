from django.conf.urls import url, include
from .views import blog_list, blog_create, blog_detail, add_comment

app_name = 'blogs'

urlpatterns = [
    url('^$', blog_list, name="list"),
    url('create/$', blog_create, name="create"),
    url(r'^(?P<blog_uuid>[\w-]+)/$', blog_detail, name="detail"),
    url(r'^(?P<blog_uuid>[\w-]+)/add_comment/$', add_comment, name="add_comment"),
    ]
