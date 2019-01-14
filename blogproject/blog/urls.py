from django.conf.urls import url

from . import views
from .views import IndexView, detailView, CategoryView, ArchiveView, TagView

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/(?P<pk>[0-9]+)/$', detailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchiveView.as_view(), name='archives'),
    url(r'^categories/(?P<pk>[0-9])/$', CategoryView.as_view(), name='categories'),
    url(r'^tags/(?P<pk>[0-9])/$', TagView.as_view(), name='tags'),
    url(r'^serach/$', views.search, name ='search')
]