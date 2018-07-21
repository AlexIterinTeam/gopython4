from django.conf.urls import url
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', blog_mainpage),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^tag/(?P<tpk>\d+)/$', post_with_tag, name='post_with_tag'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)