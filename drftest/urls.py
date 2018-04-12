from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^albums/$', views.AlbumDetailView.as_view()),
]