from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'blog/', include('blog.urls')),
    url(r'^$', blog_views.blog_list, name="home"),
    url(r'^accounts/', include('accounts.urls')),
]
