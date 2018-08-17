from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name = 'post_comment'),
    url(r'^comment/get/(?P<post_pk>[0-9]+)/$', views.post_comment, name = 'get_comments'),
    url(r'^comment/contact_msg/$', views.post_contact_msg, name='post_contact_msg')
]
