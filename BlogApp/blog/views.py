from django.shortcuts import render, redirect
from .models import Blog, BlogComments
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.cache import cache


# getting the list of all the blogs stored.
def blog_list(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


# for adding new blog(login is compulsory)
@login_required(login_url="/accounts/login/")
def blog_create(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            # save blog to db
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            return redirect('blogs:list')
    else:
        form = forms.CreateBlog()
    return render(request, 'blog/blog_create.html', {'form': form})


# for adding new comments(login compulsory)
@login_required(login_url="/accounts/login/")
def add_comment(request, blog_uuid):
    blog = Blog.objects.filter(blog_uuid=blog_uuid)[0]
    if request.method == 'POST':
        add_comment_form = forms.AddComment(request.POST)
        if add_comment_form.is_valid():
            # store comments in DB against Blog Id
            instance = add_comment_form.save(commit=False)
            instance.blog_id = blog
            instance.commented_by = request.user
            instance.save()
            comments = BlogComments.objects.filter(blog_id=blog.id)
            return render(request, 'blog/blog_detail.html', {'blog': blog,
                                                             'comments': comments})
    else:
        add_comment_form = forms.AddComment()
    return render(request, 'blog/add_comment.html', {'add_comment_form': add_comment_form,
                                                     "blog": blog})


# for getting the details of a selected blog. If the details are stored in cache return response from cache
# else get the details from DB
def blog_detail(request, blog_uuid):
    blog_cache_key = "blog_cache_{}".format(blog_uuid)
    comment_cache_key = "comment_cache_{}".format(blog_uuid)
    cached_value_for_blog = cache.ttl(blog_cache_key)
    cached_value_for_comment = cache.ttl(comment_cache_key)
    if cached_value_for_blog and cached_value_for_comment:
        print('Response from cache')
        resp_for_blog = cache.get(blog_cache_key)
        resp_for_comment = cache.get(comment_cache_key)
    else:
        resp_for_blog = Blog.objects.get(blog_uuid=blog_uuid)
        resp_for_comment = BlogComments.objects.filter(blog_id=resp_for_blog.id)
        cache.set(blog_cache_key, resp_for_blog, timeout=900)
    return render(request, 'blog/blog_detail.html', {'blog': resp_for_blog,
                                                     'comments': resp_for_comment})
