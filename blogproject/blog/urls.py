from django.conf.urls import url

from . import views
from .views import IndexView

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^categories/(?P<pk>[0-9])/$', views.categories, name='categories'),
    url(r'^tags/(?P<pk>[0-9])/$', views.tags, name='tags')
]