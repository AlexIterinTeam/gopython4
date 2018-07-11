from django.conf.urls import url
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', blog_mainpage),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)