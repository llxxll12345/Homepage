from django.conf.urls import url

from . import views
from .views import IndexView, detailView

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/(?P<pk>[0-9]+)/$', detailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^categories/(?P<pk>[0-9])/$', views.categories, name='categories'),
    url(r'^tags/(?P<pk>[0-9])/$', views.tags, name='tags'),
    url(r'^serach/$', views.search, name ='search')
]