from django.conf.urls import url
from . import views


app_name="comment"

urlpatterns = [
    url(r"^(?P<post_pk>\d+)$",views.comment,name="comment"),
]