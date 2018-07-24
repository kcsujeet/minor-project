from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Item
from machine_learning import reg_coeff
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import UserItem
import pandas as pd



class IndexView(generic.ListView):
    template_name ='category/index1a.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        return Item.objects.all()

def queryresult(request):
    queryset = Item.objects.all()
    context={"object_list":queryset,
             }

def resultview(request, pk):
    data = UserItem.objects.filter(uname=request.user, iid=pk)
    if len(data) is 0:
        data = UserItem(uname=request.user, iid=pk, clicks=1)
        data.save()
    else:
        data[0].clicks += 1
        data[0].save()

    data = {}
    for a in UserItem.objects.all():
        if a.uname in data:
            data[a.uname][a.iid] = a.clicks
        else:
            data[a.uname] = {a.iid: a.clicks}

    recommended = reg_coeff.recommend(str(request.user), 5, reg_coeff.pearson_similarity,data)
    if pk in recommended:
        del pk[recommended]
    print(request.user)
    print(data)
    print(recommended)


    data = Item.objects.get(pk=pk)
    ai_price = data.item_price
    ai_status = data.item_status
    ai_category = data.category
    data.cid = data.cid + 1
    data.save()

    upper_threshold = ai_price + ai_price * 0.1;
    lower_threshold = ai_price - ai_price * 0.1;
    myaidata = Item.objects.filter()

    objects=Item.objects.filter(pk__in=recommended.keys())

    context = {'item': data, 'items': objects, }
    print(context)
    return render(request, 'computer/detail.html', context)




class DetailView(generic.DetailView):
    model=Item
    template_name='computer/detail.html'


class ItemCreate(CreateView):
    model = Item
    fields = ['item_logo','item_name','item_status','item_price','category','item_spec','seller_info','phone','location','general_detail','description','delivery']


class ItemUpdate(UpdateView):
    model= Item
    fields = ['item_logo', 'item_name', 'item_status', 'item_price', 'item_spec', 'location','phone', 'description', 'delivery', ]


class ItemDelete(DeleteView):
    model=Item
    success_url= reverse_lazy('computer:index1a')

def adconf(request,pk):
    ad=Item.objects.get(pk=pk)
    context={'item':ad,}
    return render(request, 'computer/adconf.html',context)


def ItemListsearchView(request):

    search = request.GET["search"]
    print (search)

    itemlist= Item.objects.filter(Q(item_name__icontains=request.GET["search"])|Q(category__icontains=request.GET["search"]))
    context = {'item_list': itemlist,}
    return render(request, 'category/search_result.html', context)

def AscendingView(request):
    sorteddata=Item.objects.all().order_by('item_price')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result.html', context)

def DescendingView(request):
    sorteddata=Item.objects.all().order_by('-item_price')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result.html', context)

def PopularadView(request):
    sorteddata = Item.objects.all().order_by('-cid')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result.html', context)

def OldView(request):
    sorteddata = Item.objects.all().order_by('pk')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result.html', context)



        #return render(request, 'category/search_result.html', {'item_list': itemlist,'searchvalue':request.GET["search"]})