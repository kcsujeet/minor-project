from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from .models import Item
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name ='category/index1b.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        return Item.objects.all()

def queryresult(request):
    queryset = Item.objects.all()
    context={"object_list":queryset,
             }

def resultview(request, pk):
    data = Item.objects.get(pk=pk)
    ai_price = data.item_price
    ai_status=data.item_status
    ai_category=data.category
    data.cid=data.cid +1
    data.save()

    upper_threshold = ai_price + ai_price*0.2;
    lower_threshold = ai_price - ai_price*0.2;
    myaidata = Item.objects.filter(~Q(pk= pk))
    recommendation = myaidata.filter(item_price__gte=lower_threshold) & Item.objects.filter(item_price__lte=upper_threshold) & Item.objects.filter(item_status__icontains=ai_status)& Item.objects.filter(category__icontains=ai_category)
    context = {'item': data, 'items': recommendation,}

    return render(request, 'automobiles/detail.html',context)



class DetailView(generic.DetailView):
    model=Item
    template_name='automobiles/detail.html'


class ItemCreate(CreateView):
    model = Item
    fields = ['item_logo','item_name','item_status','item_price','category','item_spec','phone','location','seller_info','general_detail','description','delivery']


class ItemUpdate(UpdateView):
    model= Item
    fields = ['item_logo', 'item_name', 'item_status', 'item_price', 'item_spec', 'location','phone', 'description', 'delivery', ]

class ItemDelete(DeleteView):
    model=Item
    success_url= reverse_lazy('automobiles:index1b')

def adconf(request,pk):
    ad=Item.objects.get(pk=pk)
    context={'item':ad,}
    return render(request, 'automobiles/adconf.html',context)


def ItemListsearchView(request):

    search = request.GET["search"]
    print (search)

    itemlist= Item.objects.filter(Q(item_name__icontains=request.GET["search"])|Q(category__icontains=request.GET["search"]))
    context = {'item_list': itemlist,}
    return render(request, 'category/search_result1b.html', context)

def AscendingView(request):
    sorteddata=Item.objects.all().order_by('item_price')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result1b.html', context)

def DescendingView(request):
    sorteddata=Item.objects.all().order_by('-item_price')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result1b.html', context)

def PopularadView(request):
    sorteddata = Item.objects.all().order_by('-cid')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result1b.html', context)

def OldView(request):
    sorteddata = Item.objects.all().order_by('pk')
    context = {'item_list': sorteddata, }
    return render(request, 'category/search_result1b.html', context)



        #return render(request, 'category/search_result.html', {'item_list': itemlist,'searchvalue':request.GET["search"]})