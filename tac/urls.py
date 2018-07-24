from django.conf.urls import url
from . import views

app_name='category'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index1'),

    #/tac/712/
    url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),

    #/tac/item/add/
    url(r'item/add/$',views.ItemCreate.as_view(),name='item-add'),
    url(r'^itemsearch/$', views.ItemsearchView, name='itemsearch'),

]