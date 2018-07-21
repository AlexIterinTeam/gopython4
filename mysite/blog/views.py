from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from mysite.settings import STATIC_ROOT
from django.utils import timezone
from .models import Post

def helloworld(request):
    return HttpResponse('<html><head></head><body>Hello world!</body></html>')


def blog_mainpage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog_mainpage.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_with_tag(request, tpk):
    posts_with_tag = []
    for post in Post.objects.all():
        for tag in post.tags.all():
            if int(tag.pk) == int(tpk):
                posts_with_tag.append(post)
    return render(request, 'blog_mainpage.html', {'posts': posts_with_tag})