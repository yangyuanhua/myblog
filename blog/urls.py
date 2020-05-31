from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [

    url(r"^$",views.IndexView.as_view(),name="index"),
    url(r"^index$",views.IndexView.as_view(),name="index"),
    url(r"^index.html$",views.IndexView.as_view(),name="index"),
    # url(r"^posts/(?P<pk>\d+)$",views.details,name="details"),
    url(r"^posts/(?P<pk>\d+)$",views.PostDetailView.as_view(),name="details"),
    # http://127.0.0.1:8000/blog/archives/2020/5
    # url(r"^archives/(?P<year>\d{4})/(?P<month>\d{1,2})$",views.archive,name="archive"),
    url(r"^archives/(?P<year>\d{4})/(?P<month>\d{1,2})$",views.ArchiveView.as_view(),name="archive"),
    url(r"^categories/(?P<pk>\d+)$",views.CategoryView.as_view(),name="category"),
    # url(r"^tags/(?P<pk>\d+)$",views.tag,name="tag"),
    url(r"^tags/(?P<pk>\d+)$",views.TagView.as_view(),name="tag"),
    url(r"^search/",views.search,name="search"),

]