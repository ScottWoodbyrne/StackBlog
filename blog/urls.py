from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='home'),
    url(r'^blog/top$', views.post_list_top,name='top'),
    url(r'^blog/shortest', views.post_list_shortest, name='shortest'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail ,name='view_post'),
    url(r'^blog/post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post,name='edit_post'),
]

