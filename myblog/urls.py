"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from blog.feeds import AllPostsRssFeed
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"",include("blog.urls")),
    url(r"^blog/",include("blog.urls")),
    url(r"^comment/",include("comment.urls")),
    url(r"^all/rss",AllPostsRssFeed(),name="rss"),
    url(r"^search/",include("haystack.urls")),
    url(r"^test$",views.test_view,name="test"),
    url(r"^math$",views.math_view,name="math"),
]
