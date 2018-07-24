from django.conf.urls import url
from .import views

app_name='computer'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index1a'),

    #/computer/712/
    # url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)$',views.resultview,name='detail'),

    #/computer/item/add/
    url(r'item/add/$',views.ItemCreate.as_view(),name='item-add'),
    url(r'item/(?P<pk>[0-9]+)/$',views.ItemUpdate.as_view(),name='item-update'),
    url(r'item/(?P<pk>[0-9]+)/delete/$',views.ItemDelete.as_view(),name='item-delete'),
    url(r'^itemsearch/$', views.ItemListsearchView, name='itemsearch'),
    url(r'^ascending/$', views.AscendingView, name='ascending'),
    url(r'^descending/$', views.DescendingView, name='descending'),
    url(r'^popularad/$', views.PopularadView, name='popular'),
    url(r'^old/$', views.OldView, name='old'),
    url(r'conf/(?P<pk>[0-9]+)$',views.adconf,name='ad-conf'),
]