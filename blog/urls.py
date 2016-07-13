from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/top$', views.post_list_top),
    url(r'^blog/shortest', views.post_list_shortest),
    url(r'^blog/(?P<id>\d*)/$', views.post_detail ),
    url(r'^blog/post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d*)/edit$', views.edit_post),
]

