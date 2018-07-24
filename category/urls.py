from django.conf.urls import url
from . import views

from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'login/$',login,{'template_name':'category/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'category/logout.html'}, name='logout'),
    url(r'register/$',views.register,name='register'),
    url(r'^profile/$',views.view_profile,name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),



    ]