from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^ranked', views.ranked, name='ranked'),
    url(r'^compensation', views.compensation, name='compensation'),
]
